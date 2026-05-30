#!/usr/bin/env bash
set -e

echo "==== System ===="
lsb_release -a
uname -m

echo
echo "==== ROS 2 ===="
echo "ROS_DISTRO=$ROS_DISTRO"
which ros2
ros2 --help > /dev/null
echo "ros2 command: OK"

echo
echo "==== colcon ===="
which colcon
colcon --help > /dev/null
echo "colcon command: OK"

echo
echo "==== Workspace ===="
cd ~/ros2_ws
pwd
git status --short
