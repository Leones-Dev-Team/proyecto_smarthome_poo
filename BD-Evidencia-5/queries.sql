-- ============================
-- SECCIÓN: HOGARES
-- Consultas relacionadas con información de hogares,
-- ubicaciones, tipos de vivienda y tiempos de conexión.
-- ============================

-- Vista general de todos los hogares
SELECT * FROM hogares;

-- Conteos y agrupaciones relevantes
SELECT COUNT(DISTINCT ubicacion) AS ciudades_cubiertas FROM hogares;
SELECT ubicacion, COUNT(*) AS cantidad_por_ciudad FROM hogares GROUP BY ubicacion;
SELECT tipo_de_vivienda, COUNT(*) AS cantidad_por_tipo FROM hogares GROUP BY tipo_de_vivienda;

-- Métricas de tiempo de conexión
SELECT AVG(TIME_TO_SEC(tiempo_de_conexion)) AS segundos_promedio_conexion FROM hogares;
SELECT MAX(tiempo_de_conexion) AS max_tiempo_conexion FROM hogares;

-- Filtros específicos
SELECT * FROM hogares WHERE tipo_de_vivienda = 'Casa';
SELECT * FROM hogares WHERE ubicacion = 'Córdoba';

-- Ordenamientos
SELECT * FROM hogares ORDER BY tiempo_de_conexion ASC;
SELECT * FROM hogares ORDER BY tiempo_de_conexion DESC;


-- ============================
-- SECCIÓN: USUARIOS
-- Consultas relacionadas con usuarios, roles,
-- edades y su distribución en hogares.
-- ============================

-- Vista general de todos los usuarios
SELECT * FROM usuarios;

-- Conteos y agrupaciones relevantes
SELECT COUNT(*) AS total_usuarios FROM usuarios;
SELECT id_hogar, COUNT(*) AS usuarios_por_hogar FROM usuarios GROUP BY id_hogar;
SELECT rol, COUNT(*) AS cantidad_por_rol FROM usuarios GROUP BY rol;

-- Métricas de edad
SELECT AVG(edad) AS edad_promedio FROM usuarios;
SELECT MIN(edad) AS edad_minima FROM usuarios;

-- Filtros específicos
SELECT * FROM usuarios WHERE rol = 'admin';
SELECT * FROM usuarios WHERE edad > 30;

-- Ordenamientos
SELECT * FROM usuarios ORDER BY edad ASC;
SELECT * FROM usuarios ORDER BY tiempo_de_conexion DESC;


-- ============================
-- SECCIÓN: DISPOSITIVOS DE CONTROL
-- Consultas sobre dispositivos de control,
-- su estado (activos, apagados, en ahorro) y conexiones.
-- ============================

-- Vista general de todos los dispositivos de control
SELECT * FROM dispositivos_control;

-- Conteos y agrupaciones relevantes
SELECT COUNT(*) AS total_controles FROM dispositivos_control;
SELECT id_usuario_conectado, SUM(dispositivos_activos) AS total_activos FROM dispositivos_control GROUP BY id_usuario_conectado;
SELECT dispositivos_activos, COUNT(*) AS cantidad_por_activos FROM dispositivos_control GROUP BY dispositivos_activos;

-- Métricas de estado
SELECT AVG(dispositivos_apagados) AS promedio_apagados FROM dispositivos_control;
SELECT MAX(dispositivos_en_ahorro) AS max_ahorro FROM dispositivos_control;

-- Filtros específicos
SELECT * FROM dispositivos_control WHERE dispositivos_activos > 1;
SELECT * FROM dispositivos_control WHERE dispositivos_en_ahorro > 0;

-- Ordenamientos
SELECT * FROM dispositivos_control ORDER BY hora_de_conexion ASC;
SELECT * FROM dispositivos_control ORDER BY hora_de_conexion DESC;


-- ============================
-- SECCIÓN: DISPOSITIVOS DEL HOGAR
-- Consultas sobre dispositivos del hogar,
-- consumo energético, tipos y ubicación.
-- ============================

-- Vista general de todos los dispositivos del hogar
SELECT * FROM dispositivos_hogar;

-- Conteos y agrupaciones relevantes
SELECT COUNT(*) AS total_dispositivos FROM dispositivos_hogar;
SELECT tipo_dispositivo, COUNT(*) AS cantidad_por_tipo FROM dispositivos_hogar GROUP BY tipo_dispositivo;
SELECT ubicacion, AVG(consumo_energetico) AS promedio_consumo_ubicacion FROM dispositivos_hogar GROUP BY ubicacion;

-- Métricas de consumo
SELECT SUM(consumo_energetico) AS total_consumo FROM dispositivos_hogar;
SELECT MAX(consumo_energetico) AS max_consumo FROM dispositivos_hogar;

-- Filtros específicos
SELECT * FROM dispositivos_hogar WHERE estado_dispositivo = 'encendido';
SELECT * FROM dispositivos_hogar WHERE es_esencial = TRUE;

-- Ordenamientos
SELECT * FROM dispositivos_hogar ORDER BY consumo_energetico ASC;
SELECT * FROM dispositivos_hogar ORDER BY hora_de_conexion DESC;