import streamlit as st

def calcular_reynolds(densidad, velocidad, diametro, viscosidad):
    """Calcula el número de Reynolds."""
    return (densidad * velocidad * diametro) / viscosidad

def clasificar_flujo(reynolds):
    """Clasifica el tipo de flujo según el número de Reynolds."""
    if reynolds < 2000:
        return "Laminar"
    elif reynolds < 4000:
        return "Transitorio"
    else:
        return "Turbulento"

st.title("Cálculo del Número de Reynolds y Clasificación de Flujo")


# Valores por defecto sugeridos para agua a temperatura ambiente y condiciones típicas
densidad = st.number_input(
    "Densidad del fluido (kg/m³)",
    min_value=0.0,
    value=1000.0,
    help="Ejemplo: Agua = 1000 kg/m³, Aceite = 900 kg/m³"
)
velocidad = st.number_input(
    "Velocidad del fluido (m/s)",
    min_value=0.0,
    value=1.0,
    help="Ejemplo: 1 m/s es típico en tuberías domésticas"
)
diametro = st.number_input(
    "Diámetro del tubo (m)",
    min_value=0.0,
    value=0.05,
    help="Ejemplo: 0.05 m = 5 cm (tubería pequeña)"
)
viscosidad = st.number_input(
    "Viscosidad dinámica (Pa·s)",
    min_value=0.000001,
    value=0.001,
    help="Ejemplo: Agua = 0.001 Pa·s, Aceite = 0.1 Pa·s"
)

if st.button("Calcular"):
    reynolds = calcular_reynolds(densidad, velocidad, diametro, viscosidad)
    tipo_flujo = clasificar_flujo(reynolds)
    st.write(f"Número de Reynolds: {reynolds:.2f}")
    st.write(f"Tipo de flujo: **{tipo_flujo}**")