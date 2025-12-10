import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from chapters.suelos import text

hojar_file = "chapters/suelos/dat/comp_hoja.csv"
flujos_file = "chapters/suelos/dat/flujos.csv"
compos_file = "chapters/suelos/dat/composs.csv"
sites_file = "chapters/suelos/dat/sitios.csv"
logo = "shared/figs/Color.png"

###   Bar data

hojar = pd.read_csv(hojar_file)
flujos = pd.read_csv(flujos_file)
compos = pd.read_csv(compos_file)

###   Map data

sites = pd.read_csv(sites_file)

md = f'# {text.title}\n\n### {text.author}\n\n'
md += '#### Jardín Botánico de Bogotá, eje Conservación _in situ_'
md += f'{text.main}\n\n#\n\n'
st.markdown(md, unsafe_allow_html=True)

with st.container(border=True, horizontal_alignment='center'):

	bar = px.bar(
		hojar, 
		y="Densidad (t ha⁻¹)", 
		x="Sitio",
		color="Componente de hojarasca",
		barmode='group',
		title='Composición de la hojarasca',
		color_discrete_sequence=['OrangeRed', 'DarkRed', 'LightSalmon', 'Bisque']
	)

	#bar = bar.update_layout(height=500)
	st.plotly_chart(bar)

with st.container(border=True, horizontal_alignment='center'):

	bar1 = px.bar(
		flujos, 
		x="Flujo CO₂ (microl m² s⁻¹)", 
		y="Sitio",
		title='Flujo de CO₂ en el suelo',
		color_discrete_sequence=['DarkRed']
	)

	#bar1 = bar1.update_layout(height=500)
	st.plotly_chart(bar1)

with st.container(border=True, horizontal_alignment='center'):

	st.markdown("""**Principales variables fisico-químicas de los suelos estudiados**""")

	st.dataframe(compos)

with st.container(border=True, horizontal_alignment='center'):

	sites['Size'] = 15

	fig = px.scatter_map(
		sites,
		title="Lugares de trabajo en la vigencia 2025",
		lat='Latitud',
		lon='Longitud',
		hover_name = 'Sitio',
		hover_data={'Size':False, 'Latitud':False, 'Longitud':False},
		#color_continuous_scale=px.colors.cyclical.IceFire, 
		color_discrete_sequence=['OrangeRed'],
		zoom=10,
		size="Size",
		height=800
	)

	st.plotly_chart(fig, use_container_width=True)

st.markdown("""#""")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)


exit(0)