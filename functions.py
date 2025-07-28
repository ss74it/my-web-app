
PROMPT_TODO = 'Enter a new ToDo: '
TODOS_FILE = 'todos.txt'


def get_todos(filepath=TODOS_FILE):
    with open(filepath, 'r') as text_file:
        todos = text_file.readlines()
    return todos


def save_todos(my_list, filepath=TODOS_FILE):
    with open(filepath, 'w') as file:
        file.writelines(my_list)


def normalize_command(my_list):
    return normalize_text(" ".join(my_list))


def ask_new_todo():
    while True:
        new_entry = input("Enter the new ToDo: ")
        new_entry = normalize_text(new_entry)
        if not new_entry:
            print("You have to enter a new ToDo. Please try again.")
            continue
        return new_entry


def normalize_text(text):
    return text.strip().title()


def ask_task(prompt):
    while True:
        entry = input(f"Enter the ToDo number or text to {prompt}: ")
        entry = normalize_text(entry)
        if not entry:
            print(f"Error: You have to enter a number or a text to {prompt}. Please try again.")
            continue
        return entry


def get_task_index(todos, task_id, prompt):
    if not todos:
        print(f"The ToDo list is empty. You have to add at least one entry before you can use {prompt}.")
        return None
    if not task_id:
        commands = ask_task(prompt)
    else:
        commands = normalize_command(task_id)

    if commands.isdigit():
        task_index = int(commands) - 1
        if task_index not in range(len(todos)):
            print(f"Error: Todo number is out of range. Range is from 1 to {len(todos)}. Please try again.")
            return None
        return task_index
    else:
        stripped_todos = [item.strip('\n') for item in todos]
        if commands in stripped_todos:
            task_index = stripped_todos.index(commands)
            return task_index
        else:
            print(f"Error. Task '{commands}' not present in the ToDo List. Please try again.")
            return None
