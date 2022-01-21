import cv2
import matplotlib as ptl
import zipfile 

print(cv2.__version__)

pose_path = "/home/bio/Documents/Projeto/visão-computacional-openCV/pose.zip"
zip_object = zipfile.ZipFile(file = pose_path, mode ="r")
zip_object.extractall("./visão-computacional-openCV")

imagens_path = "/home/bio/Documents/Projeto/visão-computacional-openCV/imagens.zip"
zip_object = zipfile.ZipFile(file = imagens_path, mode= "r")
zip_object.extractall("./visão-computacional-openCV")
zip_object.close()