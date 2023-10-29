import pickle
import streamlit as st

model = pickle.load(open('sephora.sav', 'rb'))

st.title('Sephora website')

id = st.number_input('input id produk')
number_of_reviews = st.number_input('input reviews pelangan')
limited_edition = st.number_input('input produk limited')
value_price = st.number_input('input nilai harga')
love = st.number_input('input produk paling laku')

predict = ''

if st.button('cek harga'):
    predict = model.predict(
        [[id, number_of_reviews, limited_edition, value_price, love]]
    )
    st.write ('estimasi harga sephora dalam ponds :', predict)
    st.write ('estimasi harga sephora dalam IDR (Juta) :', predict*19000)