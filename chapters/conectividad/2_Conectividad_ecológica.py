import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from chapters.conectividad import text

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

md = f'# {text.title}\n\n### {text.author}\n\n'
md += '#### Jardín Botánico de Bogotá, eje Conservación _in situ_'
md += f'{text.main}\n\n#\n\n'
st.markdown(md)

#######################
#      plot pies
#######################

with st.container(border=True, horizontal_alignment='center'):

	st.markdown('**Conectividad de la estructura ecológica principal**')
	pie0 = px.pie(
		co_eep_pd, 
		values='Área (ha)', 
		names='Connectividad', 
		#title='Conectividad de la estructura ecológica principal',
		color_discrete_sequence=['#92a311', '#d9c663'],
	)
	st.plotly_chart(pie0)

	st.markdown('### Conectividad de la estructura ecológica principal + parques urbanos')
	pie1= px.pie(
		co_eep_parks_pd, 
		values='Área (ha)', 
		names='Connectividad', 
		title='Conectividad de la estructura ecológica principal + parques urbanos',
		color_discrete_sequence=['#92a311', '#d9c663']
	)
	st.plotly_chart(pie1)

	st.markdown("Aunque un alto porcentaje de la Estrucutra Ecológica Principal ya esta conectada entre sí, la inclusión de los parques urbanos aumenta ligeramente el área conectada.")

with st.container(border=True, horizontal_alignment='center'):

	pie2 = px.pie(
		fl_eep_pd, 
		values='Porcentaje', 
		names='Clase de área', 
		title='Tipo de área de la estructura ecológica principal',
		color_discrete_sequence=['#92a311', '#d9c663']
	)
	st.plotly_chart(pie2)

	pie3 = px.pie(
		fl_parks_pd, 
		values='Porcentaje', 
		names='Clase de área', 
		title='Tipo de área de los parques urbanos',
		color_discrete_sequence=['#92a311', '#d9c663']
	)
	st.plotly_chart(pie3)

	pie4 = px.pie(
		fl_eep_parks_pd, 
		values='Porcentaje', 
		names='Clase de área', 
		title='Tipo de área de la estructura ecológica principal + parques urbanos',
		color_discrete_sequence=['#92a311', '#d9c663']
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
		color_continuous_scale="Speed",
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