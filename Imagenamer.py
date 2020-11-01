"""This Program is used to rename image files with its content"""

"""SETUP"""
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import string
import uuid

namearray = []
indexnow = 0

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract' #absolute path to out tesseract instalation

"""FUNCTIONS"""
def ocr(filename):
    newname = pytesseract.image_to_string(Image.open(absolutebasepathin+"\\"+filename))  # Use pillow to open an image for pytesseract image2string to use
    return newname

def namecleaner(filename):
    print("filenameis "+filename)
    filename = "_".join(filename.split()) # Get rig of line braks and spaces
    filename = filename.replace("__","_") # Cleaning duplicated '_'s
    filename = filename.replace(" ","") # Get rig of spaces(For recursion)
    filename = filename.replace("\n","") # Get rig of line braks(For recursion)
    #Get rid of forbiden characters
    filename = filename.replace("<","")
    filename = filename.replace(">","")
    filename = filename.replace(":","")
    filename = filename.replace("\"","")
    filename = filename.replace("/","")
    filename = filename.replace("\\","")
    filename = filename.replace("|","")
    filename = filename.replace("?","")
    filename = filename.replace("*","")
    ##################################
    outputname = filename.replace(".","") # Get rid of extra dots
    print("outputnameis "+outputname)
    return outputname

"""CORECODE"""
# Define the input and output directories
basepathin = '.\ImagesToConvert'
print("basepathin = "+basepathin)
basepathout = '.\ImageOutput'
print("basepathout = "+basepathout)

# Getting the absolute path to the before named directories
absolutebasepathin = os.path.abspath('.\ImagesToConvert')
print("absolutebasepathin = "+absolutebasepathin)
absolutebasepathout = os.path.abspath('.\ImagesOutput')
print("absolutebasepathout = "+absolutebasepathout)

# List all files in a directory using scandir()
with os.scandir(absolutebasepathin) as entries:
    for entry in entries:
        if entry.is_file():
            # Fill an array with the list
            namearray.append(entry.name)

# Get array length for the loop
arraylength = len(namearray)
print("arraylength = "+str(arraylength))

while indexnow < arraylength:
    # Get file name from the array
    basename = namearray[indexnow]
    print("basename = "+basename)
    # Call ocr
    newname = ocr(basename)
    print("newname = "+newname)
    # Call "namecleaner" to get rid of forbiden characters, line breaks and spaces.
    cleanname = namecleaner(newname)
    print("cleanname = "+cleanname)
    if cleanname != "":
        cleanname = cleanname + basename[len(basename)-4:len(basename)]
        os.rename(absolutebasepathin+"\\"+basename, absolutebasepathout+"\\"+cleanname)
        print(basename+" is now renamed as "+cleanname)
    else:
        UUIDnow = str(uuid.uuid4())
        cleanname = namecleaner(UUIDnow)
        cleanname = cleanname + basename[len(basename)-4:len(basename)]
        os.rename(absolutebasepathin+"\\"+basename, absolutebasepathout+"\\"+cleanname)
        print(basename+" is now "+cleanname)

    indexnow += 1


print("All images are given a name")
