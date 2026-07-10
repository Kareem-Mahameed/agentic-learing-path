# Repository and Python Setup

This page prepares the repository for the Python phase projects. You only need
to complete the machine setup once. Each phase will have its own project files
and may have its own virtual environment.

## Learning outcome

After this lesson, you will be able to:

- Open the repository in VS Code.
- Verify which Python interpreter is running.
- Create and activate an isolated virtual environment.
- Select the same interpreter in VS Code.
- Explain which generated files should not be committed to Git.
- Run a Python module from the Phase 1 project.

## Prerequisites

You need:

- Git
- Python 3.12 or newer
- Visual Studio Code
- The Microsoft **Python** and **Pylance** VS Code extensions

The examples use macOS or Linux shell commands. Windows alternatives are shown
where activation differs.

## 1. Verify Git and Python

Open a terminal and run:

```bash
git --version
python3 --version
```

Both commands should print a version. For example:

```text
git version 2.x.x
Python 3.14.x
```

The exact patch versions do not need to match. If `python3` is not found,
install Python before continuing. After installation, close and reopen the
terminal so it can discover the new command.

## 2. Move to the repository

Run the following command, replacing the path if your clone is elsewhere:

```bash
cd /path/to/agentic-learing-path
```

Confirm your location:

```bash
pwd
```

List the repository contents:

```bash
ls
```

You should see entries including `README.md`, `tutorial`, and `projects`.

## 3. Open the repository in VS Code

If the `code` command is installed:

```bash
code .
```

Otherwise, open VS Code and select **File → Open Folder**, then choose the
repository root. Opening the root rather than an individual Python file keeps
the tutorial and all phase snapshots visible in the Explorer.

Install these VS Code extensions from the Extensions view:

- **Python**, published by Microsoft
- **Pylance**, published by Microsoft

The Python extension runs and debugs Python. Pylance provides completion, type
information, and early error detection.

## 4. Enter the Phase 1 project

Open VS Code's integrated terminal with **Terminal → New Terminal**, then run:

```bash
cd projects/phase-01-python-cli
```

Check the location again:

```bash
pwd
```

The path should end with:

```text
projects/phase-01-python-cli
```

The current working directory matters. The commands in the Phase 1 README
assume that the terminal is inside this directory.

## 5. Create a virtual environment

A virtual environment is an isolated Python installation for one project. It
prevents packages required by one phase from changing the dependencies of
another phase or your system Python.

Create it inside the Phase 1 directory:

```bash
python3 -m venv .venv
```

The command creates a `.venv` directory. Do not edit anything inside it by
hand, and do not commit it to Git. It can always be recreated.

### Activate it on macOS or Linux

```bash
source .venv/bin/activate
```

### Activate it in Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal prompt usually begins with `(.venv)`.

Verify the active interpreter:

```bash
python --version
which python
```

On Windows PowerShell, use this instead of `which`:

```powershell
Get-Command python
```

The interpreter path should point inside `phase-01-python-cli/.venv`.

Activation only affects the current terminal session. When you open a new
terminal later, return to the phase directory and activate the environment
again.

To leave the environment, run:

```bash
deactivate
```

## 6. Select the interpreter in VS Code

The terminal and VS Code editor should use the same Python interpreter.

1. Press **Cmd+Shift+P** on macOS or **Ctrl+Shift+P** on Windows/Linux.
2. Search for **Python: Select Interpreter**.
3. Select the interpreter whose path contains
   `phase-01-python-cli/.venv`.

If it is not listed, choose **Enter interpreter path** and locate:

```text
.venv/bin/python
```

On Windows, locate:

```text
.venv\Scripts\python.exe
```

## 7. Understand the Phase 1 files

The initial Phase 1 layout is:

```text
phase-01-python-cli/
├── .venv/                    # Generated locally; never committed
├── README.md                 # Phase objective and commands
├── pyproject.toml            # Project and tool configuration
├── agentic_assistant/
│   ├── __init__.py           # Marks a Python package
│   └── task_manager.py       # Phase 1 implementation
└── tests/                    # Automated tests added during the phase
```

The `agentic_assistant` directory is a Python package because it contains
`__init__.py`. The command `python -m` can therefore run one of its modules by
its dotted name.

## 8. Understand ignored files

Generated and secret files should not be committed. Create a `.gitignore` in
the repository root so that its rules apply to every phase. It should cover at
least:

```gitignore
**/.venv/
**/__pycache__/
*.py[cod]
**/.pytest_cache/
**/.ruff_cache/
**/.env
.DS_Store
```

- `.venv` contains a machine-specific environment.
- `__pycache__` and `.pyc` files are generated bytecode.
- `.pytest_cache` and `.ruff_cache` are generated tool caches.
- `.env` may contain API keys and other secrets in later phases.

If a phase already has its own `.gitignore`, keeping it is harmless, but a rule
inside one phase does not apply to its sibling phases.

Check repository changes with:

```bash
git status --short
```

You should not see `.venv` or `__pycache__` files in the output.

## 9. Run the Phase 1 module

With the environment active and the terminal inside
`projects/phase-01-python-cli`, run:

```bash
python -m agentic_assistant.task_manager
```

An empty `task_manager.py` exits without printing anything. That is still a
successful run. After the next lesson, the file will begin producing output.

Why use `python -m agentic_assistant.task_manager` instead of running the file
path directly?

- Python treats the code as part of its package.
- Imports behave consistently as the project grows.
- The same command works regardless of the internal source filename location.

## Troubleshooting

### `python3: command not found`

Python is not installed or is not available on your shell's command path.
Install Python, reopen the terminal, and repeat the version check.

### `No module named venv`

Some Linux distributions package virtual-environment support separately.
Install the `venv` package that matches your Python version, then repeat the
creation command.

### `No module named agentic_assistant`

The terminal is probably in the wrong directory. Run `pwd`. It must end in
`projects/phase-01-python-cli` when you execute the module command.

### VS Code uses a different Python version

Run **Python: Select Interpreter** again and choose the interpreter inside the
phase's `.venv`. Opening a new terminal after selection can also refresh the
environment.

### `.venv` appears in `git status`

Confirm that an applicable `.gitignore` contains `**/.venv/`. Ignore rules in
one phase directory do not apply to sibling phase directories, so repository-
wide rules belong in the repository root.

## Completion checkpoint

Before continuing, confirm every statement:

- [ ] `python3 --version` prints Python 3.12 or newer.
- [ ] VS Code has the Python and Pylance extensions.
- [ ] The Phase 1 `.venv` exists and can be activated.
- [ ] `which python` or `Get-Command python` points inside `.venv`.
- [ ] VS Code has the same `.venv` interpreter selected.
- [ ] `python -m agentic_assistant.task_manager` runs without an import error.
- [ ] `git status --short` does not show `.venv` or cache files.

---

**Previous:** [← Tutorial home](README.md)

**Next:** [45-minute Python orientation →](02-python-orientation.md)
