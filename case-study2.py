
# face recognition

# import packages

import streamlit as st
from PIL import Image
import os
import boto3


def load_image(image_file):
    img=Image.open(image_file)
    return (img)

def maddy_face_algorithm(sourceImage,targetImage):
    client=boto3.client('rekognition')
    sImage=open(sourceImage,"rb")
    tImage=open(targetImage,"rb")

    response=client.compare_faces(SimilarityThreshold=70,SourceImage={'Bytes':sImage.read()},TargetImage={'Bytes':tImage.read()})
    try:
        print(response['FaceMatches'][0])
        return (1)
    except:
        return (0)

st.header('Face Recognition Demo')

face_image_file=st.file_uploader("Upload Images",type=["png","jpg","jpeg"])

if face_image_file is not None:
    file_details={"filename":face_image_file,"filetype":face_image_file.type,"filesize":face_image_file.size}
    st.write(file_details)
    st.image(load_image(face_image_file),width=250)

    with open(os.path.join('faces','target.jpg'),'wb') as f:
        f.write(face_image_file.getbuffer())
        st.success('File Saved')

if st.button('Recognise Face'):
    a=0
    if(maddy_face_algorithm('faces/mad.jpg','faces/target.jpg')):
        st.success('Face Matched with Maddy')
        a=1
    if(maddy_face_algorithm('faces/naresh.jpeg','faces/target.jpg')):
        st.success('Face Matched with Naresh')
        a=1
    if(maddy_face_algorithm('faces/venky.jpeg','faces/target.jpg')):
        st.success('Face Matched with Venky')
        a=1
    if(a==0):
        st.error('New Face Found')
