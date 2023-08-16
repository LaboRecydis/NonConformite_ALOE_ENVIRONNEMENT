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
    st.write(" PRODUCTEUR DU DÉCHET : ALOE ENVIRONNEMENT ")
    st.write("NUMÉRO DE BSD : BSD-20230809-0GA5934RJ ")
    st.write("Nature du déchet : Eaux souillées")
    
    st.write("  --------------------------------------------------------------------------------------------------------------------------------------------")
    
    st.write("### II. Description de l'anomalie")
    st.write("Le déchet reçu n'est pas de l'eau souillée mais ce sont des petits échantillons d'huiles conditionnés en fûts.") 
    st.write("La dénomination du déchet doit être requalifiée en échantillons d'huile hydraulique usagée avec édition d'un nouveau BSD." )
    st.write("Le déchet est mis dans la zone des non-conformités en attendant la validation par client." )  

    st.write("  --------------------------------------------------------------------------------------------------------------------------------------------")
   
    # Display the LOGO
    img1 = Image.open("IMG_PAPREC.jpg")
    img2 = Image.open("IMG_RECYDIS.jfif") 
    #img3 = Image.open("photo_resine1.jpg")
    #img4 = Image.open("photo_resine3.jpg")
    #img5 = Image.open("photo_PE.jpg")
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)


    
    #st.write("### III. Photos")
    #st.image(img4, width=250)
    #st.image(img3, width=250)
    
    st.write("### III. Vidéo")
    video_file = open('echant-huile-aloe-env.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_file)
    
   
