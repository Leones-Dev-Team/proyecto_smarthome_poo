-- ============================================
-- BASE DE DATOS: SMART HOME
-- Script de inicialización (init.sql)
-- ============================================

CREATE DATABASE smarthome;
USE smarthome;

-- ============================================
-- CREACIÓN DE TABLAS
-- ============================================

-- Hogares
CREATE TABLE hogares (
    id_hogar INT PRIMARY KEY,
    ubicacion VARCHAR(50) NOT NULL,
    tipo_de_vivienda VARCHAR(50) NOT NULL
);

-- Perfiles
CREATE TABLE perfiles (
    id_perfil INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    mail VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    registro_actividad VARCHAR(200)
);

-- Usuarios
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY,
    clave VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    rol VARCHAR(20) NOT NULL,
    id_hogar INT NOT NULL,
    id_perfil INT NOT NULL,
    FOREIGN KEY (id_hogar) REFERENCES hogares(id_hogar),
    FOREIGN KEY (id_perfil) REFERENCES perfiles(id_perfil)
);

-- Dispositivos del hogar
CREATE TABLE dispositivos_hogar (
    id_dispositivo INT PRIMARY KEY,
    id_hogar INT NOT NULL,
    nombre_dispositivo VARCHAR(50) NOT NULL,
    tipo_dispositivo VARCHAR(50) NOT NULL,
    marca_dispositivo VARCHAR(50),
    estado_dispositivo VARCHAR(20) NOT NULL,
    consumo_energetico FLOAT NOT NULL,
    es_esencial BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_hogar) REFERENCES hogares(id_hogar)
);

-- Dispositivos de control
CREATE TABLE dispositivos_control (
    id_dispositivo_control INT PRIMARY KEY,
    id_usuario INT NOT NULL,
    hora_de_conexion TIME,
    dispositivos_activos INT,
    dispositivos_apagados INT,
    dispositivos_en_ahorro INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Automatizaciones
CREATE TABLE automatizaciones (
    id_automatizacion INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Relación automatización-dispositivo
CREATE TABLE automatizacion_dispositivo (
    id_automatizacion INT,
    id_dispositivo INT,
    PRIMARY KEY (id_automatizacion, id_dispositivo),
    FOREIGN KEY (id_automatizacion) REFERENCES automatizaciones(id_automatizacion),
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos_hogar(id_dispositivo)
);

-- ============================================
-- INSERCIÓN DE DATOS INICIALES
-- ============================================

-- Hogares
INSERT INTO hogares VALUES
    (1, 'Córdoba', 'Casa'),
    (2, 'Buenos Aires', 'Departamento'),
    (3, 'Rosario', 'Casa'),
    (4, 'Mendoza', 'Departamento'),
    (5, 'Salta', 'Casa'),
    (6, 'San Juan', 'Casa'),
    (7, 'Neuquén', 'Departamento'),
    (8, 'La Plata', 'Casa'),
    (9, 'San Luis', 'Departamento'),
    (10, 'Santa Fe', 'Casa');

-- Perfiles
INSERT INTO perfiles VALUES
    (1, 'Lucas', 'lucas@example.com', '3511111111', 'Inicio de sesión'),
    (2, 'Ana', 'ana@example.com', '3512222222', 'Inicio de sesión'),
    (3, 'Juan', 'juan@example.com', '3513333333', 'Inicio de sesión'),
    (4, 'María', 'maria@example.com', '3514444444', 'Inicio de sesión'),
    (5, 'Pedro', 'pedro@example.com', '3515555555', 'Inicio de sesión'),
    (6, 'Sofía', 'sofia@example.com', '3516666666', 'Inicio de sesión'),
    (7, 'Diego', 'diego@example.com', '3517777777', 'Inicio de sesión'),
    (8, 'Laura', 'laura@example.com', '3518888888', 'Inicio de sesión'),
    (9, 'Martín', 'martin@example.com', '3519999999', 'Inicio de sesión'),
    (10, 'Carla', 'carla@example.com', '3510000000', 'Inicio de sesión');

-- Usuarios
INSERT INTO usuarios VALUES
    (1, '1234', 30, 'admin', 1, 1),
    (2, 'abcd', 25, 'estandar', 1, 2),
    (3, 'pass', 40, 'admin', 2, 3),
    (4, 'clave', 35, 'estandar', 2, 4),
    (5, 'xyz', 28, 'admin', 3, 5),
    (6, 'pass1', 32, 'estandar', 3, 6),
    (7, 'pass2', 45, 'admin', 4, 7),
    (8, 'pass3', 29, 'estandar', 4, 8),
    (9, 'pass4', 33, 'admin', 5, 9),
    (10, 'pass5', 27, 'estandar', 5, 10);

-- Dispositivos del hogar
INSERT INTO dispositivos_hogar VALUES
    (101, 1, 'Luz principal', 'Luz', 'Philips', 'encendido', 10.5, TRUE),
    (102, 1, 'Heladera', 'Electrodoméstico', 'LG', 'encendido', 150.0, TRUE),
    (103, 2, 'Ventilador', 'Electrodoméstico', 'Samsung', 'apagado', 50.0, FALSE),
    (104, 2, 'Calefón', 'Electrodoméstico', 'Rheem', 'encendido', 200.0, TRUE),
    (105, 3, 'Cargador EV', 'Electrodoméstico', 'Tesla', 'apagado', 3000.0, TRUE),
    (106, 3, 'TV', 'Electrodoméstico', 'Sony', 'encendido', 120.0, FALSE),
    (107, 4, 'Microondas', 'Electrodoméstico', 'Whirlpool', 'apagado', 80.0, FALSE),
    (108, 4, 'Aire acondicionado', 'Electrodoméstico', 'Daikin', 'encendido', 1500.0, TRUE),
    (109, 5, 'Secador', 'Electrodoméstico', 'Philips', 'apagado', 60.0, FALSE),
    (110, 5, 'Lámpara', 'Luz', 'Philips', 'encendido', 15.0, FALSE);

-- Dispositivos de control
INSERT INTO dispositivos_control VALUES
    (1, 1, '11:00:00', 2, 1, 0),
    (2, 2, '11:05:00', 1, 2, 1),
    (3, 3, '11:10:00', 3, 0, 2),
    (4, 4, '11:15:00', 0, 3, 1),
    (5, 5, '11:20:00', 2, 1, 2),
    (6, 6, '11:25:00', 1, 1, 0),
    (7, 7, '11:30:00', 2, 0, 1),
    (8, 8, '11:35:00', 3, 2, 2),
    (9, 9, '11:40:00', 1, 3, 0),
    (10, 10, '11:45:00', 2, 2, 1);

-- Automatizaciones
INSERT INTO automatizaciones VALUES
    (1, 'Ahorro nocturno'),
    (2, 'Modo vacaciones'),
    (3, 'Seguridad básica');

-- Automatización-dispositivo
INSERT INTO automatizacion_dispositivo VALUES
    (1, 101),
    (1, 102),
    (2, 105),
    (2, 106),
    (3, 108),
    (3, 110);
