# Phase 1: Python CLI Task Manager

## Objective

Build an in-memory command-line task manager that lets a user add, list,
complete, and remove tasks. This project practices Python fundamentals without
databases, web APIs, third-party frameworks, or AI models.

## Learning outcomes

After completing this phase, you should be able to:

- Organize a small Python program into functions.
- Use strings, integers, booleans, lists, and dictionaries.
- Write conditions and loops.
- Validate user input.
- Use function parameters, return values, and type hints.
- Build an interactive command-line loop.
- Explain how task data flows through the program.
- Validate behavior with assertions or automated tests.

## Project structure

```text
phase-01-python-cli/
├── README.md
├── pyproject.toml
├── agentic_assistant/
│   ├── __init__.py
│   └── task_manager.py
└── tests/
```

The complete application can remain in `task_manager.py` during this phase.
Later phases can split responsibilities into additional modules when the
program becomes more complex.

## Task data model

Store all tasks in a list. Represent each individual task as a dictionary with
exactly these required fields:

```python
{
    "id": 1,
    "title": "Learn Python",
    "completed": False,
}
```

| Field | Type | Meaning |
|---|---|---|
| `id` | `int` | A positive identifier unique within the current run |
| `title` | `str` | A non-empty description with surrounding spaces removed |
| `completed` | `bool` | Whether the task has been completed |

Tasks exist only while the program is running. JSON persistence is introduced
in Phase 2.

## Required functions

The implementation should provide these behaviors. Exact helper functions may
vary, but each major operation should be isolated from the menu code.

### `is_valid_title`

```python
def is_valid_title(title: str) -> bool:
    ...
```

Requirements:

- Return `True` when the title contains at least one non-whitespace character.
- Return `False` for an empty or whitespace-only title.
- Do not modify the task collection.

### `format_task`

```python
def format_task(task: dict[str, object]) -> str:
    ...
```

Requirements:

- Return a string rather than printing it directly.
- Display `[ ]` for an incomplete task.
- Display `[x]` for a completed task.
- Include the task ID and title.

Example strings:

```text
[ ] 1: Learn Python
[x] 2: Build task manager
```

### `add_task`

```python
def add_task(tasks: list[dict[str, object]], title: str) -> bool:
    ...
```

Requirements:

- Remove surrounding whitespace from the title.
- Reject an empty or whitespace-only title.
- Create a positive numeric ID that is not already used by another task.
- Store the cleaned title.
- Set `completed` to `False`.
- Append the new task to `tasks`.
- Return `True` when a task is added.
- Return `False` without changing `tasks` when the title is invalid.

An ID based only on `len(tasks) + 1` can become duplicated after a task is
removed. The final implementation must account for this case.

### `list_tasks`

```python
def list_tasks(tasks: list[dict[str, object]]) -> None:
    ...
```

Requirements:

- Print `No tasks found.` when the list is empty.
- Display every task when the list is not empty.
- Use `format_task` so display formatting is defined in one place.
- Preserve the list's current order.

### `complete_task`

```python
def complete_task(
    tasks: list[dict[str, object]],
    task_id: int,
) -> bool:
    ...
```

Requirements:

- Find a task by its ID.
- Change its `completed` value to `True`.
- Return `True` when the task is found.
- Return `False` without changing other tasks when the ID is not found.
- Completing an already completed task must not create an error.

### `remove_task`

```python
def remove_task(
    tasks: list[dict[str, object]],
    task_id: int,
) -> bool:
    ...
```

Requirements:

- Find a task by its ID.
- Remove only that task.
- Return `True` when the task is removed.
- Return `False` without changing the list when the ID is not found.
- Do not renumber the remaining tasks after removal.

## Command-line menu requirements

The final application must repeatedly display a menu similar to:

```text
Task Manager
1. Add task
2. List tasks
3. Complete task
4. Remove task
5. Exit
Choose an option:
```

The exact wording may differ, but all five operations must be available.

### Menu behavior

- Continue showing the menu until the user chooses Exit.
- Add asks the user for a title and reports whether it was accepted.
- List shows the current tasks.
- Complete asks for a task ID and reports success or failure.
- Remove asks for a task ID and reports success or failure.
- Exit ends the program cleanly.
- An unsupported menu option prints a helpful message and returns to the menu.

### Reading user input with `input()`

Python's built-in `input()` function reads one line of text from the terminal.
It performs three steps:

