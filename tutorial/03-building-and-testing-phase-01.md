# Build and Test the Phase 1 Task Manager

This lesson turns the Python concepts from the orientation into a complete
command-line project. You will build the application in small milestones and
validate each milestone before continuing.

The detailed function contracts, edge cases, example session, and definition
of done live in the
[Phase 1 project requirements](../projects/phase-01-python-cli/README.md).
Treat that README as the authoritative specification and this page as the
recommended learning sequence.

## Learning outcomes

After completing this lesson, you will be able to:

- Build a small application incrementally.
- Separate task operations from terminal interaction.
- Read and validate terminal input.
- Prevent duplicate task IDs after removal.
- Turn temporary assertions into pytest tests.
- Capture printed output with pytest's `capsys` fixture.
- Perform both automated and manual validation.

## Before starting

Move into the Phase 1 project and activate its environment:

```bash
cd projects/phase-01-python-cli
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Confirm the interpreter:

```bash
python --version
```

Run the module once:

```bash
python -m agentic_assistant.task_manager
```

Keep orientation experiments in `exercises/python_orientation.py`. The project
module should contain only the task manager's application logic.

## Milestone 1: Define one task

Represent one task as a dictionary with three fields:

```python
{
    "id": 1,
    "title": "Learn Python",
    "completed": False,
}
```

Represent the collection as a list of those dictionaries:

```python
tasks: list[dict[str, object]] = []
```

At this stage, explain why:

- A list is appropriate for an ordered, mutable collection.
- A dictionary gives each task field a meaningful name.
- `completed` is a boolean instead of a status string.
- The task ID is different from the task's position in the list.

Do not introduce classes or persistence yet.

## Milestone 2: Format and validate

Implement two small helpers before changing the task collection:

```python
def is_valid_title(title: str) -> bool:
    ...


def format_task(task: dict[str, object]) -> str:
    ...
```

`is_valid_title` should reject empty and whitespace-only titles.
`format_task` should return, rather than print, a string such as:

```text
[ ] 1: Learn Python
[x] 2: Build task manager
```

Returning a string makes formatting easy to test independently from terminal
output.

### Checkpoint

Use temporary assertions:

```python
assert is_valid_title("Learn Python") is True
assert is_valid_title("") is False
assert is_valid_title("   ") is False
```

Also verify both status markers with task dictionaries that differ only in
their `completed` value.

## Milestone 3: Add and list tasks

Implement:

```python
def add_task(
    tasks: list[dict[str, object]],
    title: str,
) -> bool:
    ...


def list_tasks(tasks: list[dict[str, object]]) -> None:
    ...
```

Keep these responsibilities separate:

- `add_task` cleans and validates the title, creates the dictionary, and
  changes the list.
- `list_tasks` displays the empty state or formats every existing task.

### Checkpoint

Validate this sequence:

1. Listing an empty collection prints `No tasks found.`
2. Adding `"   "` returns `False` and leaves the collection empty.
3. Adding two valid titles returns `True` twice.
4. Both tasks are incomplete and have different IDs.
5. Listing displays both tasks in order.

Use assertions for return values and stored data. Inspect printed output
manually until the pytest output-capture section later in this lesson.

## Milestone 4: Complete and remove tasks

Implement:

```python
def complete_task(
    tasks: list[dict[str, object]],
    task_id: int,
) -> bool:
    ...


def remove_task(
    tasks: list[dict[str, object]],
    task_id: int,
) -> bool:
    ...
```

Both functions should return `True` when the ID is found and `False` when it is
not found. They should not print messages; the menu decides how to present the
result to the user.

### Checkpoint

Verify that:

- Completing an existing task changes only that task.
- Completing it again succeeds without an error.
- Completing an unknown ID returns `False`.
- Removing an existing task removes only that task.
- Removing the same ID again returns `False`.
- Removing from an empty collection returns `False`.

## Milestone 5: Keep IDs unique

Do not generate an ID with only `len(tasks) + 1`. Removing a task can make that
calculation collide with an existing ID.

For example:

```text
Existing IDs: 1, 2
Remove ID 1
List length: 1
len(tasks) + 1: 2  <- collision
```

Create a helper that finds the largest current integer ID and returns the next
number. The empty collection should produce ID `1`.

### Checkpoint

Run this scenario:

1. Add tasks with IDs 1 and 2.
2. Remove ID 1.
3. Add another task.
4. Confirm the remaining IDs are 2 and 3.

## Milestone 6: Build the command-line menu

Create a function that owns terminal interaction:

```python
def run_menu(tasks: list[dict[str, object]]) -> None:
    ...
