#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def hello():
    pub = rospy.Publisher('hello', String, queue_size=10)
    rospy.init_node('hello',anonymous=True)
    rate=rospy.Rate(0.5)
    hello_str = "Hello,"
    while not rospy.is_shutdown():
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        hello()
    except rospy.ROSInterruptException:
        pass
