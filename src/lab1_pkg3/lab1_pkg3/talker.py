import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
from rclpy.qos import QoSProfile

class talkerPublisher(Node):
    def __init__(self):
        super().__init__('talker_publisher')
        # Create a QoS profile for the subscription
        qos_profile = QoSProfile(depth=10)

        self.publisher = self.create_publisher(AckermannDriveStamped, 'ROS2_Drive', qos_profile)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.v = self.declare_parameter('speed', 0.0).get_parameter_value().double_value
        self.d = self.declare_parameter('steering_angle', 0.0).get_parameter_value().double_value
    def timer_callback(self):
        if (self.d < 120):
            msg = AckermannDriveStamped()
            msg.drive.speed = self.v 
            msg.drive.steering_angle = self.d
            self.publisher.publish(msg)
            self.get_logger().info('Talker saying: speed = "%.2f"' %msg.drive.speed
                            + 'and steering angle = "%.2f"\n' %msg.drive.steering_angle)
            self.v += 2
            self.d += 1

def main(args=None):
    rclpy.init(args=None)
    talker = talkerPublisher()
    rclpy.spin(talker)


    talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

