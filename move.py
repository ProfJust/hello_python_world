#!/usr/bin/env python
# --- move.py ------
# Version vom 17.09.2018 by OJ
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class TurtleClass:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

	# Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',  Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
	
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
	

    def euclidean_distance(self, x, y):
        """Euclidean distance between current pose and (x,y)."""
        return sqrt(pow((x - self.pose.x), 2) +
                    pow((y - self.pose.y), 2))

    def way2goX(self, start_x, dist_x):
	return abs(start_x + dist_x - self.pose.x)


    def move(self):
        """Moves the turtle ."""
              
        # Get the input from the user.
        dist_x = input("Set your x dist: ")
        #dist_y = input("Set your y dist: ")

 	# Get start Position of Turtle - meanwhile received?
        start_x = self.pose.x
        start_y = self.pose.y

        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        #dist_tolerance = input("Set your tolerance: ")
	rospy.loginfo("Start Pose is %s %s", start_x, start_y)
 	rospy.loginfo("Way to Go %s ", abs( dist_x ))

        vel_msg = Twist()

        while abs(start_x - self.pose.x) < dist_x:

            # Linear velocity in the x-axis.
            vel_msg.linear.x = 0.2
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0

	    rospy.loginfo("Pose is %s %s", self.pose.x, self.pose.y)
 	    rospy.loginfo("Still to Go %s ", dist_x -abs(start_x - self.pose.x)  )

            #if dist_y - self.pose.y > 0:
           # 	vel_msg.angular.z = 0.1
	    #else:
		#vel_msg.angular.z = -0.1

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        # If we press control + C, the node will stop.
        rospy.spin()

if __name__ == '__main__':
    try:
        turtle1 = TurtleClass()
        turtle1.move()
    except rospy.ROSInterruptException:
        pass


