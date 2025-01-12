import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
from rclpy.qos import QoSProfile

class talkerPublisher(Node):
    def __init__(self):
        super().__init__('talker_publisher')
        # Create a QoS profile for the subscription
        qos_profile = QoSProfile(depth=10)

        self.publisher = self.create_publisher(AckermannDriveStamped, 'ROS2_rive', qos_profile)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.v = 0.0
        self.d = 0.0
    def timer_callback(self):
        if (self.d < 120):
            msg = AckermannDriveStamped()
            msg.drive.speed = self.v * 3
            msg.drive.steering_angle = self.d * 3
            self.publisher.publish(msg)
            self.get_logger().info('Talker saying: speed = "%f"' %msg.drive.speed + 'and steering angle = "%f"' %msg.drive.steering_angle)
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

