import streamlit as st

# Custom imports
from multipage import MultiPage
from pages import main, reporte_proyecto, otros_datos, descarga_data # import your pages here

# Create an instance of the app
app = MultiPage()

# Add all your applications (pages) here
app.add_page("Aplicación",main.app)
app.add_page("Descarga la data",descarga_data.app)
app.add_page("Otros datos",otros_datos.app)
app.add_page("Reporte del proyecto", reporte_proyecto.app)

# The main app
app.run()
