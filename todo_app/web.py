import streamlit as st
import functions

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my to-do app.")
st.write("This app is to improve your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(placeholder="Add a todo...")