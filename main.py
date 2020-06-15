import os
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
import csv
import time

# _listはリスト
# np_はnp.arrayに格納されている


def main():  # メイン関数
    start_time = time.time()

    # 変数調整はここで行う
    PtoC = 1.0 / 27.7  # pixel to cm  ImageJ等で前もって計測
    # 校正の必要あり。複数枚で確認が要必要。
    extension = ".JPEG"  # 拡張子は調節して使う
    size_ex = int(len(extension)) * -1
    # binaryとcrosingの調節はMainPGArea内で直接行うこと

    # 以下メインの流れ
    path = "./photo"
    os.chdir(path)
    name_list, area_list = procedure(PtoC, extension, size_ex)
    os.chdir("../")
    savefile(name_list, area_list)

    # 計測(実測)値と計算値の比較用 基本的にコメントアウト
    verification()

    print(">>> complete {0:.2f} sec <<<".format(time.time() - start_time))


def procedure(PtoC, extension, size_ex):
    jpg_list = glob.glob("*{0}".format(extension))  # JPGの探索とループ
    name_list = []
    area_list = []
    for i in range(len(jpg_list)):
        my_file = jpg_list[i]
        name = my_file[:size_ex]
        print("{0}/{1}: {2}".format(i+1, len(jpg_list), name))
        img = cv2.imread(my_file)
        obj = MainPGArea(name, img)
        name_list.append(name)
        area_list.append(round(obj.pixels * (PtoC ** 2), 2))  # 小数点以下2桁

    return name_list, area_list


def savefile(name_list, area_list):
    savecsv_buffer = np.array([name_list, area_list])
    savecsv = savecsv_buffer[:, np.argsort(savecsv_buffer[0])].T
    with open("calculated_area.csv", "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        for i in range(len(name_list)):
            writer.writerow(savecsv[i])


def verification():
    print("Start Verification")
    np_mea = np.loadtxt('measured_area.csv', delimiter=',', usecols=(1))
    np_cal = np.loadtxt('calculated_area.csv', delimiter=',', usecols=(1))
    print("Measured: {0}".format(np_mea))
    print("Calculated: {0}".format(np_cal))

    # 可視化
    np_check = np.array([-10000, 10000])

    coef_1 = np.polyfit(np_mea, np_cal, 1)
    print("y = ax + b")
    print("a: {0}".format(coef_1[0]))
    print("b: {0}".format(coef_1[1]))
    y_pred_1 = coef_1[0] * np_check + coef_1[1]

    ax = plt.figure(num=0, dpi=360).gca()
    ax.set_title("Verification", fontsize=14)
    ax.scatter(np_mea, np_cal, s=2, color="red", label="Verification")
    ax.scatter(np.mean(np_mea), np.mean(np_cal), s=40, marker="*", color="purple", label="Mean Value")
    ax.plot(np_check, y_pred_1, linewidth=1, color="red", label="fitting: y={0:.2f}x+{1:.2f}".format(coef_1[0], coef_1[1]))  # 最小2乗法 1次式
    ax.plot(np_check, np_check, linewidth=1, color="black", label="y=x")
    plt.grid(which='major')
    plt.legend()
    ax.set_xlim([0, 3000])
    ax.set_ylim([0, 3000])
    ax.set_xlabel('Measured', fontsize=14)
    ax.set_ylabel('Calculated', fontsize=14)
    ax.set_aspect('equal', adjustable='box')
    plt.savefig("Verification.png", bbox_inches='tight', pad_inches=0.1)
    plt.pause(0.3)  # 計算速度を上げる場合はコメントアウト
    plt.clf()


class MainPGArea:  # 色調に差があり、輪郭になる場合HSVに変換>>>2値化して判別
    def __init__(self, file_name, img):
        self.file_name = file_name
        self.img = img
        self.pixels = 0
        self.hsv_transration()
        self.gauss_transration()
        self.hsv_binary()
        self.closing()
        self.save_image()
        self.calculation_area()

    def hsv_transration(self):  # 色調変換
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    def gauss_transration(self):  # ガウス変換
        self.gauss = cv2.GaussianBlur(self.hsv, (15, 15), 3)  # フィルタの大きさ

    def hsv_binary(self):  # HSV制限2値化
        lower = np.array([22, 90, 90])  # 下限 0 0 0
        upper = np.array([76, 255, 255])  # 上限 180 255 255
        self.bin = cv2.inRange(self.gauss, lower, upper)

    def closing(self):  # 膨張収縮処理により穴埋め
        kernel = np.ones((19, 19), np.uint8)
        self.cl = cv2.morphologyEx(self.bin, cv2.MORPH_CLOSE, kernel)

    def save_image(self):  # 画像の保存
        path = "../save_image"
        os.makedirs(path, exist_ok=True)
        os.chdir(path)
        # cv2.imwrite("{0}_hsv.jpg".format(self.file_name), self.hsv)
        # cv2.imwrite("{0}_gauss.jpg".format(self.file_name), self.gauss)
        # cv2.imwrite("{0}_bin.jpg".format(self.file_name), self.bin)
        cv2.imwrite("{0}_cl.jpg".format(self.file_name), self.cl)
        os.chdir("../photo")

    def calculation_area(self):  # 面積pixel分の計算
        self.pixels = cv2.countNonZero(self.cl)  # 計算する画像の名前に変更


if __name__ == '__main__':
    main()
