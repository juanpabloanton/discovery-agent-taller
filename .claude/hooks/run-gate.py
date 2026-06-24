#!/usr/bin/env python3
"""Ejecuta un gate Python conservando el payload JSON recibido por stdin."""

from pathlib import Path
import subprocess
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: run-gate.py <readiness-gate.py|hypothesis-gate.py>", file=sys.stderr)
        return 2

    gate_name = Path(sys.argv[1]).name
    allowed = {"readiness-gate.py", "hypothesis-gate.py"}
    if gate_name not in allowed:
        print(f"Gate no permitido: {gate_name}", file=sys.stderr)
        return 2

    gate_path = Path(__file__).with_name(gate_name)
    payload = sys.stdin.read()
    result = subprocess.run(
        [sys.executable, str(gate_path)],
        input=payload,
        text=True,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
