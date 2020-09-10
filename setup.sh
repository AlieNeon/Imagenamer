#!/bin/bash

echo "JUST FOR LINUX OR XDG OSs"

echo "install python: https://www.python.org/downloads/"
xdg-open "https://www.python.org/downloads/"

echo "also install tesseract https://tesseract-ocr.github.io/tessdoc/Downloads.html"
xdg-open "https://tesseract-ocr.github.io/tessdoc/Downloads.html"

read -p "Press any key to resume when installation finishes"

mkdir ImagesToConvert
mkdir ImagesOutput
pip install Pillow
pip install pytesseract

echo "Installation finished!"
