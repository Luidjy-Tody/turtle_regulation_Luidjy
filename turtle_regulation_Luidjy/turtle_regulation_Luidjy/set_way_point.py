#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
from std_msgs.msg import Bool
from turtle_interfaces.srv import SetWayPoint as SetWayPointSrv


# (1) Créer un noeud set_way_point.py dans turtle_regulation
class SetWayPoint(Node):
    def __init__(self):
        super().__init__("set_way_point")

        # (2) Créer un attribut pour stocker la pose de la tortue
        self.pose_tortue = None

        # (3) Définir un attribut waypoint avec les coordonnées (7,7)
        self.waypoint_x = 7.0
        self.waypoint_y = 7.0

        # (5) Définir la constante Kp pour la commande proportionnelle
        self.kp = 2.0

        # (2) Souscrire au topic /turtle1/pose de type Pose
        self.subscription = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_callback,
            10
        )

        # (5) Créer un publisher pour publier sur /turtle1/cmd_vel
        self.publisher_cmd = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        # (Partie 2 - 2) Gain linéaire
        self.kpl = 3.0

        # (Partie 2 - 3) Seuil de distance
        self.distance_tolerance = 0.1

        # (Partie 2 - 4) Publisher sur /is_moving
        self.publisher_moving = self.create_publisher(
            Bool,
            "/is_moving",
            10
        )

        # (5) Créer un timer pour exécuter la régulation régulièrement
        self.timer = self.create_timer(0.1, self.control_loop)

        # (Partie 3 - 4) Création du service
        self.service = self.create_service(
            SetWayPointSrv,
            "set_waypoint_service",
            self.set_waypoint_callback
        )

    # (2) Quand on reçoit un message pose, on met à jour l’attribut pose_tortue
    def pose_callback(self, msg):
        self.pose_tortue = msg

    # (4) Calculer l’angle désiré entre la tortue et le waypoint
    def calcul_angle_desire(self):
        if self.pose_tortue is None:
            return None

        xA = self.pose_tortue.x
        yA = self.pose_tortue.y

        xB = self.waypoint_x
        yB = self.waypoint_y

        theta_desired = math.atan2(yB - yA, xB - xA)
        return theta_desired

    # (Partie 2 - 1) Calcul de la distance euclidienne
    def calcul_distance(self):
        if self.pose_tortue is None:
            return None

        xA = self.pose_tortue.x
        yA = self.pose_tortue.y

        xB = self.waypoint_x
        yB = self.waypoint_y

        distance = math.sqrt((xB - xA)**2 + (yB - yA)**2)
        return distance

    # (5) Calculer l’erreur, la commande u, puis publier cmd_vel
    def control_loop(self):
        if self.pose_tortue is None:
            return

        theta_desired = self.calcul_angle_desire()
        theta = self.pose_tortue.theta

        e = 2 * math.atan(math.tan((theta_desired - theta) / 2))
        u = self.kp * e

        # (Partie 2 - 2) Calcul distance
        distance = self.calcul_distance()

        # message booléen pour is_moving
        msg = Bool()

        # (Partie 2 - 3) Si la tortue est proche du waypoint, elle s’arrête
        if distance < self.distance_tolerance:
            cmd = Twist()
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.publisher_cmd.publish(cmd)

            msg.data = False
            self.publisher_moving.publish(msg)
            return

        # (Partie 2 - 2) vitesse linéaire
        v = self.kpl * distance

        cmd = Twist()
        cmd.angular.z = u
        cmd.linear.x = v

        self.publisher_cmd.publish(cmd)

        # (Partie 2 - 4) publier True si la tortue bouge
        msg.data = True
        self.publisher_moving.publish(msg)

    # (Partie 3 - 4) Callback du service
    def set_waypoint_callback(self, request, response):
        self.waypoint_x = request.x
        self.waypoint_y = request.y
        self.get_logger().info(f"Nouveau waypoint: {request.x}, {request.y}")
        response.res = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = SetWayPoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()