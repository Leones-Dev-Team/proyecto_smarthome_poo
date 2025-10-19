-- ============================================
-- SECCIÓN: TABLAS PRINCIPALES
-- Definición de entidades y relaciones
-- ============================================

-- Tabla de hogares
CREATE TABLE hogares (
    id_hogar INT PRIMARY KEY,
    registro_actividad VARCHAR(100),
    tiempo_de_conexion TIME,
    ubicacion VARCHAR(50),
    tipo_de_vivienda VARCHAR(50)
);

-- Tabla de usuarios (relacionada con hogares)
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY,
    clave VARCHAR(50) NOT NULL,
    tiempo_de_conexion TIME,
    edad INT,
    mail VARCHAR(100),
    telefono VARCHAR(20),
    registro_actividad VARCHAR(100),
    rol VARCHAR(20),
    id_hogar INT NOT NULL,
    FOREIGN KEY (id_hogar) REFERENCES hogares(id_hogar)
);

-- Tabla de dispositivos de control (relacionada con usuarios)
CREATE TABLE dispositivos_control (
    id_dispositivo_control INT PRIMARY KEY,
    id_usuario_conectado INT NOT NULL,
    hora_de_conexion TIME,
    FOREIGN KEY (id_usuario_conectado) REFERENCES usuarios(id_usuario)
);

-- Tabla de dispositivos del hogar (relacionada con usuarios y hogares)
CREATE TABLE dispositivos_hogar (
    id_dispositivo INT PRIMARY KEY,
    id_usuario_conectado INT NOT NULL,
    ubicacion VARCHAR(50),
    hora_de_conexion TIME,
    nombre_dispositivo VARCHAR(50),
    tipo_dispositivo VARCHAR(50),
    marca_dispositivo VARCHAR(50),
    estado_dispositivo VARCHAR(20),
    consumo_energetico FLOAT,
    es_esencial BOOLEAN DEFAULT FALSE,
    id_hogar INT,
    FOREIGN KEY (id_usuario_conectado) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_hogar) REFERENCES hogares(id_hogar)
);

-- Tabla de automatizaciones (relacionada con dispositivos del hogar)
CREATE TABLE automatizaciones (
    id_automatizacion INT PRIMARY KEY,
    id_dispositivo INT NOT NULL,
    nombre_automatizacion VARCHAR(100),
    tipo_automatizacion VARCHAR(50),
    condicion_activacion VARCHAR(200),
    accion VARCHAR(200),
    hora_programada TIME,
    dias_semana VARCHAR(20),
    activa BOOLEAN DEFAULT TRUE,
    fecha_creacion DATE,
    descripcion VARCHAR(250),
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos_hogar(id_dispositivo)
);


-- ============================================
-- SECCIÓN: INSERCIÓN DE DATOS (DML INICIAL)
-- Datos de prueba para poblar las tablas
-- ============================================

-- Insertar hogares (5 registros)
INSERT INTO hogares VALUES
(1, 'Registro inicial hogar 1', '01:20:00', 'Córdoba', 'Casa'),
(2, 'Registro inicial hogar 2', '00:45:00', 'Buenos Aires', 'Departamento'),
(3, 'Registro inicial hogar 3', '02:10:00', 'Rosario', 'Casa'),
(4, 'Registro inicial hogar 4', '00:30:00', 'Mendoza', 'Departamento'),
(5, 'Registro inicial hogar 5', '01:00:00', 'Salta', 'Casa');

-- Insertar usuarios (10 registros)
INSERT INTO usuarios VALUES
(1, '1234', '00:30:00', 30, 'lucas@example.com', '3511111111', 'Inicio de sesión', 'admin', 1),
(2, 'abcd', '00:20:00', 25, 'ana@example.com', '3512222222', 'Inicio de sesión', 'estándar', 1),
(3, 'pass', '00:15:00', 40, 'juan@example.com', '3513333333', 'Inicio de sesión', 'admin', 2),
(4, 'clave', '00:50:00', 35, 'maria@example.com', '3514444444', 'Inicio de sesión', 'estándar', 2),
(5, 'xyz', '00:10:00', 28, 'pedro@example.com', '3515555555', 'Inicio de sesión', 'admin', 3),
(6, 'pass1', '00:25:00', 32, 'sofia@example.com', '3516666666', 'Inicio de sesión', 'estándar', 3),
(7, 'pass2', '00:40:00', 45, 'diego@example.com', '3517777777', 'Inicio de sesión', 'admin', 4),
(8, 'pass3', '00:35:00', 29, 'laura@example.com', '3518888888', 'Inicio de sesión', 'estándar', 4),
(9, 'pass4', '00:12:00', 33, 'martin@example.com', '3519999999', 'Inicio de sesión', 'admin', 5),
(10, 'pass5', '00:55:00', 27, 'carla@example.com', '3510000000', 'Inicio de sesión', 'estándar', 5);

-- Insertar dispositivos de control (5 registros)
INSERT INTO dispositivos_control VALUES
(1, 1, '11:00:00'),
(2, 3, '11:05:00'),
(3, 5, '11:10:00'),
(4, 7, '11:15:00'),
(5, 9, '11:20:00');

