# 🐢 Turtle Regulation - ROS2 Project

## 📌 Description

Ce projet a été réalisé avec ROS2 et le simulateur turtlesim.

L'objectif est de :
- contrôler le mouvement d’une tortue avec une régulation proportionnelle
- utiliser un service pour définir un waypoint
- créer un client qui envoie des coordonnées
- faire déplacer la tortue pour tracer un carré

---

## 📁 Structure du projet

Le projet contient deux packages :

- turtle_interfaces → contient le service SetWayPoint.srv  
- turtle_regulation_Luidjy → contient les noeuds (régulation + client)

---

## ⚙️ Installation

### 1️⃣ Créer un workspace ROS2

```bash
mkdir -p ~/ros2_workspace
cd ~/ros2_workspace

### 2️⃣ Cloner le projet

- git clone https://github.com/Luidjy-Tody/turtle_regulation_Luidjy.git

### 3️⃣ Renommer le dossier en src

- mv turtle_regulation_Luidjy src

### 4️⃣ Compiler le projet

- colcon build

### 5️⃣ Sourcer le workspace

- source install/setup.bash

## 🚀 Exécution

Terminal 1 : lancer turtlesim:

- ros2 run turtlesim turtlesim_node

Terminal 2 : lancer le noeud de régulation:

- ros2 run turtle_regulation_Luidjy set_way_point

Terminal 3 : lancer le client:

- ros2 run turtle_regulation_Luidjy set_waypoint_client

## 🎯 Fonctionnement

Le client envoie des coordonnées (waypoints)
Le service met à jour la position cible
La tortue se déplace vers chaque point
La tortue trace un carré en suivant les différents points

## 🧠 Concepts utilisés

ROS2 Node
Publisher / Subscriber
Service / Client
Régulation proportionnelle (Kp)
Simulation avec turtlesim

## ✅ Résultat attendu

La tortue se déplace automatiquement et trace un carré.
