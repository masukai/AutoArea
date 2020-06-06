import os
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
import csv

# _listはリスト
# np_はnp.arrayに格納されている


def main():  # メイン関数
    path = "./photo"
    os.chdir(path)
    procedure()
    os.chdir("../")


def procedure():
    jpg_list = glob.glob("*.JPG")  # JPGの探索とループ
    for i in range(len(jpg_list)):
        my_file = jpg_list[i]
        print("{0}/{1}: {2}".format(i, len(jpg_list), my_file))
        img = cv2.imread(my_file)


if __name__ == '__main__':
    main()