-- Insertar dispositivos del hogar (10 registros)
INSERT INTO dispositivos_hogar VALUES
(101, 1, 'Living', '10:00:00', 'Luz principal', 'Luz', 'Philips', 'encendido', 10.5, TRUE, 1),
(102, 2, 'Cocina', '10:05:00', 'Heladera', 'Electrodomestico', 'LG', 'encendido', 150.0, TRUE, 1),
(103, 3, 'Dormitorio', '10:10:00', 'Ventilador', 'Electrodomestico', 'Samsung', 'apagado', 50.0, FALSE, 2),
(104, 4, 'Baño', '10:15:00', 'Calefón', 'Electrodomestico', 'Rheem', 'encendido', 200.0, TRUE, 2),
(105, 5, 'Garage', '10:20:00', 'Cargador EV', 'Electrodomestico', 'Tesla', 'apagado', 3000.0, TRUE, 3),
(106, 6, 'Living', '10:25:00', 'TV', 'Electrodomestico', 'Sony', 'encendido', 120.0, FALSE, 3),
(107, 7, 'Cocina', '10:30:00', 'Microondas', 'Electrodomestico', 'Whirlpool', 'apagado', 80.0, FALSE, 4),
(108, 8, 'Dormitorio', '10:35:00', 'Aire acondicionado', 'Electrodomestico', 'Daikin', 'encendido', 1500.0, TRUE, 4),
(109, 9, 'Baño', '10:40:00', 'Secador', 'Electrodomestico', 'Philips', 'apagado', 60.0, FALSE, 5),
(110, 10, 'Living', '10:45:00', 'Lámpara', 'Luz', 'Philips', 'encendido', 15.0, FALSE, 5);

-- Insertar automatizaciones (12 registros)
INSERT INTO automatizaciones VALUES
(1, 101, 'Luz nocturna automática', 'Programada', 'Hora >= 20:00', 'Encender luz', '20:00:00', 'Lun-Dom', TRUE, '2024-01-15', 'Enciende automáticamente la luz principal del living cada noche'),
(2, 101, 'Apagar luz madrugada', 'Programada', 'Hora >= 06:00', 'Apagar luz', '06:00:00', 'Lun-Dom', TRUE, '2024-01-15', 'Apaga la luz principal del living en la madrugada'),
(3, 103, 'Ventilador verano', 'Condicional', 'Temperatura > 25°C', 'Encender ventilador', '14:00:00', 'Lun-Dom', TRUE, '2024-02-01', 'Activa el ventilador cuando hace calor durante el día'),
(4, 105, 'Carga nocturna EV', 'Programada', 'Tarifa nocturna activa', 'Iniciar carga', '23:00:00', 'Lun-Dom', TRUE, '2024-01-20', 'Programa la carga del vehículo eléctrico en horario de tarifa reducida'),
(5, 106, 'TV modo ahorro', 'Condicional', 'Sin actividad > 2 horas', 'Modo standby', '22:00:00', 'Lun-Dom', TRUE, '2024-01-25', 'Pone la TV en modo ahorro si no se detecta actividad'),
(6, 107, 'Seguridad microondas', 'Condicional', 'Nadie en casa', 'Apagar dispositivo', '00:00:00', 'Lun-Dom', TRUE, '2024-02-05', 'Apaga el microondas por seguridad cuando no hay nadie en casa'),
(7, 108, 'Aire acondicionado inteligente', 'Condicional', 'Temperatura < 18°C', 'Ajustar a 20°C', '21:00:00', 'Lun-Vie', TRUE, '2024-01-30', 'Regula automáticamente la temperatura del aire acondicionado'),
(8, 109, 'Secador fin de semana', 'Programada', 'Días sábado y domingo', 'Disponible para uso', '08:00:00', 'Sab-Dom', TRUE, '2024-02-10', 'Habilita el secador automáticamente los fines de semana'),
(9, 110, 'Lámpara lectura nocturna', 'Programada', 'Hora >= 21:00', 'Encender con intensidad baja', '21:00:00', 'Lun-Dom', TRUE, '2024-01-18', 'Enciende la lámpara con luz tenue para lectura nocturna'),
(10, 102, 'Mantenimiento heladera', 'Programada', 'Primer día del mes', 'Verificar temperatura', '06:00:00', 'Lun-Dom', TRUE, '2024-02-01', 'Revisa automáticamente el funcionamiento de la heladera mensualmente'),
(11, 104, 'Calefón modo eco', 'Condicional', 'Consumo bajo por 3 días', 'Activar modo eco', '05:00:00', 'Lun-Dom', TRUE, '2024-01-22', 'Activa modo de ahorro energético en el calefón'),
(12, 101, 'Luz presencia', 'Condicional', 'Detección de movimiento', 'Encender luz temporal', '18:00:00', 'Lun-Dom', TRUE, '2024-02-15', 'Enciende la luz automáticamente al detectar presencia en el living');