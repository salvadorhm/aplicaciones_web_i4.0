CREATE DATABASE agenda_db;

USE agenda_db;

CREATE TABLE personas(
    id_persona int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(100) NOT NULL,
    email varchar(100) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;

INSERT INTO personas(nombre,email)
VALUES
('Dejah', 'dejah@barson.com'),
('Jhon','jhon@earth.com');

CREATE USER 'user_agenda'@'localhost' IDENTIFIED BY 'Agenda.2020';
GRANT ALL PRIVILEGES ON agenda_db.* TO 'user_agenda'@'localhost';
FLUSH PRIVILEGES;
