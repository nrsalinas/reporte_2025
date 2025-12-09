import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

cob_ori_file = "chapters/coberturas/dat/Ecosistemas_originaless_v7_light.shp"
cob_act_file = "chapters/coberturas/dat/Ecosistemas_actuales_v5_light.shp"
logo = "shared/figs/Color.png"

###  Map data

cob_ori = gpd.read_file(cob_ori_file)
cob_ori = cob_ori.to_crs(4326)
ctr = cob_ori.dissolve().centroid
ctr_lon = ctr.x.item()
ctr_lat = ctr.y.item()

cob_act = gpd.read_file(cob_act_file)
cob_act = cob_act.to_crs(4326)

st.markdown("""
			
# Coberturas
			
### Hernán Serrano

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
El estudio de las coberturas de la tierra y los ecosistemas es esencial para comprender la dinámica territorial y garantizar una planificación urbana sostenible. Las coberturas actuales representan el uso que el ser humano le da al territorio, mientras que el estudio de los ecosistemas de referencia revela el potencial natural y la vocación de la tierra. La comparación entre ambos es útil para:
			
- Cuantificar la pérdida de biodiversidad y la degradación de hábitats.

- Evaluar la presión antrópica sobre recursos vitales (como el agua y el suelo).

- Identificar áreas prioritarias para la conservación y la restauración ecológica, asegurando que las intervenciones estén dirigidas a reconstruir el Ecosistema Potencial de Referencia (EPR).

Para el territorio de Bogotá, D. C., esta información es vital para la gestión del riesgo y la toma de decisiones relativas a la Estructura Ecológica Principal (EEP), especialmente en zonas de alta fragilidad como el páramo y el bosque altoandino. Para ello se delimitaron espacialmente los diferentes ecosistemas utilizando la base cartográfica del Mapa de Ecosistemas Continentales, Costeros y Marinos (MEC) a escala 1:100.000 (IDEAM 2024). De esta manera se identificaron 12 ecosistemas, entre los que destacan los páramos (55%) y los bosques (15%), que ocupan un 70% del territorio. Por otro lado, los territorios artificializados (IDEAM 2024) cubren cerca del 21% del área de la ciudad. 

El área correspondiente a ecosistemas transformados, asociados a procesos de intervención (principalmente producción agropecuaria y expansión urbana), fue reconstruida a su Ecosistema Potencial de Referencia (EPR). Los resultados indican que el 70% de las áreas transformadas correspondían a páramos y bosques altoandinos en el pasado, y que más de la mitad de los ecosistemas originales de Bogotá han desaparecido o están transformados en áreas urbanas y agroecosistemas. De esta manera, los ecosistemas con mayor transformación son humedales (88%), bosques (81%), enclaves subxerofíticos (77%) y páramos (50%).

Que el 70% de nuestras áreas impactadas tengan el potencial de volver a ser páramo o bosque altoandino no es solo una cifra, es una oportunidad tangible y urgente. La mitad de nuestros ecosistemas originales esperan nuestra acción. Proteger lo que queda y trabajar decididamente para restaurar el potencial natural de estas áreas no es solo una meta ambiental, sino una inversión directa en la calidad del aire, el suministro de agua y la seguridad frente a los riesgos. El momento de actuar es ahora y requiere el compromiso colectivo de cada ciudadano para garantizar la sostenibilidad y el bienestar de las próximas generaciones.

#
			
""")

#######################
#      plot map
#######################

with st.container(border=True, horizontal_alignment='center'):

	st.markdown("**Coberturas vegetales originales**")

	fig = px.choropleth_map(
		cob_ori,
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

with st.container(border=True, horizontal_alignment='center'):

	st.markdown("**Coberturas vegetales actuales**")

	fig = px.choropleth_map(
		cob_act,
		geojson=cob_act.geometry,
		locations=cob_act.index,
		hover_name="ecos_sinte",
		color="ecos_sinte",
		labels={"ecos_sinte": "Ecosistema actual"},
		color_discrete_sequence=[
			'LightSteelBlue', # Agroecosistema            
			'Olive', # Arbustal                  
			'Green', # Bosque                    
			'DarkSeaGreen', # Bosque Fragmentado        
			'Black', # Complejos Rocosos         
			'DarkCyan', # Cuerpo de Agua Artificial 
			'DarkSeaGreen', # Herbazal                  
			'Blue', # Laguna                    
			'SaddleBrown', # Paramo                    
			'Teal', # Rio                       
			'OrangeRed', # Subxerofitia              
			'Gray', # Territorio Artificializado
			'LightSlateGrey', # Transicional Transformado 
			'LightSeaGreen', # Turbera                   
			'LightGreen', # Vegetacion Secundaria     
			'DodgerBlue', # Zona Pantanosa            
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