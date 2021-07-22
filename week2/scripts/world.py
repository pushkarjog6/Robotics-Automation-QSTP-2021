#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def world():
    pub = rospy.Publisher('world', String, queue_size=10)
    rospy.init_node('world',anonymous=True)
    rate=rospy.Rate(0.5)
    world_str = "World!"
    while not rospy.is_shutdown():
        rospy.loginfo(world_str)
        pub.publish(world_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        world()
    except rospy.ROSInterruptException:
        pass
