#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def radius():
    pub = rospy.Publisher('radius', Float64, queue_size=10)
    rospy.init_node('radius',anonymous=True)
    rate=rospy.Rate(0.5)
    rad = 1
    while not rospy.is_shutdown():
        rospy.loginfo(rad)
        pub.publish(rad)
        rate.sleep()

if __name__ == '__main__':
    try:
        radius()
    except rospy.ROSInterruptException:
        pass
