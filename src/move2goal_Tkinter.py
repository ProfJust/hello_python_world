#!/usr/bin/env python
# --- move2goal_Tkinter.py ------
# Editor Eric
# sudo apt-get install eric
# Version vom 31.10.2018 by OJ
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
from Tkinter import * #python2 Tkinter,  python3 tkinter

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
        self.dist_x=0
        self.dist_y=0

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
	
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)       
        vel_msg = Twist() 
        rospy.loginfo("Callback %s %s ", self.dist_x, self.dist_y)
        if(self.dist_y>0 or self.dist_x>0):
            sollTheta = atan2(self.dist_y,self.dist_x)
            if abs(self.pose.theta - sollTheta) > 0.015:
                #Winkel correction
                if self.pose.theta > math.pi:
                    self.pose.theta=self.pose.theta-2*math.pi
                elif self.pose.theta < -math.pi:
                    self.pose.theta=self.pose.theta+2*math.pi

                # Angular velocity in the z-axis.
                if self.pose.theta - sollTheta > 0:
                    vel_msg.angular.z = -0.1
                else:
                    vel_msg.angular.z = 0.1
                rospy.loginfo("Pose is %s", self.pose.theta)
                rospy.loginfo("Goal pose is %s", sollTheta)
                rospy.loginfo("Still to Go %s ", abs(self.pose.theta - sollTheta))
                # Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)
                # Publish at the desired rate.
                self.rate.sleep()        
            elif sqrt(pow((start_x -self.pose.x),2)+pow((start_y -self.pose.y),2)) < abs(dist):
                # Linear velocity in the x-axis.
                vel_msg.linear.x = 0.2
                rospy.loginfo("Pose is %s %s", self.pose.x, self.pose.y)
                rospy.loginfo("Still to Go %s ", dist-sqrt(pow((start_x -self.pose.x),2)+pow((start_y -self.pose.y),2))  )
                # Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)
                # Publish at the desired rate.
                self.rate.sleep()
            # Stopping our robot after the movement is over.
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)	

    def euclidean_distance(self, x, y):
        """Euclidean distance between current pose and (x,y)."""
        return sqrt(pow((x - self.pose.x), 2) + pow((y - self.pose.y), 2))

    def way2goX(self, start_x, dist_x):
	    return abs(start_x + dist_x - self.pose.x)

    def move(self):
        """Moves the turtle ."""              
        # Get the input from the user.
       # dist_x = input("Set your x dist: ")
        #dist_y = input("Set your y dist: ")
        dist = sqrt(pow(self.dist_x,2)+pow(self.dist_y,2))
        sollTheta = atan2(self.dist_y,self.dist_x)
        self.pose.theta=self.pose.theta-2*math.pi
        # Get start Position of Turtle - meanwhile received?
        start_x = self.pose.x
        start_y = self.pose.y
        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        #dist_tolerance = input("Set your tolerance: ")
        rospy.loginfo("Start Pose is %s %s", start_x, start_y)
        rospy.loginfo("Way to Go %s ", dist)
        rospy.loginfo("Still to Go %s ", abs(self.pose.theta - sollTheta)  )
        # If we press control + C, the node will stop.
       #rospy.spin()

# Klasse definieren 
class Application(Frame):
    #--- Konstruktor ---
    def __init__(self,master=None):
        Frame.__init__(self, master)  #vErerbung von Frame
 	   #--- 3 Label Vorname, Nachname und Ausgabe ---
        Label(master,text="Dist X").grid(row=0)
        Label(master,text="Dist Y").grid(row=1)
        Label(master,text="Die Eingabe").grid(row=2)
      #--- Label mit Bezeichner lbl1 fuer Ausgabe ---
        self.lbl1=Label(master, bg="yellow", fg="blue")
        self.lbl1.grid(row=2, column=1)

      #--- Eingabefelder ---
        self.goalX = Entry(master)
        self.goalY = Entry(master)
        self.goalX.grid(row=0, column=1)
        self.goalY.grid(row=1, column=1)
      
       #--- 2 Buttons OK und Abbrechen ---
        #      Beschriftung, Event-Funktion, Position im Grid
        Button(master,text='GO',width=20,command=self.callback).grid(row=3, column=0)
        Button(master,text='Abbrechen',width=20,command=root.destroy).grid(row=3, column=1)
       
    
    #--- Die Event-Handler-Funktion --
    def callback(self):
        self.lbl1.config(text = 'Dist to Go' + self.goalX.get() + '  '+  self.goalY.get() )
        turtle1.dist_x = float(self.goalX.get()) 
        turtle1.dist_y = float(self.goalY.get())      
        turtle1.move()
        
if __name__ == '__main__':
    try:
        turtle1 = TurtleClass()
	    #Tk Objekt instanzieren
        root=Tk()
        #Application Objekt instanzieren
        app=Application(master=root)
        #Mainloop starten
        app.mainloop()		
    except rospy.ROSInterruptException:
        pass
