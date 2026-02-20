import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from chapters.artropofauna import text

loc_file = "shared/loca/Loca.shp"
artr_map = "chapters/artropofauna/dat/riqueza_localidad.shp"
logo = "shared/figs/Color.png"

###  Map data

loc = gpd.read_file(artr_map)
loc = loc.to_crs(4326)
ctr = loc.dissolve().centroid
ctr_lon = ctr.x.item()
ctr_lat = ctr.y.item()
#loc["LocNombre"] = loc.LocNombre.str.title()

md = f'# {text.title}\n\n### {text.author}\n\n'
md += '#### Jardín Botánico de Bogotá, eje Conservación _in situ_'
md += f'{text.main}\n\n#\n\n'
st.markdown(md)

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
		hover_data={"Riqueza":True},
		color="Riqueza",
		labels={"Riqueza": "Número de especies"},
		#color_continuous_scale="Reds",
		color_continuous_scale="Speed",
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

st.markdown(f'### Referencias\n\n{text.references}\n\n#\n\n')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)



exit()