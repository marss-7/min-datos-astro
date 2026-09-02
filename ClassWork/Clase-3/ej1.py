import numpy as np

tiempo = np.linspace(0,10,10000)

señal = np.sin(2 * np.pi * 5 * tiempo) * np.exp(-tiempo / 3)
mask = señal > 0.5
señalnew = señal[mask]

print(f"tiempos originales totales: ", {len(tiempo)})
print(f"tiempos mayores a 0.5: ", {len(señalnew)})

# 4

flujo_total = np.sum(señalnew)
print(f"El flujo total es: ", {flujo_total})

