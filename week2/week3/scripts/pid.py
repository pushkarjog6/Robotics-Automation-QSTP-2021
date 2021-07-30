#!/usr/bin/env python3

import sys
from math import pi,atan2,sqrt
import rospy
from nav_msgs.msg import Path,Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion


class controller():

    def __init__(self,path_topic):
        rospy.init_node("pid")
        self.i=0
        self.j=0
        self.x=self.y=self.yaw=0
        self.kp1=0.2
        self.kp2=0.5

        self.path_topic=path_topic
        self.pub=rospy.Publisher('cmd_vel',Twist,queue_size=0)
        rospy.Subscriber(self.path_topic,Path,self.callback)
        rospy.spin()


    def callback(self,data):
        rospy.Subscriber("odom",Odometry,self.callback2)
        self.px=data.poses[self.i].pose.position.x
        self.py=data.poses[self.i].pose.position.y
        #e1=round(sqrt((self.y-self.py)**2 + (self.x-self.px)**2),2)
        theta=atan2(self.py-self.y,self.px-self.x)
        #e2=round(theta-self.yaw,2)
        e1=sqrt((self.y-self.py)**2 + (self.x-self.px)**2)
        e2=theta-self.yaw
        while e2>pi:
            e2=e2-(2*pi)
        while e2<(-1*pi):
            e2=e2+(2*pi)
        """if e2>pi:
            e2-=2*pi
        if e2<(-1*pi):
            e2+=2*pi
            """

        vl=self.kp1*e1
        va=self.kp2*e2
        if vl>0.2:
            vl=0.2
        if va>2.5:
            va=2
        v=Twist()
        v.linear.x=vl
        v.angular.z=va
        self.pub.publish(v)
        print(self.i)
        print(e1)
        print(e2*180/pi)

        if self.j==1:

            self.j=0

        if round(e1,1)==0:
            v.linear.x=0
            v.angular.z=0
            self.pub.publish(v)
            self.j=1
            if self.i==(len(data.poses)-1):
                rospy.signal_shutdown('successful')
            else:
                self.i+=1

    def callback2(self,data):
        self.x=data.pose.pose.position.x
        self.y=data.pose.pose.position.y
        orientation=data.pose.pose.orientation
        orientation_list=[orientation.x,orientation.y,orientation.z,orientation.w]
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
        data2=euler_from_quaternion(orientation_list)
        self.yaw=yaw


def usage():
     return "please enter path as path1,path2,path3"
"""
if len(sys.argv) == 2:
    path_topic = sys.argv[1]
else:
    print(usage())
    sys.exit(1)
"""
path_topic = sys.argv[1]
c1=controller(path_topic)
