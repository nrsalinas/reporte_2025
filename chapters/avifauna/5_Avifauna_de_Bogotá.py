import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

####    Input files    ####

loc_file = 'chapters/avifauna/dat/shp/localidad/Localidad_resgistros_aves_v01.shp'
ard_alba = "chapters/avifauna/figs/Ardea_alba_JZC.JPG"
pod_pod = "chapters/avifauna/figs/Podilymbus podiceps_PMS0140.jpg"
oxy_jam = "chapters/avifauna/figs/Oxyura_jamaicensis_JZC.JPG"
ral_sem = "chapters/avifauna/figs/Rallus_semiplumbeus_Oswaldo_Cortes.jpg"
syn_sub = "chapters/avifauna/figs/Synallaxis_subpudica_PMS4136.jpg"
por_mel = "chapters/avifauna/figs/Porphyriops_melanops_JZC.JPG"
eri_ves = "chapters/avifauna/figs/Eriocnemis_vestita_PMS1084.jpg"
coe_hae = "chapters/avifauna/figs/Coeligena_helianthea_PMS8988.jpg"
pen_mon = "chapters/avifauna/figs/Penelope_motagnii_JZC.JPG"
cis_apo = "chapters/avifauna/figs/Cistothorus_apolinari_PMS1168.jpg"
oxy_gue = "chapters/avifauna/figs/Oxypogon_guerinii_PMS0903.jpg"
gra_alt = "chapters/avifauna/figs/Grallaria_alticola_PMS1043.jpg"
con_sit = "chapters/avifauna/figs/Dubusia_taeniata_Conirostrum_sitticolor_PMS8052.jpg"
and_nig = "chapters/avifauna/figs/Andigena_nigrirostris_PMS7745.jpg"
tur_fal = "chapters/avifauna/figs/Turdus_fuscater_PMS8290.jpg"
col_cor = "chapters/avifauna/figs/Colibri_coruscans _PMS7008.jpg"
logo = "shared/figs/Color.png"

####    Map data    ####

loc = gpd.read_file(loc_file)
loc = loc.to_crs(4326)
ctr = loc.dissolve().centroid
ctr_lon = ctr.x.item()
ctr_lat = ctr.y.item()
loc["Localidad"] = loc.LocNombre.str.title()


st.markdown("""
			
# Avifauna de Bogotá
			
### Juliana Zuluaga-Carrero

#### Jardín Botánico de Bogotá, eje Conservación _in situ_
			
Bogotá se ubica en la convergencia de ecosistemas de alta montaña formados por procesos geológicos y evolutivos de la cordillera oriental, lo que originó una avifauna única con especies endémicas y de distribución restringida. A pesar de su intensa transformación por el desarrollo urbano, la ciudad aún conserva remanentes de ecosistemas andinos que albergan una alta diversidad de aves, una cifra que alcanza 358 especies de aves. Sin embargo, cerca del 70% del territorio corresponde a zonas rurales donde persisten hábitats como humedales, cuerpos de agua, bosques andinos y altoandinos, enclaves secos, páramos y agroecosistemas.
			
La mayor parte de las especies registradas en la ciudad son residentes (78%), seguidas de migratorias boreales (17%), endémicas (2%), migratorias australes (1%) y exóticas establecidas (1%). Su presencia en ecosistemas urbanos, periurbanos y rurales resalta la importancia de Bogotá como un territorio clave para la conservación de la avifauna altoandina. Según las categorías del Libro Rojo de Aves de Colombia, el 89,16% de las especies de Bogotá no han sido evaluadas, mientras que el 6,96% se considera en categoría de preocupación menor (LC), un 1,46% vulnerables (VU), 1,13% en peligro (EN), 0,65% casi amenazadas (NT), 0,49% en peligro crítico (CR) y 0,16% con datos deficientes (DD).
			 
Actualmente el Jardín Botánico de Bogotá contribuye a un proyecto sombrilla llamado observatorio de biodiversidad y cambio climático, en el marco del cual hemos estado monitoreando la biodiversidad de la ciudad. El observatorio divide a la ciudad en 513 celdas de 2×2 km, en las cuales se analiza la información existente y también se toman nuevos datos. A la fecha, más del 60% de la ciudad no cuenta con registros y más del 50% de la información disponible está concentrada en 10 celdas, ubicadas en sitios el Parque Simón Bolívar, Jardín Botánico, Humedal Córdoba, Humedal Burro y Chisacá que llevan la delantera.

Estos valores reflejan tanto la riqueza de avifauna como la necesidad de fortalecer las acciones de monitoreo y protección de los espacios naturales donde estas aves aún subsisten. Con este reporte queremos resaltar el valor de los ecosistemas presentes en Bogotá, no solo como hábitat de especies emblemáticas y endémicas, sino también como espacios fundamentales para el bienestar humano. Aún tenemos una muy baja representación de la avifauna en enclaves secos, bosque altoandinos, plantaciones forestales, bosques urbanos e, incluso, páramos de la ciudad. Invitamos a la ciudadanía a conocer esta biodiversidad como primer paso para diseñar y fortalecer estrategias de conservación para entender sus requerimientos de conservación y asegurar su permanencia en el tiempo. 

#""")



