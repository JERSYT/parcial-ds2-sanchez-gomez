use huilasoft
// 1. Coleccion agentes
db.agentes.insertMany([
  { codigo: "A1", nombre: "Laura Cerquera", nivel: "senior", tickets_hora: 10, turno: true },
  { codigo: "A2", nombre: "Andres Perdomo", nivel: "junior", tickets_hora: 6, turno: false }
])
// 2. Coleccion tickets
db.tickets.insertMany([
  { codigo: "T1", llegada: 0, atencion: 5, prioridad: "Alta", agente: "Laura Cerquera" },
  { codigo: "T2", llegada: 3, atencion: 7, prioridad: "Alta", agente: "Laura Cerquera" },
  { codigo: "T3", llegada: 6, atencion: 4, prioridad: "Media", agente: "Laura Cerquera" },
  { codigo: "T4", llegada: 14, atencion: 8, prioridad: "Baja", agente: "Laura Cerquera" },
  { codigo: "T5", llegada: 25, atencion: 6, prioridad: "Alta", agente: "Laura Cerquera" },
  { codigo: "T6", llegada: 28, atencion: 5, prioridad: "Media", agente: "Laura Cerquera" },
  { codigo: "T7", llegada: 40, atencion: 9, prioridad: "Baja", agente: "Laura Cerquera" },
  { codigo: "T8", llegada: 52, atencion: 4, prioridad: "Alta", agente: "Laura Cerquera" }
])
// 3. Coleccion campana de pruebas
db.campana_pruebas.insertMany([
  { semana: 1, defectos: 28 },
  { semana: 2, defectos: 23 },
  { semana: 3, defectos: 22 },
  { semana: 4, defectos: 17 },
  { semana: 5, defectos: 16 },
  { semana: 6, defectos: 12 },
  { semana: 7, defectos: 12 },
  { semana: 8, defectos: 9 }
])
// Consultas solicitadas
// 1. Tickets prioridad Alta
db.tickets.find({ prioridad: "Alta" })
// 2. Tickets con atencion mayor a 6 minutos ($gt)
db.tickets.find({ atencion: { $gt: 6 } })
// 3. Semanas con menos de 15 defectos ($lt)
db.campana_pruebas.find({ defectos: { $lt: 15 } })
// Actualizacion: cambiar prioridad de T7 a Media
db.tickets.updateOne({ codigo: "T7" }, { $set: { prioridad: "Media" } })
// Eliminacion de prueba
db.tickets.insertOne({ codigo: "T_temp", llegada: 99, atencion: 2, prioridad: "Baja", agente: "Laura Cerquera" })
db.tickets.deleteOne({ codigo: "T_temp" })
