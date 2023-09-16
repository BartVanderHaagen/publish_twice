#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(msg):
    # Publish the received message to two different topics
    pub1.publish(msg)
    pub2.publish(msg)

if __name__ == "__main__":
    rospy.init_node("cmd_vel_republisher")

    # Create two publishers for the republished messages
    pub1 = rospy.Publisher("/rear/hoverboard_velocity_controller/cmd_vel", Twist, queue_size=10)
    pub2 = rospy.Publisher("/front/hoverboard_velocity_controller/cmd_vel", Twist, queue_size=10)

    # Subscribe to the /cmd_vel topic
    rospy.Subscriber("/cmd_vel", Twist, cmd_vel_callback)

    rospy.spin()


