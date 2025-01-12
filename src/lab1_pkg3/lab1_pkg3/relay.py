import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
from rclpy.qos import QoSProfile

class relayPublisher(Node):
    def __init__(self):
        super().__init__('relay_publisher')
        qos_profile = QoSProfile(depth=10)
        self.subscription = self.create_subscription(AckermannDriveStamped,'ROS2_Drive', self.listener_callback , qos_profile)
        self.subscription 
    def listener_callback(self, msg):
        
        self.get_logger().info('Relay info: speed = "%.2f"' %(msg.drive.speed *3)
                                + ' and steering angle = "%.2f"\n' %(msg.drive.steering_angle*3))
                               
def main(args=None):
    rclpy.init(args=None)

    relay = relayPublisher()

    rclpy.spin(relay)

    rclpy.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()


