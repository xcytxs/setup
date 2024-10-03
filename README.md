xcytos-setup Documentation
Overview
xcytos-setup is an automated setup tool designed to streamline the process of configuring a Python-based application. It ensures that all necessary dependencies are installed, validates Python availability, and manages basic configurations like ports, usernames, and passwords. The tool also assists with setting up the environment and identifying missing dependencies.

Features
1. Python Verification
Description: Ensures that Python is installed and available in the system. This step is critical to ensure the script and any associated Python files can be executed.
Functionality: It runs the python --version command to check if Python is properly installed.
Purpose: To verify the presence of Python before continuing with other setup steps.
2. Requirements Installation
Description: Installs Python dependencies listed in a requirements.txt file if it is present in the project directory.
Functionality: The tool looks for a requirements.txt file and runs pip install -r requirements.txt to install all necessary libraries.
Purpose: Ensures that all Python libraries required by the project are installed, making it ready to run the application.
3. Dependency Discovery
Description: Analyzes Python files in the current directory to identify any imported modules that might be missing from the system.
Functionality: The tool parses all .py files in the current project directory, extracting imported modules. It then checks if they are installed and prompts the user to install them if necessary.
Purpose: To help identify any missing dependencies that may not be covered in the requirements.txt.
4. Port Handling
Description: Allows the user to specify the ports for various services like a web application or admin interface.
Functionality: The tool prompts the user for port numbers, ensuring that the selected ports are not already in use by other processes on the system. It checks the availability of the specified ports.
Purpose: Ensures that the necessary services can be bound to the specified ports without conflicts.
5. User Input (Username and Password)
Description: Prompts the user to specify a username and password.
Functionality: If not provided via the command line, the tool will ask the user to input these values interactively.
Purpose: Configures credentials for services that require authentication.
Command-Line Arguments
The xcytos-setup script accepts the following command-line arguments:

--port: Specifies the ports to be used for services (e.g., main, admin). If not specified, the tool will prompt the user interactively.
--services: Specifies the names of the services for which ports are being set up. For example, main, admin. Must be specified if --port is used.
--username: Specifies a username for the application or services.
--password: Specifies a password for the application or services.
Example Usage
To run the xcytos-setup with basic parameters:

bash
Copy code
python xcytos-setup.py --port 8000 --services main admin --username admin --password admin
This will:
Set up the main service on port 8000.
Set up the admin service on the next available port.
Use admin as the username and admin as the password for the services.
If any arguments are omitted, the script will prompt the user interactively.

Example with Default Port Setup
If you do not want to specify ports manually:

bash
Copy code
python xcytos-setup.py --services main admin
This will:
Prompt the user to choose available ports for the main and admin services.
The tool will handle port selection and validation.
How It Works
Steps Performed by xcytos-setup
Python Verification: Ensures Python is installed by running sys.executable --version.
Install Requirements: Checks if requirements.txt exists and installs dependencies using pip.
Find Missing Dependencies: Parses .py files in the project directory to identify any libraries used but not installed.
Port Handling: If services and ports are specified, the script prompts for the user to assign ports that are not already in use on the system.
User Inputs (Username & Password): Prompts for credentials if not provided as command-line arguments.
Expected File Structure
bash
Copy code
xcytos-setup.py
requirements.txt       # Optional, for listing Python dependencies
config.json            # Configuration file (if needed)
Known Limitations
Currently, xcytos-setup only handles basic Python-based setup tasks. Docker, service configuration, and advanced setups like setting up databases or services are not yet implemented in the current version.
Conclusion
xcytos-setup is a lightweight and flexible tool for ensuring that your Python environment is set up correctly, including dependency management and basic configuration. It reduces the complexity of manual setup by automating key tasks, ensuring you can quickly get up and running with minimal effort.

For more advanced features like Docker or service management, additional functionality can be added as needed.
