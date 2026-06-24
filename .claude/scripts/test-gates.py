#!/usr/bin/env python3
"""Demostración reproducible: ambos gates bloquean y luego permiten."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[2]
RUNNER = PROJECT / ".claude" / "hooks" / "run-gate.py"


def invoke(gate: str, target: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    payload = json.dumps({"tool_input": {"file_path": target}, "cwd": str(cwd)})
    return subprocess.run(
        [sys.executable, str(RUNNER), gate], input=payload, text=True, capture_output=True
    )


def write_interview(folder: Path, role: str) -> None:
    (folder / f"{role}.md").write_text(
        f"---\nrol_entrevistado: {role}\nprimera_persona: true\n---\n# Entrevista\n",
        encoding="utf-8",
    )


def require(result: subprocess.CompletedProcess[str], expected: int, step: str) -> None:
    if result.returncode != expected:
        raise RuntimeError(f"{step}: se esperaba exit {expected}, se obtuvo {result.returncode}.\n{result.stderr}")


def main() -> int:
    root = Path(tempfile.mkdtemp(prefix="discovery-gate-demo-"))
    try:
        discovery = root / "demo"
        interviews = discovery / "interviews"
        outputs = discovery / "outputs"
        interviews.mkdir(parents=True)
        outputs.mkdir()

        write_interview(interviews, "rectora")
        (outputs / "evidence-map.json").write_text(json.dumps({
            "personas": [
                {"name": "Rectora", "role": "rectora", "primary": True},
                {"name": "Secretaria", "role": "secretaria", "primary": True},
            ],
            "pains": [{"id": "dolor", "source": "rectora.md"}],
        }), encoding="utf-8")
        require(invoke("readiness-gate.py", "demo/outputs/mvp-canvas.md", root), 2, "Readiness sin entrevista")

        write_interview(interviews, "secretaria")
        require(invoke("readiness-gate.py", "demo/outputs/mvp-canvas.md", root), 0, "Readiness corregido")

        (outputs / "mvp-canvas.md").write_text("# MVP\n", encoding="utf-8")
        (outputs / "experiment-board.json").write_text(json.dumps({"hypotheses": [{
            "id": "H-01", "assumption": "x", "hypothesis": "Creemos que x",
            "metric": "Número de descargas", "threshold": "10 en 7 días",
            "experiment": "fake door", "decision": "Si pasa, construir; si falla, descartar.",
        }]}), encoding="utf-8")
        require(invoke("hypothesis-gate.py", "demo/outputs/hypotheses.md", root), 2, "Hipótesis de vanidad")

        (outputs / "experiment-board.json").write_text(json.dumps({"hypotheses": [{
            "id": "H-01", "assumption": "x", "hypothesis": "Creemos que x",
            "metric": "Porcentaje de reportes aprobados en la primera revisión",
            "threshold": "90% en 7 días", "experiment": "prototipo",
            "decision": "Si pasa, construir; si falla, descartar.",
        }]}), encoding="utf-8")
        require(invoke("hypothesis-gate.py", "demo/outputs/hypotheses.md", root), 0, "Hipótesis corregida")
        print("OK: ambos gates bloquearon y luego permitieron al corregir la causa.")
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
