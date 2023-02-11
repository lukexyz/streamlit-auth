import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader

# chage streamlit icon
st.set_page_config(page_title='Streamlit Authenticator', page_icon=':lock:')
st.write(':lock: Streamlit Authenticator')

# --------------------------- #
# 1. Load authenticator       #
# --------------------------- #

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
if authentication_status == True:
    st.code(f'name = "{name}" \nusername = "{username}" \nauthentication_status = {authentication_status}')

# --------------------------- #
# 2. Logic Control            #
# --------------------------- #

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.header('🔒 Secret Authorized Content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

# --------------------------- #
# 3. Password Reset           #
# --------------------------- #


try:
    if authenticator.reset_password(username, 'Reset password'):
        st.success('Password modified successfully')
        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
except Exception as e:
    st.error(e)

# --------------------------- #
# 4. New User                 #
# --------------------------- #


try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
except Exception as e:
    st.error(e)
