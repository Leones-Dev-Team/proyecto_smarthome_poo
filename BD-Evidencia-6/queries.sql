-- ============================================
-- BASE DE DATOS: SMART HOME
-- Script de consultas (queries.sql)
-- ============================================

-- ============================
-- CONSULTAS SIMPLES POR TABLA
-- ============================

-- Hogares: mostrar todos los hogares
SELECT *
FROM hogares;

-- Perfiles: listar nombre y mail de todos los perfiles
SELECT nombre, mail
FROM perfiles;

-- Usuarios: mostrar id, rol y hogar asociado
SELECT id_usuario, rol, id_hogar
FROM usuarios;

-- Dispositivos del hogar: listar nombre y consumo
SELECT nombre_dispositivo, consumo_energetico
FROM dispositivos_hogar;

-- Dispositivos de control: vista general
SELECT *
FROM dispositivos_control;

-- Automatizaciones: vista general
SELECT *
FROM automatizaciones;

-- ============================================
-- CONSULTAS MULTITABLA
-- ============================================

-- 1. Usuarios y su hogar (JOIN explícito)
-- Permite ver qué usuarios pertenecen a qué vivienda
SELECT
    u.id_usuario,
    p.nombre,
    u.rol,
    h.ubicacion,
    h.tipo_de_vivienda
FROM usuarios u
INNER JOIN perfiles p ON u.id_perfil = p.id_perfil
INNER JOIN hogares h ON u.id_hogar = h.id_hogar;

-- 2. Dispositivos del hogar con el usuario responsable (JOIN implícito estilo WHERE)
-- Útil para saber qué usuario gestiona cada dispositivo
SELECT
    d.id_dispositivo,
    d.nombre_dispositivo,
    p.nombre AS usuario
FROM dispositivos_hogar d, usuarios u, perfiles p
WHERE d.id_hogar = u.id_hogar
  AND u.id_perfil = p.id_perfil;

-- 3. Dispositivos de control con usuario y hogar
-- Permite auditar qué controles están activos en cada vivienda
SELECT
    dc.id_dispositivo_control,
    dc.hora_de_conexion,
    dc.dispositivos_activos,
    p.nombre,
    h.ubicacion
FROM dispositivos_control dc
JOIN usuarios u ON dc.id_usuario = u.id_usuario
JOIN perfiles p ON u.id_perfil = p.id_perfil
JOIN hogares h ON u.id_hogar = h.id_hogar;

-- 4. Automatizaciones y dispositivos asociados
-- Permite verificar qué reglas afectan a qué dispositivos
SELECT
    a.nombre AS automatizacion,
    d.nombre_dispositivo,
    d.tipo_dispositivo
FROM automatizaciones a
JOIN automatizacion_dispositivo ad ON a.id_automatizacion = ad.id_automatizacion
JOIN dispositivos_hogar d ON ad.id_dispositivo = d.id_dispositivo;

-- ============================================
-- SUBCONSULTAS
-- ============================================

-- 1. Usuarios cuya edad es mayor al promedio de todos los usuarios
-- Caso de negocio: identificar usuarios senior
SELECT
    p.nombre,
    u.rol,
    u.id_usuario
FROM usuarios u
JOIN perfiles p ON u.id_perfil = p.id_perfil
WHERE u.edad > (
    SELECT AVG(edad)
    FROM usuarios
);

-- 2. Dispositivos cuyo consumo supera el promedio de su hogar
-- Caso de negocio: detectar dispositivos de alto consumo
SELECT
    d.id_dispositivo,
    d.nombre_dispositivo,
    d.consumo_energetico,
    h.ubicacion
FROM dispositivos_hogar d
JOIN hogares h ON d.id_hogar = h.id_hogar
WHERE d.consumo_energetico > (
    SELECT AVG(d2.consumo_energetico)
    FROM dispositivos_hogar d2
    WHERE d2.id_hogar = d.id_hogar
);

-- ============================================
-- CONSULTAS CON GROUP BY Y ORDER BY
-- ============================================

-- Cantidad de usuarios por rol
SELECT rol, COUNT(*) AS cantidad
FROM usuarios
GROUP BY rol;

-- Consumo promedio por tipo de dispositivo
SELECT tipo_dispositivo, AVG(consumo_energetico) AS promedio_consumo
FROM dispositivos_hogar
GROUP BY tipo_dispositivo;

-- Ordenar dispositivos por consumo descendente
SELECT nombre_dispositivo, consumo_energetico
FROM dispositivos_hogar
ORDER BY consumo_energetico DESC;
