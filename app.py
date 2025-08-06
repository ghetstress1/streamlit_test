import streamlit as st

st.header('Lanzar una moneda')

number_of_trials = st.slider('Numero de intentos', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st_write(f'Experimento con {number of trials} intentos en curso.')

st.write('Esta aplicacion aun no es funcional. En construccion.')
