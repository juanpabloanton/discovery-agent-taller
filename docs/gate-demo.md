# Demostración reproducible de los gates

Ejecuta desde la raíz del proyecto:

```powershell
py -3 .claude/scripts/test-gates.py
```

La prueba construye un discovery temporal y no modifica `discoveries/cienciayfe`.

1. Declara a Secretaría como persona primaria sin una entrevista propia: el
   `readiness-gate` debe bloquear el MVP.
2. Agrega la entrevista de Secretaría: el mismo gate permite continuar.
3. Declara una hipótesis con la métrica de vanidad “Número de descargas”: el
   `hypothesis-gate` la bloquea.
4. La reemplaza por “Porcentaje de reportes aprobados en la primera revisión”,
   con umbral y regla de fallo: el gate permite continuar.

El resultado esperado final es:

```text
OK: ambos gates bloquearon y luego permitieron al corregir la causa.
```
