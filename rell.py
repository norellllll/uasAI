import pickle
import streamlit as st

#membaca model
target_model_random = pickle.load(open('target_model_random.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Penyakit Ginjal')

# Create user_state
if 'user_state' not in st.session_state:
    st.session_state.user_state = {
        'username': '',
        'password': '',
        'logged_in': False
    }

if not st.session_state.user_state['logged_in']:
    # Create login form
    st.write('Please login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    submit = st.button('Login')

  # Check if user is logged in
    if submit and st.session_state.user_state['logged_in'] == False:
        if username == 'admin' and password == '1234':
            st.session_state.user_state['username'] = username
            st.session_state.user_state['password'] = password
            st.session_state.user_state['logged_in'] = True
            st.write('You are logged in')
            st.rerun()
        else:
            st.write('Invalid username or password')
elif st.session_state.user_state['logged_in']:
    st.write('Welcome to the app')
    st.write('You are logged in as:', st.session_state.user_state['username'])

age = st.text_input ('input nilai age')

sex = st.text_input ('input nilai sex')

cp  = st.text_input ('input nilai cp')

trestbps = st.text_input ('input nilai trestbps')

chol = st.text_input ('input nilai chol')

fbs = st.text_input ('input nilai fbs')

restecg = st.text_input ('input nilai restecg')

thalach = st.text_input ('input nilai thalach')

exang = st.text_input ('input nilai exang')

oldpeak = st.text_input ('input nilai oldpeak')

slope = st.text_input ('input nilai slope')

ca = st.text_input ('input nilai ca')

thal = st.text_input ('input nilai thal')


# code untuk prediksi
diab_heart = ''

# membuat tombol untuk prediksi
if st.button('Tes Prediksi ginjal'):
    diab_prediction = target_model_random.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if(diab_prediction[0] == 1):
        diab_heart = 'Pasien Terkena ginjal'
    else :
        diab_heart = 'Pasien Tidak Terkena ginjal'

st.success(diab_heart)