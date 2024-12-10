import streamlit as st

st.title("¡SUMA DE DOS NÚMEROS!")

st.write("Bienvenido/a/e a la app para sumar dos números.")
valor1 = st.text_input("Introduce el primer valor:")
valor2 = st.text_input("Introduce el segundo valor:")

if valor1 and valor2:
    try:
        suma = int(valor1) + int(valor2)
        st.write("La suma de los valores ", valor1, " y ", valor2, " es: ", suma, "!!")
    except:
        st.write("La suma no se ha podido realizar, comprueba los valores introducidos :(")
else:
    st.write("¡¡Introduce los valorees!!")


