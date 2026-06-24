# Hipótesis y experimentos — discovery cienciayfe

> Ordenadas de mayor a menor riesgo. Se prueba primero lo que más puede tumbar el MVP.

---

```mermaid
flowchart TD
  classDef test fill:#E2EAF3,stroke:#1A4E8A,color:#0E1A26;
  classDef ok fill:#E3F1E8,stroke:#2E7D52,color:#0E1A26;
  classDef no fill:#F6E2DD,stroke:#B3402F,color:#0E1A26;
  classDef warn fill:#FDF3DC,stroke:#9A6605,color:#0E1A26;

  H1["H-01 ⚠ ALTO\nNombres en BD aceptables"]:::test
  H2["H-02 ⚠ ALTO\nCentralización sin pérdida"]:::test
  H3["H-03 ▲ MEDIO\nNombres = bloqueador principal"]:::test

  H1 -->|"≥ 85 % correctos"| OK1["Fuente maestra activada\n→ Construir extracción dinámica"]:::ok
  H1 -->|"< 85 % correctos"| NO1["Crear interfaz de\nadministración de materias primero"]:::no

  H2 -->|"100 % recuperado\npara ≥ 3 niveles"| OK2["Avanzar con\ntabla centralizada"]:::ok
  H2 -->|"Pérdida o duplicados"| NO2["Centralización incremental\npor niveles prioritarios"]:::no

  H3 -->|"0 devoluc. por nombres\n≤ 1 por otra causa"| OK3["Comprometer 90 %\nde primera revisión"]:::ok
  H3 -->|"Otros bloqueadores\nfrecuentes"]| NO3["Ampliar scope del MVP\nrevisar US-01 a US-05"]:::warn
```

---

### [H-01] Nombres de materias en BD aceptables como fuente única — riesgo: alto

- **Supuesto a probar:** Los nombres de las materias en la base de datos actual son suficientemente correctos para usarse directamente como fuente única de verdad en todos los reportes, sin limpieza previa masiva.
- **Hipótesis:** Creemos que la secretaria aceptará los nombres de materias extraídos dinámicamente de la BD si el desarrollador audita y corrige las discrepancias antes de la primera entrega, porque el problema actual es que los nombres están quemados (no se actualizan), no que la BD tenga datos fundamentalmente erróneos.
- **Señal medible:** Porcentaje de nombres de materias en la BD que coinciden con los esperados por la secretaria para los cuadros del período 2025-2026.
- **Criterio de éxito:** ≥ 85 % de nombres coinciden o requieren solo corrección menor (capitalización o tildes), verificado en sesión de auditoría de 2 horas.
- **Experimento:** Auditoría de datos dirigida — el desarrollador extrae la lista de materias de las tablas más usadas en los SP y la presenta a la secretaria para validación nombre a nombre.
- **Caja de tiempo/costo:** 1 día del desarrollador para extraer y preparar la lista + 2 horas de la secretaria para la revisión.
- **Regla de decisión:** Si pasa (≥ 85 % aceptables) → centralizar esos nombres como fuente maestra y corregir el resto antes de generar los reportes del MVP. Si falla (< 85 % requieren corrección significativa) → construir primero una interfaz de administración de materias antes de activar la extracción dinámica; no usar la BD actual sin limpieza previa.

---

### [H-02] Centralización de calificaciones técnicamente viable sin pérdida de datos — riesgo: alto

- **Supuesto a probar:** Es posible crear una vista SQL unificada de calificaciones sobre las tablas existentes sin pérdida de datos del período 2025-2026 en curso, sin necesidad de una migración destructiva.
- **Hipótesis:** Creemos que el desarrollador podrá recuperar el 100 % de las calificaciones del período actual desde una vista unificada si mapea las tablas existentes de cada nivel, porque aunque las tablas son inconsistentes en estructura, el dato de calificación existe en alguna tabla para cada nivel.
- **Señal medible:** Porcentaje de calificaciones del período 2025-2026 recuperables correctamente (sin pérdida ni duplicados) desde la vista unificada, comparadas contra los reportes generados por el sistema actual.
- **Criterio de éxito:** 100 % de calificaciones recuperadas sin pérdida ni duplicados para al menos 3 niveles distintos (básica, media, bachillerato), en un spike de 3 días.
- **Experimento:** Spike técnico — el desarrollador mapea todas las tablas de calificaciones, documenta sus relaciones y construye una vista SQL de prueba para 3 niveles; compara resultados fila a fila contra los cuadros generados actualmente por el sistema.
- **Caja de tiempo/costo:** 3 días de trabajo del desarrollador. Sin costo adicional: se trabaja sobre la BD existente en ambiente de desarrollo.
- **Regla de decisión:** Si pasa (100 % de datos recuperados para ≥ 3 niveles) → avanzar con la tabla centralizada como base del MVP. Si falla (datos faltantes o duplicados) → abordar la centralización por niveles de forma incremental, priorizando los cursos de 2.° a bachillerato que van al distrito; posponer la centralización de inicial y básica baja.

---

### [H-03] Los nombres de materias son el principal bloqueador de las devoluciones — riesgo: medio

- **Supuesto a probar:** La inconsistencia en los nombres de las materias es la causa principal de las devoluciones; eliminarla permitirá que ≥ 90 % de los cuadros sean aprobados en la primera revisión.
- **Hipótesis:** Creemos que la secretaria aprobará los cuadros en la primera revisión si los nombres de las materias son consistentes entre cuadro de calificaciones, cuadro final y acta de promoción, porque la mayoría de las devoluciones registradas en las entrevistas son por discrepancias de nombres, no por errores de datos académicos ni de layout.
- **Señal medible:** Número de causas de devolución distintas identificadas por la secretaria al revisar reportes de muestra con nombres de materias alineados manualmente.
- **Criterio de éxito:** 0 devoluciones por nombres incorrectos y ≤ 1 devolución por otra causa, al revisar un set de 3 reportes de muestra (trimestral + final + acta de promoción del mismo nivel) en sesión controlada de 1 hora.
- **Experimento:** Revisión de prototipo en papel — el desarrollador prepara manualmente 3 reportes de muestra con nombres de materias consistentes (alineados a mano sin cambiar el sistema); la secretaria los revisa como si fueran entrega real y señala qué correcciones haría.
- **Caja de tiempo/costo:** ½ día del desarrollador para preparar los reportes de muestra + 1 hora de la secretaria.
- **Regla de decisión:** Si pasa (0 devoluciones por nombres, ≤ 1 por otra causa) → confirmar que el MVP puede comprometerse con la métrica de 90 % de primera revisión. Si falla (se identifican otros bloqueadores frecuentes además de los nombres) → ampliar el scope del MVP para cubrir esas causas antes de comprometerse con la métrica; revisar los criterios de aceptación de US-01 a US-05.
