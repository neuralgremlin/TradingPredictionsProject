import streamlit as st
from PIL import Image
 
def app():
    #st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)

    st.title("Reporte del proyecto")
    st.image(Image.open('./pages/Images/IMG1_UP.png'))
    st.title("App Web para Monitoreo de Portafolio")
    st.write("Muñoz, Guillermo")
    st.write("Ortíz-Monasterio, Pedro")
    st.write("Trillas, Josune") 
    st.write("Procesamiento de lenguaje natural")
    st.write("2do semestre")
    st.write("Profesor PHD Raul Morales Salcedo")
    st.write("06 de octubre del 2021")

    
    st.header("Comprensión general de problema")
    st.write("""En este proyecto trabajaremos con las acciones que conforman a un portafolio de inversión, seleccionado por un
    fondo de inversionistas, hecho a la medida para el perfil de riesgo e intereses de inversión de sus clientes.""")
    st.write("""Lo que un fondo de inversión busca es optimizar el dinero de sus clientes a través de la selección
    de acciones y porcentajes para la inversión que maximicen las ganancias para el dinero puesto en juego. 
    El manejo de los portafolios de inversión tiene toda una ciencia detrás. Cuenta con distintos métodos para 
    el armado de los portafolios según el nivel de riesgo que se quiere, el capital a invertir y el plazo en el que 
    se espera retorno. Con base en lo anterior, se diseñan portafolios de inversión a la medida de los clientes, siempre
    buscando satisfacer sus requerimientos.""")
    st.write("""Una labor que los especialistas realizan una vez armado el portafolio es el monitoreo del valor de las acciones. El objetivo natural de un portafolio es contar con la volatilidad histórica de la acción
    al momento de armarlo, sin embargo, el monitoreo sirve para detectar cambios en el mercado que puedan afectar 
    la rentabilidad y/o riesgo que puedan proyectarse al futuro más allá de lo contemplado en el diseño del portafolio.
    Cuando esto sucede, se recomienda al cliente mover su capital de una acción a otra o cambiar la mezcla  de las
    acciones para salvaguardar el rendimiento y el riesgo del portafolio en su  conjunto.""")
    
    st.subheader("Objetivos comerciales de la solución")
    st.write("""El presente trabajo busca desarrollar una aplicación, montada en la nube, que sirva como
    herramienta de apoyo al monitoreo de los valores de las acciones a través de predicciones del valor basado 
    en el histórico de la acción y factores externos, principalmente noticias y actividad de actores clave para
    las acciones.""") 
    st.write("""El objetivo de que la solución esté montada en la nube es evitar altas inversiones por parte del
    fondo de inversión para crear infraestructura que pueda soportar el análisis de todos sus portafolios.  
    Así siempre podrán hacerse soluciones modulares, escalables y a medida que satisfagan las necesidades actuales
    del negocio.""")

    st.write("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    st.subheader("Este es un subheader")
    st.write("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    st.write("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
