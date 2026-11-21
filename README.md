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

---

### Parte 2. Opción seleccionada

Opción A: Teoría de colas (Clase `MesaDeAyuda`)

Se implementó el modelo en `src/modelo.py` y se ejecuta desde `src/main.py`. El programa consulta la información en MongoDB usando pymongo, aplica las fórmulas matemáticas de colas M/M/1, simula la atención paso a paso de los tickets, guarda la tabla resultante en `resultado_simulacion.csv` y genera la gráfica en `graficas/resultado.png`.

---

### Parte 3. Interpretación de Resultados

Según la teoría M/M/1 el tiempo promedio de espera en cola es de 24 minutos (Wq = 0.40 horas), mientras que en la simulación paso a paso dio apenas 1.625 minutos. Esta diferencia se debe a que la fórmula teórica asume un sistema continuo en estado estable a largo plazo, mientras que en la simulación evaluamos una muestra corta de 8 tickets arrancando a las 8:00 a.m. con el servidor desocupado. Como los intervalos entre llegadas fueron suficientes, Laura atendió rápido y tickets como T1, T5, T7 y T8 no tuvieron ninguna espera, tal como se refleja en la gráfica. Al evaluar el escenario con demanda pico (lambda = 9.5), la utilización sube a 0.95 y la espera teórica se dispara a 114 minutos (1.9 horas). Por tanto, recomendamos a HuilaSoft activar a Andrés Perdomo en horas pico para operar como M/M/2 y evitar la congestión.

---

### Parte 4. Instrucciones de ejecución

Cargar las colecciones y datos en MongoDB:
```bash
mongosh --file mongo/script_mongosh.js
```

Ejecutar la simulación principal:
```bash
python src/main.py
```

Ejecutar las pruebas unitarias:
```bash
python tests/test_modelo.py
```
