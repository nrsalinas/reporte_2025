import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

inter_all = "chapters/interacciones/dat/interacciones_todas_long.csv"
inter_no_nat = "chapters/interacciones/dat/interacciones_no_nativas_long.csv"
spp_nat = "chapters/interacciones/dat/spp_nativas.csv"
spp_no_nat = "chapters/interacciones/dat/spp_no_nativas.csv"


###  Bar data

inter_all_df = pd.read_csv(inter_all)
inter_no_nat_df = pd.read_csv(inter_no_nat)
spp_nat_df = pd.read_csv(spp_nat)
spp_no_nat_df = pd.read_csv(spp_no_nat)

st.markdown("""
			
# Interacciones bióticas
			
### Juan Camilo Garibello

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
En Bogotá se han registrado una gran cantidad de interacciones bióticas entre diferentes
organismos biológicos.
			

""")


with st.container(border=True, horizontal_alignment='center'):

	bar2 = px.bar(
		spp_nat_df, 
		y="Especie", 
		x="Registros",
		color="Interacción",
		title='Especies nativas con mayor número de registros',
		#color_discrete_sequence=['Bisque', 'DarkRed', 'Coral']
	)

	#bar2 = bar2.update_layout(height=500)
	st.plotly_chart(bar2)

	bar3 = px.bar(
		spp_no_nat_df, 
		y="Especie", 
		x="Registros",
		color="Interacción",
		title='Especies no nativas con mayor número de registros',
		#color_discrete_sequence=['Bisque', 'DarkRed', 'Coral']
	)

	#bar3 = bar3.update_layout(height=500)
	st.plotly_chart(bar3)


with st.container(border=True, horizontal_alignment='center'):

	bar0 = px.bar(
		inter_all_df, 
		y="Interacción", 
		x="Registros",
		color="Potencial invasor",
		title='Interacciones de todas las plantas',
		color_discrete_sequence=['Bisque', 'DarkRed', 'Coral']
	)

	#bar0 = bar0.update_layout(height=500)
	st.plotly_chart(bar0)

	bar1 = px.bar(
		inter_no_nat_df, 
		y="Interacción", 
		x="Registros",
		color="Potencial invasor",
		title='Interacciones de plantas no nativas',
		color_discrete_sequence=['Bisque', 'DarkRed', 'Coral']
	)

	#bar1 = bar1.update_layout(height=500)
	st.plotly_chart(bar1)


exit(0)