1. Displays an optional prompt.
2. Pauses the program until the user types a value and presses Enter.
3. Returns the typed value as a string.

For example:

```python
choice = input("Choose an option: ")
```

If the user types `2` and presses Enter, `choice` contains the string `"2"`,
not the integer `2`. Menu options can therefore be compared directly with
strings:

```python
choice = input("Choose an option: ").strip()

if choice == "1":
    print("Add a task")
elif choice == "2":
    print("List tasks")
```

The prompt text is displayed to the user but is not included in the returned
value. The newline produced when the user presses Enter is also not included.

#### Removing surrounding whitespace

Users may accidentally enter spaces before or after a value. Calling
`.strip()` removes surrounding whitespace:

```python
title = input("Enter a task title: ").strip()
```

For example, an entry of `"  Learn Python  "` becomes `"Learn Python"`.
Spaces inside the title are preserved. An empty entry or an entry containing
only spaces becomes `""` and must be rejected.

It is also acceptable for `add_task` to perform the title cleanup. Keeping
validation in the operation function ensures that titles are checked even when
the function is called from a test or from code other than the menu.

#### Converting numeric input

`input()` always returns a string, even when the user types digits. Convert a
task ID with `int()`:

```python
task_id_text = input("Enter the task ID: ").strip()
task_id = int(task_id_text)
```

However, `int()` raises `ValueError` for input such as `abc`, `1.5`, or an
empty string. The menu must handle that error instead of terminating:

```python
task_id_text = input("Enter the task ID: ").strip()

try:
    task_id = int(task_id_text)
except ValueError:
    print("Task ID must be a whole number.")
    continue
```

The `continue` statement immediately starts the next iteration of the menu
loop. Code after this block runs only when conversion succeeds.

Converting a value does not prove that the corresponding task exists. After a
successful conversion, pass the ID to `complete_task` or `remove_task` and use
the returned boolean to report whether a task was found.

#### Keeping input in the menu layer

Core operations such as `add_task`, `complete_task`, and `remove_task` should
receive normal function parameters rather than calling `input()` themselves.
The menu owns the terminal interaction and the functions own task behavior:

```text
input() → validate or convert → call operation → display result
```

This separation allows the core functions to be tested without simulating a
person typing at the terminal. Never use `eval(input(...))` to convert user
input; `eval` executes arbitrary Python code and is unnecessary for this
project.

### Input validation

The program must handle these inputs without crashing:

- An empty task title.
- A title containing only spaces.
- An unknown menu option.
- A non-numeric task ID such as `abc`.
- A numeric task ID that does not exist.
- Completing an already completed task.
- Removing a task from an empty list.

## Example session

The wording does not need to match exactly, but the behavior should resemble:

```text
Task Manager
1. Add task
2. List tasks
3. Complete task
4. Remove task
5. Exit
Choose an option: 1
Enter a task title: Learn Python
Task added.

Choose an option: 1
Enter a task title: Build task manager
Task added.

Choose an option: 2
[ ] 1: Learn Python
[ ] 2: Build task manager

Choose an option: 3
Enter the task ID: 1
Task completed.

Choose an option: 2
[x] 1: Learn Python
[ ] 2: Build task manager

Choose an option: 5
Goodbye!
```

## Validation requirements

Use manual validation for the interactive user experience and assertions or
tests for deterministic behavior.

### Minimum behavior checks

- Listing an empty collection prints the empty-state message.
- A whitespace-only title is rejected and does not change the list.
- Adding two valid tasks creates two incomplete tasks with different IDs.
- Surrounding whitespace is removed from a valid title.
- Completing a known ID changes only the matching task.
- Completing an unknown ID returns `False`.
- Removing a known ID removes only the matching task.
- Removing an unknown ID returns `False`.
- Adding a task after removal does not reuse an ID that is still in use.
- Formatting uses the correct status marker.
- Invalid menu and task-ID input does not terminate the program unexpectedly.

Temporary assertions may be used while developing. The completed project
should keep validation outside the interactive `main` function, preferably in
files under `tests/`.

## Running the project

From `projects/phase-01-python-cli`, activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the application as a module:

```bash
python -m agentic_assistant.task_manager
```

## Running tests

### What pytest is

`pytest` is a Python testing framework. It finds test files and test functions,
runs them, and reports which expectations passed or failed. Tests use normal
Python functions and plain `assert` statements, so you do not need to create a
test class for this project.

