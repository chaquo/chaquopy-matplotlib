# Chaquopy Matplotlib demo

This is the source code of the app demonstrated in my [interview with Eric
Decanini](https://www.youtube.com/watch?v=X0JNxGay7JY). It uses
[Chaquopy](https://chaquo.com/chaquopy/) to include Python code and libraries in an Android app.

* The [top-level](https://github.com/chaquo/chaquopy-matplotlib/blob/master/build.gradle) and 
  [module-level](https://github.com/chaquo/chaquopy-matplotlib/blob/master/app/build.gradle) 
  build.gradle files contain the Chaquopy configuration, including installing 
  [Matplotlib](https://matplotlib.org/).
* The [MainActivity](https://github.com/chaquo/chaquopy-matplotlib/blob/master/app/src/main/java/com/chaquo/myapplication/MainActivity.kt) 
  inputs two strings from text boxes and passes them to a Python function.
* The [Python code](https://github.com/chaquo/chaquopy-matplotlib/blob/master/app/src/main/python/plot.py)
  parses the strings into lists of numbers, and uses Matplotlib to plot them on a chart.
* The Python function then returns the chart image as a byte array in PNG format, which the
  MainActivity displays in an ImageView.
