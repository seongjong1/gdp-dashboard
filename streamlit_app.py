import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.write("""
    hello""")
st.write("""hello2""")

x = st.slider("X의 값 입력", 0,100,30) # 0~ 100의 범의의 slider , 초기값 50
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot([x],[y],marker="o")
st.pyplot(fig)
