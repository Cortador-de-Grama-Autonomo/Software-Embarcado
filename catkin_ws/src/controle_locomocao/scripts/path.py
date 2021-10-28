#! /usr/bin/env python3
import rospy

from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

def odom_cb(data):
    path.header = data.header
    pose = PoseStamped()
    pose.header = data.header
    pose.pose = data.pose.pose
    path.poses.append(pose)
    path_pub.publish(path)

def main():
    global path
    global path_pub
    path = Path()
    rospy.init_node('path_node')

    odom_sub = rospy.Subscriber('/odom', Odometry, odom_cb)
    path_pub = rospy.Publisher('/path', Path, queue_size=10)
    
    rospy.spin()


if __name__ == '__main__':
    main()