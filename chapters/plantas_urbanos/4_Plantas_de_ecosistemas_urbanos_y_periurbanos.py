import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from chapters.plantas_urbanos import text

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

md = f'# {text.title}\n\n### {text.author}\n\n'
md += '#### Jardín Botánico de Bogotá, eje Conservación _in situ_'
md += f'{text.main}\n\n#\n\n'
st.markdown(md)

with st.container(border=True, horizontal_alignment='center'):

	st.markdown('**Origen geográfico de las plantas de enclaves subxerofíticos**')
	pie0 = px.pie(
		encl_ori, 
		values='Porcentaje', 
		names='Origen', 
		#title='Origen geográfico de las plantas de enclaves subxerofíticos',
		color_discrete_sequence=['#92a311', '#d9c663']
	)
	st.plotly_chart(pie0)

	st.markdown('**Origen geográfico de las plantas de humedales**')
	pie1 = px.pie(
		hum_ori, 
		values='Porcentaje', 
		names='Origen', 
		#title='Origen geográfico de las plantas de humedales',
		color_discrete_sequence=['#92a311', '#d9c663']
	)
	#pie1 = pie1.update_layout(showlegend=False)
	st.plotly_chart(pie1)

	st.markdown('**Origen geográfico de las plantas de parques urbanos**')
	pie2 = px.pie(
		parq_ori, 
		values='Porcentaje', 
		names='Origen', 
		#title='Origen geográfico de las plantas de parques urbanos',
		color_discrete_sequence=['#92a311', '#d9c663']
	)
	#pie2 = pie2.update_layout(showlegend=False)
	st.plotly_chart(pie2)

	st.markdown("""
	La gran mayoría de plantas de los enclaves subxerofíticos son nativas, 
	pero en los humedales y los parques urbanos este panorama cambia, dado que 
	existe una proporción significativa de flora introducida an ambas unidades.
	""")

with st.container(border=True, horizontal_alignment='center'):

	st.markdown('**Endemismo**')
	pie3 = px.pie(
		end, 
		values='Porcentaje', 
		names='Ecosistema', 
		#title='Endemismo',
		color_discrete_sequence=['#36811c','#859f0c','#e0cd72']
	)
	#pie3 = pie3.update_layout(showlegend=False)
	st.plotly_chart(pie3)

	st.markdown("""
	Se registraron varias especies endémicas de Colombia en los ecosistemas urbanos 
	de Bogotá, principalmente en los parques urbanos.
	""")

with st.container(border=True, horizontal_alignment='center'):

	st.markdown('**Plantas amenazadas**')
	myyy = [i for i in iucn_pd.columns if i != 'Ecosistema']
	bar0 = px.bar(
		iucn_pd, 
		x='Ecosistema', 
		y = myyy,
		#title='Plantas amenazadas',
		color_discrete_sequence=["#18351f", "#1f7425", "#809d0b", "#b1af2c", "#f3e9ab"]
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
		color_discrete_sequence=['DodgerBlue', 'DarkOliveGreen', 'SandyBrown'],
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

