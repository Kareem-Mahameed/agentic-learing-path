# 45-Minute Python Orientation

This lesson is for programmers who know another language but are new to
Python. It focuses only on the syntax needed to begin the Phase 1 command-line
task manager.

Do not try to memorize every Python feature. Type and run each example, then use
the checkpoints to confirm that you understand what happened.

## Learning outcome

After 45 minutes, you will be able to:

- Read and write basic Python syntax.
- Use strings, integers, booleans, lists, and dictionaries.
- Write conditions, loops, and functions.
- Add useful type hints.
- Explain Python's module entry-point pattern.
- Model an in-memory task without building the complete task manager.

## Before starting

Activate the Phase 1 environment:

```bash
cd projects/phase-01-python-cli
source .venv/bin/activate
```

Windows PowerShell users should activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Activation remains in effect when you move to another directory in the same
terminal. Return to the repository root before creating and running the
orientation exercise:

```bash
cd ../..
```

Create this practice file inside the repository:

```text
exercises/python_orientation.py
```

Run it from the repository root with:

```bash
python exercises/python_orientation.py
```

You can erase or comment out an example before typing the next one.

## Minute 0–5: Statements, values, and output

Python does not require variable declarations or semicolons:

```python
title = "Learn Python"
task_id = 1
completed = False

print(title)
print(task_id)
print(completed)
```

Expected output:

```text
Learn Python
1
False
```

Names are case-sensitive. `completed`, `Completed`, and `COMPLETED` are three
different names. Python's boolean values are written `True` and `False`, with
capital letters. The absence of a value is represented by `None`.

Inspect a value's runtime type with `type`:

```python
print(type(title))
print(type(task_id))
print(type(completed))
```

The output identifies `str`, `int`, and `bool`.

### Checkpoint

Change the values and print a sentence containing all three. The next section
shows the preferred formatting syntax.

## Minute 5–10: Strings and f-strings

Python strings can use single or double quotes. Be consistent within a project.
An f-string inserts expressions into text:

```python
status = "done" if completed else "pending"
print(f"Task {task_id}: {title} [{status}]")
```

Expected output:

```text
Task 1: Learn Python [pending]
```

The expression in this example is Python's conditional expression:

```text
value_when_true if condition else value_when_false
```

Useful string operations include:

```python
raw_title = "  Learn Python  "
clean_title = raw_title.strip()

print(clean_title)
print(clean_title.lower())
print(len(clean_title))
```

`strip()` removes surrounding whitespace. This will later help reject a title
that contains spaces but no meaningful text.

### Checkpoint

Predict the result before running:

```python
name = "agent"
print(f"{name.upper()} has {len(name)} letters")
```

## Minute 10–15: Conditions and indentation

Python uses indentation instead of braces to define a block:

```python
title = "Learn Python"

if title.strip() == "":
    print("A title is required")
else:
    print(f"Adding: {title}")
```

The colon begins a block. The standard indentation is four spaces. Statements
at the same indentation level belong to the same block.

Python's common comparison and logical operators are:

| Meaning | Python |
|---|---|
| Equal | `==` |
| Not equal | `!=` |
| Greater/less than | `>`, `<`, `>=`, `<=` |
| Logical AND | `and` |
| Logical OR | `or` |
| Logical NOT | `not` |
| Membership | `in`, `not in` |

For an empty string, list, or dictionary, Python allows a shorter condition:

```python
if not title.strip():
    print("A title is required")
```

### Common mistake

This code is invalid because its block is not indented:

```python
if title:
print(title)
```

Python reports `IndentationError`. Indent `print(title)` by four spaces.

### Checkpoint

Write a condition that prints `valid` only when `task_id` is greater than zero
and the cleaned title is not empty.

## Minute 15–22: Lists and loops

A list is an ordered, mutable collection:

```python
titles = ["Learn Python", "Build task manager"]

titles.append("Write tests")

print(titles[0])
print(len(titles))
```

List indexes start at zero. `append` changes the existing list by adding one
item.

Loop directly over the values:

```python
for title in titles:
    print(title)
```

Use `enumerate` when you also need a position:

```python
for position, title in enumerate(titles, start=1):
    print(f"{position}. {title}")
```

Expected output:

```text
1. Learn Python
2. Build task manager
3. Write tests
```

Do not manually manage a numeric loop index when `enumerate` expresses the
intent more clearly.

### Checkpoint

Add a fourth title and print only the titles whose text contains `Python`.
String membership uses the `in` operator.

## Minute 22–28: Dictionaries

A dictionary maps keys to values. It is a natural first representation for one
task:

```python
task = {
    "id": 1,
    "title": "Learn Python",
    "completed": False,
}

print(task["title"])

task["completed"] = True
print(task)
```

The trailing comma after the final entry is allowed and makes future edits
easier. Accessing a missing key with square brackets raises `KeyError`.

Use `get` when a missing key is acceptable:

```python
print(task.get("description"))
print(task.get("description", "No description"))
```

A task manager holds multiple task dictionaries in a list:

```python
tasks = [
    {"id": 1, "title": "Learn Python", "completed": True},
    {"id": 2, "title": "Build task manager", "completed": False},
]

for task in tasks:
    print(f'{task["id"]}: {task["title"]}')
```

Here, `task` is the loop variable for one dictionary at a time.

### Checkpoint

Add a third task dictionary, then print only incomplete tasks.

