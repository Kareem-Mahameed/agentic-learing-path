# Agentic Development Tutorial

This tutorial turns the 12-week learning plan into a sequence of practical,
self-contained lessons. It assumes that you understand basic programming in
another language, but that you may be completely new to Python.

You do not need Codex or another AI assistant to complete the lessons. Each page
explains the objective, commands, concepts, exercises, expected results, and
common problems.

## How to use this tutorial

1. Complete the pages in order.
2. Type the examples yourself instead of copying large completed programs.
3. Run every example and compare its output with the expected result.
4. Complete each checkpoint before moving to the next page.
5. Keep your phase projects independent so that earlier versions remain
   available for comparison.

## Tutorial pages

| Step | Lesson | Outcome |
|---:|---|---|
| 1 | [Repository and Python setup](01-repository-and-python-setup.md) | Prepare Git, Python, a virtual environment, and VS Code |
| 2 | [45-minute Python orientation](02-python-orientation.md) | Learn enough Python syntax to begin the task manager |
| 3 | [Build and test the Phase 1 task manager](03-building-and-testing-phase-01.md) | Build the CLI incrementally and validate it with pytest |

More pages will be added as later phase projects progress.

## Repository map

```text
agentic-learing-path/
├── README.md                 # The complete 12-week plan
├── tutorial/                 # The lessons you are reading
├── exercises/                # Small, focused practice programs
├── notes/                    # Your own learning notes
└── projects/
    ├── phase-01-python-cli/
    ├── phase-02-api-json-async/
    └── ...
```

Each directory under `projects/` is a standalone snapshot. A later phase may be
based on an earlier phase, but completing a later phase must not overwrite the
earlier implementation.

## Getting help without an AI assistant

When something fails:

1. Read the complete error message from the bottom upward.
2. Confirm that the terminal is in the directory shown by the lesson.
3. Confirm that the virtual environment is active.
4. Compare spelling, capitalization, indentation, and punctuation carefully.
5. Reduce the program to the smallest example that still fails.
6. Consult the official Python documentation for the specific function or
   error type.

---

**Next:** [Repository and Python setup →](01-repository-and-python-setup.md)
