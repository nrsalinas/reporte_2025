import streamlit as st

pg = st.navigation(
	[
		st.Page("chapters/intro/0_Introducción.py", default=True, url_path="intro"),
		st.Page("chapters/coberturas/1_Coberturas.py", url_path="coberturas"),
		st.Page("chapters/conectividad/2_Conectividad_ecológica.py", url_path="conectividad"), 
		st.Page("chapters/flora/3_Flora_de_Bogotá.py", url_path="flora"), 
		st.Page("chapters/plantas_urbanos/4_Plantas_de_ecosistemas_urbanos_y_periurbanos.py", url_path="ecosistemas_urbanos"), 	
		st.Page("chapters/avifauna/5_Avifauna_de_Bogotá.py", url_path="aves"),
		st.Page("chapters/ciencia_participativa_biodiversidad/8_Biodiversidad_y_ciencia_participativa.py", url_path="biodiv_ciencia_part"),
		st.Page("chapters/interacciones/9_Interacciones_bióticas.py", url_path="interacciones"),
		st.Page("chapters/suelos/11_Hojarasca_y_suelos.py", url_path="hojarasca")
	]
)

pg.run()


exit(0)