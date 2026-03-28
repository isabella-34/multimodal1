import streamlit as st
from  PIL import Image

st.title("Esta es mi primera app en la nube")
st.header("En este espacio comienzo a desarrollar mis apps de Interfaces Multimodales")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('heart.jpeg')
st.image(image, caption='Ilustración')


texto = st.text_input('¿Qué opinas de mi ilustración?', 'Opino que...')
st.write('Piensas que ', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Señala si crees correcta la afirmación")
  st.write("Las ilustraciones comunican sentimientos de manera diferente, aegún quien las mire.")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('¡Así es!')

with col2:
  st.subheader("Tus preferencias")
  modo = st.radio("¿Qué movimiento artistico te gusta más?", ('Expresionismo', 'Surrealismo', 'Dadaísmo'))
  if modo == 'Expresionismo':
    st.write("Te interesa la expresión emocional intensa.")
  if modo == 'Surrealismo':
    st.write("Te interesa explorar del inconsciente y los sueños.")
  if modo == 'Dadaísmo':
    st.write("Te interesa lo anti-arte, absurdo y protesta.")

st.subheader("Uso de botones")
if st.button('Presiona el botón'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aún')