####   plot map    ####

with st.container(border=True, horizontal_alignment='center'):

	st.markdown("**Número de registros por localidad**  \n  \n")

	fig = px.choropleth_map(
		loc,
		title='Número de registros por localidad',
		geojson=loc.geometry,
		locations=loc.index,
		hover_name="Localidad",
		hover_data={"Reg_aves":True},
		color="Reg_aves",
		labels={"Reg_aves": "Número de registros"},
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


st.markdown("#\n\n\n")

with st.container(border=True):

	st.markdown("""
	### Especies representativas de los cuerpos de agua
	####
	""")
	st.image(ard_alba, caption="Garza del ganado (*Ardea alba*). @Juliana Zuluaga.")
	st.markdown("---")
	st.image(pod_pod, caption="Pato zambullidor (*Podilymbus podiceps*). @PMS.")
	st.markdown("---")
	st.image(oxy_jam, caption="Pato turrio (*Oxyura jamaicensis*). @Juliana Zuluaga.")

with st.container(border=True):

	st.markdown("""
	### Especies representativas de humedales
	####
	""")
	st.image(ral_sem, caption="Tingua bogotana (*Rallus semiplumbeus*). @Oswaldo Cortés.")
	st.markdown("---")
	st.image(syn_sub, caption="Chamicero cundiboyacense (*Synallaxis subpudica*). @PMS.")
	st.markdown("---")
	st.image(por_mel, caption="Tingua de pico verde (*Porphyrio melanops*). @Juliana Zuluaga")

with st.container(border=True):

	st.markdown("""
	### Especies representativas de bosques altoandinos
	####
	""")
	st.image(eri_ves, caption="Colibri calzoncitos relucientes (*Eriocnemis vestita*). @PMS.")
	st.markdown("---")
	st.image(coe_hae, caption="*Coeligena haelianthea*. @PMS.")
	st.markdown("---")
	st.image(pen_mon, caption="Pava andina (*Penelope montagnii*). @Juliana Zuluaga")

with st.container(border=True):

	st.markdown("""
	### Especies representativas de páramo
	####
	""")
	st.image(cis_apo, caption="Cucarachero de pantano (*Cistothorus apolinari*). @PMS.")
	st.markdown("---")
	st.image(oxy_gue, caption="Barbudito de páramo (*Oxypogon guerinii*). @PMS.")
	st.markdown("---")
	st.image(gra_alt, caption="Tororoi muisca (*Grallaria quitensis*). @PMS")

with st.container(border=True):

	st.markdown("""
	### Especies representativas de bosques andinos
	####
	""")
	st.image(con_sit, caption="*Conirostrum siticolor* y *Dubusia taeniata*. @PMS.")
	st.markdown("---")
	st.image(and_nig, caption="Perlanque pechiazul (*Andigena nigrirostris*). @PMS.")

with st.container(border=True):

	st.markdown("""
	### Especies representativas de parque urbanos
	####
	""")
	st.image(tur_fal, caption="Mirla patinaranja (*Turdus fuscater*) . @PMS.")
	st.markdown("---")
	st.image(col_cor, caption="Colibri chillón (*Colibri coruscans*). @PMS.")



left_co, cent_co,last_co = st.columns(3)
with cent_co:
	st.image(logo)



exit(0)