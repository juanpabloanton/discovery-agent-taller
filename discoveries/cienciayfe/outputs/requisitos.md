# Requisitos candidatos — discovery cienciayfe

## Funcionales

- **[R-01]** El sistema debe generar cuadros trimestrales de calificaciones con escala cualitativa (AA+, A-, B-) para inicial y básica hasta 4.° y cuantitativa (numérica) desde 5.° en adelante.
  - Tipo: funcional
  - Origen: secretaria.md · Secretaria

- **[R-02]** El sistema debe generar cuadros finales de calificaciones y actas de promoción por nivel educativo.
  - Tipo: funcional
  - Origen: rectora.md, secretaria.md · Rectora, Secretaria

- **[R-03]** Los reportes deben reservar espacio para la firma del docente y para dos sellos: uno del colegio y uno del distrito educativo.
  - Tipo: funcional
  - Origen: secretaria.md · Secretaria

- **[R-04]** Los nombres de las materias en todos los reportes deben extraerse dinámicamente de la base de datos; no deben estar codificados en las plantillas RDLC ni en los documentos Word.
  - Tipo: funcional
  - Origen: desarrollador.md, secretaria.md · Desarrollador, Secretaria

- **[R-05]** Debe existir una tabla centralizada de calificaciones que unifique los datos de todos los niveles educativos (inicial, básica, bachillerato).
  - Tipo: funcional
  - Origen: rectora.md, desarrollador.md · Rectora, Desarrollador

- **[R-06]** Las plantillas de reportes (cuadros y promociones) deben ser reutilizables y configurables por nivel, sin necesidad de una plantilla distinta por cada curso.
  - Tipo: funcional
  - Origen: desarrollador.md, rectora.md · Desarrollador, Rectora

- **[R-07]** El sistema debe generar la nómina de estudiantes abanderados del período 2026-2027.
  - Tipo: funcional
  - Origen: rectora.md · Rectora

- **[R-08]** Debe existir un canal formal para registrar, confirmar y hacer seguimiento de los requerimientos de cambio en reportes, evitando retrabajo por malentendidos.
  - Tipo: funcional
  - Origen: secretaria.md, desarrollador.md · Secretaria, Desarrollador

- **[R-09]** El nuevo sistema debe consolidar los sistemas interno y externo actuales en una sola plataforma, eliminando la duplicidad operativa.
  - Tipo: funcional
  - Origen: rectora.md · Rectora

- **[R-10]** Los cuadros de comportamiento deben presentarse con escala visual reducida para no opacar la información académica principal.
  - Tipo: funcional
  - Origen: secretaria.md · Secretaria

## No funcionales

- **[R-11]** El sistema debe cumplir con la Ley Orgánica de Protección de Datos Personales del Ecuador.
  - Tipo: no funcional
  - Origen: rectora.md · Rectora

- **[R-12]** La arquitectura del sistema debe ser mantenible: sin duplicación de lógica de negocio, con componentes desacoplados y lógica de reportes parametrizable (sin SP de miles de líneas ni plantillas quemadas).
  - Tipo: no funcional
  - Origen: desarrollador.md, rectora.md · Desarrollador, Rectora

- **[R-13]** El sistema debe desplegarse mediante contenedores Docker con soporte de integración y entrega continua (CI/CD) en dos servidores Ubuntu.
  - Tipo: no funcional
  - Origen: desarrollador.md, rectora.md · Desarrollador, Rectora

- **[R-14]** El sistema debe adaptarse a cambios en los lineamientos del Ministerio de Educación sin requerir modificación masiva de plantillas o código.
  - Tipo: no funcional
  - Origen: rectora.md, secretaria.md · Rectora, Secretaria
