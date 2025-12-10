import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from chapters.flora import text

loc_file = "shared/loca/Loca.shp"
loc_spp_csv = "chapters/flora/dat/Especies_localidad.csv"
fam_file = "chapters/flora/dat/Familias_mas_diversas.csv"
gen_file = "chapters/flora/dat/Generos_mas_diversos.csv"

espeletia_pic = "chapters/flora/figs/Espeletia-nicolas-torres-fernandez-sinfondo.png"
epidendrum_pic = "chapters/flora/figs/Epidendrum_ibaguense_Pseudopanax.jpg"
logo = "shared/figs/Color.png"

###  Bar data

fams = pd.read_csv(fam_file)
gens = pd.read_csv(gen_file)

###  Map data

loc = gpd.read_file(loc_file)
loc = loc.to_crs(4326)
ctr = loc.dissolve().centroid
ctr_lon = ctr.x.item()
ctr_lat = ctr.y.item()
loc["LocNombre"] = loc.LocNombre.str.title()
loc_spp = pd.read_csv(loc_spp_csv)
#st.dataframe(loc_spp)
loc = loc.merge(loc_spp, left_on="LocNombre", right_on="Localidad", how="left")
#st.dataframe(loc)

###  Pie data

ori = {'Origen': ['Introducida', 'Nativa'], 'Porcentaje': [32, 68]}
oripd = pd.DataFrame.from_dict(ori)
#st.dataframe(oripd)

cat = {'Categoría': ['En Peligro Crítico', 'En Peligro', 'Vulnerable'], 'Porcentaje': [14, 46, 40]}
catpd = pd.DataFrame.from_dict(cat)
#st.dataframe(oripd)

md = f'# {text.title}\n\n### {text.author}\n\n'
md += '#### Jardín Botánico de Bogotá, eje Conservación _in situ_'
md += f'{text.main}\n\n#\n\n'
st.markdown(md)


#######################
#      pie plots
#######################

with st.container(border=True, horizontal_alignment='center'):

	pie = px.pie(oripd, values='Porcentaje', names='Origen', color_discrete_sequence=['LightSalmon', 'DarkRed'])
	st.plotly_chart(pie)

	st.markdown("""
	La mayoría de plantas de Bogotá son originarias de ecosistemas nativos, 
	como páramos y bosques.
	""")

with st.container(border=True, horizontal_alignment='center'):

	pie2 = px.pie(catpd, values='Porcentaje', names='Categoría', color_discrete_sequence=['OrangeRed', 'DarkRed', 'LightSalmon'])
	st.plotly_chart(pie2)

	st.markdown("""
	En Bogotá existen **108 especies** de plantas amenazadas.
	""")


###  Bar plot

with st.container(border=True):

	st.bar_chart(
		fams, 
		x="Familia", 
		y="Número de especies",
		sort="-Número de especies",
		color="#b65c28",
		height=500
	)

	#st.markdown("""#""")

	left_co, right_co = st.columns(2, vertical_alignment='center')
	
	with left_co:
		st.image(espeletia_pic, caption="@ Nicolás Torres Fernandez")

	with right_co:
		st.markdown("""
			Las **compuestas** (el grupo de los frailejones, girasoles, manzanillas y caléndula) son el grupo más diverso de flora bogotana.			
		""")

st.markdown("""
#			
""")

with st.container(border=True):

	st.bar_chart(
		gens, 
		x="Género", 
		y="Número de especies",
		sort="-Número de especies",
		color="#b65c28",
		height=500
	)

	#st.markdown("""#""")

	left_co, right_co = st.columns(2, vertical_alignment='center')
	
	with left_co:
		st.image(epidendrum_pic, caption="@ Pseudopanax")

	with right_co:
		st.markdown("""
			__*Epidendrum*__ es el género de plantas vasculares más diverso en Bogotá.			
		""")


#######################
#      plot map
#######################

with st.container(border=True, horizontal_alignment='center'):

	fig = px.choropleth_map(
		loc,
		title='Número de especies por localidad',
		geojson=loc.geometry,
		locations=loc.index,
		hover_name="Localidad",
		hover_data={"No. especies":True},
		color="No. especies",
		labels={"No. especies": "Número de especies"},
		color_continuous_scale="Reds",
		opacity=0.7,
		#marker_line_width=2,  # Thin line for boundaries
		#marker_line_color='white',  # Boundary color
		#projection="mercator"
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