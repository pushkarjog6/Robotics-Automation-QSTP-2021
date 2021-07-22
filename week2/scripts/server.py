#!/usr/bin/env python3

import rospy
import numpy as np
from week2.srv import trajectory, trajectoryResponse

def traj(request):
    x = request.x;
    y = request.y;
    theta = request.theta;
    v = request.v;
    w = request.w;
    dt = 0.05
    n = 50
    x_points = [x]
    y_points = [y]
    for i in range(n):
        x += v*np.cos(theta)*dt
        y += v*np.sin(theta)*dt
        theta += w*dt;
        x_points.append(x)
        y_points.append(y)
    return trajectoryResponse(xi=x_points,yi=y_points)

def server():
    rospy.init_node('server')
    s = rospy.Service('trajectory',trajectory,traj)
    rospy.spin()

if __name__ == "__main__":
    server()
