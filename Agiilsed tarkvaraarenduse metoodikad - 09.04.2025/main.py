import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 See on TodoList")

def add_task():
    task = st.text_input("Sisesta uus ülesanne", key="new_task_input")
    if st.button("Lisa"):
        if task.strip():
            st.session_state.tasks.append({"text": task, "done": False})
            st.experimental_rerun()
        else:
            st.warning("Sisesta mitte-tühi ülesanne.")

add_task()

def show_tasks():
    if not st.session_state.tasks:
        st.info("📭 Nimekiri on tühi")
        return

    for i, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.08, 0.80, 0.12])
        with cols[0]:
            st.session_state.tasks[i]["done"] = st.checkbox(
                "", value=task["done"], key=f"done_{i}"
            )
        with cols[1]:
            if task["done"]:
                st.markdown(f"~~{task['text']}~~")
            else:
                st.markdown(task["text"])
        with cols[2]:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()

show_tasks()
