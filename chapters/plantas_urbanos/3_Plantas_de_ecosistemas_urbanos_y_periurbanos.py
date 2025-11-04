import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px


logo = "shared/figs/Color.png"




###  Pie data

encl_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [8.5, 91.5]}
encl_ori_pd = pd.DataFrame.from_dict(encl_ori)
#st.dataframe(oripd)

hum_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [41.6, 58.4]}
hum_ori_pd = pd.DataFrame.from_dict(hum_ori)
#st.dataframe(oripd)

parq_ori = {'Origen': ['Introducidas', 'Nativas'], 'Porcentaje': [47, 53]}
parq_ori_pd = pd.DataFrame.from_dict(parq_ori)
#st.dataframe(oripd)


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

left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)

