# User Stories — discovery cienciayfe

> **Alcance:** estas historias cubren el MVP del módulo de reportes académicos.
> Se priorizan por impacto en el ciclo de devoluciones que afecta a las tres personas.

---

- **[US-01]** Como secretaria, quiero que los nombres de las materias sean idénticos en el cuadro de calificaciones, el cuadro final y el acta de promoción, para aprobar los reportes en la primera revisión sin necesidad de devolverlos.
  - Criterios de aceptación:
    - Dado que existe un cuadro trimestral y un acta de promoción del mismo nivel, cuando la secretaria los compara, entonces todos los nombres de materia coinciden exactamente entre ambos documentos.
    - Dado que el desarrollador cambia el nombre de una materia en la base de datos, cuando se regeneran los reportes, entonces el cambio aparece en el cuadro trimestral, el cuadro final y el acta de promoción sin intervención manual adicional.
  - Fuente: secretaria.md, desarrollador.md

---

- **[US-02]** Como secretaria, quiero generar cuadros trimestrales con escala cualitativa (AA+, A-, B-) para básica de 1.° a 4.° y escala cuantitativa (numérica) para 5.° en adelante, para que los cuadros cumplan la normativa vigente del Ministerio de Educación.
  - Criterios de aceptación:
    - Dado un cuadro de un curso de básica de 1.° a 4.°, cuando se genera el reporte, entonces las calificaciones aparecen en escala cualitativa (AA+, A-, B-) y no en formato numérico.
    - Dado un cuadro de un curso de 5.° o superior, cuando se genera el reporte, entonces las calificaciones aparecen en formato numérico.
    - Dado un cuadro de cualquier nivel, cuando se genera el reporte, entonces el cuadro de comportamiento aparece en escala visual reducida, sin opacar la información académica principal.
  - Fuente: secretaria.md

---

- **[US-03]** Como secretaria, quiero que los cuadros de calificaciones y actas de promoción incluyan el espacio designado para la firma del docente y los dos sellos (colegio y distrito), para que los documentos sean formalmente válidos al enviarse al distrito educativo.
  - Criterios de aceptación:
    - Dado un reporte generado (trimestral, final o acta de promoción), cuando se imprime, entonces contiene una sección visible con línea de firma del docente, un espacio para el sello del colegio y un espacio para el sello del distrito.
    - Dado que se genera el reporte para niveles de 2.° a bachillerato, cuando se valida el documento, entonces los espacios de firma y sellos están ubicados de forma que no colisionan con la información académica.
  - Fuente: secretaria.md

---

- **[US-04]** Como desarrollador, quiero que los nombres de las materias se extraigan dinámicamente de la base de datos en todos los reportes, para poder corregir o actualizar una materia en un solo lugar y que el cambio se refleje automáticamente en todos los documentos.
  - Criterios de aceptación:
    - Dado que la base de datos contiene la tabla maestra de materias por nivel, cuando se genera cualquier reporte (trimestral, final, promoción), entonces los nombres de las materias provienen de esa tabla y no están codificados en la plantilla.
    - Dado que se modifica el nombre de una materia en la tabla maestra, cuando se regenera cualquier reporte que contenga esa materia, entonces el nuevo nombre aparece sin requerir cambios en la plantilla ni en el código del reporte.
  - Fuente: desarrollador.md, secretaria.md

---

- **[US-05]** Como desarrollador, quiero una plantilla de reporte parametrizada por nivel educativo (en lugar de una plantilla por curso), para aplicar correcciones en un único lugar sin riesgo de dañar los reportes de otros cursos.
  - Criterios de aceptación:
    - Dado que existe un defecto visual en un cuadro trimestral, cuando el desarrollador corrige la plantilla del nivel correspondiente, entonces todos los cursos de ese nivel quedan corregidos y los cuadros de otros niveles no se ven afectados.
    - Dado que el sistema genera reportes para todos los cursos de básica, cuando se comparan los layouts, entonces todos comparten la misma plantilla base parametrizada (no hay un RDLC separado por curso).
  - Fuente: desarrollador.md, rectora.md

---

- **[US-06]** Como rectora, quiero que los cuadros trimestrales, cuadros finales y actas de promoción del período 2025-2026 se generen con información correcta y consistente antes del cierre de año, para cumplir con el requerimiento urgente del distrito educativo.
  - Criterios de aceptación:
    - Dado que se solicita la generación de los cuadros del período 2025-2026, cuando el sistema los produce, entonces la secretaria los aprueba sin devolución en la primera revisión.
    - Dado que los documentos deben enviarse al distrito, cuando se revisa el contenido, entonces los cuadros de 2.° a bachillerato están completos, con firmas y sellos, y con nombres de materias consistentes entre cuadro de calificaciones y acta de promoción.
  - Fuente: rectora.md, secretaria.md
