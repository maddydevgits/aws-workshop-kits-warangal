# face matching

# import the packages

import streamlit as st
from PIL import Image
import os
import boto3

def load_image(image_file):
    img=Image.open(image_file)
    return img

# create ui
col1,col2 = st.columns(2)

col1.subheader("Enter Input Image")
src_image_file=col1.file_uploader("Upload Images",type=["png","jpg","jpeg"],key=1)

col2.subheader("Enter Target Image")
target_image_file=col2.file_uploader("Upload Images",type=["png","jpg","jpeg"],key=2)



# we have to check whether image is uploaded or not
if src_image_file is not None:
    file_details={"filename":src_image_file,"filetype":src_image_file.type,"filesize":src_image_file.size}
    col1.write(file_details)
    col1.image(load_image(src_image_file),width=250)

    with open(os.path.join("uploads","src.jpg"),"wb") as f:
        f.write(src_image_file.getbuffer())
        col1.success("File Saved")

if target_image_file is not None:
    file_details={"filename":target_image_file,"filetype":target_image_file.type,"filesize":target_image_file.size}
    col2.write(file_details)
    col2.image(load_image(target_image_file),width=250)

    with open(os.path.join("uploads","target.jpg"),"wb") as f:
        f.write(target_image_file.getbuffer())
        col2.success("File Saved")

if st.button("Compare Faces"):
    imageSource=open("uploads/src.jpg","rb")
    targetSource=open("uploads/target.jpg","rb")

    client=boto3.client('rekognition')
    response=client.compare_faces(SimilarityThreshold=70,SourceImage={'Bytes': imageSource.read()},TargetImage={'Bytes':targetSource.read()})
    try:
        print(response['FaceMatches'][0])
        st.success("Faces are Matched")
    except:
        st.error("Faces Not Matched")



