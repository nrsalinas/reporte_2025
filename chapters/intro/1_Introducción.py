import streamlit as st

logo = "shared/figs/Color.png"

st.markdown("""
			
# Reporte Estado de la Biodiversidad 2025
			
## Jardín Botánico de Bogotá
			
## Eje Conservación _in situ_
			
#### Carlos Vargas y Nelson R. Salinas (editores)

#

Este es el reporte de estado de la biodiversidad de Bogotá 2025.

""")



left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)
