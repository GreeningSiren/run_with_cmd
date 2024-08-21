# Run with CMD
## This program only works on Windows
## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/) (version 3.7 or later)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
- [Git](https://git-scm.com/) (for version control)
- [PyInstaller](https://www.pyinstaller.org/) (for building the executable)

## Getting Started

### 1. Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/GreeningSiren/run_with_cmd.git
cd run_with_cmd
```

### 2. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 3. Running the Application
To run the application you need to give it an argument to specify the command that needs to be run:
```bash
python run_with_cmd.py "command"
```
As an example:
```bash
python run_with_cmd.py "echo Test!"
```

### 4. Build Executable (Optional)
Install PyInstaller if you haven't already:
```bash
pip install pyinstaller
```
Once all dependencies are installed, you can build an executable from your Python script. Assuming your main Python file is named main.py, run the following command:
```bash
pyinstaller --onefile run_with_cmd.py
```
--onefile: This option tells PyInstaller to bundle everything into a single executable file.

After the build process completes, you can find the executable in the dist directory within the project folder.

### 5. Run the Executable
To run the executable you need to give it an argument to specify the command that needs to be run:
```bash
.\dist\run_with_cmd.exe "command"
```
As an example:
```bash
.\dist\run_with_cmd.exe "echo Test!"
```
