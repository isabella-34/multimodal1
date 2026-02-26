import streamlit as st
from  PIL import Image

st.title("Esta es mi primera app en la nube")
st.header("En este espacio comienzo a desarrollar mis apps de Interfaces Multimodales")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('heart.jpeg')
st.image(image, caption='Ilustración')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('¡Correcto!')
    
