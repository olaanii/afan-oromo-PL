# Afan Oromo Programming Language (AOBL) - Translator
Group Memebers
Name                              Id.no

1. Samuel Tesfachew -------------   UGR/31190/15

2. Olani Shambel ------------------ UGR/31097/15

3. Yeabsira Zerihun --------------  UGR/31384/15

4. Kenenisa Mekonen ------------    UGR/30771/15

5. Israel Bekele -----------------  UGR/30715/15

A beginner-oriented programming language that translates Afan Oromo source code (`.or` files) into executable Python 3 code. AOBL reduces the English syntax barrier for Afan Oromo speakers learning programming by using familiar native language keywords and terminology.

## Overview

AOBL (Afan Oromo Beginner Language) provides an accessible entry point into programming by combining:
- **Native language support**: Keywords and error messages in Afan Oromo
- **Structured compiler architecture**: Proper lexical analysis, parsing, type checking, and code generation
- **Python compatibility**: Translated code runs as standard Python 3
- **Educational focus**: Designed for beginners transitioning to mainstream programming

## Architecture & Compilation Pipeline

The translator follows a structured multi-stage compilation process:

```
.or Source Code
      ↓
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    Lexer    │ --> │    Parser   │ --> │ Type Checker│ --> │   Generator │
│  (Tokens)   │     │    (AST)    │     │  (Validate) │     │  (Python)   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

1. **Lexical Analysis** (`lexer.py`): Converts source text into tokens, handles indentation (space-based), and supports Unicode identifiers
2. **Parsing** (`parser.py`): Recursive descent parser builds an Abstract Syntax Tree (AST) with operator precedence
3. **Type Checking** (`type_checker.py`): Validates type consistency and infers types with localized error messages
4. **Code Generation** (`generator.py`): Produces clean, executable Python 3 code

## Project Structure

### Root Directory

| File | Purpose |
|------|---------|
| `translator.py` | CLI entry point and main translation orchestrator. Handles file I/O, error reporting, and coordinates the compilation pipeline |
| `netlify.toml` | Deployment configuration (for associated web frontend project) |
| `README.md` | This documentation file |

### Core Language Package (`afan_oromo_lang/`)

| File | Purpose | Key Components |
|------|---------|----------------|
| `__init__.py` | Package initialization | Declares the afan_oromo_lang package |
| `lexer.py` | Tokenization and lexical analysis | `Token` dataclass, `KEYWORDS` set, `Lexer` class with indentation tracking, `LexerError` exception |
| `parser.py` | Syntax analysis and AST construction | `Parser` class with recursive descent parsing, `ParserError` exception, operator precedence handling |
| `ast_nodes.py` | Abstract Syntax Tree node definitions | All AST node classes: `Program`, `VarDecl`, `FunctionDef`, `IfStatement`, `WhileStatement`, `ForStatement`, `BinaryOp`, `Literal`, etc. |
| `type_checker.py` | Semantic analysis and type validation | `TypeChecker` class, `TypeEnv` environment, `TypeErrorAfan` exception with localized messages |
| `generator.py` | Python code generation | `CodeGenerator` class that traverses AST and emits Python code |

### Documentation (`docs/`)

| File | Purpose |
|------|---------|
| `language_spec.md` | Complete language specification covering keywords, syntax, type system, and compilation process |
| `short_report.md` | Project overview, design objectives, and development summary |

### Examples (`examples/`)

| File | Purpose |
|------|---------|
| `basic.or` | Sample Afan Oromo source code demonstrating basic syntax |
| `basic.py` | Generated Python code from `basic.or` |
| `basic.out` | Expected output from running the example |

### Tests (`tests/`)

| File | Purpose |
|------|---------|
| `test_translator.py` | Unit tests covering translation pipeline: basic expressions, conditionals, loops, functions, exception handling |

## Language Features

### Keywords (Afan Oromo)

| Afan Oromo | English Equivalent | Purpose |
|------------|-------------------|---------|
| `haa` | let/var | Variable declaration |
| `yoo` | if | Conditional statement |
| `yoo_tahe` | elif | Else-if condition |
| `yookaan` | else | Else condition |
| `hanga` | while | While loop |
| `irra ... keessa` | for ... in | For loop |
| `hojii` | def | Function definition |
| `deebi'i` | return | Return statement |
| `maxxansi` | print | Output function |
| `dhugaa` | True | Boolean true |
| `soba` | False | Boolean false |
| `fi` | and | Logical AND |
| `yookiin` | or | Logical OR |
| `miti` | not | Logical NOT |
| `yaali` | try | Try block |
| `qabsiisi` | except | Exception handler |
| `dhuma` | finally | Finally block |
| `kuti` | break | Loop break |
| `itti_fufi` | continue | Loop continue |
| `darbi` | pass | No-op statement |

