import streamlit as st #importando a biblioteca streamlit

st.title('APP Aula IA-EngBio: IMC')
st.write('Oi, estamos no aplicativo para calcular o IMC') #st.write escreve na tela

#o usuario ira fornecer peso e altura
peso = st.number_input('Digite o seu peso:')
altura = st.number_input('Digite a sua altura:')
#calcula o IMC
if st.button('Calcular'):
  imc = peso/(altura*altura)
  if imc < 18.5:
    st.write('O seu IMC vale',imc,'e esta abaixo do peso')
    st.image('abaixoPeso.jpg')
  if imc >=18.5 and imc < 25:
    st.write('O seu IMC vale',imc,'e esta com peso normal')
  if imc >= 25:
    st.write('O seu IMC vale',imc,'e esta acima do peso')
  

