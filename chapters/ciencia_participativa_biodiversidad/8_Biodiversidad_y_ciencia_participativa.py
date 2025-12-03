import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px

loc_file = "shared/loca/Loca.shp"
loc_data_csv = "chapters/ciencia_participativa_biodiversidad/dat/localidades_comms.csv"
comm_file = "chapters/ciencia_participativa_biodiversidad/dat/comms.csv"
recs_file = "chapters/ciencia_participativa_biodiversidad/dat/recs_group.csv"
recs_spp_file = "chapters/ciencia_participativa_biodiversidad/dat/recs_spp.csv"

colibri_pic = "chapters/ciencia_participativa_biodiversidad/figs/Colibri_coruscans_Consuelo_Sanchez.jpg"
apis_pic = "chapters/ciencia_participativa_biodiversidad/figs/Apis_mellifera_Ivar_Leidus.jpg"
turdus_pic = "chapters/ciencia_participativa_biodiversidad/figs/Turdus_fuscater_Dick_Daniels.jpg"
logo = "shared/figs/Color.png"


####    Pie data    ####

comm = pd.read_csv(comm_file)
recs = pd.read_csv(recs_file)

####    Bar data    ####

spp = pd.read_csv(recs_spp_file)

####    Load map data   #####

loc = gpd.read_file(loc_file)
loc = loc.to_crs(4326)
loc_data = pd.read_csv(loc_data_csv)		
#st.dataframe(loc_data)
loc["Localidad"] = loc.LocNombre.str.title()
loc = loc.merge(loc_data, on="Localidad", how="left")
loc = loc.fillna(0)
#st.markdown(" - ".join(loc.columns.tolist()))

st.markdown("""
			
# Biodiversidad y ciencia participativa
			
### Ángela Montoya

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
La Ciencia Participativa es una estrategia que permite la generación del conocimiento de la biodiversidad mediante la observación y registro de especies en distintos puntos de Bogotá, vinculando a la comunidad en los procesos de investigación y conservación. El Jardín Botánico de Bogotá ha venido implementando dicha estrategia en diferentes puntos de la ciudad, contando con la participación de 42 observadores distribuidos en nueve comunidades: cuatro en etapa de diagnóstico, dos en caracterización y tres en monitoreo.
Esta estrategia ha permitido el registro de 3303 observaciones de fauna (aves y artrópodos) y flora. En total, se han reportado 90 especies de aves, 158 de artrópodos y 248 de flora, de las cuales el 45% corresponden a especies nativas y el 55% a no nativas. La localidad con mayor número de observaciones es Usaquén, con 10133, seguida de Teusaquillo (377), Puente Aranda (372) y Kennedy (289). También se registró la presencia de especies migratorias, especialmente en las localidades del sur y centro de la ciudad, como _Piranga rubra_ (la más observada con 60 registros), _Buteo platypterus_ (41 observaciones) y _Contopus virens_ (33 observaciones).  
			
Esta estrategia fomenta la educación ambiental, el reconocimiento de la biodiversidad urbana y la generación de datos científicos colaborativos que fortalecen la gestión ambiental de la ciudad.

""")


####    Pie plots    ####

with st.container(border=True, horizontal_alignment='center'):

	pie = px.pie(
		comm, 
		values='Número de grupos', 
		names='Etapa', 
		color_discrete_sequence=['OrangeRed', 'DarkRed', 'LightSalmon']
	)
	st.plotly_chart(pie)

	st.markdown("""
	Existen nueve grupos de observadores en el programa en diferentes etapas de formación en ciencia participativa.
	""")

with st.container(border=True, horizontal_alignment='center'):

	pie = px.pie(
		recs,
		values='Número de especies', 
		names='Grupo biológico', 
		color_discrete_sequence=['OrangeRed', 'DarkRed', 'LightSalmon']
	)
	st.plotly_chart(pie)

	st.markdown("""
	Los registros de biodiversidad del programa de Ciencia Participativa se han concentrado en 3 grupos biológicos: plantas, aves y artrópodos.
	""")

####    Bar plot    ####

with st.container(border=True, horizontal_alignment='center'):

	st.bar_chart(
		spp, 
		x="Especie", 
		y="Número de registros",
		sort="-Número de registros",
		color="#b65c28",
		height=500
	)

	left_co, ctr_co, right_co = st.columns(3, vertical_alignment='center')
	
	with left_co:
		st.image(colibri_pic, caption="@ Consuelo Sánchez")

	with ctr_co:
		st.image(apis_pic, caption="@ Ivar Leidus")

	with right_co:
		st.image(turdus_pic, caption="@Dick Daniels")


	st.markdown("""
	Entre las especies más comunmente registradas se encuentran el colibrí chillón, 
	la abeja común y la mirla patinaranja.
	""")


#########    Plot map     ########

with st.container(border=True, horizontal_alignment='center'):

	fig = px.choropleth_map(
		loc,
		title='Localidades de trabajo',
		geojson=loc.geometry,
		locations=loc.index,
		hover_name="Localidad",
		hover_data={
			"Zona de estudio":True,
			"Número de observaciones":True,
			"Número de observadores":True,
			"Flora":True,
			"Aves residentes":True,
			"Aves migratorias":True,
			"Artropodos":True
		},
		color="Número de observaciones",
		#labels={"No. especies": "Número de especies"},
		color_continuous_scale="Reds",
		opacity=0.7,
		#marker_line_width=2,  # Thin line for boundaries
		#marker_line_color='white',  # Boundary color
		#projection="mercator"
	)
	
#	fig.update_geos(
#		fitbounds="geojson", 
#		visible=False,
#		bgcolor='rgba(0,0,0,0)',
#		framewidth=3,
#		)

	fig.update_layout(
		margin={"r":0,"t":0,"l":0,"b":0},
		paper_bgcolor='rgba(0,0,0,0)',
		height=700,
		map=dict(
			center={"lat":4.645310, "lon":-74.113101},
			zoom=10,
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