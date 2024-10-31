import streamlit as st
from PIL import image 
image= Image.open('capibaraaa.png')

st.image(image, caption='Capibara')

st.title("Las capibaras los amigos de todos")
st.header ("Nombres de las capibaras:")
st.write ("1. Carpinchos")
texto=st.text_input("Escribe tu comentario"," ...")

st.subheader("Usamos dos columnas")
col1,col2 = st.columns (2)

with col1:
  st.subheader("Primera columna")
  st.write("La mejor capibara que a existido jamas es Jasinta")
  resp=st.checkbox("Jasinta es la mejor")
  if resp:
    st.write("SIIIII")
with col2: 
  st.subheadern ('Segunda columna')
  modo= st.radio('Te gustaria tener una capibara de mascota?',('si','No','NO porque es ilegal'))
  if modo =='si':
    st.write('Comprate una pues')
  if modo=='No'
    st.write ('Mejor')
  if modo=='NO porque es ilegal'
    st.write ('Muy bien cuida la fauna')
