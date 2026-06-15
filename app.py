import streamlit as st
import random

#Session
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)

if "guess" not in st.session_state:
    st.session_state.guess = 0

st.title("Selamat datang di game tebak angka (1-100) ")

#User input
user_input = st.number_input("Tebak angka: ", step=1)
col1, col2, col3 = st.columns(3)

#Logic
with col1:
    if st.button("Tebak"):
        st.session_state.guess += 1
        st.write(f"Percobaan: {st.session_state.guess}")

        if user_input < st.session_state.secret:
            st.info("📉 Kekecilan bro! ")
        elif user_input > st.session_state.secret:
            st.warning("📈 Kegedean bro! ")
        else:
            st.success(f"🎉 Selamat! anda berhasil menebak angka rahasia {st.session_state.secret} dalam { st.session_state.guess} percobaan")
        st.divider()

#Reset game
with col2:
    if st.button("Reset game"):
        st.session_state.secret = random.randint(1, 100)
        st.session_state.guess = 0
        st.info("Game baru dimulai! ")
        st.divider()

#update selasa
with col3:


