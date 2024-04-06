import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Константы
m_e = 9.1093837 * 10**(-31)  # масса электрона
q_e = 1.6022 * 10**(-19)     # заряд электрона
r_nucleus = 10**(-15)        # радиус ядра атома
q_nucleus = 9.1093837 * 10**(-31) # заряд ядра атома

# Начальные условия для электрона
x0 = 0                # начальная координата x
vx0 = 0               # начальная скорость x
y0 = r_nucleus        # начальная координата y
vy0 = 0               # начальная скорость y

# Функция для решения уравнений движения
def atomic_model(z, t):
    x, vx, y, vy = z
    F = q_e**2 / ((x**2 + y**2)**0.5)
    ax = F * x / m_e
    ay = F * y / m_e
    return vx, ax, vy, ay

# Решение уравнений движения
t = np.linspace(0, 10, 1000) # временной интервал
sol = odeint(atomic_model, (x0, vx0, y0, vy0), t)

# Графическое представление движения электрона
plt.plot(sol[:, 0], sol[:, 2])
plt.axis('equal')
plt.show()