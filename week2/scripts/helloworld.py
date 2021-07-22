#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

s1=s2=""


def callback(data):
    global s1
    s1=data.data
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", s1)


def callback2(data):
    global s2
    s2=data.data
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", s2)
    pub = rospy.Publisher('helloworld', String, queue_size=10)
    pub.publish(s1+" "+s2)

def listener():
    rospy.init_node('helloworld',anonymous=True)
    global s1
    global s2
    rospy.Subscriber("hello",String,callback)
    rospy.Subscriber("world",String,callback2)

    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
