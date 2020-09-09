try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import string

namearray = []
indexnow = 0

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def ocr(filename):
    newname = pytesseract.image_to_string(Image.open(absolutebasepathin+"\\"+filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return newname

def namecleaner(filename):
    print("filenameis "+filename)
    filename = "_".join(filename.split())
    filename = filename.replace(" ","")
    filename = filename.replace("\n","")
    filename = filename.replace("<","")
    filename = filename.replace(">","")
    filename = filename.replace(":","")
    filename = filename.replace("\"","")
    filename = filename.replace("/","")
    filename = filename.replace("\\","")
    filename = filename.replace("|","")
    filename = filename.replace("?","")
    filename = filename.replace("*","")
    filename = filename.replace(".","")
    outputname = filename+basename[len(basename)-4:len(basename)]
    print("outputnameis "+outputname)
    return outputname

# List all files in a directory using scandir()
basepathin = '.\ImagesToConvert'
print("basepathin = "+basepathin)
absolutebasepathin = os.path.abspath('.\ImagesToConvert')
print("absolutebasepathin = "+absolutebasepathin)
basepathout = '.\ImageOutput'
print("basepathout = "+basepathout)
absolutebasepathout = os.path.abspath('.\ImagesOutput')
print("absolutebasepathout = "+absolutebasepathout)
with os.scandir(basepathin) as entries:
    for entry in entries:
        if entry.is_file():
            namearray.append(entry.name)

arraylength = len(namearray)
print("arraylength = "+str(arraylength))

while indexnow < arraylength:
    basename = namearray[indexnow]
    print("basename = "+basename)
    newname = ocr(basename)
    print("newname = "+newname)
    cleanname = namecleaner(newname)
    print("cleanname = "+cleanname)
    os.rename(absolutebasepathin+"\\"+basename, absolutebasepathout+"\\"+cleanname)
    print(basename+" is now renamed as "+cleanname)
    indexnow = indexnow + 1


print("All images are given a name")
