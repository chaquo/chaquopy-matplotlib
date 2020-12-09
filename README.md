# Chaquopy Matplotlib demo

This is the source code of the app demonstrated in my [interview with Eric
Decanini](https://www.youtube.com/watch?v=X0JNxGay7JY). It uses
[Chaquopy](https://chaquo.com/chaquopy/) to easily include Python code and libraries in an
Android app.

* MainActivity takes two strings from text boxes and passes them to a Python function.
* The Python code parses the strings into lists of numbers, and uses Matplotlib to plot them on
  a chart.
* The Python function then returns the chart image as a byte array in PNG format, which
  MainActivity displays in an ImageView.
