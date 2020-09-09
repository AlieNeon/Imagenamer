@echo off

echo JUST FOR WINDOWS

echo install python: https://www.python.org/downloads/
start https://www.python.org/downloads/

echo also install tesseract https://tesseract-ocr.github.io/tessdoc/Downloads.html
start https://tesseract-ocr.github.io/tessdoc/Downloads.html

echo wait untill instalation
pause

md ImagesToConvert
md ImagesOutput
pip install Pillow
pip install pytesseract
