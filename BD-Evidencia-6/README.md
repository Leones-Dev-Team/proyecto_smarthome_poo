
# 🏠 Ejecución de la Base de Datos en OneCompiler (MySQL)

Este proyecto incluye dos scripts MySQL:

- **init.sql** → Contiene las sentencias DDL para crear la base de datos y sus tablas.  
- **queries.sql** → Contiene las sentencias DML para insertar datos iniciales y realizar consultas simples.

---

## 🚀 Vista rápida en OneCompiler

Si quiere visualizar las consultas ejecutándose automáticamente, puede utilizar el siguiente enlace directo:  
👉 [Ejecutar en OneCompiler](https://onecompiler.com/mysql/43yypdp99)

---

## 📋 Pasos para ejecución manual en OneCompiler

### 1. Ingresar a OneCompiler

Abrir el navegador y acceder a: [https://onecompiler.com/](https://onecompiler.com/)

### 2. Seleccionar el lenguaje MySQL

En la barra de búsqueda de lenguajes, escribir **MySQL**.  
Hacer clic en **MySQL** para iniciar un nuevo proyecto en dicho lenguaje.

### 3. Agregar el archivo `init.sql`

En la parte izquierda, donde aparece la lista de archivos, hacer clic en el botón **+** (Agregar archivo).  
Automáticamente se creará un archivo con el nombre **init.sql**.  
Pegar dentro de `init.sql` el contenido del archivo `init.sql` que se encuentra en este repositorio.

⚠️ **Importante:** Para que funcione correctamente en OneCompiler, **no incluya** esta sección al inicio de `init.sql`.  
OneCompiler ya maneja automáticamente la base de datos por defecto:

```sql
-- ============================================
-- BASE DE DATOS: SMART HOME
-- Script de inicialización (init.sql)
-- ============================================

DROP DATABASE IF EXISTS smarthome;
CREATE DATABASE smarthome;
USE smarthome;
```

### 4. Agregar el archivo `queries.sql`

Crear un nuevo archivo llamado **queries.sql** y pegar dentro el contenido del archivo `queries.sql` que se encuentra en este repositorio.

⚠️ **Importante:** Para que funcione correctamente en OneCompiler, **no incluya** esta sección al inicio de `queries.sql`.  
OneCompiler ya maneja automáticamente la base de datos por defecto:

```sql
-- ============================================
-- ARCHIVO: QUERIES.SQL
-- Consultas dinámicas para el sistema Smart Home
-- ============================================

USE smarthome;
```

### 5. Ejecutar los scripts

OneCompiler ejecuta primero `init.sql` y luego `queries.sql` de forma automática.  
Hacer clic en el botón **Run** (Ejecutar) en la parte superior.  
Verificar en la consola de salida que las tablas se crean correctamente y que las consultas muestran los datos insertados.

---

## ⚙️ Configuración local con `.env`

Si desea probar el proyecto en su entorno local con MySQL, debe configurar las credenciales de conexión:

1. Copiar el archivo **`.env.example`** que se encuentra en el repositorio.  
2. Renombrarlo a **`.env`**.  
3. Modificar su contenido con los datos de su instalación de MySQL:

```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_DATABASE=smarthome
```

Esto permitirá que la clase `DatabaseConnection` utilice las variables de entorno correctas para conectarse a la base de datos.

---

## 📝 Notas

- **Orden de ejecución:** OneCompiler siempre ejecuta `init.sql` antes que `queries.sql`, por lo que no es necesario modificar el orden manualmente.  
- **Compatibilidad:** Los scripts están escritos para MySQL, por lo que no requieren cambios para funcionar en OneCompiler.  
- **Verificación:** Si todo está correcto, debería visualizar en la salida los resultados de los `SELECT` de cada tabla con los datos insertados.

---
