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

If the project uses `pytest`:

```bash
python -m pytest
```

If you have not introduced `pytest` yet, run a standalone validation script or
use Python's built-in `unittest` module. Do not claim the project is complete
until repeatable checks cover the core task operations.

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
