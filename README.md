# 🏠 SmartHome – Evidencia N°5 (Módulo Programador)

## 📘 Descripción General

**SmartHome** es un sistema simplificado de gestión domótica desarrollado como parte de la **Evidencia N°5 del Módulo Programador** de la Tecnicatura Superior en Desarrollo de Software (ISPC – Córdoba).

El proyecto aplica **Programación Orientada a Objetos (POO)** para modelar un sistema doméstico inteligente, donde usuarios pueden controlar dispositivos del hogar y automatizar acciones.

---

## ⚙️ Objetivos del Proyecto

* Implementar principios fundamentales de POO:

  * **Abstracción**
  * **Encapsulamiento**
  * **Principio de Responsabilidad Única (SRP)**
  * **Modularidad**
* Representar las relaciones entre clases mediante un **diagrama UML**.
* Integrar una base de datos relacional simple y scripts SQL básicos.
* Documentar la estructura y justificar las decisiones de diseño.

---

## 🧩 Estructura del Proyecto

```Markdown
proyecto_smarthome_poo/
│
├── modelos/
│   ├── usuario.py
│   ├── perfil.py
│   ├── dispositivo_hogar.py
│   └── automatizacion.py
│
├── archivos-dummy/
│   ├── hogar_dummy.py
│   ├── dispositivo_hogar_dummy.py
│   ├── dispositivo_control_dummy.py
│   ├── test_hogar_dummy.py
│   ├── test_dispositivo_hogar_dummy.py
│   └── test_dispositivo_control_dummy.py
│
├── tests/
│   ├── test_usuario.py
│   ├── test_perfil.py
│   ├── test_dispositivo.py
│   └── test_automatizacion.py
│
├── BD-Evidencia-5/
│   ├── init.sql
│   ├── queries.sql
│   └── README.md   ← Documentación específica de la base de datos
│
├── DC-Evidencia-5/
│   └── Justificación_POO_UML_DiagramaClases_Corregido_EV5.md
│
└── README.md   ← Este archivo (documentación principal)
```

---

## 🧱 Clases Principales

| Clase                | Descripción                                                                                                  | Relación Principal                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **Usuario**          | Gestiona credenciales y rol del usuario. Delegación al perfil para datos personales y registro de actividad. | *Composición* con `Perfil`          |
| **Perfil**           | Contiene datos personales y registro de actividad.                                                           | *Composición* desde `Usuario`       |
| **DispositivoHogar** | Representa un dispositivo controlable (luz, ventilador, etc.) con estado encendido/apagado.                  | *Asociación* con `Usuario`          |
| **Automatizacion**   | Implementa reglas automáticas, como apagar dispositivos no esenciales.                                       | *Agregación* con `DispositivoHogar` |

---

## 🧠 Principios Aplicados

* **Encapsulamiento:**
  Todos los atributos internos son privados (`_atributo`) con acceso controlado mediante `@property`.

* **SRP (Responsabilidad Única):**
  `Usuario` solo gestiona autenticación y delega tareas de perfil y actividad a `Perfil`.

* **Abstracción:**
  Cada clase modela una entidad real del sistema domótico, ocultando detalles internos.

* **Modularidad:**
  Cada clase se encuentra en su propio archivo dentro del paquete `modelos/`.

---

## 📂 Archivos Dummy

La carpeta `archivos-dummy/` contiene clases y tests **sin lógica funcional**, utilizadas como *placeholders* para futuras expansiones (por ejemplo, la clase `Hogar` o `DispositivoControl`).

Estos archivos fueron incluidos para cumplir con los lineamientos de modularidad del proyecto, pero **no participan de la ejecución principal** ni de las pruebas unitarias formales.

**Archivos incluidos:**

* `hogar_dummy.py`
* `dispositivo_hogar_dummy.py`
* `dispositivo_control_dummy.py`
* `test_hogar_dummy.py`
* `test_dispositivo_hogar_dummy.py`
* `test_dispositivo_control_dummy.py`

> 💡 Su propósito es mostrar cómo se podría ampliar el sistema con nuevas clases sin afectar el núcleo actual.

---

## 🧪 Pruebas Unitarias

El proyecto incluye una suite básica de tests en la carpeta `tests/`, compatibles con **pytest** o **unittest**.

Para ejecutarlas:

```bash
pytest
```

---

## 🗄️ Base de Datos

El modelo relacional y los scripts SQL (`init.sql` y `queries.sql`) se encuentran en:

```Markdown
/BD-Evidencia-5/
```

> 📄 **Nota:** la documentación específica de la base de datos se encuentra en
> [`BD-Evidencia-5/README.md`](./BD-Evidencia-5/README.md)

---

## 📊 Diagrama UML y Justificación POO

El diagrama UML y su análisis detallado se encuentran en la carpeta:

```Markdown
/DC-Evidencia-5/
```

Archivo principal:
`Justificación_POO_UML_DiagramaClases_Corregido_EV5.md`

Incluye explicación textual y código PlantUML.

---

## 🧰 Requisitos Técnicos

* Python 3.10 o superior
* pytest (opcional, para ejecutar tests)

```bash
pip install pytest
```

---

## 📚 Créditos

Proyecto desarrollado por **LeonesDev**
para la materia **Programador – ISPC Córdoba (2025)**.

> *"Evidencian muy buen trabajo de gestión de proyecto."* — Feedback docente.
