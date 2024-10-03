import os
import sys
import ast
import subprocess
import argparse
import socket

def verify_python_installation():
    try:
        subprocess.run([sys.executable, '--version'], check=True, stdout=subprocess.PIPE)
        print("Python is installed.")
    except subprocess.CalledProcessError:
        print("Python is not installed or not found in the PATH.")
        sys.exit(1)

def install_requirements():
    if os.path.exists('requirements.txt'):
        print("Installing from requirements.txt...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    else:
        print("No requirements.txt found. Skipping dependency installation.")

def find_missing_dependencies():
    print("Checking Python files for missing dependencies...")
    modules = set()
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    tree = ast.parse(f.read(), filename=file)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                modules.add(alias.name)
                        elif isinstance(node, ast.ImportFrom):
                            modules.add(node.module)

    print(f"Modules detected: {modules}")
    return modules

def install_missing(modules):
    for module in modules:
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', module], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to install {module}")

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def choose_port(service_name, default_port):
    while True:
        port = input(f"Enter port to use for {service_name} (default {default_port}): ") or default_port
        if not check_port(int(port)):
            print(f"Port {port} is available for {service_name}")
            return port
        else:
            print(f"Port {port} is in use, try a different one.")

def main():
    verify_python_installation()

    parser = argparse.ArgumentParser(description="Automated setup tool")
    parser.add_argument('--port', nargs='+', type=int, help='Specify ports for the app, separated by space (e.g., main admin)')
    parser.add_argument('--services', nargs='+', type=str, help='Specify service names for ports (e.g., main admin)')
    parser.add_argument('--username', type=str, help='Specify a username')
    parser.add_argument('--password', type=str, help='Specify a password')
    args = parser.parse_args()

    install_requirements()

    missing_modules = find_missing_dependencies()
    install_missing(missing_modules)

    if args.services:
        ports = {}
        for idx, service in enumerate(args.services):
            default_port = 8000 + idx
            if args.port and len(args.port) > idx:
                port = args.port[idx]
            else:
                port = choose_port(service, default_port)
            ports[service] = port
        print(f"Using ports: {ports}")
    else:
        print("No services specified. Exiting.")
        return

    username = args.username or input("Enter username: ")
    password = args.password or input("Enter password: ")
    
    print(f"Configuration complete with ports: {ports}, username: {username}")

if __name__ == "__main__":
    main()
