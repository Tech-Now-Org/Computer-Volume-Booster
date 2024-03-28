import sys
import subprocess

def run_booster(increase_percent):
    if sys.platform.startswith('win'):
        subprocess.run(['python', 'Windows/Booster.py', str(increase_percent)])
    elif sys.platform == 'darwin':
        subprocess.run(['python', 'MacOs/Booster.py', str(increase_percent)])
    elif sys.platform.startswith('linux'):
        subprocess.run(['python', 'Linux/Booster.py', str(increase_percent)])
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        percentage = float(sys.argv[1])
        run_booster(percentage)
    else:
        print("Usage: python main.py <increase_percent>")
