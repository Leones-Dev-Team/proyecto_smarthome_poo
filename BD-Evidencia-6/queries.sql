-- ============================================
-- ARCHIVO: QUERIES.SQL
-- Consultas din�micas para el sistema Smart Home
-- ============================================

-- ============================================
-- CONSULTAS PARA REEMPLAZAR DATOS DERIVADOS
-- Calculan din�micamente la informaci�n que antes se almacenaba en dispositivos_control
-- ============================================

-- Consulta 1: Contar dispositivos activos por usuario
-- Reemplaza el campo "dispositivos_activos" eliminado de dispositivos_control
SELECT 
    u.id_usuario,
    u.mail,
    COUNT(CASE WHEN dh.estado_dispositivo = 'encendido' THEN 1 END) as dispositivos_activos
FROM usuarios u
LEFT JOIN dispositivos_hogar dh ON u.id_usuario = dh.id_usuario_conectado
GROUP BY u.id_usuario, u.mail
ORDER BY u.id_usuario;

-- Consulta 2: Contar dispositivos apagados por usuario
-- Reemplaza el campo "dispositivos_apagados" eliminado de dispositivos_control
SELECT 
    u.id_usuario,
    u.mail,
    COUNT(CASE WHEN dh.estado_dispositivo = 'apagado' THEN 1 END) as dispositivos_apagados
FROM usuarios u
LEFT JOIN dispositivos_hogar dh ON u.id_usuario = dh.id_usuario_conectado
GROUP BY u.id_usuario, u.mail
ORDER BY u.id_usuario;

-- Consulta 3: Contar dispositivos en modo ahorro por usuario
-- Reemplaza el campo "dispositivos_en_ahorro" eliminado de dispositivos_control
SELECT 
    u.id_usuario,
    u.mail,
    COUNT(CASE WHEN dh.estado_dispositivo = 'ahorro' THEN 1 END) as dispositivos_en_ahorro
FROM usuarios u
LEFT JOIN dispositivos_hogar dh ON u.id_usuario = dh.id_usuario_conectado
GROUP BY u.id_usuario, u.mail
ORDER BY u.id_usuario;

-- Consulta 4: Resumen completo de estados de dispositivos por usuario
-- Combina toda la informaci�n que antes se almacenaba como datos derivados
SELECT 
    u.id_usuario,
    u.mail,
    u.rol,
    dc.hora_de_conexion,
    COUNT(dh.id_dispositivo) as total_dispositivos,
    COUNT(CASE WHEN dh.estado_dispositivo = 'encendido' THEN 1 END) as dispositivos_activos,
    COUNT(CASE WHEN dh.estado_dispositivo = 'apagado' THEN 1 END) as dispositivos_apagados,
    COUNT(CASE WHEN dh.estado_dispositivo = 'ahorro' THEN 1 END) as dispositivos_en_ahorro,
    SUM(CASE WHEN dh.estado_dispositivo = 'encendido' THEN dh.consumo_energetico ELSE 0 END) as consumo_total_activo
FROM usuarios u
LEFT JOIN dispositivos_control dc ON u.id_usuario = dc.id_usuario_conectado
LEFT JOIN dispositivos_hogar dh ON u.id_usuario = dh.id_usuario_conectado
GROUP BY u.id_usuario, u.mail, u.rol, dc.hora_de_conexion
ORDER BY u.id_usuario;

-- ============================================
-- CONSULTAS ADICIONALES PARA AN�LISIS DEL SISTEMA
-- ============================================

-- Consulta 5: Automatizaciones activas por dispositivo
SELECT 
    dh.nombre_dispositivo,
    dh.tipo_dispositivo,
    dh.ubicacion,
    COUNT(a.id_automatizacion) as total_automatizaciones,
    COUNT(CASE WHEN a.activa = TRUE THEN 1 END) as automatizaciones_activas
FROM dispositivos_hogar dh
LEFT JOIN automatizaciones a ON dh.id_dispositivo = a.id_dispositivo
GROUP BY dh.id_dispositivo, dh.nombre_dispositivo, dh.tipo_dispositivo, dh.ubicacion
ORDER BY automatizaciones_activas DESC;

-- Consulta 6: Consumo energ�tico por hogar
SELECT 
    h.id_hogar,
    h.ubicacion,
    h.tipo_de_vivienda,
    COUNT(dh.id_dispositivo) as total_dispositivos,
    SUM(CASE WHEN dh.estado_dispositivo = 'encendido' THEN dh.consumo_energetico ELSE 0 END) as consumo_actual,
    SUM(dh.consumo_energetico) as consumo_maximo_posible,
    ROUND(
        (SUM(CASE WHEN dh.estado_dispositivo = 'encendido' THEN dh.consumo_energetico ELSE 0 END) / 
         SUM(dh.consumo_energetico)) * 100, 2
    ) as porcentaje_uso_energia
FROM hogares h
LEFT JOIN dispositivos_hogar dh ON h.id_hogar = dh.id_hogar
GROUP BY h.id_hogar, h.ubicacion, h.tipo_de_vivienda
ORDER BY consumo_actual DESC;

