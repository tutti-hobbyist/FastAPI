
import streamlit as st
import pandas as pd
import numpy as np


st.write("hi")
st.markdown("# Hello")
st.code("""
import numpy as np

arr = np.ones(3)
""")

df = pd.DataFrame({
    "A": [i for i in range(5)],
    "B": [i**2 for i in range(5)],
})
st.dataframe(df)

df_chart = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
st.line_chart(df_chart)

