import streamlit as st #importando a biblioteca streamlit

st.title('APP Aula IA-EngBio: IMC')
st.write('Oi, estamos no aplicativo para calcular o IMC') #st.write escreve na tela

#o usuario ira fornecer peso e altura
peso = st.number_input('Digite o seu peso:')
altura = st.number_input('Digite a sua altura:')

imc = peso/(altura*altura)

st.write('O seu IMC vale',imc)

