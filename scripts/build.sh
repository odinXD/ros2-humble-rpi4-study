#!/usr/bin/env bash
set -e

cd ~/ros2_ws

source /opt/ros/humble/setup.bash

colcon build --symlink-install

if [ -f install/setup.bash ]; then
  source install/setup.bash
fi

echo "Build completed."
