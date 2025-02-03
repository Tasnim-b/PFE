#! /usr/bin/python3

# Python 2/3 compatibility imports
from __future__ import print_function
from six.moves import input

#Include the necessary libraries 
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib

try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi
    
    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

class MyRobot:

    # Default Constructor
    def __init__(self, Group_Name):

        #Initialize the moveit_commander and rospy node
        self._commander = moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('node_set_predefined_pose', anonymous=True)

        
        #Instantiate a RobotCommander object. This object is the outer-level interface to the robot
        self._robot = moveit_commander.RobotCommander()
        #Instantiate a PlanningSceneInterface object. This object is an interface to the world surrounding the robot.
        self._scene = moveit_commander.PlanningSceneInterface()
        
        #define the movegoup for the robotic 
        #Move group name is taken as input when initializing an object from the MyRobot Class
        self._planning_group = Group_Name
        #Instantiate a MoveGroupCommander Object. This Object is an interface to the one group of joints. this interface can be used to plan and execute the motions on the robotic arm
        self._group = moveit_commander.MoveGroupCommander(self._planning_group)
        
        #Create a DisplayTrajectory ROS publisher which is used to display trajectories in Rviz
        self._display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

        #Create action client for the "Execute Trajectory" action server
        self._exectute_trajectory_client = actionlib.SimpleActionClient('execute_trajectory', moveit_msgs.msg.ExecuteTrajectoryAction)
        self._exectute_trajectory_client.wait_for_server()

        #Get the planning frame, end effector link and the robot group names
        self._planning_frame = self._group.get_planning_frame()
        self._eef_link = self._group.get_end_effector_link()
        self._group_names = self._robot.get_group_names()

#juste pour la verification du compilation 
       
        rospy.loginfo('\033[95m' + "Planning Group: {}".format(self._planning_frame) + '\033[0m')
        rospy.loginfo('\033[95m' + "End Effector Link: {}".format(self._eef_link) + '\033[0m')
        rospy.loginfo('\033[95m' + "Group Names: {}".format(self._group_names) + '\033[0m')
        rospy.loginfo('\033[95m' + " >>> MyRobot initialization is done." + '\033[0m')

    def set_pose(self, arg_pose_name):
        rospy.loginfo('\033[32m' + "Going to Pose: {}".format(arg_pose_name) + '\033[0m')
        


        #Set the predefined position as the named joint configuration as the goal to plan for the move group. The predefined positions are defined in the Moveit Setup Assistant
        self._group.set_named_target(arg_pose_name)
        
        #Plan to the desired joint-space goal using the default planner
        plan_success, plan, planning_time, error_code = self._group.plan()
        
        #Create a goal message object for the action server
        goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
        #Update the trajectory in the goal message
        goal.trajectory = plan
        #Send the goal to the action server
        self._exectute_trajectory_client.send_goal(goal)
        self._exectute_trajectory_client.wait_for_result()
        #Print the current pose pour la vérification aussi
        rospy.loginfo('\033[32m' + "Now at Pose: {}".format(arg_pose_name) + '\033[0m')
    

    # Class Destructor
    def __del__(self):
        #When the actions are finished, shut down the moveit commander
        moveit_commander.roscpp_shutdown()
        #vérif aussi
        rospy.loginfo(
            '\033[95m' + "Object of class MyRobot Deleted." + '\033[0m')


def main():
    hand =  MyRobot("hand")
    #Create a new arm object from the MyRobot class
    arm = MyRobot("arm_group")
   
    
    #call the function to set the position to "initial_pose"
    arm.set_pose("initial-pose")
    #Wait for 2 seconds
    rospy.sleep(1)
    
   
    #Here, we will repeat the cycle of setting to various positions
    while not rospy.is_shutdown():
    
  
        #Go to soudure-pose
        arm.set_pose("soudure-pose")
        rospy.sleep(1)
        
    	#Go to transmission-pose
        arm.set_pose("transmission-pose")
        rospy.sleep(1)
        
        #Go to third-transmission-pose
        arm.set_pose("third-trasmission-pose")
        rospy.sleep(1)
        
        #Go to final-pose
        arm.set_pose("final-pose")
        rospy.sleep(1)

    #delete the arm object at the end of code
    del arm
    del hand

if __name__ == '__main__':
    main()



