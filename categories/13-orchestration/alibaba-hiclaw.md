> https://github.com/alibaba/hiclaw

# HiClaw (1,541 stars)

## Problem & Solution
A single Agent struggles to handle complex tasks and lacks collaboration and supervision mechanisms. HiClaw builds an Agent Teams system on top of OpenClaw, where a Manager Agent coordinates multiple Worker Agents, enabling visual collaboration and human intervention in Matrix IM, solving the problems of task division and supervision for complex workflows.

## Key Features
- Manager Agent acts as an AI director, creating Workers, assigning tasks, and monitoring progress
- All communication occurs in Matrix Rooms, allowing users to intervene at any time
- Security design: Workers only hold consumer tokens; real credentials are managed by the Higress AI Gateway
- One-click installation script with built-in Matrix server, file storage, and web client
- Supports pulling 80,000+ community skills from skills.sh
- Periodic heartbeat monitoring with automatic alerts when Workers get stuck
- Supports CoPaw Workers (80% memory reduction, local browser automation)
