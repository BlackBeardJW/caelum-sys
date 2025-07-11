import sys
from .core_actions import do

def main():
    if len(sys.argv) < 2:
        print("Usage: caelum-sys \"<command>\"")
        return
    command = " ".join(sys.argv[1:])
    do(command)