For example:

```python
def test_addition() -> None:
    assert 1 + 1 == 2
```

The function name begins with `test_`, which allows pytest to discover it
automatically. If an assertion fails, pytest displays the expression and the
values involved. This is more useful and repeatable than checking printed
output by eye after every change.

pytest is a development dependency: it is used to verify the application but
is not needed by a user who only runs the task manager.

### Installing pytest

Activate the Phase 1 virtual environment before installing anything:

```bash
source .venv/bin/activate
```

Install pytest into that environment:

```bash
python -m pip install pytest
```

Verify that the active Python interpreter can find it:

```bash
python -m pytest --version
```

Using `python -m pip` and `python -m pytest` ensures that installation and test
execution use the same active Python interpreter. If pytest is installed
outside `.venv`, another phase or Python installation may use a different
version or may not find it at all.

### Test layout and discovery

Place Phase 1 tests in:

```text
tests/
└── test_task_manager.py
```

By default, pytest discovers files named `test_*.py` or `*_test.py` and
functions named `test_*`. A descriptive name explains the behavior being
verified:

```python
def test_add_task_rejects_whitespace_title() -> None:
    ...
```

Avoid names such as `test_1` because a failure report should tell you what
behavior broke without requiring you to open the file first.

### Importing the application functions

At the top of `tests/test_task_manager.py`, import only the functions the tests
need:

```python
from agentic_assistant.task_manager import (
    add_task,
    complete_task,
    format_task,
    list_tasks,
    remove_task,
)
```

Run pytest from `projects/phase-01-python-cli`, not from inside `tests/`. The
project directory then acts as the import root for `agentic_assistant`.

### Arrange, Act, Assert

A small test is easiest to understand when it has three conceptual sections:

1. **Arrange:** create the starting data.
2. **Act:** call the behavior being tested.
3. **Assert:** verify the result and resulting state.

For example:

```python
def test_add_task_creates_an_incomplete_task() -> None:
    # Arrange
    tasks: list[dict[str, object]] = []

    # Act
    result = add_task(tasks, "Learn Python")

    # Assert
    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Learn Python"
    assert tasks[0]["completed"] is False
```

The comments are useful while learning but optional when the sections are
already obvious.

### Keep tests independent

Each test should create its own task list:

```python
def test_one() -> None:
    tasks: list[dict[str, object]] = []
    ...


def test_two() -> None:
    tasks: list[dict[str, object]] = []
    ...
```

Do not share one mutable list between tests. Shared state can make a test pass
or fail depending on which test ran first. A test should produce the same
result when run alone or as part of the complete suite.

### Testing rejected input

Test both the return value and the unchanged state:

```python
def test_add_task_rejects_whitespace_title() -> None:
    tasks: list[dict[str, object]] = []

    result = add_task(tasks, "   ")

    assert result is False
    assert tasks == []
```

Checking only `result` could miss a bug where the function returns `False` but
still adds an invalid task.

### Testing state changes

For completion and removal, verify that the intended task changes while other
tasks remain unchanged:

```python
def test_complete_task_changes_only_the_matching_task() -> None:
    tasks: list[dict[str, object]] = [
        {"id": 1, "title": "First", "completed": False},
        {"id": 2, "title": "Second", "completed": False},
    ]

    result = complete_task(tasks, 2)

    assert result is True
    assert tasks[0]["completed"] is False
    assert tasks[1]["completed"] is True
```

Also write a test for an unknown ID and confirm that the entire list remains
unchanged.

### Testing return strings

`format_task` returns a string, so it can be tested directly:

```python
def test_format_task_marks_completed_task() -> None:
    task = {"id": 3, "title": "Write tests", "completed": True}

    result = format_task(task)

    assert result == "[x] 3: Write tests"
```

This is one reason to return formatted text from `format_task` instead of
printing inside that function.

### Testing printed output with `capsys`

`list_tasks` prints instead of returning its display text. pytest provides the
built-in `capsys` fixture to capture terminal output during a test:

```python
def test_list_tasks_prints_empty_message(capsys) -> None:
    tasks: list[dict[str, object]] = []

    list_tasks(tasks)
    captured = capsys.readouterr()

    assert captured.out == "No tasks found.\n"
    assert captured.err == ""
```

A fixture is a resource pytest supplies to a test. Adding the reserved
parameter name `capsys` asks pytest to provide its output-capture fixture.
`captured.out` contains standard output and `captured.err` contains standard
error output. The expected output includes `\n` because `print()` adds a
newline.

