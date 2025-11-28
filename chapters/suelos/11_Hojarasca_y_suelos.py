import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

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

st.markdown("""
			
# Hojarasca y suelos en áreas de importancia ecológica de Bogotá
			
### Angie Montañez y Luisa Betancourt

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
En áreas verdes urbanas, el suelo además de ser un refugio de biodiversidad es un aliado estratégico para la mitigación del cambio climático. En este estudio se analizó la variación del aporte de hojarasca fina, el flujo de CO<sub>2</sub> y algunas propiedades del suelo (carbono, materia orgánica, pH y densidad aparente) en tres áreas de importancia ecológica de Bogotá (El Jardín Botánico de Bogotá, Las Mercedes y el Bosque Urbano de Ciudad Montes - BUCM). El Jardín Botánico exhibió un mayor aporte de hojarasca (4.17 t ha<sup>-1</sup>) y flujo de CO<sub>2</sub> (2.77 µmol m<sup>-2</sup> s<sup>-1</sup>), lo que sugiere mejor actividad biológica y respiratoria en el suelo. En las Mercedes se presentaron valores intermedios de hojarasca y CO<sub>2</sub> del suelo; mientras que el BUCM presentó los valores más bajos en aporte de hojarasca (1.49 t ha<sup>-1</sup>) y flujo de CO<sub>2</sub> (1.56 µmol m<sup>-2</sup> s<sup>-1</sup>). En relación con las propiedades del suelo, el BUCM exhibió un valor alto de carbono orgánico (180.2 t ha<sup>-1</sup>), sugiriendo un alto potencial de secuestro de carbono pese a que la densidad aparente refleja compactación y baja aireación del suelo. Estos hallazgos evidencian que las áreas verdes urbanas pueden actuar como sumideros de carbono, especialmente cuando se implementan prácticas de conservación del suelo, como mantener la cobertura de hojarasca.
			
""", unsafe_allow_html=True)

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