-- ============================================
-- CONSULTAS SOBRE HOGARES
-- ============================================

-- Vista general
SELECT * FROM hogares;

-- Ciudades únicas
SELECT DISTINCT ciudad FROM hogares;

-- Orden por tiempo de registro descendente
SELECT * FROM hogares
ORDER BY tiempo_registro DESC;

-- Hogares en Córdoba
SELECT * FROM hogares
WHERE ciudad = 'Córdoba';

-- Cantidad de hogares tipo 'Casa'
SELECT COUNT(*) AS cantidad_casas
FROM hogares
WHERE tipo = 'Casa';

-- Cantidad de hogares por tipo
SELECT tipo, COUNT(*) AS cantidad
FROM hogares
GROUP BY tipo;

-- Hogares con tiempo de registro mayor a 01:00:00
SELECT * FROM hogares
WHERE tiempo_registro > '01:00:00';

-- Hogar con menor tiempo de registro
SELECT * FROM hogares
ORDER BY tiempo_registro ASC
LIMIT 1;

-- Hogares con descripción que contiene 'inicial'
SELECT * FROM hogares
WHERE descripcion LIKE '%inicial%';

-- Promedio de tiempo de registro
SELECT SEC_TO_TIME(AVG(TIME_TO_SEC(tiempo_registro))) AS promedio_tiempo
FROM hogares;

-- ============================================
-- CONSULTAS SOBRE USUARIOS
-- ============================================

-- Vista general
SELECT * FROM usuarios;

-- Emails y teléfonos
SELECT email, telefono
FROM usuarios;

-- Orden por edad descendente
SELECT * FROM usuarios
ORDER BY edad DESC;

-- Usuarios mayores de 30 años
SELECT * FROM usuarios
WHERE edad > 30;

-- Cantidad de usuarios por hogar
SELECT id_hogar, COUNT(*) AS cantidad_usuarios
FROM usuarios
GROUP BY id_hogar;

-- Edad promedio
SELECT AVG(edad) AS edad_promedio
FROM usuarios;

-- Usuarios con email @example.com
SELECT * FROM usuarios
WHERE email LIKE '%@example.com';

-- Usuario con menor tiempo de uso
SELECT * FROM usuarios
ORDER BY tiempo_uso ASC
LIMIT 1;

-- Usuarios del hogar 3
SELECT * FROM usuarios
WHERE id_hogar = 3;

-- Cantidad de usuarios menores de 30 años
SELECT COUNT(*) AS menores_30
FROM usuarios
WHERE edad < 30;

-- ============================================
-- CONSULTAS SOBRE DISPOSITIVOS DE CONTROL
-- ============================================

-- Vista general
SELECT * FROM dispositivos_control;

-- Usuario y estado de cada dispositivo
SELECT id_usuario, estado
FROM dispositivos_control;

-- Dispositivos encendidos
SELECT * FROM dispositivos_control
WHERE estado = 1;

-- Dispositivos en modo 2
SELECT * FROM dispositivos_control
WHERE modo = 2;

-- Cantidad por estado
SELECT estado, COUNT(*) AS cantidad
FROM dispositivos_control
GROUP BY estado;

-- Orden por hora de control ascendente
SELECT * FROM dispositivos_control
ORDER BY hora_control ASC;

-- Último usuario con dispositivo
SELECT * FROM dispositivos_control
ORDER BY id_usuario DESC
LIMIT 1;

-- Dispositivos de usuarios del hogar 1
SELECT dc.*
FROM dispositivos_control dc
JOIN usuarios u ON dc.id_usuario = u.id_usuario
WHERE u.id_hogar = 1;

-- Cantidad por modo
SELECT modo, COUNT(*) AS cantidad
FROM dispositivos_control
GROUP BY modo;

-- Verificación de dispositivos encendidos
SELECT CASE
    WHEN COUNT(*) > 0 THEN 'Hay dispositivos encendidos'
    ELSE 'No hay dispositivos encendidos'
END AS resultado
FROM dispositivos_control
WHERE estado = 1;
