import streamlit as st

# Título de la aplicación
st.title("Calculadora")

# Ingresar los números
num1 = st.number_input("Ingresa el primer número", value=0)
num2 = st.number_input("Ingresa el segundo número", value=0)

# Operaciones
operation = st.selectbox("Elige la operación", ("Sumar", "Restar", "Multiplicar", "Dividir"))

# Realizar la operación
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

# Mostrar el resultado
st.write(f"El resultado de la operación es: {result}")
 