import streamlit as st

st.title("Calculadora 🧮")


st.markdown("""
Esta es una calculadora sencilla que permite realizar las operaciones básicas: **sumar**, **restar**, **multiplicar** y **dividir**.
""")

num1 = st.number_input("Ingresa el primer número", value=0.0, format="%.2f")
num2 = st.number_input("Ingresa el segundo número", value=0.0, format="%.2f")


operation = st.selectbox("Elige la operación", ("Sumar", "Restar", "Multiplicar", "Dividir"))


result = None

if st.button("Calcular"):
    if operation == "Sumar":
        result = num1 + num2
    elif operation == "Restar":
        result = num1 - num2
    elif operation == "Multiplicar":
        result = num1 * num2
    elif operation == "Dividir":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: No se puede dividir por 0."
    

    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"El resultado de la operación es: **{result:.2f}**")
