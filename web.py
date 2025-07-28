import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    to_do = st.session_state["new_todo"]
    todos.append(to_do + '\n')
    functions.save_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}.{todo}")
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[f"{index}.{todo}"]
        st.rerun()

st.text_input(label="", placeholder="Enter a new to-do",
              on_change=add_todo, key="new_todo")


st.session_state
