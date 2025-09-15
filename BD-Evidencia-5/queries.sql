-- CONSULTAS HOGARES (10)
SELECT * FROM hogares;
SELECT DISTINCT ciudad FROM hogares;
SELECT * FROM hogares ORDER BY tiempo_registro DESC;
SELECT * FROM hogares WHERE ciudad = 'Córdoba';
SELECT COUNT(*) AS cantidad_casas FROM hogares WHERE tipo = 'Casa';
SELECT tipo, COUNT(*) AS cantidad FROM hogares GROUP BY tipo;
SELECT * FROM hogares WHERE tiempo_registro > '01:00:00';
SELECT * FROM hogares ORDER BY tiempo_registro ASC LIMIT 1;
SELECT * FROM hogares WHERE descripcion LIKE '%inicial%';
SELECT SEC_TO_TIME(AVG(TIME_TO_SEC(tiempo_registro))) AS promedio_tiempo FROM hogares;

-- CONSULTAS USUARIOS (10)

SELECT * FROM usuarios;
SELECT email, telefono FROM usuarios;
SELECT * FROM usuarios ORDER BY edad DESC;
SELECT * FROM usuarios WHERE edad > 30;
SELECT id_hogar, COUNT(*) AS cantidad_usuarios FROM usuarios GROUP BY id_hogar;
SELECT AVG(edad) AS edad_promedio FROM usuarios;
SELECT * FROM usuarios WHERE email LIKE '%@example.com';
SELECT * FROM usuarios ORDER BY tiempo_uso ASC LIMIT 1;
SELECT * FROM usuarios WHERE id_hogar = 3;
SELECT COUNT(*) AS menores_30 FROM usuarios WHERE edad < 30;

-- CONSULTAS DISPOSITIVOS_CONTROL (10)
SELECT * FROM dispositivos_control;
SELECT id_usuario, estado FROM dispositivos_control;
SELECT * FROM dispositivos_control WHERE estado = 1;
SELECT * FROM dispositivos_control WHERE modo = 2;
SELECT estado, COUNT(*) AS cantidad FROM dispositivos_control GROUP BY estado;
SELECT * FROM dispositivos_control ORDER BY hora_control ASC;
SELECT * FROM dispositivos_control ORDER BY id_usuario DESC LIMIT 1;
SELECT dc.* 
FROM dispositivos_control dc
JOIN usuarios u ON dc.id_usuario = u.id_usuario
WHERE u.id_hogar = 1;
SELECT modo, COUNT(*) AS cantidad FROM dispositivos_control GROUP BY modo;
SELECT CASE WHEN COUNT(*) > 0 THEN 'Hay dispositivos encendidos' 
            ELSE 'No hay dispositivos encendidos' END AS resultado
FROM dispositivos_control WHERE estado = 1;