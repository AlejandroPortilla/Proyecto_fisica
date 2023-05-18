import numpy as np
import matplotlib.pyplot as plt

# Defino condiciones iniciales
v0 = 60  # m/s
theta = 91/59.2758  # angulo entre 1 radian en grados
g = 9.8  # m/s^2
# Esto tienen que hacerlo para que el usuario puedo meterlo por terminal


#NOtocar formulas numericas porfavor
xm = (v0**2 *np.sin(2*theta) / g)
ym = (v0*np.sin(theta))**2/(2*g)
#ym = 0.5
tv = (2*v0*np.sin(theta)/g)

if(xm>ym):
    escala = xm
else:
    escala = ym

print (tv)
print (xm)
print (ym)
print (escala)
#Crea una lista para almacenar las coordenadas x e y del proyectil
x = []
y = []

# Calcular la posición del proyectil en cada paso de tiempo
for t in np.arange(0, xm, 0.01):
    # Calcular los desplazamientos horizontal y vertical
    x_t = v0 * t * np.cos(theta)
    #x_t = t
    y_t = v0 * t * np.sin(theta) - 0.5 * g * t**2
  
    # Agregue las coordenadas x e y a la lista
    x.append(x_t)
    y.append(y_t)
   
# Traza la trayectoria
plt.xlim([0,escala*1.1])
plt.ylim([0,escala*1.1])
plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()