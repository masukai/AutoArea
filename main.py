import os
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
import csv

# _listはリスト
# np_はnp.arrayに格納されている


def main():  # メイン関数
    files = []
    path = './'
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            files.append(filename)
    print(files)


if __name__ == '__main__':
    main()
