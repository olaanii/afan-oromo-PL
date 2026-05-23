#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from afan_oromo_lang.generator import CodeGenerator
from afan_oromo_lang.lexer import Lexer, LexerError
from afan_oromo_lang.parser import Parser, ParserError
from afan_oromo_lang.type_checker import TypeChecker, TypeErrorAfan


def translate_source(source: str) -> str:
    print("🔍 Starting lexical analysis...", file=sys.stderr, flush=True)
    tokens = Lexer().tokenize(source)
    print("✓ Lexical analysis complete", file=sys.stderr, flush=True)
    
    print("🌳 Building abstract syntax tree...", file=sys.stderr, flush=True)
    program = Parser(tokens).parse()
    print("✓ AST construction complete", file=sys.stderr, flush=True)
    
    print("🔎 Running type checker...", file=sys.stderr, flush=True)
    TypeChecker().check_program(program)
    print("✓ Type checking complete", file=sys.stderr, flush=True)
    
    print("⚙️ Generating Python code...", file=sys.stderr, flush=True)
    result = CodeGenerator().generate(program)
    print("✓ Code generation complete", file=sys.stderr, flush=True)
    
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Afan Oromo gara Python translator")
    parser.add_argument("input", type=Path, help="Faayila .or")
    parser.add_argument("-o", "--output", type=Path, help="Faayila output .py")
    args = parser.parse_args()

    src_path: Path = args.input
    out_path: Path = args.output or src_path.with_suffix(".py")

    try:
        translated = translate_source(src_path.read_text(encoding="utf-8"))
        out_path.write_text(translated, encoding="utf-8")
    except FileNotFoundError:
        print("Dogoggora: faayilli hin argamne")
        return 1
    except (LexerError, ParserError, TypeErrorAfan) as exc:
        print(str(exc))
        return 1

    print(file=sys.stderr)  # Blank line to separate pipeline logs from result
    print(f"Milkaa'e: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
