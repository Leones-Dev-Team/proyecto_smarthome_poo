
# 🏠 SmartHome – Evidencia N°5 y N°6 (Módulo Programador)

---

## 📘 Descripción General

**SmartHome** es un sistema de gestión desarrollado como parte de las **Evidencias N°5 y N°6 del Módulo Programador** de la Tecnicatura Superior en Desarrollo de Software (ISPC – Córdoba).

El proyecto aplica **Programación Orientada a Objetos (POO)** y el patrón **DAO** para modelar un sistema doméstico inteligente, donde usuarios pueden controlar dispositivos del hogar, gestionar automatizaciones y persistir datos en una base de datos relacional.

---

## ⚙️ Objetivos del Proyecto

* Implementar principios fundamentales de POO:

  * **Abstracción**
  * **Encapsulamiento**
  * **Principio de Responsabilidad Única (SRP)**
  * **Modularidad**
* Representar las relaciones entre clases mediante un **diagrama UML técnico**.
* Integrar una base de datos relacional con scripts SQL (`init.sql`, `queries.sql`).
* Implementar el patrón **DAO** con interfaces para separar lógica de negocio y persistencia.
* Documentar la estructura y justificar las decisiones de diseño.

---

## 🧩 Estructura del Proyecto

```Markdown
proyecto_smarthome_poo/
│
├── main.py
│
├── dominio/
│   ├── usuario.py
│   ├── perfil.py
│   ├── hogar.py
│   ├── dispositivo_hogar.py
│   ├── dispositivo_control.py
│   └── automatizacion.py
│
├── dao/
│   ├── usuario_dao.py
│   ├── perfil_dao.py
│   ├── dispositivo_dao.py
│   ├── automatizacion_dao.py
│   └── interfaces/
│       ├── i_usuario_dao.py
│       ├── i_perfil_dao.py
│       ├── i_dispositivo_dao.py
│       └── i_automatizacion_dao.py
│
├── connection/
│   └── obtener_conexion.py
│
├── BD-Evidencia-5/
│   ├── init.sql
│   ├── queries.sql
│   └── README.md
│
├── BD-Evidencia-6/
│   ├── init.sql
│   ├── queries.sql
│   └── README.md
│
├── DC-Evidencia-5/
│   └── Justificacion_POO_UML_Diagrama_Clases.pdf
│
└── DC-Evidencia-6/
    ├── init.sql
    ├── queries.sql
    ├── README.md
    └── Justificacion_POO_UML_Diagrama_Clases.pdf
```

---

## 🧱 Clases Principales

| Clase                | Descripción                                                                                                  | Relación Principal                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **Usuario**          | Gestiona credenciales, rol y asociación con un hogar. Contiene un `Perfil`.                                  | *Composición* con `Perfil`          |
| **Perfil**           | Contiene datos personales y registro de actividad.                                                           | *Composición* desde `Usuario`       |
| **Hogar**            | Representa una vivienda con ubicación y tipo.                                                                | *Agregación* con `DispositivoHogar` |
| **DispositivoHogar** | Representa un dispositivo controlable (luz, electrodoméstico, etc.) con estado y consumo energético.          | *Asociación* con `Hogar`            |
| **DispositivoControl** | Registra métricas de dispositivos activos, apagados y en ahorro.                                           | *Asociación* con `Usuario`          |
| **Automatizacion**   | Implementa reglas automáticas, como apagar dispositivos no esenciales.                                       | *Agregación* con `DispositivoHogar` |

---

## 🧠 Principios Aplicados

* **Encapsulamiento:**  
  Todos los atributos internos son privados (`_atributo`) con acceso controlado mediante `@property`.

* **SRP (Responsabilidad Única):**  
  Cada clase tiene una única responsabilidad (ej. `Usuario` gestiona credenciales y rol, `Perfil` maneja datos personales, `DAO` maneja persistencia).

* **Abstracción:**  
  Cada clase modela una entidad real del sistema domótico, ocultando detalles internos.

* **Modularidad:**  
  Cada clase y DAO se encuentra en su propio archivo dentro de `dominio/` y `dao/`.

* **Patrón DAO:**  
  Se implementaron interfaces (`IUsuarioDAO`, `IPerfilDAO`, etc.) y sus implementaciones concretas para separar lógica de negocio y acceso a datos.

---

## 🧪 Pruebas Unitarias

El proyecto incluye una suite de tests compatibles con **pytest**.  
En EV6 se mantuvieron en verde, garantizando compatibilidad con las nuevas clases y DAOs.

Para ejecutarlas:

```bash
pytest
```

---

## 🗄️ Base de Datos

Los modelos relacionales y scripts SQL (`init.sql` y `queries.sql`) se encuentran en:

```Markdown
/BD-Evidencia-5/
/BD-Evidencia-6/
```

> 📄 **Nota:** cada carpeta incluye un `README.md` con instrucciones para ejecutar los scripts en un DBMS online.

---

## 📊 Diagrama UML y Justificación POO

Los diagramas UML y sus análisis detallados se encuentran en:

```Markdown
/DC-Evidencia-5/
/DC-Evidencia-6/
```

Archivos principales:  

* `EV5_Justificacion_POO_UML_Diagrama_Clases.pdf`
* `EV6_Justificacion_POO_UML_Diagrama_Clases.pdf` 

Incluyen explicación textual y código PlantUML.

---

## 🧰 Requisitos Técnicos

* Python 3.10 o superior
* pytest (opcional, para ejecutar tests)
* DBMS compatible (MySQL/MariaDB recomendado)

```bash
pip install pytest
```

---

## 📚 Créditos

Proyecto desarrollado por **LeonesDev**  
para la materia **Programador I – ISPC Córdoba (2025)**.

---
