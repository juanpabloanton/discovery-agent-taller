---
fuente: entrevista
rol_entrevistado: rectora
primera_persona: true
anonimizada: true
fecha: 2026-00-00
---

# Entrevista — rectora

**Entrevistador:** ¿Qué necesidades son prioritarias en este momento?

**R. (rectora):** Tenemos que solventar los requerimientos actuales. El proyecto académico es .NET ASP con base de datos SQL Server y el área es Secretaría. Necesitamos los cuadros trimestrales y quimestrales, los cuadros finales y la entrega de promociones.

**R. (rectora):** Todos esos documentos tienen que estar firmados por el docente y sellados por el distrito; se tienen que manejar de manera urgente. Son documentos del período 2025-2026 para cierre de año, eso es prioridad.

**R. (rectora):** Después de entregar eso se requiere hacer la nómina de estudiantes abanderados, que es requerimiento del período 2026-2027.

**Entrevistador:** ¿Qué les han explicado los desarrolladores sobre el sistema actual?

**R. (rectora):** Los desarrolladores indican que van a trabajar, pero comunican varias inconsistencias en la base de datos y en el código. La programación no está clara y el código no es mantenible. En la base se maneja por SP: un SP llama a otro, hay queries mal generados y SP de 30 mil líneas; se arregla una cosa y se daña otra.

**R. (rectora):** La información no está centralizada. Cada tabla es distinta a otra, no hay un esquema de base de datos y no existe una sola tabla de calificaciones: de una se saca inicial y de otra se sacan los otros cursos. Los SP no se reutilizan, se crea uno nuevo, y eso dificulta todo porque la misma información que debería estar en un reporte no está en otro.

**R. (rectora):** Por cada curso hay una plantilla para los cuadros de calificaciones, promociones y cuadros finales; manualmente hay que hacer los cambios por archivos. Eso genera tiempo, especialmente los RDLC de cada cuadro trimestral y final. Cada curso tiene su RDLC porque el Ministerio de Educación es cambiante y no ha habido un estándar.

**Entrevistador:** ¿Qué se plantea después de estabilizar los entregables urgentes?

**R. (rectora):** Una vez culminado eso se procederá a realizar un proyecto para reemplazar el actual, desde cero: un sistema académico nuevo. Se plantea React 18 y Ant Design 5 en frontend; Java 21 LTS, Spring Boot 3.5.x, Spring Security 6 y Spring Data JPA en backend; PostgreSQL 16.8, Apache POI 5.4.x y JasperReports 7.x. También Docker, Git, Maven 3.9.x y RabbitMQ.

**R. (rectora):** Se crearán los proyectos de discovery, gateway con login y Redis, config, files, worker, académico, financiero, secretaría y talento humano. Se hará una base de configuración que apunte a la base final como medida de seguridad, Nginx para leer el build de React, dos servidores Ubuntu: uno con despliegue automatizado CI/CD en Git y otro para recibir los ejecutables. También se creará la nueva base de datos PostgreSQL.

**R. (rectora):** Hay que cumplir la ley de protección de datos personales y analizar el lineamiento académico actual del Ministerio para desarrollar la lógica del sistema nuevo.

**R. (rectora):** Pero antes de culminar lo nuevo hay que tener estable lo antiguo para dedicarnos de lleno. También se quiere reestructurar la página institucional y vincularla al sistema académico actual, hacer mejoras visuales y de rendimiento. Hay dos sistemas, uno interno y otro externo; se quiere dar de baja el externo y mantener uno solo para tener eficiencia.

**R. (rectora):** Somos dos desarrolladores: uno está con el cuadro final y trimestral, el otro con promociones, cuestiones internas, configuración del servidor para el nuevo sistema, modificaciones del antiguo y la nómina de abanderados 2026-2027.
