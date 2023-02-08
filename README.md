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

- i.e. `config.yaml`

```python
credentials:
  usernames:
    jsmith:
      email: jsmith@gmail.com
      name: John Smith
      password: abc # To be replaced with hashed password
    rbriggs:
      email: rbriggs@gmail.com
      name: Rebecca Briggs
      password: def # To be replaced with hashed password
cookie:
  expiry_days: 30
  key: some_signature_key # Must be string
  name: some_cookie_name
preauthorized:
  emails:
  - melsby@gmail.com
```

- Use the Hasher module to convert the plain text passwords into hashed passwords.

```python
import streamlit_authenticator as stauth
hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
```

## 3. Create a login widget

- In your `app.py` file

```python
with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
```

## 4. Authenticate users

- 🔐✅ **Allow your verified user to proceed** to restricted content using the returned name and authentication status.
- 🔓 **Add an optional logout button**

```python
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
```
