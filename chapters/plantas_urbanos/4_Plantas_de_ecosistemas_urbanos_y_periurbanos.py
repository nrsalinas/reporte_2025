import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px


logo = "shared/figs/Color.png"
shape_file = "chapters/plantas_urbanos/dat/shape/ecos.shp"


###   Plot data   ###

shape = gpd.read_file(shape_file)
shape = shape.to_crs(4326)

###  Chart data   ###

encl_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [8.5, 91.5]}
encl_ori_pd = pd.DataFrame.from_dict(encl_ori)

hum_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [41.6, 58.4]}
hum_ori_pd = pd.DataFrame.from_dict(hum_ori)

parq_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [47, 53]}
parq_ori_pd = pd.DataFrame.from_dict(parq_ori)
#st.dataframe(parq_ori_pd)

end = {
	'Ecosistema': ['Enclaves secos', 'Humedales', 'Parques urbanos'],
	'Porcentaje': [17, 24, 63]	
}
end_pd = pd.DataFrame.from_dict(end)

iucn = {
	'Ecosistema': ['Enclaves secos', 'Humedales', 'Parques urbanos'],
	'Peligro Crítico': [0, 6, 2],
	'En Peligro': [0, 8, 8],
	'Vulnerable': [2, 7, 6],
	'Casi Amenazado': [2, 11, 21],
	'Preocupación Menor': [17, 105, 108],
}
iucn_pd = pd.DataFrame.from_dict(iucn)


st.markdown("""
			
# Plantas de los ecosistemas urbanos y peri-urbanos de Bogotá
			
### Esther Velásquez, Lina Corrales y José Guerrero

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
La documentación de la flora de Bogotá ha sido una tarea continua desde el siglo XVIII, cuando la real expedición botánica —liderada por José Celestino Mutis— inició el registro de la riqueza vegetal del territorio. Más de dos siglos después, y pese a los numerosos esfuerzos posteriores de investigación, aún persisten vacíos en el conocimiento sobre la composición y el estado de conservación de la flora en el Distrito Capital. Esta investigación busca aportar a la consolidación de esa información mediante la integración de tres estudios desarrollados en 2025 por el eje Conservación _in situ_ del Jardín Botánico de Bogotá: la flora de enclaves subxerofíticos andinos, la flora de humedales urbanos y la flora de parques urbanos. 
			
El objetivo de este trabajo conjunto fue caracterizar la diversidad vegetal de tres tipos de ecosistemas representativos de la matriz ecológica urbana y periurbana, fortaleciendo la línea base de flora de Bogotá y evidenciando su papel en la conectividad ecológica y la provisión de servicios ecosistémicos. La consolidación de estas investigaciones permitió generar un panorama unificado de la vegetación bogotana, facilitando el análisis comparativo entre ecosistemas y promoviendo la gestión integrada para su conservación.
			
En los enclaves secos andinos se evidenció una flora predominantemente nativa, rica en especies adaptadas a condiciones de aridez, con rasgos morfológicos como suculencia, espinas y crecimiento herbáceo. Estos ecosistemas conservan un conjunto importante de especies endémicas y constituyen refugios azonales de biodiversidad únicos en el paisaje periurbano de Bogotá. Los humedales urbanos, por otro lado, son de composición mixta, donde conviven especies locales y exóticas, reflejando la influencia antrópica sobre estos ecosistemas. A pesar de ello, mantienen un papel esencial en la conectividad ecológica, la regulación hídrica y la provisión de hábitats para la fauna silvestre. En los parques urbanos, la vegetación representa una transición entre lo nativo y las especies foráneas, con una alta representatividad de especies endémicas, destacando su función como corredores ecológicos y espacios de interacción entre la ciudadanía y la biodiversidad. Estos tres ecosistemas albergan numerosas especies en diferentes categorías de amenaza, lo que resalta la necesidad de fortalecer las acciones de restauración ecológica, manejo de la flora nativa y conservación de los ecosistemas.

En conjunto, este primer Reporte de Estado de la Diversidad en plantas de los ecosistemas urbanos y periurbanos de Bogotá evidencia la alta riqueza florística de la ciudad y la necesidad de continuar unificando datos y esfuerzos interinstitucionales para cerrar vacíos de información, promover la investigación aplicada y consolidar una gestión urbana más resiliente frente al cambio climático. 
			
""")

with st.container(border=True, horizontal_alignment='center'):

	pie0 = px.pie(
		encl_ori, 
		values='Porcentaje', 
		names='Origen', 
		title='Origen geográfico de las plantas de enclaves subxerofíticos',
		color_discrete_sequence=['LightSalmon', 'DarkRed']
	)
	st.plotly_chart(pie0)

	pie1 = px.pie(
		hum_ori, 
		values='Porcentaje', 
		names='Origen', 
		title='Origen geográfico de las plantas de humedales',
		color_discrete_sequence=['LightSalmon', 'DarkRed']
	)
	#pie1 = pie1.update_layout(showlegend=False)
	st.plotly_chart(pie1)

	pie2 = px.pie(
		parq_ori, 
		values='Porcentaje', 
		names='Origen', 
		title='Origen geográfico de las plantas de parques urbanos',
		color_discrete_sequence=['LightSalmon', 'DarkRed']
	)
	#pie2 = pie2.update_layout(showlegend=False)
	st.plotly_chart(pie2)

	st.markdown("""
	La gran mayoría de plantas de los enclaves subxerofíticos son nativas, 
	pero en los humedales y los parques urbanos este panorama cambia, dado que 
	existe una proporción significativa de flora introducida an ambas unidades.
	""")

with st.container(border=True, horizontal_alignment='center'):

	pie3 = px.pie(
		end, 
		values='Porcentaje', 
		names='Ecosistema', 
		title='Endemismo',
		color_discrete_sequence=['Bisque', 'DarkRed', 'Coral']
	)
	#pie3 = pie3.update_layout(showlegend=False)
	st.plotly_chart(pie3)

	st.markdown("""
	Se registraron varias especies endémicas de Colombia en los ecosistemas urbanos 
	de Bogotá, principalmente en los parques urbanos.
	""")

with st.container(border=True, horizontal_alignment='center'):

	myyy = [i for i in iucn_pd.columns if i != 'Ecosistema']
	bar0 = px.bar(
		iucn_pd, 
		x='Ecosistema', 
		y = myyy,
		title='Plantas amenazadas',
		color_discrete_sequence=[
			'FireBrick',
			'IndianRed',
			'DarkSalmon',
			'SeaGreen',
			'MediumTurquoise'
		]
	)
	bar0 = bar0.update_layout(height=500)
	st.plotly_chart(bar0)


###   plot maps   ###

with st.container(border=True, horizontal_alignment='center'):

	st.markdown("Localización de los principales ecosistemas urbanos de la ciudad: :blue[humedales], :green[parques urbanos] y :orange[enclaves subxerofíticos]")

	fig = px.choropleth_map(
		shape,
		title='Ecosistemas urbanos',
		geojson=shape.geometry,
		locations=shape.index,
		hover_name="Ecosistema",
		color="Ecosistema",
		color_discrete_sequence=['Blue', 'Green', 'OrangeRed'],
		opacity=0.7,
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
		height=1300,
		map=dict(
			center={"lat":4.645310, "lon":-74.113101},
			zoom=11,
		),
		showlegend=False,
		coloraxis_showscale=False
	)

	st.plotly_chart(fig, use_container_width=True)

st.markdown("""#""")


left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)

