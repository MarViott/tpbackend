SELECT
    *
FROM
    `USUARIOS`.`USUARIOS` LIMIT 1000;

SELECT * FROM `usuarios` WHERE Ocupacion in("estudiante", "docente") ORDER BY Apellido LIMIT 2;   