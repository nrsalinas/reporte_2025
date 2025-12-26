import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px
from chapters.ciencia_participativa_interacciones import text

res_file = "chapters/ciencia_participativa_interacciones/dat/interacciones_recurso.csv"
types_file = "chapters/ciencia_participativa_interacciones/dat/interacciones_registros.csv"
logo = "shared/figs/Color.png"
butter_file = "chapters/ciencia_participativa_interacciones/figs/Dione_glycera_Angela_Montoya.jpg"
bird_file = "chapters/ciencia_participativa_interacciones/figs/Spinus_spaltria_Oswaldo_Pinzon.jpg"

###   Pie data   ###
res = pd.read_csv(res_file)
types = pd.read_csv(types_file)

md = f'# {text.title}\n\n### {text.author}\n\n'
md += '#### Jardín Botánico de Bogotá, eje Conservación _in situ_'
md += f'{text.main}\n\n#\n\n'
st.markdown(md)


with st.container(border=True, horizontal_alignment='center'):

	pie = px.pie(
		res, 
		values='Reportes', 
		names='Recurso consumido',
		title="Recursos asociados a registros de interacciones",
		color_discrete_sequence=list(
			reversed(
				["#18351f", "#10572b", "#1f7425", "#4e8b14", "#809d0b", "#b1af2c", "#dbc969", "#f3e9ab"]
			)
		) 
	)
	st.plotly_chart(pie)

	left_co, right_co = st.columns(2, vertical_alignment='center')
	
	with left_co:
		st.image(bird_file, caption="@ Oswaldo Pinzón")

	with right_co:
		st.markdown("""
		El principal recurso registrado por la red de observadores ciudadanos es la flor.
		""")


with st.container(border=True, horizontal_alignment='center'):

	pie = px.pie(
		types, 
		values='Reportes', 
		names='Tipo de interacción',
		title="Clases de interacciones registradas",
		color_discrete_sequence=["#1f7425", "#4e8b14", "#809d0b", "#b1af2c", "#dbc969"]
	)
	st.plotly_chart(pie)

	left_co, right_co = st.columns(2, vertical_alignment='center')
	
	with left_co:
		st.image(butter_file, caption="@ Angela Montoya")

	with right_co:
		st.markdown("""
		Un gran numero de reportes están en revisión por parte del equipo científico del JBB. Sin embargo, los datos preliminares confirman que las interacciones de consumo son las más comunmente reportadas.
		""")

st.markdown("""#""")


left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)



