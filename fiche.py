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
    st.write(" PRODUCTEUR DU DÉCHET : DS SMITH ")
    st.write("NUMÉRO DE BSD : BSD-20230808-7QQW18PM2 ")
    st.write("Nature du déchet : Pâteux (mélange  d'encre, de colle et d'eau) ")
    
    st.write("  --------------------------------------------------------------------------------------------------------------------------------------------")
    
    st.write("### II. Description de l'anomalie")
    st.write("Le déchet reçu, Pâteux (mélange  d'encre, de colle et d'eau), est  classé sous le code ONU 1263.  Il est par conséquent  soumis à l'ADR. Il doit donc être conditionné dans un emballage homologué, approprié et répondant aux instructions définies par l'ADR. Or 2 des GRV de pâteux reçus ont été découpés et fermés par un simple film. Il ne répondent plus à l'exigence d'étanchièté.  Un déversement a été constaté sur la plateau du camion.") 
    st.write("Dans le cas où le découpage des GRV a été réalisé dans un but pratique, vous pouvez utiliser un entonnoir." )
    st.write("Leur éxpédition vers le centre de traitement nécessite leur recondtionnement dont le coût sera défini par le service commercial." )  

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
    video_file = open('grv-ds-smith.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_file)
    
   
