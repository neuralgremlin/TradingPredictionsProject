import streamlit as st
import base64


def app():

    def st_display_pdf(pdf_file):
        with open(pdf_file,"rb") as f:
          base64_pdf = base64.b64encode(f.read()).decode('utf-8')
          pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'        
        st.markdown(pdf_display, unsafe_allow_html=True)

    st.title("Reporte del proyecto")
    st.title("App Web para Monitoreo de Portafolio")
    st.write("Muñoz, Guillermo")
    st.write("Ortíz-Monasterio, Pedro")
    st.write("Trillas, Josune") 
    st.write("Procesamiento de lenguaje natural")
    st.write("2do semestre")
    st.write("Profesor PHD Raul Morales Salcedo")
    st.write("06 de octubre del 2021")
    
    with open("reporte_proyecto_eq3.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
