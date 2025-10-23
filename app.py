# app.py
import streamlit as st
import random
import time

st.title("🎲 주사위 게임 (Dice Game)")
st.write("버튼을 눌러 주사위를 굴려보세요!")

if st.button("🎯 주사위 굴리기"):
    with st.spinner("주사위를 굴리는 중..."):
        time.sleep(1.2)
    결과 = random.randint(1, 6)
    st.success(f"결과는 🎲 {결과} 입니다!")
    st.balloons()
