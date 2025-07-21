USE "uni2";
GO;

CREATE TABLE asignaturas(
    id INTEGER NOT NULL AUTO_INCREMENT,
    codigo_asignatura VARCHAR(5) NOT NULL,
    nombre_asignatura VARCHAR(255) NOT NULL,

    CONSTRAINT pk_asignaturas PRIMARY KEY(id)

);