### Type System

| Afan Oromo Type | Python Type | Description |
|-----------------|-------------|-------------|
| `lakkoofsa` | `int` | Integer numbers |
| `lakkf` | `float` | Floating-point numbers |
| `barruu` | `str` | Strings |
| `dhugaa` | `bool` | Boolean values |

### Syntax Examples

**Variable Declaration:**
```or
haa x: lakkoofsa = 5
haa name = "Oromia"
```

**Conditional Statements:**
```or
yoo x > 5:
    maxxansi("Greater")
yoo_tahe x > 3:
    maxxansi("Medium")
yookaan:
    maxxansi("Small")

# Natural form:
yoo (x > 5) ta'e:
    maxxansi("Yes")
yoo hin ta'in:
    maxxansi("No")
```

**Loops:**
```or
# While loop
hanga x < 10:
    x = x + 1

# For loop
irra item keessa tarree:
    maxxansi(item)
```

**Functions:**
```or
hojii add(a: lakkoofsa, b: lakkoofsa) -> lakkoofsa:
    deebi'i a + b
```

**Exception Handling:**
```or
yaali:
    risky_operation()
qabsiisi error:
    maxxansi("Error occurred")
dhuma:
    maxxansi("Cleanup")
```

## Usage

### Command Line

**Translate a .or file to Python:**
```bash
# Linux/macOS
python translator.py examples/basic.or

# Windows (PowerShell)
python .\translator.py examples\basic.or
```

**Specify custom output file:**
```bash
python translator.py examples/basic.or -o output.py
```

**Run the generated Python:**
```bash
python examples/basic.py
```

### As a Module

```python
from translator import translate_source

source = """
haa x = 10
maxxansi(x)
"""

python_code = translate_source(source)
print(python_code)  # Output: x = 10\nprint(x)\n
```

## Error Messages

All error messages are localized in Afan Oromo:

| Error | Meaning |
|-------|---------|
| `Dogoggora: indentation sirrii miti` | Indentation is incorrect |
| `Dogoggora: type hin wal simne` | Type mismatch |
| `Dogoggora: barruu guutuu hin cufamne` | String not properly closed |
| `Dogoggora: jecha hin beekamne` | Unknown character/token |

## Testing

Run the test suite:
```bash
python -m pytest tests/test_translator.py -v
```

Tests cover:
- Basic variable translation and arithmetic
- If/else conditional translation
- For and while loop translation
- Function definition with type annotations
- Try/except/finally exception handling
- Natural language conditional forms

## Current Limitations

- No class/object-oriented programming support
- No module/import system
- No dictionary or set data structures
- No decorators or async/await
- No advanced type hints (generics, unions, etc.)
- Single-file translation only

## Design Principles

1. **Accessibility First**: Error messages and keywords in Afan Oromo
2. **Python Compatibility**: Generated code is standard Python 3
3. **Structured Design**: Real compiler pipeline, not string replacement
4. **Educational Focus**: Simple syntax for beginners transitioning to Python
5. **Unicode Support**: Full support for Afan Oromo characters in identifiers

## Future Enhancements

- Extended type system with generics
- Module/package import system
- Dictionary and set literals
- Class definition support
- Standard library in Afan Oromo
- IDE integration and syntax highlighting
- Interactive REPL environment

## License

This project is developed for educational purposes to promote programming accessibility for Afan Oromo speakers.

## Acknowledgments

AOBL demonstrates how programming languages can be adapted to local languages and cultures, improving accessibility and learning outcomes for non-English speaking beginner programmers.