## Minute 28–36: Functions

Functions are declared with `def`:

```python
def format_task(task):
    marker = "x" if task["completed"] else " "
    return f'[{marker}] {task["id"]}: {task["title"]}'


task = {"id": 1, "title": "Learn Python", "completed": False}
formatted = format_task(task)
print(formatted)
```

Expected output:

```text
[ ] 1: Learn Python
```

`return` sends a value to the caller. A function without an explicit `return`
returns `None`.

The two blank lines between top-level functions and other top-level code follow
Python's standard style convention.

### Local and global names

A name created inside a function is local to that function. A mutable list
passed into a function can be changed by that function:

```python
def add_title(titles, title):
    titles.append(title)


titles = []
add_title(titles, "Learn Python")
print(titles)
```

For the first task manager, you may use a module-level `tasks` list to keep the
exercise simple. Later phases will improve state management and persistence.

### Checkpoint

Write `is_valid_title(title)` that returns `True` when a title contains
non-whitespace characters and `False` otherwise. Test it with these values:

```python
"Learn Python"
""
"   "
```

## Minute 36–40: Type hints

Python type hints describe expected values for readers and development tools:

```python
def is_valid_title(title: str) -> bool:
    return bool(title.strip())
```

Type hints normally do not enforce types at runtime. They improve editor
feedback and can be checked by additional tools.

Built-in collection types can also be annotated:

```python
titles: list[str] = []
task: dict[str, object] = {
    "id": 1,
    "title": "Learn Python",
    "completed": False,
}
```

`dict[str, object]` means that keys are strings and values may be different
Python object types. Later, you will learn more precise representations such as
classes, data classes, or `TypedDict`. They are unnecessary for this first
exercise.

### Checkpoint

Add type hints to the `format_task` function. Its parameter is currently a
dictionary with string keys, and its return value is a string.

## Minute 40–45: Modules and the entry point

Python executes top-level statements when a file is imported or run. This
pattern distinguishes direct execution from importing:

```python
def main() -> None:
    print("Task manager starting")


if __name__ == "__main__":
    main()
```

When the module is run directly, Python sets `__name__` to `"__main__"` and
calls `main`. When another module imports it, the functions become available
without automatically starting the application.

Place the example in
`projects/phase-01-python-cli/agentic_assistant/task_manager.py`, then run it
from the Phase 1 directory:

```bash
python -m agentic_assistant.task_manager
```

Expected output:

```text
Task manager starting
```

## Final exercise: model two tasks

Move or retype your `format_task` function into
`projects/phase-01-python-cli/agentic_assistant/task_manager.py` above `main`.
Without copying a completed task-manager solution, extend `main` so it:

1. Creates an empty list named `tasks`.
2. Creates two task dictionaries.
3. Appends both dictionaries to the list.
4. Loops over the list.
5. Uses `format_task` to print each task.

Expected output should follow this shape:

```text
[ ] 1: Learn Python
[x] 2: Complete orientation
```

The exact titles may differ. At least one task should be complete and one
should be incomplete.

## Knowledge check

Answer these questions before continuing. Suggested answers appear below the
divider.

1. Why is a list suitable for holding multiple tasks?
2. Why is a dictionary suitable for representing one task initially?
3. What is the difference between `=` and `==`?
4. Why does indentation matter in Python?
5. What does `return` do?
6. Do type hints automatically reject incorrect runtime values?
7. Why use the `if __name__ == "__main__"` condition?

<details>
<summary>Suggested answers</summary>

1. A list is ordered, can contain multiple items, and can be changed with
   operations such as `append`.
2. A dictionary associates named keys such as `id` and `title` with their
   values without requiring a class.
3. `=` assigns a value; `==` compares two values for equality.
4. Indentation defines which statements belong to conditions, loops,
   functions, and other blocks.
5. `return` stops the function and sends a value back to its caller.
6. No. Type hints mainly help readers, editors, and static-analysis tools.
7. It starts the program when the module is executed while preventing that
   startup behavior when the module is imported.

</details>

## Common errors

### `IndentationError`

Check that every statement inside a function, condition, or loop is indented by
four spaces. Avoid mixing tabs and spaces.

### `SyntaxError`

Look immediately before the indicated location for a missing colon, quote,
parenthesis, bracket, or comma.

### `NameError`

The name may be misspelled, have different capitalization, or exist only in a
different scope.

### `KeyError`

The requested dictionary key does not exist. Print the dictionary and compare
the exact key spelling.

### `TypeError`

An operation received an incompatible value. Read the message to identify the
operation and the actual types involved, then use `type(value)` if necessary.

## Completion checkpoint

- [ ] I can use Python indentation without braces.
- [ ] I can create and modify a list.
- [ ] I can create, read, and update a dictionary.
- [ ] I can loop over a list of task dictionaries.
- [ ] I can write and call a function.
- [ ] I understand that type hints document expectations but do not normally
      enforce them at runtime.
- [ ] I can explain the module entry-point condition.
- [ ] My final two-task exercise runs successfully.

You are now ready to implement `add_task` and `list_tasks` in the Phase 1 task
manager.

---

**Previous:** [← Repository and Python setup](01-repository-and-python-setup.md)

**Next:** [Build and test the Phase 1 task manager →](03-building-and-testing-phase-01.md)

**Tutorial home:** [Tutorial index](README.md)
