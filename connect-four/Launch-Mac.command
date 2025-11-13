#!/bin/bash
# Launch-Mac.command
cd "$(dirname "$0")"
if [ ! -f "ConnectFourCLI.class" ]; then
  javac ConnectFourCLI.java || { read -p "Compilation failed. Press Enter."; exit 1; }
fi
java ConnectFourCLI --time 12 --ai-first true --ansi true --anim true --anim-delay 40
read -p "Press Enter to exit..."