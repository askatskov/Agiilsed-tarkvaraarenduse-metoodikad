import streamlit as st

st.session_state.tasks = []

st.title("See on TodoList ")

def add_task():
    task = st.textInput("Sisesta uus ülesanne", key="new_task_input")
    if st.button("Lisa"):
        if task.strip():
            st.session_state.tasks.append({"text": task, "done": False})

            st.rerun
        else:
            st.warning("sisesta mitte-tühi sõnum")
add_task