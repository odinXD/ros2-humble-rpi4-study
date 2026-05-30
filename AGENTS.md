# AGENTS.md

## Project Overview

This repository is a ROS 2 Humble beginner study and portfolio project running on a Raspberry Pi 4B.

The goal is to learn ROS 2 fundamentals, follow the official ROS 2 Humble tutorials, document the learning process, and maintain the repository in a portfolio-friendly structure.

## Environment

- Target device: Raspberry Pi 4B
- Target OS: Ubuntu Desktop 22.04 LTS 64-bit
- ROS distribution: ROS 2 Humble
- Workspace path on Raspberry Pi: `~/ros2_ws`
- Remote access: Tailscale, SSH, VSCode Remote

## Important Workflow

The actual ROS 2 runtime environment is the Raspberry Pi.

Codex may be used from a Windows development machine, but build and runtime results must not be assumed unless the user explicitly provides terminal output from the Raspberry Pi.

Preferred workflow:

1. Modify documentation, scripts, or source code in the Git repository.
2. Commit changes in small meaningful units.
3. Push changes to GitHub.
4. Pull changes on the Raspberry Pi.
5. Run `colcon build --symlink-install` on the Raspberry Pi.
6. Run ROS 2 commands on the Raspberry Pi.
7. Record results in `notes/`.

## Repository Policy

Track:

- `src/`
- `notes/`
- `scripts/`
- `README.md`
- `AGENTS.md`
- `.gitignore`

Do not track:

- `build/`
- `install/`
- `log/`
- cache files
- temporary files

## Documentation Style

Write learning notes in Korean.

Each topic note should include:

- 학습 목표
- 핵심 개념
- 사용한 명령어
- 실행 결과 요약
- 에러 및 해결
- 회의/보고용 요약

Do not copy official documentation directly. Summarize concepts in a project-oriented style.

## Git Commit Style

Use small and meaningful commits.

Examples:

- `docs: add ROS 2 environment setup notes`
- `docs: summarize node and topic concepts`
- `scripts: add workspace build script`
- `feat: add simple C++ publisher`
- `feat: add simple Python listener`

## Current Status

Completed:

- Raspberry Pi 4B Ubuntu Desktop setup
- Tailscale, SSH, VSCode Remote setup
- ROS 2 Humble installation
- rviz2 installation
- `demo_nodes_cpp` and `demo_nodes_py` installation
- talker/listener pub-sub test
- `~/ros2_ws` workspace creation
- Git initialization
- README and `.gitignore` commits

Next steps:

1. Create setup and meeting notes.
2. Connect GitHub remote repository.
3. Start ROS 2 CLI tutorials: nodes, topics, services, parameters, actions.
4. Create simple C++ and Python ROS 2 packages.