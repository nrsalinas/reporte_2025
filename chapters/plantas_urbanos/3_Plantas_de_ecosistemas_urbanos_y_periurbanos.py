import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px


logo = "shared/figs/Color.png"




###  Chart data

encl_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [8.5, 91.5]}
encl_ori_pd = pd.DataFrame.from_dict(encl_ori)

hum_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [41.6, 58.4]}
hum_ori_pd = pd.DataFrame.from_dict(hum_ori)

parq_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [47, 53]}
parq_ori_pd = pd.DataFrame.from_dict(parq_ori)
#st.dataframe(parq_ori_pd)

end = {
	'Ecosistema': ['Subxerofítico', 'Humedal', 'Urbano'],
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
			
Bogotá tiene muchas plantas! Yeah! 
			
""")

with st.container(border=True, horizontal_alignment='center'):

	pie0 = px.pie(encl_ori, values='Porcentaje', names='Origen', color_discrete_sequence=['LightSalmon', 'DarkRed'])
	st.plotly_chart(pie0)

	pie1 = px.pie(hum_ori, values='Porcentaje', names='Origen', color_discrete_sequence=['LightSalmon', 'DarkRed'])
	pie1 = pie1.update_layout(showlegend=False)
	st.plotly_chart(pie1)

	pie2 = px.pie(parq_ori, values='Porcentaje', names='Origen', color_discrete_sequence=['LightSalmon', 'DarkRed'])
	pie2 = pie2.update_layout(showlegend=False)
	st.plotly_chart(pie2)

	st.markdown("""
	La mayoría de plantas de los enclaves sub-xerofíticos son nativas.
	""")

with st.container(border=True, horizontal_alignment='center'):

	pie3 = px.pie(end, values='Porcentaje', names='Ecosistema', color_discrete_sequence=['Bisque', 'DarkRed', 'Coral'])
	#pie3 = pie3.update_layout(showlegend=False)
	st.plotly_chart(pie3)

	st.markdown("""
	Se registraron varias especies endémicas de Colombia.
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

left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)

