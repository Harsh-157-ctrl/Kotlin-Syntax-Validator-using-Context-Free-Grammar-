# Kotlin Subset Lexer & Parser

A Python-based lexer and parser for a subset of the Kotlin programming language. Built using the **PLY (Python Lex-Yacc)** library, this project can process Kotlin code snippets, validate their syntax, and generate an Abstract Syntax Tree (AST).

It includes an interactive command-line interface (REPL) that allows you to type multi-line Kotlin code and immediately see the generated AST or syntax errors.

## Features

This parser supports a core subset of Kotlin syntax, including:
* **Variable Declarations:** `var` and `val` with optional type annotations and initialization.
* **Loops:** `while` loops and `for...in` loops.
* **Control Flow:** `return` statements and block scoping (`{ }`).
* **Expressions:** Binary operations (`+`, `-`, `*`, `/`), comparisons (`<`, `>`, `<=`, `>=`, `==`, `!=`), and grouping.
* **Data Types:** Integers, Floats, Strings, and Identifiers.
* **Comments:** Single-line (`//`) and Multi-line (`/* */`).

## Requirements

* Python 3.x
* PLY (Python Lex-Yacc)

You can install the required dependency via pip:
```bash
pip install ply