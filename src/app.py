import streamlit as st

st.title("¡SUMA DE DOS NÚMEROS!")

st.write("Bienvenido/a/e a la app para sumar dos números.")
st.write("Valores por defecto: 1 y 2")

valor1 = 1
valor2 = 2

valor1 = st.text_input("Introduce el primer valor:")
valor2 = st.text_input("Introduce el segundo valor:")

try:
    suma = valor1 + valor2
    st.write("La suma de los valores ", valor1, " y ", valor2, " es: ", suma, "!!")
except:
    st.write("La suma no se ha podido realizar, comprueba los valores introducidos :(")


