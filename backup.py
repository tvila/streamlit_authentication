import yaml
from yaml.loader import SafeLoader

import streamlit as st
import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

print(hashed_passwords)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

print(authenticator)
