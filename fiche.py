import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
#import matplotlib
#import matplotlib.pyplot as plt
#matplotlib.use('Agg')
import json
#import plotly.express as px
import altair as alt





if __name__=="__main__":
    st.set_page_config(
        page_title="Streamlit basics app",
        layout="centered"
    )

    st.title(" Fiche de non conformité ")

    st.write("Auteur : Brahim AIT OUALI  - Technicien chimiste")
    st.write("### I. Identification")
    st.write(" PRODUCTEUR DU DECHET : -------------")
    st.write("NUMERO DE BSD : -------------")
    st.write(" : -------------")
    
    st.write("### II. Description de l'anomalie")
    st.write(" : -------------")
   
    # Display the LOGO
    img1 = Image.open("IMG_PAPREC.jpg")
    img2 = Image.open("IMG_RECYDIS.jfif") 
    img3 = Image.open("photo_resine1.jpg")
    img4 = Image.open("photo_resine3.jpg")
    img5 = Image.open("photo_PE.jpg")
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)


    
    st.write("### III. Photos")
    st.image(img4, width=250)
    st.image(img3, width=250)
    
    st.write("### IV. Vidéos")
    video_file = open('video-resine.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    
    st.write("Point éclair = 115,0 °C")
    st.image(img5)
    st.write("Pas de chlore (test de flamme négatif au chlore)")
  


  
    



