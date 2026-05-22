import numpy as np
import matplotlib.pyplot as plt

g = 9.81
k = 0.1
m = 1.0
v0 = 30.0
theta = np.pi / 4
dt = 0.01

# No drag — while loop version
x_nd = np.array([0.0])
y_nd = np.array([0.0])
vx_nd = v0 * np.cos(theta)
vy_nd = v0 * np.sin(theta)
speed_nd = np.array([v0])

while y_nd[-1] >= 0:
    vx_nd = vx_nd                    # no drag → vx constant
    vy_nd = vy_nd - g * dt           # gravity only
    x_nd = np.append(x_nd, x_nd[-1] + vx_nd * dt)
    y_nd = np.append(y_nd, y_nd[-1] + vy_nd * dt)
    speed_nd = np.append(speed_nd, np.sqrt(vx_nd**2 + vy_nd**2))


#Drag - while loop version
x_d = np.array([0.0])
y_d = np.array([0.0])
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)
speed_d = np.array([v0])

while y_d[-1] >= 0 :
    vx = vx - (k/m) * vx * dt        # vx reduces every step
    vy = vy - g*dt - (k/m)*vy*dt     # vy has both gravity and drag
    x_d =  np.append(x_d,x_d[-1] + vx*dt)
    y_d = np.append(y_d, y_d[-1] + vy*dt)
    speed_d = np.append(speed_d, np.sqrt(vx**2 + vy**2))


plt.figure(figsize=(6, 5))
plt.plot(x_nd, y_nd, label='No drag')   
plt.plot(x_d, y_d, label = 'Drag')
plt.title('Path of projectile')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.tight_layout()
plt.savefig('projectile_path.png', dpi=150)
plt.show()


t_nd = np.arange(len(speed_nd)) * dt
t_d  = np.arange(len(speed_d))  * dt

plt.figure(figsize=(6, 5))
plt.plot(t_nd, speed_nd, label='No drag')
plt.plot(t_d,  speed_d,  label='Drag')
plt.title('Speed over time')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.legend()
plt.tight_layout()
plt.savefig('speed_plot.png', dpi=150)
plt.show()


print("No drag — max height:", round(np.max(y_nd), 2), "m")
print("No drag — range:     ", round(np.max(x_nd), 2), "m")
print("Drag   — max height:", round(np.max(y_d), 2), "m")
print("Drag   — range:     ", round(np.max(x_d), 2), "m")