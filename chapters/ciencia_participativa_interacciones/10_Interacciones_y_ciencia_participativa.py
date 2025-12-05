import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px

res_file = "chapters/ciencia_participativa_interacciones/dat/interacciones_recurso.csv"
types_file = "chapters/ciencia_participativa_interacciones/dat/interacciones_registros.csv"
logo = "shared/figs/Color.png"
butter_file = "chapters/ciencia_participativa_interacciones/figs/Dione_glycera_Angela_Montoya.jpg"
bird_file = "chapters/ciencia_participativa_interacciones/figs/Spinus_spaltria_Oswaldo_Pinzon.jpg"

###   Pie data   ###
res = pd.read_csv(res_file)
types = pd.read_csv(types_file)

st.markdown("""
			
# Interacciones y ciencia participativa
			
### Angela Montoya

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
La estrategia Ciencia Participativa e Interacciones Bióticas integra observaciones ciudadanas para caracterizar las relaciones entre organismos que hacen parte de los ecosistemas de Bogotá. A partir de 377 reportes ciudadanos se documentaron diversos tipos de interacción, de los cuales el 72% corresponde a relaciones de consumo, el 16% a crecimiento sobre otras especies y un 9% a interacciones generales, mientras que anidación, parasitismo y simbiosis representaron proporciones menores. El análisis de los recursos consumidos muestra una dominancia del uso de flores (63,8%), seguida por tallos (11%), néctar (9,4%), frutos (7,1%), hojas y semillas (2,8% cada una), y polen (1,4%). Estas interacciones evidencian patrones tanto mutualistas como antagonistas, como *Thygare aethlops* en *Salvia bogotensis*, *Spinus psaltria* en *Streptosolen jamesonii* y *Danaus plexippus* en *Lantana camara*. La información recolectada permite identificar redes tróficas y asociaciones ecológicas relevantes para la gestión de la biodiversidad urbana, aportando a la comprensión de las dinámicas de las especies y la adaptación al desarrollo de la ciudad. El enfoque participativo fortalece la capacidad de observación comunitaria y genera datos verificables para análisis y seguimiento de dinámicas biológicas en el Distrito Capital.

#

""")


with st.container(border=True, horizontal_alignment='center'):

	pie = px.pie(
		res, 
		values='Reportes', 
		names='Recurso consumido', 
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



