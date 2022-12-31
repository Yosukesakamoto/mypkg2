import rclpy                     
from rclpy.node import Node      
from std_msgs.msg import Int16
        
rclpy.init()
node = Node("talker")
srv = node.create_service(Int16, "countup", 10)
n = 0            
