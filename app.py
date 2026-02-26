import streamlit as st
from  PIL import Image

st.title("Esta es mi primera app en la nube")
st.header("En este espacio comienzo a desarrollar mis apps de Interfaces Multimodales")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('poster')
st.image(image, caption='Interfaces Multimodales')
