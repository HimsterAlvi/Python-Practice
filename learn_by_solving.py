#!/usr/bin/env python3
"""
learn_by_solving.py - Learn to code by solving the 10 practice problems.
  - Pick a problem, read it, code your solution, then run it here.
  - The program can run your solution (with test input) and run code_checker for you.
"""

import subprocess
import sys
from pathlib import Path

# Base folder for solutions and scripts
SCRIPT_DIR = Path(__file__).resolve().parent

PROBLEMS = [
    {
        "num": 1,
        "title": "Positive or Negative",
        "topic": "if / else",
        "difficulty": 1,
        "description": "Ask the user for a number. Print 'Positive' if > 0, 'Negative' if < 0, 'Zero' if == 0.",
        "example": "Input -5 -> Output 'Negative'",
        "hint": "SYNTAX_TUTORIAL.md -> if / elif / else",
        "suggested_file": "solution_1.py",
        "tests": [("0", "Zero"), ("7", "Positive"), ("-3", "Negative")],
    },
    {
        "num": 2,
        "title": "Sum 1 to N",
        "topic": "for, range",
        "difficulty": 1,
        "description": "Ask for positive integer n. Compute and print sum 1 + 2 + ... + n.",
        "example": "Input 5 -> Output 15",
        "hint": "for i in range(1, n + 1): and add to a variable",
        "suggested_file": "solution_2.py",
        "tests": [("5", "15"), ("1", "1"), ("10", "55")],
    },
    {
        "num": 3,
        "title": "Countdown",
        "topic": "while",
        "difficulty": 1,
        "description": "Ask for a positive integer. Print countdown from that number to 1, then 'Go!'",
        "example": "Input 3 -> Output 3, 2, 1, Go!",
        "hint": "while loop; decrease variable each time",
        "suggested_file": "solution_3.py",
        "tests": [("2", "2\n1\nGo!")],
    },
    {
        "num": 4,
        "title": "Valid Number (1–10)",
        "topic": "while, break, input validation",
        "difficulty": 2,
        "description": "Keep asking until user enters an integer between 1 and 10. Then print 'Valid: X'.",
        "example": "After 0, 15, abc, then 7 -> Output 'Valid: 7'",
        "hint": "CODING_REFERENCE.md -> Repeat until valid input; while True and break when valid",
        "suggested_file": "solution_4.py",
        "tests": [("0\n20\n5", "Valid: 5")],
    },
    {
        "num": 5,
        "title": "Multiplication Table",
        "topic": "nested for",
        "difficulty": 2,
        "description": "Ask for n. Print table: row i has i×1, i×2, ... i×n.",
        "example": "Input 3 -> Output '1 2 3', '2 4 6', '3 6 9'",
        "hint": "Two for loops: outer rows, inner columns",
        "suggested_file": "solution_5.py",
        "tests": [("3", "1 2 3\n2 4 6\n3 6 9")],
    },
    {
        "num": 6,
        "title": "Area of Circle",
        "topic": "function, return, math",
        "difficulty": 2,
        "description": "Function circle_area(radius) returns area using math.pi. Get radius from user (valid: positive, < 1000), print result.",
        "example": "Input 5 -> Output area ~78.54",
        "hint": "CODING_REFERENCE.md -> Circle area; prefer return over print",
        "suggested_file": "solution_6.py",
        "tests": [],  # float output, skip strict test
    },
    {
        "num": 7,
        "title": "List of Squares",
        "topic": "lists, for",
        "difficulty": 2,
        "description": "Ask for n. Build list of squares 1², 2², ... n² and print the list.",
        "example": "Input 4 -> Output [1, 4, 9, 16]",
        "hint": "squares = []; loop and squares.append(i ** 2)",
        "suggested_file": "solution_7.py",
        "tests": [("4", "[1, 4, 9, 16]")],
    },
    {
        "num": 8,
        "title": "Min and Max",
        "topic": "function, list",
        "difficulty": 2,
        "description": "Function min_max(numbers) returns (smallest, largest). Don't use built-in min/max. Get 3 numbers from user, print result.",
        "example": "Input 3, 1, 2 -> Output (1, 3)",
        "hint": "Loop over list; track smallest and largest",
        "suggested_file": "solution_8.py",
        "tests": [("3\n1\n2", "(1, 3)")],
    },
    {
        "num": 9,
        "title": "Word Repeater",
        "topic": "function, string",
        "difficulty": 2,
        "description": "Function repeat_word(word, n) returns word repeated n times with spaces. Get word and n from user, print result.",
        "example": "Input hello, 2 -> Output 'hello hello'",
        "hint": "(word + ' ') * n then strip, or loop",
        "suggested_file": "solution_9.py",
        "tests": [("hi\n3", "hi hi hi")],
    },
    {
        "num": 10,
        "title": "Counter Class (OOP)",
        "topic": "class, __init__, methods",
        "difficulty": 3,
        "description": "Class Counter: __init__(self, start=0), increment(self), value(self). Create counter, increment 3 times, print value (3).",
        "example": "No input -> Output 3",
        "hint": "SYNTAX_TUTORIAL.md -> OOP; use self for current count",
        "suggested_file": "solution_10.py",
        "tests": [("", "3")],
    },
]


def stars(d: int) -> str:
    return "*" * d + "-" * (3 - d)  # e.g. *-- for easy, *** for hard


