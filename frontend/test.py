import streamlit as st
import numpy as np
import pandas as pd



slider_ = st.slider('This is a slider', key="cool_slider")
st.write(slider_, 'squared is', slider_ * slider_)

# You can access the value at any point with:
st.write(f"An otehr option to acces the sldier is with the session_state, like this: {st.session_state.cool_slider}")


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(5, 3),
       columns=['a', 'b', 'c'])

    chart_data

# -------- Sidebar --------
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Choose an option',
    ('A', 'B', 'C')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")