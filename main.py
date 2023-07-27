# Autenticación 
import os
import streamlit as st


def credentials():
    """
    Crea los sessions state para el nombre de usuario y password, además de la lógica de autenticación.

    """

    user_name_secret = os.environ['USER_NAME']
    password_secret = os.environ['PASSWORD']
    
    if st.session_state['user'].strip() == user_name_secret and st.session_state['pass'].strip() == password_secret:
        st.session_state['authenticated'] = True
    else:
        st.session_state['authenticated'] = False
        if not st.session_state['pass']:
            st.warning('Introduce la contraseña')
        elif not st.session_state['user']:
            st.warning('Introduce el usuario')
        else:
            st.error('El usuario o password es incorrecto')
        
def st_login_view():
    """
    Crea la página de login

    """
    
    st.markdown('# Bienvenido/a a <span style="color:pink"> triaje.ai</span>', unsafe_allow_html=True)
    st.text_input(label='Nombre de usuario:', value='', key="user", on_change=credentials)
    st.text_input(label='Contraseña:', value='', key='pass', type='password', on_change=credentials)
    st.button('Acceder')
    

def authetication():
    if "authenticated" not in st.session_state:
        buttons = st_login_view()
        return False
    else:
        if st.session_state['authenticated']:
            return True
        else:
            buttons = st_login_view()
            return False
           
    button_loggin = st.button('Acceder')

def st_logout():
    button = st.sidebar.button('logout')
    if button: 
        st.session_state['authenticated'] = False
        st.experimental_rerun()


if authetication():
    logout_bt = st_logout()
    st.success('Login correcto')
    st.balloons()
   

    
