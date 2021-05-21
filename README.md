# AutoArea

This **AutoArea** can calculate something's area in each picture repeatedly by Python 3 (3.8.6) instead of [ImageJ](https://imagej.nih.gov/ij/).
(2021.05.21: Python version was updated.)

## Dependencies

- Numpy (1.19.5)
- OpenCV2 (4.5.1)

(2021.05.21: Numpy and OpenCV2 versions were updated.)

## Install

```
git clone https://github.com/masukai/AutoArea.git
```

If you do not install Python 3, Numpy and OpenCV2, please install them, following below.

- [Python 3](https://www.python.org/downloads/)
- Numpy and OpenCV2

```
pip(3) install numpy
pip(3) install opencv-python
```

If you need "(3)" to use Python 3, not Python 2, please add it.

## Usage

### First Step

please set your pictures in which you want to calculate areas in the **photo(YOU CAN CHANGE THE NAME)** folder.
I saved 2 sample pictures. If you want to calculate your data (pictures), please delete my samples.

### Second Step

You have to regulate and set 5 parameters below in [main.py](https://github.com/masukai/AutoArea/blob/master/main.py).

1. (line.19) **PtoC; scale transration** in _main_ function: change the unit from pixel to cm.
2. (line.21) **extension** in _main_ function: select your using extension; "png", "jpg" and "JPEG".
3. (line.26) **folder_name** in _main_ function: give the name you want to give it.
4. (line.132-133) **lower and upper of HSV threshold** in _hsv_binary_ method of class _MainPGArea_: binary transration
5. (line.137) **kernel** in _closing_ method of class _MainPGArea_: choose a closing size that suits your purpose.

You need to know **PtoC; scale transration** and **lower and upper of HSV threshold** by ImageJ or other softwares.

It is NOW possible to specify the number of cores of your computer to be used (2021.05.21).
(line.53) **Pool(multi.cpu_count())** in function I have already set the maximum number of cores on your computer to use.
If you want to lower the number of cores, change **multi.cpu_count()** to the number of cores you want to use.
For example, if you want to use 4 cores, change **4** from **multi.cpu_count()**.

### Third Step

Move to _AutoArea_ directory and type below,

```
python(3) main.py
```

then, you will gain the results in the **photo_calculated_area.csv** file.

You can find calculated binary images in the **photo_save_image** folder, please check it out!

### Additional Step

If you do not want to use closing process, please comment out the _closing_ method of class _MainPGArea_.

In the _save_image_ method of class _MainPGArea_, you can select stages of calculated images.

## Verification

If you want to verify the calculated values with AutoArea,
you write the measured values in the **measured_area.csv** file.

Do not comment out **verification()** in _main_ function.

Forthermore, you need to install Matplotlib (3.1.1) like below.

```
pip(3) install matplotlib
```

You can visualize and check the values in the **measured_area.csv** and
**photo_calculated_area.csv** files by making a one-to-one correspondence
between them, like _Verification2_.

### Verification 1

<img src="https://user-images.githubusercontent.com/37993351/84643037-417d9500-af38-11ea-9970-eebc43c89d9a.jpg" width=40%>
<img src="https://user-images.githubusercontent.com/37993351/84643058-48a4a300-af38-11ea-9c1d-d4712667f096.jpg" width=40%>

You can see that the corners are rounded due to the closing filter.

This is a 6 cm square with an area of 36 cm2,
but the ImageJ and AutoArea Both are now 35.85 cm2.
That means that only the error of the value
when re-scaling from pixel to cm is reflected.

### Verification 2

<img src="https://user-images.githubusercontent.com/37993351/84643155-6a058f00-af38-11ea-9e01-295343fdaef7.png" width=60%>
90 images as measured by ImageJ (Measured) and calculated by AutoArea (Calculated).
(I do not publish 90 images.)

ImageJ has a few large values, but this is probably due to manual error.
The point is that the mean values are almost identical
for both ImageJ and AutoArea, and are close to
the intersection of the line with y=x and
the line fitted by the least-squares method.
Even if the values are slightly different,
the result shows that the same trend can be firmly established
by manual work with ImageJ and automatic calculations with AutoArea.

## CAUSION

- **An environment of taking pictures is the most important.**
  Please take pictures or images in the almost same environment.

- This program has been performed by **only** MacOS 10.15.4.
  If you find some bugs, please tell me about them.
