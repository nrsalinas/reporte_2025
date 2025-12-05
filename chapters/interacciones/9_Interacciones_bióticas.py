import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

inter_all = "chapters/interacciones/dat/interacciones_todas_long.csv"
inter_no_nat = "chapters/interacciones/dat/interacciones_no_nativas_long.csv"
spp_nat = "chapters/interacciones/dat/spp_nativas.csv"
spp_no_nat = "chapters/interacciones/dat/spp_no_nativas.csv"
loc_file = "chapters/interacciones/dat/mapa/interact.shp"


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

st.markdown("""
			
# Interacciones bióticas
			
### Juan Camilo Garibello, Angela Montoya, Esteban Tulande y Juliana Zuluaga

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
Las interacciones planta-animal son relaciones ecológicas que incluyen mutualismos (como polinización y dispersión de semillas) y antagonismos (herbivoría, depredación), entre otras. Estas interacciones son fundamentales para el funcionamiento de los ecosistemas, la biodiversidad y la evolución de especies, influyendo en la estructura y dinámica de comunidades naturales. Por otro lado, las invasiones de especies exóticas provocan una reducción significativa de la biodiversidad nativa, alterando la composición y estructura de comunidades vegetales y animales. Además, afectan servicios ecosistémicos clave, como la provisión de alimentos, la regulación de la erosión y la polinización, comprometiendo el bienestar humano. La capacidad de las plantas exóticas invasoras para interactuar con la fauna del ecosistema receptor puede influir en el éxito o no de la invasión. Sin embargo, este aspecto ha sido menos estudiado en comparación con otros factores como la competencia con plantas nativas, la abundante producción de semillas y la explotación eficiente de recursos. En Bogotá, las plantas invasoras (tanto nativas como exóticas) mantienen interacciones con la biota local. No obstante, las interacciones de plantas invasoras dentro del grupo de especies foráneas son más comunes: alcanzan el 20% de los registros de visitas florales y herbivoría, y el 34% de los registros de epibiosis (colonización de la superficie de la planta por parte de otros organismos como musgos y líquenes , Figura 1). Los registros que involucraron plantas invasoras dentro del grupo de nativas no superaron el 7% al examinar las mismas interacciones (Figura 2). Cuatro plantas con estatus invasor según "Global Invasive Species Data Base" (GISD) aparecieron entre las 10 especies más registradas en el grupo de exóticas: la palma *Phoenix canariensis* (primer puesto), el árbol *Pittosporum undulatum* (séptima) y las hierbas *Taraxacum officinale* e *Hypochaeris radicata* (cuarta y décima, respectivamente) (Figura 3). *Pittosporum*, una planta ampliamente cultivada a lo largo y ancho de la ciudad, es de particular preocupación dado que se han reportado invasiones de esta especie en bosques montanos tropicales. La literatura reporta efectos ecológicos tanto negativos como positivos de las interacciones de plantas invasoras con biota del ecosistema residente, sin importar si se trata de relaciones en principio mutualistas o en principio antagónicas. La oferta floral de plantas invasoras puede beneficiar polinizadores nativos o la oferta alimenticia de sus hojas puede aumentar la abundancia de insectos invasores a expensas de plantas e insectos nativos. Por lo anterior, es necesario estudiar este tipo de interacciones a mayor profundidad con el fin de entender las invasiones y diseñar, probar y validar alternativas de control.
			

""")


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

exit(0)