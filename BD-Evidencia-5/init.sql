-- Tabla hogares
CREATE TABLE
    hogares (
        id_hogar INT PRIMARY KEY,
        registro_actividad TEXT,
        tiempo_de_conexion TIME,
        ubicacion VARCHAR(100),
        tipo_de_vivienda VARCHAR(50)
    );

-- Tabla usuarios
CREATE TABLE
    usuarios (
        id_usuario INT PRIMARY KEY,
        clave VARCHAR(100) NOT NULL,
        tiempo_de_conexion TIME,
        edad INT,
        mail VARCHAR(100),
        telefono VARCHAR(20),
        registro_actividad TEXT,
        id_hogar INT NOT NULL,
        FOREIGN KEY (id_hogar) REFERENCES hogares (id_hogar)
    );

-- Tabla dispositivos_control
CREATE TABLE
    dispositivos_control (
        id_dispositivo_control INT PRIMARY KEY,
        id_usuario_conectado INT NOT NULL,
        hora_de_conexion TIME,
        dispositivos_activos INT,
        dispositivos_apagados INT,
        dispositivos_en_ahorro INT,
        FOREIGN KEY (id_usuario_conectado) REFERENCES usuarios (id_usuario)
    );

-- Tabla dispositivos_hogar
CREATE TABLE
    dispositivos_hogar (
        id_dispositivo INT PRIMARY KEY,
        id_usuario_conectado INT NOT NULL,
        ubicacion VARCHAR(100),
        hora_de_conexion TIME,
        nombre_dispositivo VARCHAR(50),
        tipo_dispositivo VARCHAR(50),
        marca_dispositivo VARCHAR(50),
        estado_dispositivo VARCHAR(30),
        consumo_energetico FLOAT,
        id_dispositivo_control INT,
        FOREIGN KEY (id_usuario_conectado) REFERENCES usuarios (id_usuario),
        FOREIGN KEY (id_dispositivo_control) REFERENCES dispositivos_control (id_dispositivo_control)
    );