# Informe final 1/3: Discovery Agent — Ciencia y Fe

## Resumen

El Discovery Agent transforma entrevistas de negocio en artefactos trazables para
decidir **qué problema resolver antes de construir software**. Esta es la primera
etapa del flujo:

```text
Discovery Agent  ->  Agile Delivery Team  ->  Quality Agent
problema validado     plan de entrega          verificación
```

El caso analizado es **Ciencia y Fe**, una institución educativa que necesita
reducir errores y retrabajo en sus reportes académicos. El agente usa evidencia de
la rectora, la secretaria y el desarrollador; si falta una fuente, el readiness gate
bloquea la generación del MVP.

## Objetivo y alcance

El objetivo fue convertir entrevistas en personas, dolores, requisitos, historias
INVEST, un MVP Canvas e hipótesis comprobables. Esta etapa no implementa código ni
define el Sprint: entrega evidencia estructurada al Agile Delivery Team.

## Estructura relevante

```text
discovery-agent-taller/
├── CLAUDE.md
├── .claude/
│   ├── commands/discovery/
│   ├── hooks/
│   ├── scripts/
│   └── skills/discovery/SKILL.md
└── discoveries/cienciayfe/
    ├── interviews/
    ├── outputs/
    └── evidencia - fotos/
```

## Prompts y comandos utilizados

Los comandos se ejecutan desde la raíz del repositorio con Claude Code:

```text
/discovery:analyze discoveries/cienciayfe
/discovery:generate-mvp discoveries/cienciayfe
/discovery:experiments discoveries/cienciayfe
/discovery:report discoveries/cienciayfe
```

| Orden | Comando | Motivo | Resultado |
|---:|---|---|---|
| 1 | `/discovery:analyze` | Leer todas las entrevistas y extraer únicamente hechos respaldados. | `personas.md`, `requisitos.md`, `evidence-map.json` |
| 2 | `/discovery:generate-mvp` | Priorizar el núcleo de valor y generar historias INVEST. | `user-stories.md`, `mvp-canvas.md` |
| 3 | `/discovery:experiments` | Convertir supuestos riesgosos en hipótesis falsables. | `hypotheses.md`, `experiment-board.json` |
| 4 | `/discovery:report` | Crear un reporte HTML reproducible desde los JSON. | `outputs/report.html` |

El prompt completo no es una descripción genérica: cada comando está definido en
`.claude/commands/discovery/` y exige citar fuentes, respetar formatos y no inventar
evidencia.

## Análisis de la ejecución

### 1. Bloqueo por evidencia insuficiente

Durante el primer intento, el mapa citaba `secretaria.md`, pero el archivo no estaba
presente. El gate detectó además que la persona Secretaria no tenía entrevista de
primera mano. La escritura del MVP fue bloqueada y el agente indicó levantar la
evidencia faltante.

![Readiness gate bloqueado](<discoveries/cienciayfe/evidencia - fotos/Antes.png>)

Log visible en la captura:

```text
Persona “Secretaria” no tiene una entrevista en primera persona en disco.
Acción: levanta más evidencia (agrega/entrevista) y reintenta.
```

### 2. Corrección y generación del MVP

Después de incorporar `interviews/secretaria.md`, se repitió exactamente:

```text
/discovery:generate-mvp discoveries/cienciayfe
```

El agente cargó la skill, leyó tres artefactos y escribió `user-stories.md` y
`mvp-canvas.md`.

![MVP generado después de corregir la evidencia](<discoveries/cienciayfe/evidencia - fotos/despues.png>)

### 3. Historia de usuario obtenida

Una salida representativa es **US-01**:

> Como Secretaria, quiero generar el cuadro de calificaciones trimestral con los
> nombres de materias obtenidos de la base de datos, para enviarlo al distrito sin
> errores de nomenclatura.

Sus criterios verifican que los nombres provengan de la BD y que los cambios se
reflejen sin modificar plantillas o procedimientos almacenados. La historia cita
`secretaria.md`, por lo que existe una cadena verificable:

```text
entrevista -> dolor “materias quemadas” -> requisito R-01 -> historia US-01
```

## Resultados y evidencias

| Evidencia | Ubicación | Qué demuestra |
|---|---|---|
| Entrevistas | `discoveries/cienciayfe/interviews/` | Fuente primaria del análisis |
| Mapa de evidencia | `outputs/evidence-map.json` | Relación entre personas, dolores y fuentes |
| Requisitos | `outputs/requisitos.md` | Necesidades funcionales y no funcionales |
| Historias | `outputs/user-stories.md` | Historias y criterios con fuente |
| MVP Canvas | `outputs/mvp-canvas.md` | Alcance, valor y exclusiones |
| Hipótesis | `outputs/hypotheses.md` | Supuestos y reglas de decisión |
| Reporte | `outputs/report.html` | Presentación visual autocontenida |

## Gates y reproducción

Los hooks de `.claude/settings.json` protegen los archivos antes de escribirlos:

- `readiness-gate.py`: exige mapa válido, al menos dos entrevistas y evidencia de
  primera mano para personas primarias.
- `hypothesis-gate.py`: exige métrica, umbral numérico, experimento y decisiones
  para éxito y fallo.

Prueba reproducible sin Claude Code:

```powershell
python3 .claude/scripts/test-gates.py
```

Resultado esperado:

```text
OK: ambos gates bloquearon y luego permitieron al corregir la causa.
```

## Entrega a la siguiente etapa

Los siguientes archivos se copian al `inbox/` del Agile Delivery Team:

```text
personas.md
requisitos.md
user-stories.md
mvp-canvas.md
evidence-map.json
```

Delivery debe conservar los identificadores `US-xx`, `R-xx` y los dolores de
origen. Así, la solución técnica permanece conectada con la entrevista que justificó
su existencia.

## Conclusión

Discovery produjo una definición de producto respaldada y demostró su control más
importante: cuando faltó la entrevista de la Secretaria, el sistema bloqueó el MVP.
La salida queda lista para refinamiento; todavía no prueba implementación ni calidad
de código, responsabilidades de las etapas 2 y 3.
