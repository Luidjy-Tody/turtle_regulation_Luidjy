#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from turtle_interfaces.srv import SetWayPoint as SetWayPointSrv


class ClientWayPoint(Node):
    def __init__(self):
        super().__init__("client_waypoint")

        # Création du client de service
        self.client = self.create_client(
            SetWayPointSrv,
            "set_waypoint_service"
        )

        # Variable pour savoir si la tortue bouge
        self.is_moving = False

        # Subscriber sur le topic is_moving
        self.subscription = self.create_subscription(
            Bool,
            "/is_moving",
            self.is_moving_callback,
            10
        )

    def is_moving_callback(self, msg):
        self.is_moving = msg.data

    def envoyer_requete(self, x, y):
        # Attendre que le service soit disponible
        self.get_logger().info("En attente du service set_waypoint_service...")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Service non disponible, nouvelle tentative...")

        # Attendre que la tortue soit à l'arrêt avant d'envoyer
        self.get_logger().info("Attente que la tortue s'arrete...")
        while self.is_moving:
            rclpy.spin_once(self)

        # Construire la requête
        request = SetWayPointSrv.Request()
        request.x = x
        request.y = y

        # Envoyer la requête de façon asynchrone
        self.get_logger().info(f"Envoi du waypoint : ({x}, {y})")
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        # Traiter la réponse
        response = future.result()
        if response is not None and response.res:
            self.get_logger().info(f"Succes : waypoint modifie vers ({x}, {y})")
        else:
            self.get_logger().error("Echec : waypoint non modifie")
            return

        # Attendre que la tortue commence à bouger
        while not self.is_moving:
            rclpy.spin_once(self)

        # Attendre qu'elle termine son déplacement
        while self.is_moving:
            rclpy.spin_once(self)


def main(args=None):
    rclpy.init(args=args)
    node = ClientWayPoint()

    # Points du carré envoyés un par un
    node.envoyer_requete(2.0, 2.0)
    node.envoyer_requete(8.0, 2.0)
    node.envoyer_requete(8.0, 8.0)
    node.envoyer_requete(2.0, 8.0)
    node.envoyer_requete(2.0, 2.0)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()