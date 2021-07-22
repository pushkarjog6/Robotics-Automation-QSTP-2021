#!/usr/bin/env python3

import rospy
from week2.srv import compute_ang_vel,compute_ang_velResponse

def comp(request):
    r=request.r;
    v=0.1 #assumption
    w=v/r
    return compute_ang_velResponse(w)
    print(w)
def server():
    rospy.init_node('angvel')
    print(2)
    s = rospy.Service('compute_ang_vel',compute_ang_vel,comp)
    rospy.spin()

if __name__ == "__main__":
    server()
