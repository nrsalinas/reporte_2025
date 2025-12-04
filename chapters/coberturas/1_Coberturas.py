import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

cob_ori_file = "chapters/coberturas/dat/Ecosistemas_originaless_v7.shp"
cob_act_file = "chapters/coberturas/dat/Ecosistemas_actuales_v5.shp"
logo = "shared/figs/Color.png"

###  Map data

cob_ori = gpd.read_file(cob_ori_file)
cob_ori = cob_ori.to_crs(4326)
ctr = cob_ori.dissolve().centroid
ctr_lon = ctr.x.item()
ctr_lat = ctr.y.item()

cob_act = gpd.read_file(cob_act_file)
cob_act = cob_act.to_crs(4326)



#######################
#      plot map
#######################

with st.container(border=True, horizontal_alignment='center'):

	fig = px.choropleth_map(
		cob_ori,
		title='Número de especies por localidad',
		geojson=cob_ori.geometry,
		locations=cob_ori.index,
		hover_name="Eco1",
		color="Eco1",
		labels={"Eco1": "Ecosistema original"},
		color_discrete_sequence=[
			'Olive', #Arbustal
			'Green', #Bosque                     
			'Black', #Complejos Rocosos          
			'DarkCyan', #Cuerpo de Agua Artificial  
			'DarkSeaGreen', #Herbazal                   
			'Blue', #Laguna                     
			'SaddleBrown', #Paramo                     
			'Teal', #Rio                        
			'OrangeRed', #Subxerofitia               
			'Gray', #Territorio Artificializado 
			'LightSeaGreen', #Turbera                    
			'DodgerBlue', #Zona Pantanosa 
		],
		opacity=0.7,
	)

	fig.update_geos(
		fitbounds="geojson", 
		visible=False,
		bgcolor='rgba(0,0,0,0)',
		framewidth=3,
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