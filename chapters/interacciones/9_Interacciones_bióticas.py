import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

inter_all = "chapters/interacciones/dat/interacciones_todas_long.csv"

###  Bar data

inter_all_df = pd.read_csv(inter_all)

st.markdown("""
			
# Interacciones bióticas
			
### Juan Camilo Garibello

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
En Bogotá se han registrado una gran cantidad de interacciones bióticas entre diferentes
organismos biológicos.
			

""")


with st.container(border=True, horizontal_alignment='center'):

	bar0 = px.bar(
		inter_all_df[inter_all_df["Potencial invasor"] != "Total"], 
		y="Interacción", 
		x="Registros",
		color="Potencial invasor",
		title='Interacciones de todas las plantas',
		color_discrete_sequence=['Bisque', 'DarkRed', 'Coral']
	)

	bar0 = bar0.update_layout(height=500)
	st.plotly_chart(bar0)


exit(0)