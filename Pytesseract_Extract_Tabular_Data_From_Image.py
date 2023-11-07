

import cv2
import pytesseract
import numpy as np
from PIL import Image
import csv

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread('page7.jpg')

data = pytesseract.image_to_string(image, lang='eng',config='--psm 6')

print(data)

def Convert(string):

    li = list(string.split("\n"))

    while " " in li:

        li.remove(" ")

    while '' in li:

        li.remove('')

    return li

listing = Convert(data)

type(listing)

def extractDigits(lst):

    res = []

    for el in lst:

        sub = el.split(', ')

        res.append(sub)

    return(res)
    

lst = extractDigits(listing)

lst

indices_1 = (3,5,6,7,8,9)

result_list_1 = [lst[i] for i in indices_1]

result_list_1

# List convert into CSV and save
# write each item in a new row



with open('page7_table_1.csv','w', newline='') as file:

    writer  = csv.writer(file)

    writer.writerows(result_list_1)

indices_2 = (10,11,12,13,14,15,16,17,18)

result_list_2 = [lst[i] for i in indices_2]

result_list_2

with open('page7_table_2.csv','w', newline='') as file:

    writer  = csv.writer(file)

    writer.writerows(result_list_2)

