# streamlit-auth

# Streamlit-`auth`

- Authentication framework
- From [mkhorasani/Streamlit-Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator)

## 1. Install

`pip install streamlit-authenticator`

## 2. Config

Customise `yaml` file with allowed users.

```
wget -O config.yaml https://raw.githubusercontent.com/mkhorasani/Streamlit-Authenticator/main/config.yaml
```

- Import module into app

```
import streamlit as st
import streamlit_authenticator as stauth
```