You can also capture multiple printed tasks:

```python
def test_list_tasks_prints_all_tasks(capsys) -> None:
    tasks: list[dict[str, object]] = [
        {"id": 1, "title": "First", "completed": False},
        {"id": 2, "title": "Second", "completed": True},
    ]

    list_tasks(tasks)
    captured = capsys.readouterr()

    assert captured.out == "[ ] 1: First\n[x] 2: Second\n"
```

### Testing several related inputs

When the same behavior must be checked with several values, pytest can run one
test with multiple parameter sets:

```python
import pytest


@pytest.mark.parametrize("title", ["", " ", "   "])
def test_add_task_rejects_invalid_titles(title: str) -> None:
    tasks: list[dict[str, object]] = []

    result = add_task(tasks, title)

    assert result is False
    assert tasks == []
```

pytest reports each parameter set as a separate test case. This avoids copying
the same test body several times.

### Running the tests

Run the complete suite from the Phase 1 directory:

```bash
python -m pytest
```

Useful variations include:

```bash
# Show each collected test name
python -m pytest -v

# Use compact output
python -m pytest -q

# Run one file
python -m pytest tests/test_task_manager.py

# Run one test function
python -m pytest tests/test_task_manager.py::test_add_task_creates_an_incomplete_task

# Run tests whose names contain a word
python -m pytest -k "remove"
```

### Reading test results

Common result markers are:

| Marker | Meaning |
|---|---|
| `.` | Test passed |
| `F` | An assertion failed |
| `E` | The test encountered an error during setup or execution |
| `s` | Test was skipped |

For a failure, start with the failing test name, then read the assertion report
to compare the expected and actual values. The final short summary lists every
failed test. Fix the application or an incorrect expectation, then rerun the
smallest failing test before running the complete suite.

Do not change an assertion merely to make a test green unless the documented
requirement was wrong. Tests describe expected behavior; changing them can hide
an application defect.

### What to test in Phase 1

At minimum, cover:

- Valid and invalid task titles.
- Title whitespace cleanup.
- Task defaults and unique IDs.
- Adding a task after another task is removed.
- Listing empty and populated collections.
- Incomplete and completed formatting.
- Completing existing, missing, and already completed tasks.
- Removing existing and missing tasks.
- Ensuring unrelated tasks are not changed.

The interactive menu can still receive a short manual end-to-end check. Its
core operations should be covered by automated tests. Simulating repeated
`input()` calls is possible with pytest's `monkeypatch` fixture, but it is an
optional extension for this phase; prioritize small tests of the task
operations first.

For additional details, see the official
[pytest getting-started guide](https://docs.pytest.org/en/stable/getting-started.html)
and [fixture reference](https://docs.pytest.org/en/stable/reference/fixtures.html).

## Implementation constraints

For this phase:

- Use Python's standard library only unless a test runner is added.
- Keep task data in memory.
- Use normal functions for the core operations.
- Use type hints for function parameters and return values.
- Keep application logic separate from temporary learning examples.
- Do not introduce a database, JSON persistence, web API, GUI, LLM, agent
  framework, or MCP server.
- Classes are optional and unnecessary for the required solution.

## Definition of done

Phase 1 is complete when every item is true:

- [ ] The application starts with the documented module command.
- [ ] The menu repeats until Exit is selected.
- [ ] A user can add, list, complete, and remove tasks.
- [ ] Each stored task has `id`, `title`, and `completed` fields.
- [ ] Empty titles are rejected.
- [ ] Invalid menu options and task IDs do not crash the program.
- [ ] IDs remain unique after tasks are removed and new tasks are added.
- [ ] Status markers correctly show incomplete and completed tasks.
- [ ] Core operations are implemented in functions with type hints.
- [ ] Temporary orientation examples are not mixed with application logic.
- [ ] Repeatable assertions or tests validate the core operations.
- [ ] Manual testing confirms that the interactive workflow is understandable.
- [ ] You can explain how the task list changes after every operation.

## Known limitations

These limitations are intentional and will be addressed later:

- Tasks are lost when the program exits.
- The program supports only one local user.
- There are no due dates, priorities, tags, or descriptions.
- There is no API or graphical interface.
- There is no model, tool calling, agent loop, or MCP integration.

## Changes from the previous phase

This is the initial project version, so there is no previous implementation.
