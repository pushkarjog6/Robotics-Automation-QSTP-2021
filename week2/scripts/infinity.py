#!/usr/bin/env python3


import rospy

from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from week2.srv import compute_ang_vel

pi=3.14159 #pi


class infinity:
    def __init__(self):
        rospy.init_node('infinity',anonymous=True)
        self.pub=rospy.Publisher('cmd_vel',Twist,queue_size=10)
        rospy.Subscriber('radius',Float64,self.callback)
        rospy.spin()


    def callback(self, data):
        r=data.data
        rospy.wait_for_service('compute_ang_vel')
        angvel = rospy.ServiceProxy('compute_ang_vel',compute_ang_vel)
        w=angvel(r)
        v=Twist()
        v.linear.x=0.1 #assumption/hardcoded
        v.angular.z=w.w
        self.pub.publish(v)
        rospy.sleep(2*pi/w.w) #t=2pi/w
        v.angular.z=w.w*-1
        self.pub.publish(v)
        rospy.sleep(2*pi/w.w) #t=2pi/w


c1=infinity()
