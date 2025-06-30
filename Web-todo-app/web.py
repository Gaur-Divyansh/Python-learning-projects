import streamlit as st # type: ignore
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo("todos.txt",todos)

todos = functions.get_todo("todos.txt")

st.title("To-Do App")

for index,todo in enumerate(todos):
    checkbox =  st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo("todos.txt",todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo...",
              on_change = add_todo,key="new_todo")

