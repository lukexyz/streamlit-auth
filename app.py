import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader

# chage streamlit icon
st.set_page_config(page_title='Streamlit Authenticator', page_icon=':lock:')
st.write(':lock: Streamlit Authenticator')

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

# write varaible name and values
st.code(f'name = "{name}" \nusername = "{username}" \nauthentication_status = {authentication_status}')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.header('🔒 Content Authorized')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')