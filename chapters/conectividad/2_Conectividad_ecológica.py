import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

eep_file = "chapters/conectividad/dat/shape/priority_eep_1000.shp"
logo = "shared/figs/Color.png"

###   Map data

eep = gpd.read_file(eep_file)
eep = eep.to_crs(4326)
ctr = eep.dissolve().centroid
ctr_lon = ctr.x.item()
ctr_lat = ctr.y.item()


###   Chart data

co_eep = {
	"Connectividad": ["Área conectada", "Área no conectada"], 
	"Área (ha)": [96649.92, 90097.87]
}
co_eep_pd = pd.DataFrame.from_dict(co_eep)

co_eep_parks = {
	"Connectividad": ["Área conectada", "Área no conectada"], 
	"Área (ha)": [98448.79, 90104.73]
}
co_eep_parks_pd = pd.DataFrame.from_dict(co_eep_parks)

fl_eep = {
	"Clase de área": ["Conector", "Área central"], 
	"Porcentaje": [5, 95]
}
fl_eep_pd = pd.DataFrame.from_dict(fl_eep)

fl_parks = {
	"Clase de área": ["Conector", "Área central"], 
	"Porcentaje": [100, 0]
}
fl_parks_pd = pd.DataFrame.from_dict(fl_parks)

fl_eep_parks = {
	"Clase de área": ["Conector", "Área central"], 
	"Porcentaje": [57, 43]
}
fl_eep_parks_pd = pd.DataFrame.from_dict(fl_eep_parks)


st.markdown("""
			
# Conectividad de las áreas verdes de Bogotá
			
### Kristian Rubiano

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
Bogotá se ubica en una de las regiones más biodiversas del planeta, pero su rápido crecimiento urbano ha fragmentado y aislado muchas de sus áreas verdes. Para mitigar estos procesos que impactan negativamente a la biodiversidad, se creó la Estructura Ecológica Principal de Bogotá: una red de cerros, reservas, humedales, rondas de río, parques urbanos y otras áreas verdes, diseñada para conservar la naturaleza y los servicios que esta le presta a ciudad y a la región. Sin embargo, hasta ahora no se sabía con claridad qué tan bien conectados están estos espacios entre sí para proteger la biodiversidad de forma efectiva. 
			
Para ampliar nuestro conocimiento al respecto, usamos mapas detallados de la Estructura Ecológica Principal para analizar cómo están distribuidas estas áreas verdes y qué tan fácil sería para animales como aves, insectos o pequeños mamíferos desplazarse entre ellas, teniendo en cuenta las distancias entre los distintos espacios. Esto también nos permitió identificar zonas de la región que podrían ser priorizadas para aumentar la conectividad entre áreas verdes.
			
Estos análisis indicaron que cerca del 93% del área de la Estructura Ecológica Principal forma un gran “bloque” continuo de hábitat, lo que es una buena noticia para muchas especies. No obstante, dentro de la ciudad existen zonas, sobre todo altamente urbanizadas y localizadas en el borde sur, donde la Estructura Ecológica Principal casi no está presente y, por lo tanto, la conectividad es muy baja o nula. Estas zonas aparecen como "vacíos" de conectividad y deberían ser prioridad para aumentar y mejorar la presencia y calidad de las áreas verdes.
			
Los parques urbanos de menor tamaño agregan poca área verde adicional al total de la ciudad, pero cumplen un papel clave como pequeños puentes entre las grandes áreas verdes. Disminuyen las distancias entre áreas, aumentan la proximidad entre ellas y refuerzan la posibilidad de movimiento de la fauna a través de la ciudad. Es decir, aunque no sean grandes reservas de hábitat, ayudan a conectar las que ya existen y a llevar la naturaleza a barrios donde hoy casi no hay.
			
En conjunto, los resultados muestran que la Estructura Ecológica Principal ofrece una base sólida de hábitat, mientras que los parques urbanos de menor tamaño ayudan a tejer la red de conexiones entre esos núcleos principales. Esto sugiere que, si se diseñan y manejan con criterios ecológicos (tipo de vegetación, función, tamaño y ubicación), estos parques pueden convertirse en aliados estratégicos para conservar la biodiversidad y mejorar la calidad de vida en Bogotá. Por ello, deberían ser considerados de manera explícita en la planificación y en el seguimiento de cómo se conectan las áreas verdes en la ciudad.
#
			
# 

			

""")

#######################
#      plot pies
#######################

with st.container(border=True, horizontal_alignment='center'):

	pie0 = px.pie(
		co_eep_pd, 
		values='Área (ha)', 
		names='Connectividad', 
		title='Conectividad de la estructura ecológica principal',
		color_discrete_sequence=['LightSalmon', 'DarkRed']
	)
	st.plotly_chart(pie0)

	pie1= px.pie(
		co_eep_parks_pd, 
		values='Área (ha)', 
		names='Connectividad', 
		title='Conectividad de la estructura ecológica principal + parques urbanos',
		color_discrete_sequence=['LightSalmon', 'DarkRed']
	)
	st.plotly_chart(pie1)

	st.markdown("Aunque un alto porcentaje de la Estrucutra Ecológica Principal ya esta conectada entre sí, la inclusión de los parques urbanos aumenta ligeramente el área conectada.")

with st.container(border=True, horizontal_alignment='center'):

	pie2 = px.pie(
		fl_eep_pd, 
		values='Porcentaje', 
		names='Clase de área', 
		title='Tipo de área de la estructura ecológica principal',
		color_discrete_sequence=['LightSalmon', 'DarkRed']
	)
	st.plotly_chart(pie2)

	pie3 = px.pie(
		fl_parks_pd, 
		values='Porcentaje', 
		names='Clase de área', 
		title='Tipo de área de los parques urbanos',
		color_discrete_sequence=['LightSalmon', 'DarkRed']
	)
	st.plotly_chart(pie3)

	pie4 = px.pie(
		fl_eep_parks_pd, 
		values='Porcentaje', 
		names='Clase de área', 
		title='Tipo de área de la estructura ecológica principal + parques urbanos',
		color_discrete_sequence=['LightSalmon', 'DarkRed']
	)
	st.plotly_chart(pie4)

	st.markdown("La conectividad ecológica no solo aumenta cuando los elementos verdes son más grandes, también cuando actúan como puentes que enlazan el paisaje. La Estructura Ecológica Principal aporta conectividad por el tamaño de sus elementos, pero la inclusión de los parques urbanos refuerza su papel como conectores, destacando su importancia para conservar la biodiversidad.")

#######################
#      plot map
#######################

with st.container(border=True, horizontal_alignment='center'):

	st.markdown("**Mapa de conectividad ecológica para la ciudad de Bogotá**")

	fig = px.choropleth_map(
		eep,
		#title='Número de especies por localidad',
		geojson=eep.geometry,
		locations=eep.index,
		#hover_name="Localidad",
		hover_data={"ECA_Nrm":True},
		color="ECA_Nrm",
		labels={"ECA_Nrm": "Nivel de conectividad"},
		color_continuous_scale="Reds",
		opacity=0.7,
		#marker_line_width=2,  # Thin line for boundaries
		#marker_line_color='white',  # Boundary color
		#projection="mercator"
	)

	fig.update_layout(
		margin={"r":0,"t":0,"l":0,"b":0},
		paper_bgcolor='rgba(0,0,0,0)',
		height=1300,
		map=dict(
			center={"lat":ctr_lat, "lon":ctr_lon},
			zoom=9.5,
		),
		showlegend=False,
		coloraxis_showscale=False
	)

	st.plotly_chart(fig, use_container_width=True)

st.markdown("""#""")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)

exit()