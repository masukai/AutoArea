# AutoArea
This **AutoArea** can calculate something's area in each picture repeatedly by Python 3 (3.7.6) instead of [ImageJ](https://imagej.nih.gov/ij/).

## Dependencies
* Numpy (1.18.1)
* OpenCV2 (4.1.2)

## Install
```
git clone https://github.com/masukai/AutoArea.git
```
If you do not install Python 3, Numpy and OpenCV2, please install them yourself.

## Usage
### First Step
please set **pictures** in which you want to calculate areas in the **photo** folder.

I saved 2 sample pictures. If you want to calculate your data (pictures), please delete my samples.

### Second Step
You have to regulate and set 4 parameters below in [main.py](https://github.com/masukai/AutoArea/blob/master/main.py).

1. **scale transration**; from pixel to cm, in *main* function
2. **extension**, e.g., "png", "jpg" and "JPEG" in *main* function
3. **lower and upper of HSV threshold**; binary transration, in *hsv_binary* method of class *MainPGArea*
4. **kernel** of closing size in *closing* method of class *MainPGArea*

You need to know **scale transration** and **lower and upper of HSV threshold** by ImageJ or other softwares.


### Third Step
Moving to *AutoArea* directory and typing below,
```
python3 main.py
```
then, you will gain the results in the **calculated_area.csv** file.

You can find calculated binary images in the **save_image** folder, please check it out!

### Additional Step
If you do not want to use closing process, please comment out the *closing* method of class *MainPGArea*.
In the *save_image* method of class *MainPGArea*, you can select stages of calculated images.

## CAUSION
**An environment of taking pictures is most important.**
Please take pictures or images in the almost same environment.

This program has been performed by **only** MacOS 10.15.4.
If you find some bugs, please tell me about them.
