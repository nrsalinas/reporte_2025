import os
import re
from chapters.coberturas import text as cobtext
from chapters.conectividad import text as context
from chapters.flora import text as flotext
from chapters.plantas_urbanos import text as platext
from chapters.avifauna import text as avitext
#from chapters.artropofauna import text as arttext
from chapters.ciencia_participativa_biodiversidad import text as bcptext
from chapters.interacciones import text as inttext
from chapters.ciencia_participativa_interacciones import text as icptext
from chapters.suelos import text as suetext

def txt2tex(instr):
	out = re.sub('%', r'\\%', instr)
	out = re.sub(r'\n\- ', r'\n\\item ', out)
	return out

text_objs = [
	cobtext, context, flotext, platext, avitext,
	#arttext,
	bcptext, inttext, icptext,suetext
]

fig_fols=[
	'1_coberturas', 
	'2_conectividad', 
	'3_flora', 
	'4_ecosistemas_urbanos'
	'5_avifauna', 
#	'6_artropofauna', 
	'8_biodiversidad_cp', 
	'9_interacciones', 
	'10_interacciones_cp', 
	'11_suelos', 
	]

bff = r"""
\documentclass{article}
\usepackage{graphicx} % Required for inserting images
\usepackage[spanish]{babel}
\usepackage{charter}
\usepackage[left=1in,right=1in,top=1in,bottom=1in]{geometry}
%\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\title{Reporte de Estado de la Biodiversidad de Bogotá}
\date{Diciembre 2025}
\begin{document}

\maketitle

"""

for text, fol in zip(text_objs[:1], fig_fols):

	bff += f"\\section{{{text.title}}}\n\n"
	bff += f"\\textbf{{\\large {text.author}}}\n\n"
	bff += "\\emph{Jardín Botánico de Bogotá, eje Conservación \\emph{in situ}}\n\n"
	bff += f"{txt2tex(text.main)}\n\n\\bigskip\n\n"

	for d,s,f in os.walk(os.path.join("pdf_version", fol)):
		for fil in sorted(f):
			root = re.sub(r"\..+$", "", fil)
			
			bff += "\\begin{figure}\n\\centering\n"
			bff += f"\\includegraphics[height=0.9\\textheight]{{{fol}/{fil}}}\n"
			bff += f"\\caption{{{text.captions[root]}}}\n"
			bff += f"\\label{{{fol}_{root}}}\n"
			bff += f"\\end{{figure}}\n\n"

bff += "\\end{document}\n\n"
print(bff)
exit()