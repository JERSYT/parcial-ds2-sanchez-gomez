# Parcial Práctico - Electiva Desarrollo de Software II

Docente: José Miguel Llanos Mosquera  
Universidad Surcolombiana - Ingeniería de Software  
Fecha: 21 de noviembre de 2026  

### Integrantes
- Jeisson Esteban Sánchez Robles (u20221202900)
- Kevin Raúl Gómez Vera (u20221203413)

---

### Parte 1. Base de datos en MongoDB

Base de datos: `huilasoft`

Colecciones estructuradas:
- `agentes`: Personal de soporte técnico (`codigo`, `nombre`, `nivel`, `tickets_hora`, `turno`).
- `tickets`: Solicitudes recibidas de MatriculApp (`codigo`, `llegada`, `atencion`, `prioridad`, `agente`).
- `campana_pruebas`: Historial de defectos de las versiones previas (`semana`, `defectos`).

Relación: La colección `tickets` se relaciona con `agentes` mediante el campo `agente`, que almacena el nombre del agente a cargo (Laura Cerquera).

Los comandos de inserción, consultas con `$gt` y `$lt`, actualización y eliminación están en `mongo/script_mongosh.js`. Las evidencias de terminal se encuentran en `mongo/evidencias/`.
