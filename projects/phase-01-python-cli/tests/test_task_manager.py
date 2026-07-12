import pytest
from agentic_assistant.task_manager import (add_task, format_task, get_next_tax_id, is_valid_title, complete_task, list_tasks, remove_task, run_menu)

def test_add_task_rejects_whitespace_title() -> None:
    tasks = []
    result = add_task(tasks, "   ")
    assert result is False
    assert len(tasks) == 0

    result = add_task(tasks, "")
    assert result is False
    assert len(tasks) == 0

    result = add_task(tasks, "  title with spaces  ")
    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["title"] == "title with spaces"


def test_create_task_with_valid_title() -> None:
    tasks = []
    result = add_task(tasks, "Test Task")
    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Test Task"
    assert tasks[0]["completed"] is False

def test_complete_task_marks_task_as_completed() -> None:
    tasks = [{"id": 1, "title": "Test Task", "completed": False},
             {"id": 2, "title": "Another Task", "completed": False}]
    result = complete_task(tasks, 1)
    assert result is True
    assert tasks[0]["completed"] is True
    assert tasks[1]["completed"] is False

def test_format_task_returns_correct_string() -> None:
    task = {"id": 1, "title": "Test Task", "completed": False}
    formatted = format_task(task)
    assert formatted == "[ ] 1: Test Task"

    task["completed"] = True
    formatted = format_task(task)
    assert formatted == "[x] 1: Test Task"

def test_list_tasks_empty(capsys) -> None:
    tasks = []
    list_tasks(tasks)
    captured = capsys.readouterr()
    assert captured.out.strip() == "No tasks found."

def test_list_tasks_with_tasks(capsys) -> None:
    tasks = [
        {"id": 1, "title": "Task 1", "completed": False},
        {"id": 2, "title": "Task 2", "completed": True}
    ]
    list_tasks(tasks)
    captured = capsys.readouterr()
    expected_output = "[ ] 1: Task 1\n[x] 2: Task 2"
    assert captured.out.strip() == expected_output

def test_remove_task_removes_task() -> None:
    tasks = [
        {"id": 1, "title": "Task 1", "completed": False},
        {"id": 2, "title": "Task 2", "completed": True}
    ]
    result = remove_task(tasks, 1)
    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2

    result = remove_task(tasks, 1)
    assert result is False
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2

    result = remove_task(tasks, 5)
    assert result is False
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2

@pytest.mark.parametrize("title",["", "   ", "\n", "\t"])
def test_is_valid_title_rejects_invalid_titles(title) -> None:
    assert is_valid_title(title) is False
    tasks: list[dict[str, object]] = []

    result = add_task(tasks, title)

    assert result is False
    assert tasks == []

def test_add_task_after_deleting_task() -> None:
    tasks = [
        {"id": 1, "title": "Task 1", "completed": False},
        {"id": 2, "title": "Task 2", "completed": True}
    ]
    remove_task(tasks, 1)
    result = add_task(tasks, "New Task")
    assert result is True
    assert len(tasks) == 2
    assert tasks[1]["id"] == 3
    assert tasks[1]["title"] == "New Task"

def test_menu_add_task_and_list(capsys, monkeypatch) -> None:
    tasks: list[dict[str, object]] = []
    response = iter(["1", "Task 1", "1", "Task 2", "2", "4","7","5"])
    monkeypatch.setattr("builtins.input", lambda _: next(response))
    run_menu(tasks)
    captured = capsys.readouterr()  # Capture the entire simulated session
    assert len(tasks) == 2
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Task 1"
    assert tasks[1]["id"] == 2
    assert tasks[1]["title"] == "Task 2"
    assert tasks[0]["completed"] is False
    assert tasks[1]["completed"] is False
    assert captured.out.count("Task added.") == 2
    assert "[ ] 1: Task 1" in captured.out
    assert "[ ] 2: Task 2" in captured.out
    assert "Task not found." in captured.out
    assert "Good by." in captured.out