```

Use a loop to repeatedly display Add, List, Complete, Remove, and Exit options.
Read the selected option with `input()`:

```python
choice = input("Choose an option: ").strip()
```

Remember that `input()` always returns a string. Compare menu options with
`"1"`, `"2"`, and so on.

Task IDs require conversion:

```python
task_id_text = input("Enter the task ID: ").strip()

try:
    task_id = int(task_id_text)
except ValueError:
    print("Task ID must be a whole number.")
    continue
```

Keep `input()` and user-facing success or error messages in the menu. Keep the
core functions focused on task behavior so they can be tested without terminal
interaction.

Replace temporary demonstration code in `main` with the real entry point:

```python
def main() -> None:
    tasks: list[dict[str, object]] = []
    run_menu(tasks)


if __name__ == "__main__":
    main()
```

For the complete menu contract and invalid-input requirements, consult the
[Phase 1 README](../projects/phase-01-python-cli/README.md#command-line-menu-requirements).

## Milestone 7: Install pytest

pytest is used only for development and testing. With the Phase 1 virtual
environment active, install and verify it:

```bash
python -m pip install pytest
python -m pytest --version
```

Using `python -m` ensures pip and pytest belong to the active interpreter.

### Private package-index or VPN failure

If installation mentions a private Artifactory URL followed by a hostname or
DNS error, pip is configured to use an internal package index that is not
reachable. This is not evidence that pytest has no compatible version.

Recommended recovery:

1. Connect to the required company network or VPN.
2. Confirm the configured index with `python -m pip config list`.
3. Retry `python -m pip install pytest`.
4. Ask the package-index administrator if the host resolves but pytest is not
   available.

If organizational policy permits direct public PyPI access, an explicit
one-command override is:

```bash
python -m pip install \
  --isolated \
  --index-url https://pypi.org/simple \
  pytest
```

`--isolated` prevents user-level pip configuration from adding the unreachable
private index to that command. Do not bypass a required organizational package
policy. Do not use `sudo pip install`; dependencies belong inside `.venv`.

If network access remains unavailable, continue with temporary assertions or
Python's built-in `unittest` and return to pytest later.

## Milestone 8: Create the pytest suite

Create:

```text
tests/test_task_manager.py
```

pytest automatically discovers files named `test_*.py` and functions named
`test_*`. Import the application functions at the top of the test file.

Write each test using Arrange, Act, Assert:

```python
def test_add_task_rejects_whitespace_title() -> None:
    # Arrange
    tasks: list[dict[str, object]] = []

    # Act
    result = add_task(tasks, "   ")

    # Assert
    assert result is False
    assert tasks == []
```

Every test should create its own task list. Tests must not depend on state left
by another test.

Start with tests for:

- Valid and invalid titles.
- Title whitespace cleanup.
- Task defaults and unique IDs.
- Complete success and not-found behavior.
- Remove success and not-found behavior.
- Incomplete and completed formatting.

## Milestone 9: Test printed output

pytest's built-in `capsys` fixture captures output written by `print()`:

```python
def test_list_tasks_prints_empty_message(capsys) -> None:
    tasks: list[dict[str, object]] = []

    list_tasks(tasks)
    captured = capsys.readouterr()

    assert captured.out == "No tasks found.\n"
    assert captured.err == ""
```

The expected output contains `\n` because `print()` adds a newline. Add another
test that captures a list containing both an incomplete and a completed task.

The detailed pytest reference, including parametrization and useful commands,
is in the
[Phase 1 README](../projects/phase-01-python-cli/README.md#running-tests).

## Milestone 10: Run automated and manual checks

Run all automated tests from the Phase 1 directory:

```bash
python -m pytest -v
```

Then manually run the application:

```bash
python -m agentic_assistant.task_manager
```

Exercise this workflow:

1. List an empty collection.
2. Add a valid task.
3. Attempt an empty title.
4. Add a second task.
5. Complete a valid ID.
6. Enter a non-numeric ID.
7. Remove a valid ID.
8. Enter an unknown menu option.
9. Exit cleanly.

Automated tests verify deterministic behavior. Manual testing verifies that the
interactive conversation is understandable to a person.

## Phase completion checkpoint

Use the complete
[Phase 1 definition of done](../projects/phase-01-python-cli/README.md#definition-of-done).
Do not move to Phase 2 until you can check every required item and explain:

- How the task list changes after each operation.
- Why terminal input remains outside the core task functions.
- How invalid input is prevented from crashing the menu.
- Why every pytest test starts with independent data.
- What remains intentionally limited because data is only in memory.

---

**Previous:** [← 45-minute Python orientation](02-python-orientation.md)

**Tutorial home:** [Tutorial index](README.md)
