#!/usr/bin/env python3

import rospy
import sys
import matplotlib.pyplot as plt
from week2.srv import trajectory

def client(x,y,theta,v,w):
    rospy.wait_for_service('trajectory')
    try:
        traj = rospy.ServiceProxy('trajectory',trajectory)
        t = traj(x,y,theta,v,w)
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(t.xi, t.yi, color="red", alpha=0.75)
        plt.grid()
        print(1)
        plt.show()
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed : {e}")

def usage():
     return "please enter the arguments"

if __name__ == "__main__":
     if len(sys.argv) == 6:
         x = float(sys.argv[1])
         y = float(sys.argv[2])
         theta = float(sys.argv[3])
         v = float(sys.argv[4])
         w = float(sys.argv[5])
     else:
         print(usage())
         sys.exit(1)
     print("Requesting trajectory")
     client(x,y,theta,v,w)
