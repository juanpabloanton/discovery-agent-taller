---
fuente: entrevista
rol_entrevistado: desarrollador
primera_persona: true
anonimizada: true
fecha: 2026-00-00
---

# Entrevista — desarrollador

**Entrevistador:** ¿Cómo se organizan para atender los requerimientos actuales?

**D1. (desarrollador):** Como podemos hacer esto o como nos organizamos. Tú encárgate de los cuadros y yo me encargo de las promociones. Yo procedo a hacer los cuadros y los requerimientos tomados de secretaría, aunque es complicado por cómo está guardada la información.

**D1. (desarrollador):** He hecho los SP, que a veces son 30k de líneas con `if` anidados, y varios RDLC por cada curso. No está estandarizado: cada curso tiene RDLC y para modificar un curso hay que hacer bastantes cambios. Es tedioso, el editor RDLC no es amigable; si se mueve una cosa se mueve todo.

**D2. (desarrollador):** Yo procedo con las modificaciones y requerimientos de las promociones. También se demora porque cada curso tiene plantillas distintas, los nombres de las materias están quemados y no está centralizada la información en la base.

**Entrevistador:** ¿Qué avance hay para solucionar el problema de fondo?

**D2. (desarrollador):** Estoy creando la infraestructura básica del sistema: base de configuración, base de datos con tablas de roles, permisos, usuarios, personas, relaciones, menú y otras tablas de persona. Hay avance. También se creó y configuró el servidor de desarrollo donde estarán los ejecutables JAR de cada módulo.

**D2. (desarrollador):** Los proyectos son `backend-discovery` (Eureka), `backend-gateway` (login y Redis para cachear sesiones), `backend-config`, `backend-files`, `backend-worker`, `backend-academico`, `backend-frontend`, `backend-financiero`, `backend-secretaria` y `backend-talento-humano`.

**D2. (desarrollador):** Se maneja con contenedores; cada uno tiene su Dockerfile y al ejecutar `docker-compose erp-project up -d` se levanta el ecosistema. Cada ejecutable es un contenedor y para el front hay un contenedor Nginx con el build. Se hicieron configuraciones de red para habilitar los puertos 80, 443 y 3000 y un subdominio para el ambiente de desarrollo.

**D2. (desarrollador):** El sistema nuevo se va a crear para corregir todo esto y que sea mantenible, tanto en la base de datos como en plantillas que no sean repetitivas. La intención es quitar el sistema antiguo y crear uno nuevo.

**Entrevistador:** ¿Han intentado hacer dinámicos los reportes actuales?

**D1. (desarrollador):** Intenté hacer dinámicos los cuadros trimestrales, pero los nombres de la base de datos no coinciden con los del Word, que están quemados. Si hago el cambio la información no coincide y será más tedioso, entonces se procede a dejar como estaba. No se puede hacer dinámico y eso aplica para trimestrales, finales y promociones.

**D2. (desarrollador):** Para el sistema nuevo se propone hacerlo dinámico, con plantillas mantenibles y dinámicas tanto en materias como en diseño por curso.
