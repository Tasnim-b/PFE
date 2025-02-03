
# 🚀 Simulation Mécanique sous ROS Noetic avec Gazebo, MoveIt et RViz


Ce projet consiste en la conception d'un modèle mécanique sous SolidWorks, l'expotation du fichier URDF, et la simulation de ce modèle dans ROS Noetic à l'aide de Gazebo, MoveIt et RViz.

## ⚙️ Prérequis
🔹 Système d'exploitation : Ubuntu 20.04.6 LTS

🔹 Logiciels requis :

- 🛠️ ROS Noetic
- 🏗️ Gazebo : pour la Simulation
- 🎯 MoveIt : pour la planification des mouvements
- 🔍 RViz : pour la Visualisation
- 🎨 SolidWorks : Conception mécanique
- 🚀 sw_urdf_exporter : Plugin SolidWorks pour exporter des modèles en URDF
  
  ## 🖼️ Présentation de la Conception Mécanique
<p align="center">
  <img src="https://github.com/Tasnim-b/PFE/blob/b2475a1bb3d08f9ccdc8586ef9cc966af674bf38/lesImagesDeLaConceptionM%C3%A9caniqueDuSyst%C3%A9me/syst%C3%A8me%20de%20soudure%203.png" alt="Conception Mécanique" />
</p>

## 🚀 Installation & Exécution
📥 1. Cloner le projet
```
git clone https://github.com/Tasnim-b/PFE.git
cd PFE
```
🔧 2. Compiler le projet avec Catkin
```
cd catkin_ws
catkin_make
source devel/setup.bash
````
🏁 3. Lancer ROS Master (roscore)
````
roscore
````
⚠️ Important : Cette commande doit être lancée dans un nouveau terminal avant d'exécuter les autres commandes.

🏗️ 4. Lancer la simulation dans Gazebo et RViz
````
roslaunch moveit_robot_arm_sim full_robot_arm_sim.launch
````
🐍 5. Exécuter le script Python
````
rosrun moveit_robot_arm_sim node_set_prefined_pose.py
````
⚠️ Remarque : Le script Python doit Être exécutable en ajoutant les permissions d'exécution

📽️ Vidéo Démonstration

![Aperçu de la simulation](https://github.com/Tasnim-b/PFE/blob/c0f78f64905c3849697a0b5c918911d4c9cb247e/lesImagesDeLaConceptionM%C3%A9caniqueDuSyst%C3%A9me/vid%C3%A9o-finale.gif)



