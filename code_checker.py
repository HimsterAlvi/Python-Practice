#!/usr/bin/env python3
"""
code_checker.py — Run your practice scripts through this to get feedback on
how to improve and where you might be messing up. Use the output to fix code
or to ask Cursor for help at specific lines.
"""

import ast
import re
import sys
from pathlib import Path


def read_file(path: Path) -> str:
    """Read file contents; return empty string on error."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return ""


def get_lines(path: Path) -> list[str]:
    """Return list of lines (for line-number feedback)."""
    return read_file(path).splitlines()


def check_syntax(path: Path, source: str) -> list[dict]:
    """Check for syntax errors. Return list of {line, message, severity}."""
    issues = []
    try:
        ast.parse(source)
    except SyntaxError as e:
        issues.append({
            "line": e.lineno or 0,
            "message": f"Syntax error: {e.msg}",
            "severity": "error",
        })
    return issues


def check_magic_numbers(source: str, path: Path) -> list[dict]:
    """Flag likely magic numbers (e.g. 3.14 for pi)."""
    issues = []
    lines = source.splitlines()
    # Common magic numbers in practice code
    magic = [(r"\b3\.14\b", "Use math.pi instead of 3.14 (see CODING_REFERENCE.md)")]
    for i, line in enumerate(lines, start=1):
        for pattern, msg in magic:
            if re.search(pattern, line) and "math" not in line.lower():
                issues.append({"line": i, "message": msg, "severity": "suggestion"})
                break
    return issues


def check_while_break(source: str) -> list[dict]:
    """Warn if while loop has break in same block with no condition (runs once)."""
    issues = []
    lines = source.splitlines()
    in_while = False
    while_start = 0
    indent_while = -1
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("while "):
            in_while = True
            while_start = i
            indent_while = len(line) - len(line.lstrip())
        elif in_while:
            current_indent = len(line) - len(line.lstrip())
            if current_indent <= indent_while and stripped:
                in_while = False
                continue
            if "break" in stripped and "if " not in lines[max(0, i - 2) : i + 1]:
                # Simple heuristic: break very soon after while with no preceding if
                issues.append({
                    "line": i,
                    "message": "break right after 'while' often makes the loop run only once. Use break only when a condition is met (e.g. valid input). See CODING_REFERENCE.md.",
                    "severity": "warning",
                })
                in_while = False
    return issues


def check_global_usage_in_functions(tree: ast.AST, source: str, path: Path) -> list[dict]:
    """Warn about reading names in functions that look like they should be arguments."""
    issues = []
    lines = source.splitlines()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Names used in function body (simple set; not full resolution)
            used = set()
            for n in ast.walk(node):
                if isinstance(n, ast.Name) and isinstance(getattr(n, "ctx", None), ast.Load):
                    used.add(n.id)
            # Params
            args = [a.arg for a in node.args.args]
            # Common mistake: name like file_name used but not in args
            for name in used:
                if name in ("self", "True", "False", "None", "print", "range", "len", "str", "int", "float", "input"):
                    continue
                if name in args:
                    continue
                if "_" in name and name not in args:
                    # Could be a global; suggest passing as argument
                    for line_no in range(node.lineno, node.end_lineno or node.lineno + 1):
                        if line_no <= len(lines) and name in lines[line_no - 1]:
                            issues.append({
                                "line": line_no,
                                "message": f"Function uses '{name}' but it's not a parameter. Prefer passing it as an argument (see CODING_REFERENCE.md).",
                                "severity": "warning",
                            })
                            break
    return issues


def check_print_vs_return(tree: ast.AST, source: str) -> list[dict]:
    """Suggest return instead of print in functions (optional best practice)."""
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            has_print = any(
                isinstance(n, ast.Call) and getattr(n.func, "id", None) == "print"
                for n in ast.walk(node)
            )
            has_return = any(isinstance(n, ast.Return) for n in ast.walk(node))
            if has_print and not has_return and node.name != "__init__":
                issues.append({
                    "line": node.lineno,
                    "message": "Consider returning a value from this function and letting the caller print (makes code easier to test). See CODING_REFERENCE.md.",
                    "severity": "suggestion",
                })
    return issues


def check_repr_usage(source: str) -> list[dict]:
    """Suggest str() for user output instead of repr()."""
    issues = []
    for i, line in enumerate(source.splitlines(), start=1):
        if "repr(" in line and "print" in line:
            issues.append({
                "line": i,
                "message": "For user-facing output, str() is usually better than repr(). Use repr() for debugging. See CODING_REFERENCE.md.",
                "severity": "suggestion",
            })
    return issues


def run_checks(path: Path) -> list[dict]:
    """Run all checks; return combined list of issues."""
    source = read_file(path)
    if not source.strip():
        return [{"line": 0, "message": "File is empty.", "severity": "info"}]
    issues = []
    issues.extend(check_syntax(path, source))
    if not issues:  # Only continue if no syntax errors
        tree = ast.parse(source)
        issues.extend(check_magic_numbers(source, path))
        issues.extend(check_while_break(source))
        issues.extend(check_global_usage_in_functions(tree, source, path))
        issues.extend(check_print_vs_return(tree, source))
        issues.extend(check_repr_usage(source))
    return issues


def report(path: Path, issues: list[dict], lines: list[str]) -> None:
    """Print a report and Cursor-friendly hints."""
    path_str = path.resolve()
    print("=" * 60)
    print("CODE CHECKER REPORT")
    print("=" * 60)
    print(f"File: {path_str}\n")
    if not issues:
        print("No issues found. Nice work!")
        print("\nTip: Still run your code and test edge cases (e.g. bad input).")
        return
    by_severity = {"error": [], "warning": [], "suggestion": [], "info": []}
    for q in issues:
        by_severity.setdefault(q["severity"], []).append(q)
    for sev in ("error", "warning", "suggestion", "info"):
        for q in by_severity.get(sev, []):
            line_no = q["line"]
            line_preview = ""
            if line_no and line_no <= len(lines):
                line_preview = "  | " + lines[line_no - 1].strip()[:70]
            print(f"  [{sev.upper()}] Line {line_no}: {q['message']}{line_preview}")
    print()
    print("How to use this with Cursor:")
    print("  1. Open this file in Cursor and go to the line number(s) above.")
    print("  2. Ask Cursor: 'Fix the issue at line N' or 'Apply the rule from CODING_REFERENCE.md here'.")
    print("  3. Update CODING_REFERENCE.md -> 'My Problems' with what you learned.")
    print("=" * 60)


def main() -> None:
    if len(sys.argv) < 2:
        # Default: check all .py files in current directory (except this script)
        base = Path(__file__).resolve().parent
        py_files = [f for f in base.glob("*.py") if f.name != "code_checker.py"]
        if not py_files:
            print("Usage: python code_checker.py <file.py> [file2.py ...]")
            print("   Or run from Python_practice folder to check all .py files.")
            sys.exit(1)
    else:
        py_files = [Path(p) for p in sys.argv[1:] if p.endswith(".py")]
        if not py_files:
            print("Usage: python code_checker.py <file.py> [file2.py ...]")
            sys.exit(1)
    for path in py_files:
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.exists():
            print(f"File not found: {path}")
            continue
        issues = run_checks(path)
        lines = get_lines(path)
        report(path, issues, lines)


if __name__ == "__main__":
    main()
