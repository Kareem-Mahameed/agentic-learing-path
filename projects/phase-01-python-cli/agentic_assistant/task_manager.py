# title= "Learn Python"
# task_id = 1
# completed = False

# print(title)
# print(task_id)
# print(completed)
# print(type(title))
# print(type(task_id))
# print(type(completed))
# print("title: " , title , ", task_id:" , task_id , ", completed: " , completed)
# print(f"title: {title} , task_id: {task_id}, completed: {completed}")

# status = "done" if completed else "pending"
# print(f"Task {task_id}: {title} [{status}]")

# raw_title = "  Learn Python  "
# print(raw_title)
# print(raw_title.strip())
# print(raw_title.strip().lower())
# print(len(raw_title))
# print(len(raw_title.strip()))
# name = "agent"
# print(f"{name.upper()} has {len(name)} letters")

# title = "Learn Python"
# if title.strip() == "":
#     print("Title is required")
# else:
#     print(f"Title: {title}")

# if task_id >0 and raw_title.strip() != "":
#     print("valid")

# titles = ["Learn Python", "Build task manager"]

# titles.append("Write tests")
# print(titles)
# print(len(titles))

# for title in titles:
#     print(title)

# for position, title in enumerate(titles,start=1):
#     print(f"{position}. {title}")

# titles.append("Learn Advance Python")
# for position, title in enumerate(titles,start=1):
#     # if title.__contains__("Python"):
#     if "Python" in title:
#         print(f"{position}. {title}")

# task = {
#     "id":1,
#     "title":"Learn Python",
#     "completed": False
# }
# print(task["title"])
# print(task)
# task["completed"]= True
# print(task)
# print(task.get("description","No description"))

# tasks: list[dict[str,object]]= [
#     {"id": 1, "title": "Learn Python", "completed": True},
#     {"id": 2, "title": "Build task manager", "completed": False},
# ]

# tasks.append({"id": 3, "title": "Write tests", "completed": True})

# for task in tasks:
#     if task["completed"]:
#         print(f"{task['id']}: {task['title']}")



# for task in tasks:
#     formated = format_task(task)
#     print(formated)

# "Learn Python"
# ""
# "   "

# print(f"Learn Python is {is_valid_title('Learn Python')}")
# print(f"' '  is {is_valid_title(' ')}")
# print(f"'' is {is_valid_title('')}")

def format_task(task: dict[str,object]) -> str:
    marker = "x" if task["completed"] else " "
    return str(f'[{marker}] {task["id"]}: {task["title"]}')

def is_valid_title(title) -> bool:
    return bool(title.strip() != "")

def get_next_tax_id(tasks: list[dict[str, object]]) -> int:
    next_id = 1
    for task in tasks:
        if isinstance(task["id"], int) and task["id"] >= next_id:
            next_id = task["id"] + 1
    return next_id
    # if len(tasks) == 0:
    #     return 1
    # else:
    #     return max(task["id"] for task in tasks) + 1


def add_task(tasks:list[dict[str,object]], title:str) -> bool:
    title = title.strip()
    if is_valid_title(title):
        task = {"id":get_next_tax_id(tasks), "title":title, "completed":False }
        tasks.append(task)
        return True
    else:
        return False


def list_tasks(tasks:list[dict[str,object]]) -> None:
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for task in tasks:
            formated = format_task(task)
            print(formated)

def complete_task(
    tasks: list[dict[str, object]],
    task_id: int,
) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False

def remove_task(
    tasks: list[dict[str, object]],
    task_id: int,
) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False

def run_menu(tasks: list[dict[str, object]]) -> None:
    while True:
        print("\nTask Manager " \
        "\n1. Add task " \
        "\n2. List tasks " \
        "\n3. Complete task " \
        "\n4. Remove task " \
        "\n5. Exit ")

        choice = input("Choose an option:").strip()
        if choice == "1":
            title = input("Enter a task title:")
            if add_task(tasks,title):
                print("Task added.")
            else:
                print("Task title is required.")
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            task_id_text = input("Enter task id:").strip()
            task_id = int(task_id_text) if task_id_text.isdigit() else -1
            if complete_task(tasks,task_id):
                print("Task completed.")
            else:
                print("Task not found.")
        elif choice == "4":
            task_id_text = input("Enter task id:").strip()
            task_id = int(task_id_text) if task_id_text.isdigit() else -1
            if remove_task(tasks,task_id):
                print("Task removed.")
            else:
                print("Task not found.")
        elif choice == "5":
            print("Good by.")
            return
        else:
            print("Invalid option. Choose a number from 1 to 5.")



def main() -> None:
    print("Task manager starting")

    tasks: list[dict[str, object]] = []
    run_menu(tasks)

    # print("1. Empty collection:")
    # list_tasks(tasks)

    # print("\n2. Invalid title:")
    # result = add_task(tasks, "   ")
    # assert result is False
    # assert tasks == []

    # print("\n3. Add valid tasks:")
    # assert add_task(tasks, "Learn Python") is True
    # assert add_task(tasks, "Build task manager") is True

    # assert len(tasks) == 2

    # assert tasks[0]["id"] == 1
    # assert tasks[0]["title"] == "Learn Python"
    # assert tasks[0]["completed"] is False

    # assert tasks[1]["id"] == 2
    # assert tasks[1]["title"] == "Build task manager"
    # assert tasks[1]["completed"] is False

    # print("\n4. Task list:")
    # list_tasks(tasks)

    # print("\n5. Complete list:")
    # print(f"Complete non existing task, taskId:5, result: {complete_task(tasks,5)}")
    # print(f"Complete  existing task, taskId:2, result: {complete_task(tasks,2)}")
    # print(f"Complete  existing task, taskId:2, result: {complete_task(tasks,2)}")
    # list_tasks(tasks)

    # print("\n6. Remove list:")
    # print(f"Remove non existing task, taskId:5, result: {remove_task(tasks,5)}")
    # print(f"Remove  existing task, taskId:2, result: {remove_task(tasks,2)}")
    # print(f"Remove  existing task second time, taskId:2, result: {remove_task(tasks,2)}")
    # list_tasks(tasks)


    # print("\nAll assertions passed!")





if __name__ == "__main__":
    main()
