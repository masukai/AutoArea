import os
import glob
import cv2
import numpy as np
import csv

# _listはリスト
# np_はnp.arrayに格納されている


def main():  # メイン関数
    path = "./photo"
    os.chdir(path)
    PtoC = 0.02  # pixel to cm  ImageJ等で前もって計測
    name_list, area_list = procedure(PtoC)
    os.chdir("../")
    savefile(name_list, area_list)


def procedure(PtoC):
    jpg_list = glob.glob("*.JPEG")  # JPGの探索とループ
    name_list = []
    area_list = []
    for i in range(len(jpg_list)):
        my_file = jpg_list[i]
        print("{0}/{1}: {2}".format(i+1, len(jpg_list), my_file[:-4]))
        img = cv2.imread(my_file)
        obj = draw_contours(my_file[:-4], img)
        name_list.append(my_file[:-4])
        area_list.append(obj.pixels * PtoC)

    return name_list, area_list


def savefile(name_list, area_list):
    savecsv_buffer = np.array([name_list, area_list])
    savecsv = savecsv_buffer[:, np.argsort(savecsv_buffer[0])].T
    with open("calculated_area.csv", "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        for i in range(len(name_list)):
            writer.writerow(savecsv[i])


class draw_contours:  # 色調に差があり、輪郭になる場合HSVに変換>>>2値化して判別
    def __init__(self, file_name, img):
        self.file_name = file_name
        self.img = img
        self.pixels = 0
        self.hsv_transration()
        self.gauss_transration()
        self.hsv_binary()
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

    def save_image(self):  # 画像の保存
        path = "../save_image"
        os.makedirs(path, exist_ok=True)
        os.chdir(path)
        # cv2.imwrite("{0}_hsv.jpg".format(self.file_name), self.hsv)
        # cv2.imwrite("{0}_gauss.jpg".format(self.file_name), self.gauss)
        cv2.imwrite("{0}_bin.jpg".format(self.file_name), self.bin)
        os.chdir("../photo")

    def calculation_area(self):  # 面積pixel分の計算
        self.pixels = cv2.countNonZero(self.bin)


if __name__ == '__main__':
    main()
