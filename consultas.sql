SELECT * FROM `usuarios` WHERE Ocupacion in("estudiante", "docente") ORDER BY Apellido LIMIT 2; 

SELECT * FROM `usuarios`ORDER BY Id LIMIT 5,10;

SELECT * FROM `usuarios`ORDER BY Id DESC LIMIT 5,10;

SELECT Nombre, Apellido FROM usuarios WHERE Id = 5 OR Id = 6;

SELECT Nombre, Apellido FROM usuarios WHERE Id = 5 OR (Id = 6 AND Ocupacion = "estudiante");

SELECT Nombre, Apellido FROM usuarios WHERE Id = 5 OR (Id = 6 AND Ocupacion = "estudiante") AND Apellido = "Perez";

SELECT * FROM usuarios WHERE Ocupacion = "estudiante" OR Ocupacion = "docente" AND Apellido = "Perez"Id = 5 OR Id = 6 ORDER BY Apellido LIMIT 2;



