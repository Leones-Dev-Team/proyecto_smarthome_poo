-- Insertar hogares (5 registros)
INSERT INTO hogares VALUES
(1, 'Registro inicial hogar 1', '01:20:00', 'Córdoba', 'Casa'),
(2, 'Registro inicial hogar 2', '00:45:00', 'Buenos Aires', 'Departamento'),
(3, 'Registro inicial hogar 3', '02:10:00', 'Rosario', 'Casa'),
(4, 'Registro inicial hogar 4', '00:30:00', 'Mendoza', 'Departamento'),
(5, 'Registro inicial hogar 5', '01:00:00', 'Salta', 'Casa');

-- Insertar usuarios (10 registros)
INSERT INTO usuarios VALUES
(1, '1234', '00:30:00', 30, 'lucas@example.com', '3511111111', 'Inicio', 1),
(2, 'abcd', '00:20:00', 25, 'ana@example.com', '3512222222', 'Inicio', 1),
(3, 'pass', '00:15:00', 40, 'juan@example.com', '3513333333', 'Inicio', 2),
(4, 'clave', '00:50:00', 35, 'maria@example.com', '3514444444', 'Inicio', 2),
(5, 'xyz', '00:10:00', 28, 'pedro@example.com', '3515555555', 'Inicio', 3),
(6, 'pass1', '00:25:00', 32, 'sofia@example.com', '3516666666', 'Inicio', 3),
(7, 'pass2', '00:40:00', 45, 'diego@example.com', '3517777777', 'Inicio', 4),
(8, 'pass3', '00:35:00', 29, 'laura@example.com', '3518888888', 'Inicio', 4),
(9, 'pass4', '00:12:00', 33, 'martin@example.com', '3519999999', 'Inicio', 5),
(10, 'pass5', '00:55:00', 27, 'carla@example.com', '3510000000', 'Inicio', 5);

-- Insertar dispositivos_control (5 registros)
INSERT INTO dispositivos_control VALUES
(1, 1, '11:00:00', 2, 1, 0),
(2, 3, '11:05:00', 3, 0, 1),
(3, 5, '11:10:00', 1, 2, 0),
(4, 7, '11:15:00', 4, 1, 0),
(5, 9, '11:20:00', 2, 2, 1);

-- Insertar dispositivos_hogar (10 registros)
INSERT INTO dispositivos_hogar VALUES
(101, 1, 'Living', '10:00:00', 'Luz principal', 'Luz', 'Philips', 'encendido', 10.5, 1),
(102, 2, 'Cocina', '10:05:00', 'Heladera', 'Electrodomestico', 'LG', 'encendido', 150.0, 1),
(103, 3, 'Dormitorio', '10:10:00', 'Ventilador', 'Electrodomestico', 'Samsung', 'apagado', 50.0, 2),
(104, 4, 'Baño', '10:15:00', 'Calefón', 'Electrodomestico', 'Rheem', 'encendido', 200.0, 2),
(105, 5, 'Garage', '10:20:00', 'Cargador EV', 'Electrodomestico', 'Tesla', 'apagado', 3000.0, 3),
(106, 6, 'Living', '10:25:00', 'TV', 'Electrodomestico', 'Sony', 'encendido', 120.0, 3),
(107, 7, 'Cocina', '10:30:00', 'Microondas', 'Electrodomestico', 'Whirlpool', 'apagado', 80.0, 4),
(108, 8, 'Dormitorio', '10:35:00', 'Aire acondicionado', 'Electrodomestico', 'Daikin', 'encendido', 1500.0, 4),
(109, 9, 'Baño', '10:40:00', 'Secador', 'Electrodomestico', 'Philips', 'apagado', 60.0, 5),
(110, 10, 'Living', '10:45:00', 'Lámpara', 'Luz', 'Philips', 'encendido', 15.0, 5);

-- Consultas simples
SELECT * FROM hogares;
SELECT * FROM usuarios;
SELECT * FROM dispositivos_control;
SELECT * FROM dispositivos_hogar;
