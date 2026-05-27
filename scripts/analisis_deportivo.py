
import csv

# --- Cargar el dataset con csv.reader ---
partidos = []
with open("datos/resultados_torneo.csv", "r") as archivo:
    reader = csv.reader(archivo)
    next(reader)  # Saltar encabezado
    for fila in reader:
        partidos.append(fila)

print(f"Se cargaron {len(partidos)} partidos")

# --- Calcular victorias por equipo ---
victorias = {}
empates = 0

for fila in partidos:
    local = fila[1]
    visitante = fila[2]
    goles_local = int(fila[3])
    goles_visitante = int(fila[4])

    if goles_local > goles_visitante:
        victorias[local] = victorias.get(local, 0) + 1
    elif goles_visitante > goles_local:
        victorias[visitante] = victorias.get(visitante, 0) + 1
    else:
        empates += 1

print("\nVictorias por equipo:")
for equipo, v in victorias.items():
    print(f"  {equipo}: {v} victorias")
print(f"  Empates en el torneo: {empates}")

# --- Calcular promedio de goles por partido ---
total_goles = 0
for fila in partidos:
    total_goles += int(fila[3]) + int(fila[4])

promedio = total_goles / len(partidos)
print(f"\nTotal de goles: {total_goles}")
print(f"Promedio de goles por partido: {promedio:.2f}")

# --- Guardar resultados en archivo .txt ---
with open("resultados/resumen_torneo.txt", "w") as f:
    f.write("===== RESUMEN DEL TORNEO =====\n\n")
    f.write("Victorias por equipo:\n")
    for equipo, v in victorias.items():
        f.write(f"  {equipo}: {v} victorias\n")
    f.write(f"\nEmpates en el torneo: {empates}\n")
    f.write(f"Total de goles: {total_goles}\n")
    f.write(f"Promedio de goles por partido: {promedio:.2f}\n")

print("\nResultados guardados en resultados/resumen_torneo.txt")
