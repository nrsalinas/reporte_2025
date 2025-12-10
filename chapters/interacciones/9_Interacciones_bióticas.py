import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from chapters.interacciones import text

inter_all = "chapters/interacciones/dat/interacciones_todas_long.csv"
inter_no_nat = "chapters/interacciones/dat/interacciones_no_nativas_long.csv"
spp_nat = "chapters/interacciones/dat/spp_nativas.csv"
spp_no_nat = "chapters/interacciones/dat/spp_no_nativas.csv"
loc_file = "chapters/interacciones/dat/mapa/interact.shp"
logo = "shared/figs/Color.png"


###  Bar data

inter_all_df = pd.read_csv(inter_all)
inter_no_nat_df = pd.read_csv(inter_no_nat)
spp_nat_df = pd.read_csv(spp_nat)
spp_no_nat_df = pd.read_csv(spp_no_nat)

###   Map data

loc = gpd.read_file(loc_file)
loc = loc.to_crs(4326)
ctr = loc.dissolve().centroid
ctr_lon = ctr.x.item()
ctr_lat = ctr.y.item()

md = f'# {text.title}\n\n### {text.author}\n\n'
md += '#### Jardín Botánico de Bogotá, eje Conservación _in situ_'
md += f'{text.main}\n\n#\n\n'
st.markdown(md)


with st.container(border=True, horizontal_alignment='center'):

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

	bar0 = px.bar(
		inter_all_df, 
		y="Interacción", 
		x="Registros",
		color="Potencial invasor",
		title='Interacciones de plantas nativas',
		color_discrete_sequence=['Bisque', 'DarkRed', 'Coral']
	)

	#bar0 = bar0.update_layout(height=500)
	st.plotly_chart(bar0)


with st.container(border=True, horizontal_alignment='center'):

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


with st.container(border=True, horizontal_alignment='center'):

	st.markdown("**Localidades de Bogotá y registros de interacciones bióticas**")

	fig = px.choropleth_map(
		loc,
		title='Interacciones',
		geojson=loc.geometry,
		locations=loc.index,
		hover_name="Localidad",
		hover_data={"Clases":True, "Registros": True},
		color="Registros",
		labels={
			"Clases":"Clases de interacciones",
			"Registros": "Número de registros"
		},
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


exit(0)