def show_problem(p: dict) -> None:
    print()
    print("=" * 60)
    print(f"  Problem {p['num']}: {p['title']}  [{stars(p['difficulty'])}]")
    print("=" * 60)
    print(f"  Topic: {p['topic']}")
    print()
    print("  " + p["description"].replace("\n", "\n  "))
    print()
    print("  Example: " + p["example"])
    print()
    print("  Hint: " + p["hint"])
    print("  Suggested file: " + p["suggested_file"])
    print("=" * 60)
    print()


def run_solution(script_path: Path, stdin_text: str, timeout: int = 5) -> tuple[bool, str, str]:
    """Run script with optional stdin. Return (success, stdout, stderr)."""
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(script_path.parent),
            input=stdin_text,
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout"
    except Exception as e:
        return False, "", str(e)


def normalize(s: str) -> str:
    """Strip and normalize line endings for comparison."""
    return s.strip().replace("\r\n", "\n").replace("\r", "\n")


def run_tests(p: dict, script_path: Path) -> list[tuple[bool, str, str]]:
    """Run test cases. Return list of (passed, expected, got)."""
    results = []
    for stdin_text, expected in p.get("tests", []):
        ok, out, err = run_solution(script_path, stdin_text)
        got = normalize(out)
        exp = normalize(expected)
        passed = ok and exp in got or got.strip() == exp.strip()
        results.append((passed, exp, got))
    return results


def run_code_checker(script_path: Path) -> None:
    """Run code_checker.py on the given file."""
    checker = SCRIPT_DIR / "code_checker.py"
    if not checker.exists():
        print("  (code_checker.py not found; skip.)")
        return
    print("\n--- Code checker output ---")
    subprocess.run([sys.executable, str(checker), str(script_path)], cwd=str(SCRIPT_DIR))
    print("--- End code checker ---\n")


def main() -> None:
    print("\n  Learn by Solving - 10 Practice Problems")
    print("  Open PRACTICE_PROBLEMS.md for full descriptions.\n")
    while True:
        print("  1-10: Show problem N")
        print("  r N [file]: Run your solution for problem N (default file: solution_N.py)")
        print("  c N [file]: Run code_checker on solution for problem N")
        print("  t N [file]: Run tests for problem N")
        print("  q: Quit")
        choice = input("\n  Choice: ").strip().lower()
        if not choice:
            continue
        if choice == "q":
            print("  Bye. Log your progress in CODING_REFERENCE.md!")
            break
        parts = choice.split()
        cmd = parts[0]
        try:
            num = int(parts[1]) if len(parts) > 1 else None
        except (IndexError, ValueError):
            num = None
        if cmd in ("r", "c", "t") and (num is None or num < 1 or num > 10):
            print("  Use: r 3  or  r 3 my_solution.py")
            continue
        problem = next((p for p in PROBLEMS if p["num"] == num), None) if num else None
        if cmd in ("r", "c", "t") and not problem:
            continue
        suggested = problem["suggested_file"] if problem else ""
        file_name = (parts[2] if len(parts) > 2 else suggested).strip() or suggested
        script_path = (SCRIPT_DIR / file_name).resolve() if file_name else None

        if cmd.isdigit() or (len(cmd) == 1 and cmd in "1234567890"):
            n = int(cmd) if cmd.isdigit() else int(parts[0])
            p = next((x for x in PROBLEMS if x["num"] == n), None)
            if p:
                show_problem(p)
            else:
                print("  Unknown problem number.")
            continue

        if cmd == "r":
            if not script_path or not script_path.exists():
                print(f"  File not found: {script_path or file_name}. Create it and try again.")
                continue
            print(f"\n  Running: {script_path}")
            if problem.get("tests"):
                stdin_text = problem["tests"][0][0]
                print(f"  (Using sample input: {repr(stdin_text[:50])}...)")
            else:
                stdin_text = ""
            ok, out, err = run_solution(script_path, stdin_text)
            print("  stdout:", out or "(none)")
            if err:
                print("  stderr:", err)
            print("  Exit: OK" if ok else "  Exit: ERROR")
            continue

        if cmd == "c":
            if not script_path or not script_path.exists():
                print(f"  File not found: {script_path or file_name}.")
                continue
            run_code_checker(script_path)
            continue

        if cmd == "t":
            if not script_path or not script_path.exists():
                print(f"  File not found: {script_path or file_name}.")
                continue
            tests = problem.get("tests", [])
            if not tests:
                print("  No automated tests for this problem. Run it with 'r' and check by hand.")
                continue
            results = run_tests(problem, script_path)
            all_ok = True
            for i, (passed, exp, got) in enumerate(results, 1):
                status = "PASS" if passed else "FAIL"
                if not passed:
                    all_ok = False
                print(f"  Test {i}: {status}")
                if not passed:
                    print(f"    Expected (contains): {exp[:80]}")
                    print(f"    Got:                {got[:80]}")
            if all_ok:
                print(f"  All tests passed. Run code_checker next (c {num}).")
            continue

        # Show problem by number
        try:
            n = int(parts[0])
            p = next((x for x in PROBLEMS if x["num"] == n), None)
            if p:
                show_problem(p)
            else:
                print("  Unknown problem. Use 1–10.")
        except (ValueError, IndexError):
            print("  Unknown command. Use 1–10, r, c, t, or q.")


if __name__ == "__main__":
    main()
