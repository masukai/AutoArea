# AutoArea
This **AutoArea** can calculate something's area in each picture repeatedly by Python 3 (3.7.6) instead of [ImageJ](https://imagej.nih.gov/ij/).

## Dependencies
* Numpy (1.18.1)
* OpenCV2 (4.1.2)

## Install
```
git clone https://github.com/masukai/AutoArea.git
```
If you do not install Python 3, Numpy and OpenCV2, please install them, following below.

* [Python 3](https://www.python.org/downloads/)
* Numpy and OpenCV2
```
pip3 install numpy
pip3 install opencv-python
```
or
```
pip install numpy
pip install opencv-python
```

## Usage
### First Step
please set your pictures in which you want to calculate areas in the **photo** folder.
I saved 2 sample pictures. If you want to calculate your data (pictures), please delete my samples.

### Second Step
You have to regulate and set 4 parameters below in [main.py](https://github.com/masukai/AutoArea/blob/master/main.py).

1. **PtoC; scale transration**: from pixel to cm, in *main* function
2. **extension**, e.g., "png", "jpg" and "JPEG" in *main* function
3. **lower and upper of HSV threshold**: binary transration, in *hsv_binary* method of class *MainPGArea*
4. **kernel** of closing size in *closing* method of class *MainPGArea*

You need to know **PtoC; scale transration** and **lower and upper of HSV threshold** by ImageJ or other softwares.

### Third Step
Move to *AutoArea* directory and type below,
```
python3 main.py
```
then, you will gain the results in the **calculated_area.csv** file.

You can find calculated binary images in the **save_image** folder, please check it out!

### Additional Step
If you do not want to use closing process, please comment out the *closing* method of class *MainPGArea*.

In the *save_image* method of class *MainPGArea*, you can select stages of calculated images.

## Verification
### Verification 1
<img src="https://user-images.githubusercontent.com/37993351/84643037-417d9500-af38-11ea-9970-eebc43c89d9a.jpg" width=40%>
<img src="https://user-images.githubusercontent.com/37993351/84643058-48a4a300-af38-11ea-9c1d-d4712667f096.jpg" width=40%>

You can see that the corners are rounded due to the closing filter.

This is a 6 cm square with an area of 36 cm^{2},
but the ImageJ and AutoArea Both are now 35.85 cm^{2}.
That means that only the error of the value
when re-scaling from pixel to cm is reflected.

### Verification 2
<img src="https://user-images.githubusercontent.com/37993351/84643155-6a058f00-af38-11ea-9e01-295343fdaef7.png" width=60%>
90 images as measured by ImageJ (Measured) and calculated by AutoArea (Calculated).

ImageJ has a few large values, but this is probably due to manual error.
The point is that the mean values are almost identical
for both ImageJ and AutoArea, and are close to
the intersection of the line with y=x and
the line fitted by the least-squares method.
Even if the values are slightly different,
the result shows that the same trend can be firmly established
by manual work with ImageJ and automatic calculations with AutoArea.

## CAUSION
* **An environment of taking pictures is the most important.**
Please take pictures or images in the almost same environment.

* This program has been performed by **only** MacOS 10.15.4.
If you find some bugs, please tell me about them.
