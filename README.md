# 🏠 SmartHome – Evidencia N°6 (Módulo Programador)

## 📘 Descripción General

**SmartHome** es un sistema simplificado de gestión domótica desarrollado como parte de la **Evidencia N°6 del Módulo Programador** de la Tecnicatura Superior en Desarrollo de Software (ISPC – Córdoba).

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
│   ├── hogar.py
│   ├── dispositivo_hogar.py
│   ├── dispositivo_control.py
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
│   ├── test_dispositivo_hogar.py
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
| **Hogar**            | Representa un hogar con sus características básicas (ubicación, tipo, etc.). Archivo básico de compatibilidad. | *Asociación* con otros modelos      |
| **DispositivoHogar** | Representa un dispositivo controlable (luz, ventilador, etc.) con estado encendido/apagado.                  | *Asociación* con `Usuario`          |
| **DispositivoControl** | Controla el estado general de dispositivos conectados (activos, apagados, en ahorro). Archivo básico de compatibilidad. | *Asociación* con `Usuario` |
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

Archivos disponibles:
- `Justificación_POO_UML_DiagramaClases_Corregido_EV5.md` ⭐ **Versión principal**
- `Justificación_POO_UML_DiagramaClases_Corregido_EV5.docx`
- `Justificación_POO_UML_DiagramaClases_Corregido_EV5.pdf`

Incluye explicación textual completa, diagrama UML en código PlantUML, justificaciones de diseño POO y análisis de implementación.

---

## 🧰 Requisitos Técnicos

* Python 3.10 o superior
* pytest (opcional, para ejecutar tests)

```bash
pip install pytest
```

---

## � Evidencia 6 - Mejoras Implementadas

### 🔄 Cambios en la Clase Usuario (`modelos/usuario.py`)

**Aplicación del Principio de Responsabilidad Única (SRP):**
- La clase se enfoca únicamente en la gestión de credenciales y roles del usuario
- Delegación de datos personales y actividades a la clase `Perfil`
- Separación clara entre autenticación y gestión de dispositivos

**Mejoras en Encapsulamiento:**
- Validaciones básicas en el constructor para ID, clave y rol
- Métodos getters y setters apropiados usando `@property`
- Protección de la lista de dispositivos mediante copia en el getter
- Métodos públicos claros: `agregar_dispositivo()`, `quitar_dispositivo()`, `buscar_dispositivo_por_id()`

**Nuevos Métodos Agregados:**
- `buscar_dispositivo_por_id(id_dispositivo)`: Busca dispositivo por ID único
- `contar_dispositivos()`: Retorna el número total de dispositivos del usuario
- Validaciones mejoradas en `cambiar_clave()` y setters

### 🔄 Cambios en la Clase DispositivoHogar (`modelos/dispositivo_hogar.py`)

**Aplicación del SRP:**
- La clase se concentra exclusivamente en representar y controlar dispositivos
- Responsabilidades claras: estado, información básica y control de encendido/apagado
- Sin dependencias externas innecesarias

**Mejoras en Encapsulamiento:**
- Validaciones básicas para campos obligatorios (ID, nombre, tipo)
- Atributos privados con acceso controlado mediante properties
- Métodos de control simples y directos

**Nuevos Métodos Agregados:**
- `cambiar_nombre(nuevo_nombre)`: Permite modificar el nombre del dispositivo
- `obtener_estado_texto()`: Retorna el estado como texto legible ("encendido"/"apagado")
- Mejora en `__repr__()` para mostrar dispositivos esenciales con indicador `[ESENCIAL]`

### ✅ Pruebas Unitarias Mejoradas

**Para Usuario (`tests/test_usuario.py`):**
- Pruebas de validaciones básicas del constructor
- Verificación de funcionalidad de búsqueda de dispositivos
- Tests para conteo de dispositivos
- Validación de cambio de clave

**Para DispositivoHogar (`tests/test_dispositivo_hogar.py`):**
- Pruebas de validaciones del constructor
- Tests para cambio de nombre de dispositivo
- Verificación del método `obtener_estado_texto()`
- Pruebas de representación con dispositivos esenciales

### 🎯 Enfoque para Principiantes

Todos los cambios implementados utilizan conceptos básicos de programación:
- Estructuras de control simples (`if/else`)
- Concatenación de strings básica
- Métodos con validaciones sencillas
- Sin uso de características avanzadas de Python
- Código legible y fácil de entender para estudiantes de Programación 1

---

## �📚 Créditos

Proyecto desarrollado por **LeonesDev**
para la materia **Programador – ISPC Córdoba (2025)**.

> *"Evidencian muy buen trabajo de gestión de proyecto."* — Feedback docente.
