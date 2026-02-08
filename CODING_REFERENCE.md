# Python Data Analysis — Coding Reference

**Purpose:** Your space to practice Python. Use this file as the single source of truth for how you code, rules to follow, and a log of problems so you (and Cursor) can improve over time.

---

## 1. How You Code (Conventions)

- **Spacing:** You use a space after `print` before the opening parenthesis: `print ("hello")`. (Standard style is `print("hello")` — no space. Either is valid; pick one and stick to it.)
- **Comments:** You use `#` for single-line comments. Keep comments above the line or at the end of the line for short notes.
- **Naming:** Use `snake_case` for variables and functions (e.g. `circle_area`, `file_name_func`).
- **Constants:** For fixed values (e.g. pi), prefer named constants or `math.pi` instead of typing `3.14` in the code.
- **Type hints (optional):** As you get comfortable, add types for function arguments and return values, e.g. `def circle_area(radius: float) -> float:`.

---

## 2. Rules You Must Follow

1. **One or two problems per day** — Solve 1–2 practice problems daily; log them in "My Problems" below.
2. **Run through code_checker.py** — Before considering a problem "done", run it through `code_checker.py` and fix what it suggests.
3. **No magic numbers** — Use named constants or `math` (e.g. `math.pi`) instead of raw numbers like `3.14`.
4. **Functions use arguments** — Don’t rely on global variables inside functions. Pass inputs as parameters and return results (e.g. `def file_name_func(file_name):` and use `file_name` inside).
5. **Validate user input** — Check range/type before using (e.g. radius 0–100). Use loops or retries until input is valid, not a single `break` that exits immediately.
6. **Prefer `return` over `print` inside functions** — Have functions return values; let the caller `print` if needed. This keeps code testable and reusable.
7. **One logical idea per comment** — Comment *why* when it’s not obvious, not every line.

---

## 3. Methods and Patterns to Use

| Goal | Method / Pattern |
|------|-------------------|
| Get file extension | `filename.split(".")[-1]` or `pathlib.Path(filename).suffix` |
| Circle area | `math.pi * radius ** 2` (import math) |
| User input as number | `float(input("Prompt: "))` and handle `ValueError` with try/except |
| Repeat until valid input | `while True:` with validation and `break` when valid |
| String + number in message | `f"The area is {area}"` or `"The area is " + str(area)` |
| Check type at runtime | `type(x)` or `isinstance(x, int)` |

---

## 4. My Problems (Log)

*Add one short line per problem you solve. Optionally note: topic, file name, and one lesson learned.*

| Date | Problem / Topic | File | Lesson / Mistake |
|------|------------------|------|-------------------|
| *(example)* | Circle area from radius | Practice.py | Use `math.pi`, not 3.14; don’t `break` right after loop start |
| *(example)* | File extension from filename | Practice.py | Pass `file_name` into function as argument instead of using global |
| | | | |
| | | | |
| | | | |

*(Add new rows as you solve problems. Review this table when using Cursor so it knows your weak spots.)*

---

## 5. Common Mistakes to Avoid (Reminders)

- **While + immediate break** — If you `break` in the first iteration no matter what, the loop runs only once. Use `break` only when a condition is satisfied (e.g. valid input).
- **Using variables before they exist** — In a function, only use names that are passed in as parameters or defined inside the function. Don’t assume a global like `file_name` exists unless you pass it in.
- **print vs return** — Prefer `return value` in functions; print at the call site. Exception: scripts that only print to the user can use `print` inside for simplicity.
- **repr() vs str()** — Use `str(x)` for user-facing text. Use `repr(x)` when you need a debug-style representation (e.g. with quotes for strings).

---

## 6. File and Folder Conventions

- **Practice scripts:** e.g. `Practice.py`, `Variables.py`, `String methods.py`.
- **Run checker:** `python code_checker.py <path_to_your_script.py>` (or as documented in code_checker.py).
- **This reference:** `CODING_REFERENCE.md` — update "My Problems" and "Common Mistakes" as you go.
- **Syntax help:** `SYNTAX_TUTORIAL.md` — quick reference for if/for/while/OOP.

---

*Update this file whenever you add a new rule, method, or problem. Cursor can use it to give you consistent, personalized feedback.*
