import streamlit as st

pg = st.navigation(
	[
		st.Page("chapters/intro/1_Introducción.py", default=True, url_path="intro"),
		st.Page("chapters/flora/2_Flora_de_Bogotá.py", url_path="flora"), 
		st.Page("chapters/avifauna/3_Avifauna_de_Bogotá.py", url_path="aves")
	]
)

pg.run()


exit(0)