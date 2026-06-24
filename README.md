# Discovery Agent

Agente de Claude Code para convertir entrevistas de negocio en artefactos de
descubrimiento trazables. El proyecto prioriza la evidencia: no genera un MVP ni
experimentos cuando la información disponible no es suficiente o comprobable.

## Caso incluido

`discoveries/cienciayfe/` contiene el caso de la institución educativa Ciencia y
Fe. Incluye entrevistas de primera mano con rectora, secretaria y desarrollador,
y los artefactos derivados de ellas.

## Estructura

```text
.
├── CLAUDE.md                         # Constitución y reglas de trabajo
├── .claude/
│   ├── commands/discovery/            # Comandos /discovery:*
│   ├── hooks/                         # Gates de calidad
│   ├── scripts/                       # Reporte y demostración de gates
│   └── skills/discovery/SKILL.md      # Estándar de artefactos
├── discoveries/
│   ├── _template/                     # Plantilla para un discovery nuevo
│   └── cienciayfe/
│       ├── interviews/                # Evidencia cruda
│       └── outputs/                   # Artefactos generados
└── docs/gate-demo.md                  # Guía de demostración
```

## Flujo de uso

Abre Claude Code desde la raíz del proyecto y ejecuta los comandos en este orden:

```text
/discovery:analyze discoveries/cienciayfe
/discovery:generate-mvp discoveries/cienciayfe
/discovery:experiments discoveries/cienciayfe
/discovery:report discoveries/cienciayfe
```

| Comando | Resultado |
|---|---|
| `/discovery:analyze` | Personas, stakeholders, requisitos y `evidence-map.json`. |
| `/discovery:generate-mvp` | User stories INVEST y MVP Canvas. |
| `/discovery:experiments` | Hipótesis falsables, experimentos y `experiment-board.json`. |
| `/discovery:report` | Reporte visual autocontenido en HTML. |

## Gates de calidad

Los hooks se configuran en `.claude/settings.json` y se ejecutan antes de que
Claude Code escriba o edite un archivo.

- **Readiness gate:** protege `user-stories.md` y `mvp-canvas.md`. Exige un mapa
  de evidencia válido, al menos dos entrevistas, personas primarias con entrevista
  propia y dolores con fuente existente.
- **Hypothesis gate:** protege `experiment-board.json` y `hypotheses.md`. Exige
  hipótesis con métrica de negocio, umbral numérico, experimento y decisión tanto
  para éxito como para fallo.

Si un gate devuelve `exit 2`, Claude Code bloquea la escritura y muestra qué debe
corregirse. Con `exit 0`, permite continuar silenciosamente.

## Demostración reproducible

La prueba crea un discovery temporal, no modifica `discoveries/cienciayfe` y
comprueba el ciclo bloqueo → corrección → aprobación de ambos gates:

```powershell
python3 .claude/scripts/test-gates.py
```

Resultado esperado:

```text
OK: ambos gates bloquearon y luego permitieron al corregir la causa.
```

Consulta [docs/gate-demo.md](docs/gate-demo.md) para el detalle de los casos
probados.

## Artefactos del caso Ciencia y Fe

- [Entrevistas](discoveries/cienciayfe/interviews/)
- [Personas](discoveries/cienciayfe/outputs/personas.md)
- [Requisitos](discoveries/cienciayfe/outputs/requisitos.md)
- [User stories](discoveries/cienciayfe/outputs/user-stories.md)
- [MVP Canvas](discoveries/cienciayfe/outputs/mvp-canvas.md)
- [Hipótesis](discoveries/cienciayfe/outputs/hypotheses.md)
- [Reporte visual](discoveries/cienciayfe/outputs/report.html)
