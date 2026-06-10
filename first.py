import streamlit as st
import random
st.title("🎮 Shaurya ka Game!")
st.write("Computer ne 1 se 10 ke beech ek number socha Hai. Andaza lagao!")
if 'secret'not in st.session_state:
     st.session_state.secret = random.randint(1, 10)
guess = st.number_input("Apna number chuno (1-10):", min_value=1, max_value=10, value=5)
if st.button("Check Karo"):
    if guess == st.session_state.secret:
         st.success(f"🎉sahi andaza ! Sahi number {guess} hi tha!")
         del st.session_state.secret
    else:
         st.error(f"❌ Oh ho! Galat andaza. Fir se koshish karo!")