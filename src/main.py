################################################################################
# Author: James A. Chase
# Date: 2026-10-27
# File: main.py
# Description: Main program entry point for the AI Snake game
################################################################################

# imports
from core.engine import Engine

def main() -> None:
    """
    Main Program Entry Point
    """
    e = Engine()
    e.run()
    e.update_high_score()

if __name__ == '__main__':
    main()
