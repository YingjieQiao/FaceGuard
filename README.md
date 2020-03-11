# 10.009-1D-Project


#### TODO:  
Hardware: rpi, [webcam](https://www.sgbotic.com/index.php?dispatch=products.view&product_id=2849), speaker, LEDs (green and red lights)

GUI: displaying the person's face, match ID/name, green/red light

Poster,

Tidy, modularized, easy-to-read code

**A telegram bot to upload pic for visitors?**

#### More than 1 sensors:

Infra sensor (on thymio): check entrance by motion

webcam connected to rpi

#### Solution

"Smart Campus" problem
Use the concept of "Internet of Things"
Use ML to do data prediction: openCV, learnt 5 pics of me, can tell the 6 is me!



Software: 

1. openCV: to train a model using pictures of faces that can tell students from visitors
2. GPIO,~~IotJumpWay~~ (use Google fyrebase instead): LED lights control, speaker control.
3. Linux Motion on Rpi: video stream from the camera.
4. SSL: Secure streaming.
5. GUI: must be implemented with Kivy


##### IMPT Reference:
1. A working device: https://www.hackster.io/AdamMiltonBarker/facial-recognition-identification-on-raspberry-pi-1c7495
2. Face recognition: https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html
3. Brute Force match: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html
4. 


## Sotfware Dependencies:
1. opencv -- see below for set up
2. numpy
3. pillow

OpenCV
======

### Set up

I used `virtualenv` to manually set up a virtual environment and pip installed opencv using command `pip install opencv-python`. After successfullt installing opencv library, you can either type command`python -m idlelib.idle` in your terminal to open up IDLE as editor, or use PyCharm and set the environment path to the virtual environment directory.

Alternatively, you can just `pip install opencv-python` in Spyder terminal and you can use anaconda environment already (the `conda install` doesn't work for me because it keeps giving me some `UnsatisfiableError`).

**Take note, if you are using Mac, use `pip3 install opencv-python-headless` instead!**
**(also a potential problem is solved [here](https://github.com/opencv/opencv/issues/13848#issuecomment-597032231)**

(some [tutorial](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) if you want to understand how it works really well. I commented a lot to make it easier to follow too)

### Structure

**Mar 10, Tues, wk7, yingjie**

Brute force doesn't work. Try `Haar`. If still doesn't work, use CNN from Andrew Ng.

`Haar` works so far. Thinking put CNN as "further improvenment" and do (to make prof happy) if I got time.

*clean up documentation formatting after I get most stuff straight*

The face recognition code, although primitively written, sort of works now. Will make it modularised later this week.

Last terminal output (to prove it really worked):

```
188 137 513 513
yingjie
184 137 513 513
yingjie
179 141 513 513
yingjie
192 137 513 513
yingjie
179 141 513 513
yingjie
184 137 513 513
yingjie
187 132 513 513
yingjie
179 136 513 513
yingjie
179 136 513 513
yingjie
184 137 513 513
yingjie
175 137 513 513
yingjie
175 137 513 513
yingjie
205 136 513 513
yingjie
```

And what really proves it work: ![first-try-out](https://github.com/YingjieQiao/probably-fine/blob/master/asset/IMG_7461.png)
