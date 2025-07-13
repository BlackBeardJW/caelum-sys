"""CaelumSys Command Line Interface"""

import sys

from .core_actions import do


def main():
    """Main entry point for the CaelumSys command-line interface."""
    if len(sys.argv) < 2:
        print('Usage: caelum-sys "<command>"')
        return

    command = " ".join(sys.argv[1:])
    result = do(command)
    print(result)
