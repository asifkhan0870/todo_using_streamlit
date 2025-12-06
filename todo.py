import streamlit as st
import json
import os

FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

st.title("📝 Advanced To-Do List")

tasks = load_tasks()

new_task = st.text_input("Add Task")

if st.button("Add"):
    if new_task:
        tasks.append({"task": new_task, "done": False})
        save_tasks(tasks)
        st.rerun()

# Filter
filter_option = st.radio("Filter", ["All", "Completed", "Pending"])

st.subheader("Current Tasks")

for i, item in enumerate(tasks):
    if filter_option == "Completed" and not item["done"]:
        continue
    if filter_option == "Pending" and item["done"]:
        continue

    col1, col2, col3 = st.columns([6, 1, 1])

    # Checkbox
    done = col1.checkbox(item["task"], value=item["done"], key=f"cb_{i}")

    # Update status
    if done != item["done"]:
        tasks[i]["done"] = done
        save_tasks(tasks)

    # Delete button
    if col3.button("❌", key=f"del_{i}"):
        tasks.pop(i)
        save_tasks(tasks)
        st.rerun()
