#!/usr/bin/env python3

import rospy

class NodeName:         	            # Mudar

    def __init__(self):
        

if __name__ == '__main__':
    try:
        rospy.init_node(node_name)	        # Mudar
        NodeName()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
