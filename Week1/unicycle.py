"""Week I Assignment

Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w);
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
"""

import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        """
        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps

        Return:
            x, y, theta (float): final pose
        """

        for i in range(n):
            #To get coordinates
            self.x += v*np.cos(self.theta)*self.dt
            self.y += v*np.sin(self.theta)*self.dt
            self.theta += w*self.dt
            #to store the intermeditate points
            self.x_points.append(self.x)
            self.y_points.append(self.y)
        return self.x, self.y, self.theta, self.theta

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.figure()
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()

        plt.show(block=False) #block=false added to show plots for all objects together

        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        #plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":
    print("Unicycle Model Assignment")


u1=Unicycle(0,0,0,0.1)
u1.step(1,0.5,25)
u1.plot(1,0.5)

u2=Unicycle(0,0,1.57,0.2)
u2.step(0.5,1,10)
u2.plot(0.5,1)

u3=Unicycle(0,0,0.77,0.05)
u3.step(5,4,50)
u3.plot(5,4)

plt.show(block=True) #To display all the plots
