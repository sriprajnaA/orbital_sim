import numpy as np
import matplotlib.pyplot as plt
G=6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M=5.972e24     # Mass of Earth in kg
R=6371e3       # Radius of Earth in meters
#innitial position in METERS
x=R+400e3  # 400 km above Earth's surface
y=0
#innitial velocity in METERS PER SECOND
vx=0
vy=7700  # Approximate orbital velocity for low Earth orbit
# Time parameters
dt=1  # Time step in seconds
steps=10000  # Number of simulation steps
for i in range(steps):
    r=(x**2+y**2)**0.5  # Distance from Earth's center, the rootx^2+y^2
    ax=-G*M*x/r**3  # Gravitational acceleration in x direction       # F=GMm/r^2,doesn't give direction
    ay=-G*M*y/r**3  # Gravitational acceleration in y direction       #so, multiply with the unit vector.
    vx=vx+ax*dt  # Update velocity in x direction
    vy=vy+ay*dt  # Update velocity in y direction       # new v is the old v plus the change in v, which is a*dt
    x=x+vx*dt  # Update position in x direction
    y=y+vy*dt  # Update position in y direction
    plt.plot(x, y, 'b.')  # Plot the current position
plt.plot(0, 0, 'ro')  # Plot Earth at the origin
plt.show()