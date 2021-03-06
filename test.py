############################################################
#
#       Title: FloorplanReader
#
#       Description: This program is ment to read floor plans 
#       and then also read the venting file
#       This program should also be able to interpret the scale of the image
#       
#
#
#
#       Haiku:      It's snowing on mount
#                   But the season is ending
#                   Soon the rain will come
#
#
############################################################



import cv2 
from pdf2image import convert_from_path


FloorPlanPDF = "FloorPlanPDFs/###"

FloorPlanImage = convert_from_path(FloorPlanPDF)

print("Hello World")