-- Consulta 7: Dispositivos esenciales vs no esenciales por hogar
SELECT 
    h.ubicacion as hogar,
    COUNT(CASE WHEN dh.es_esencial = TRUE THEN 1 END) as dispositivos_esenciales,
    COUNT(CASE WHEN dh.es_esencial = FALSE THEN 1 END) as dispositivos_no_esenciales,
    SUM(CASE WHEN dh.es_esencial = TRUE AND dh.estado_dispositivo = 'encendido' THEN dh.consumo_energetico ELSE 0 END) as consumo_esenciales,
    SUM(CASE WHEN dh.es_esencial = FALSE AND dh.estado_dispositivo = 'encendido' THEN dh.consumo_energetico ELSE 0 END) as consumo_no_esenciales
FROM hogares h
LEFT JOIN dispositivos_hogar dh ON h.id_hogar = dh.id_hogar
GROUP BY h.id_hogar, h.ubicacion
ORDER BY h.id_hogar;

-- Consulta 8: Automatizaciones programadas por d�a de la semana
SELECT 
    a.dias_semana,
    COUNT(*) as cantidad_automatizaciones,
    COUNT(CASE WHEN a.activa = TRUE THEN 1 END) as automatizaciones_activas,
    COUNT(DISTINCT a.id_dispositivo) as dispositivos_automatizados
FROM automatizaciones a
GROUP BY a.dias_semana
ORDER BY cantidad_automatizaciones DESC;

-- Consulta 9: Top 5 dispositivos con mayor consumo energ�tico
SELECT 
    dh.nombre_dispositivo,
    dh.tipo_dispositivo,
    dh.marca_dispositivo,
    dh.ubicacion,
    dh.consumo_energetico,
    dh.estado_dispositivo,
    h.ubicacion as hogar
FROM dispositivos_hogar dh
JOIN hogares h ON dh.id_hogar = h.id_hogar
ORDER BY dh.consumo_energetico DESC
LIMIT 5;

-- Consulta 10: Usuarios administradores vs est�ndar y su actividad
SELECT 
    u.rol,
    COUNT(*) as cantidad_usuarios,
    AVG(TIME_TO_SEC(u.tiempo_de_conexion)) as tiempo_promedio_conexion_segundos,
    COUNT(DISTINCT dh.id_dispositivo) as total_dispositivos_gestionados,
    COUNT(DISTINCT dc.id_dispositivo_control) as sesiones_control_activas
FROM usuarios u
LEFT JOIN dispositivos_hogar dh ON u.id_usuario = dh.id_usuario_conectado
LEFT JOIN dispositivos_control dc ON u.id_usuario = dc.id_usuario_conectado
GROUP BY u.rol
ORDER BY cantidad_usuarios DESC;

-- ============================================
-- VISTAS PARA FACILITAR CONSULTAS RECURRENTES
-- ============================================

-- Vista 1: Resumen de dispositivos por usuario (reemplaza tabla desnormalizada)
CREATE VIEW vista_resumen_dispositivos_usuario AS
SELECT 
    u.id_usuario,
    u.mail,
    u.rol,
    COUNT(dh.id_dispositivo) as total_dispositivos,
    COUNT(CASE WHEN dh.estado_dispositivo = 'encendido' THEN 1 END) as dispositivos_activos,
    COUNT(CASE WHEN dh.estado_dispositivo = 'apagado' THEN 1 END) as dispositivos_apagados,
    COUNT(CASE WHEN dh.estado_dispositivo = 'ahorro' THEN 1 END) as dispositivos_en_ahorro,
    SUM(CASE WHEN dh.estado_dispositivo = 'encendido' THEN dh.consumo_energetico ELSE 0 END) as consumo_actual
FROM usuarios u
LEFT JOIN dispositivos_hogar dh ON u.id_usuario = dh.id_usuario_conectado
GROUP BY u.id_usuario, u.mail, u.rol;

-- Vista 2: Automatizaciones activas con informaci�n del dispositivo
CREATE VIEW vista_automatizaciones_activas AS
SELECT 
    a.id_automatizacion,
    a.nombre_automatizacion,
    a.tipo_automatizacion,
    a.condicion_activacion,
    a.accion,
    a.hora_programada,
    a.dias_semana,
    dh.nombre_dispositivo,
    dh.tipo_dispositivo,
    dh.ubicacion,
    h.ubicacion as hogar
FROM automatizaciones a
JOIN dispositivos_hogar dh ON a.id_dispositivo = dh.id_dispositivo
JOIN hogares h ON dh.id_hogar = h.id_hogar
WHERE a.activa = TRUE;

-- ============================================
-- CONSULTAS DE VALIDACI�N
-- Verifican la integridad de los datos despu�s de las correcciones
-- ============================================

-- Verificaci�n 1: Contar automatizaciones (debe ser >= 10)
SELECT 'Total automatizaciones' as descripcion, COUNT(*) as cantidad 
FROM automatizaciones;

-- Verificaci�n 2: Confirmar que no existen campos derivados en dispositivos_control
DESCRIBE dispositivos_control;

-- Verificaci�n 3: Verificar que todas las automatizaciones tienen un dispositivo v�lido
SELECT 
    'Automatizaciones con dispositivos v�lidos' as descripcion,
    COUNT(a.id_automatizacion) as cantidad
FROM automatizaciones a
JOIN dispositivos_hogar dh ON a.id_dispositivo = dh.id_dispositivo;
-- Fin del archivo queries.sql