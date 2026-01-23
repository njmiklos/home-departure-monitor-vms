# Home Departure Monitor for Verkehrsverbund Mittelsachsen
> 🚧 **Project status:** Early development
## Description
The idea is to create Raspberry Pi–powered home display that shows the next departures for selected public transport stops in the VMS ([Verkehrsverbund Mittelsachsen](https://www.vms.de/)) region. The monitor should render a departure-board style view of planned and actual departures of nearby stops.

My motivation is to create a small but complete IT project that combines backend systems and a user-facing output as a learning exercise and to demonstrate real-world, end-to-end problem solving.
## High-Level Flow
1. Fetch & cache the static schedule data
2. Parse the cached GTFS tables (stops, trips, stop_times, calendar)
3. Find "next departures" for configured stop(s)
4. Render the screen output (e-ink or LCD)
5. Refresh the output on a defined interval by repeating the steps 1-5.
# Usage Instructions
## 1. Download this Repository
- Follow the [GitHub documentation](https://docs.github.com/en/get-started/start-your-journey/downloading-files-from-github)
## 2. Install Dependencies
There are a couple of libraries used in this project. You'll need them to run the scripts.
1. Make sure you have Python installed with `python --version` or `python3 --version` for higher versions. If no specific version is shown, e.g., `Python 3.10.12`, you need to install Python.
2. a. Optional, recommended: Create a virtual environment.  
    If you're not familiar with virtual environments, here's a quick guide: A virtual environment is like a container for your Python project. It keeps the packages you install (typically with `pip`) isolated from the rest of your system (or more precisely: your system's global Python environment). This helps prevent conflicts (you might need different versions of the same package across projects) and avoids clutter (when you delete the environment, all its packages are removed too).
- Choose where to store your environments. I like having a dedicated `venvs` directory in my home folder, which you can also create: `mkdir ~/venvs`.
- Create a virtual environment in the directory called `departuremonitor` (you can choose a different name, it is only meant to mean something to you because you will be using it): `python3 -m venv ~/venvs/departuremonitor`. To work in it, you need to activate it: `source ~/venvs/departuremonitor/bin/activate`. You can see if the environment is active if its name is in the parentheses in front of you username in the terminal, e.g., `(departuremonitor) user@hostname:~$`. When you are done working in the environment, deactivate it with `deactivate` (`(departuremonitor)` will vanish).
3. b. Activate the virtual environment.
4. Optional, recommended: Upgrade pip with `pip install --upgrade pip` within the virtual environment.
5. Navigate to the project's root directory: `cd home-departure-monitor-vms`.
6. Install all required packages within the virtual environment: `pip install -r requirements.txt`.
7. Optional, recommended: Verify the installation by listing all packages within the virtual environment: `pip list`. The list should match the content of `requirements.txt`.
## 3. Create an `.env` File
To run the scripts, you must create a `.env` file with environment variables for your private paths and the selected public stops. The `.env` file is not included in this repository to protect your privacy and security.
### `.env` File Example
```
# Directory Paths
BASE_PATH=/your-path-to-repository/home-departure-monitor-vms/
INPUT_PATH=/your-path-to-repository/home-departure-monitor-vms/input/
OUTPUT_PATH=/your-path-to-repository/home-departure-monitor-vms/output/

# Selected Stops
STOP_1 = ...
STOP_2 = ...
```
### Explanation of Variables in the .env File
- `BASE_PATH`: Directory containing all Python files for this project.
- `INPUT_PATH`: Directory containing cached schedules. To explain, public transportation schedules are saved to static CSV files in an open-source, international format [GTFS](https://gtfs.org/). The schedules of VMS are published on their website in the [download section](https://www.vms.de/vms/service/downloads/), and updated weekly.
- `OUTPUT_PATH`: Directory for storing all output files, if necessary.
- `STOP_x`: The variable referring to the stops of your interest, where x is an ordinal number. Select as many stops as you wish by adding more than listed.
## 4. Run Scripts
> ⚠️ **Note:** If you work with a virtual environment, make sure that it is active.
1. Write your own `main.py` and import necessary scripts or adjust an existing main code accordingly. You can add or remove variables in the *.env file.
2. Set your working directory to `BASE_PATH` (`your-path-to-repository/home-departure-monitor-vms/`, based on #4).
- Open your terminal in `BASE_PATH` or run `cd /your-path-to-repository/home-departure-monitor-vms/` to change to it.
3. Invoke the script as a module Run: `python3 -m subdirectory.module-name`.
- Omit the `.py` extension.
- Mind `.` instead of `/` between the directory and module name.
- For top-level scripts (placed directly in `src/`), there is no subdirectory, so simply run: `python3 -m module-name`.
    _Example_: If I wanted to run `home-departure-monitor-vms/inference/classify.py`, I would run: `python3 -m inference.classify`.
# Milestones
## Planned
1. Display in the command line next departures for a single stop based on the static schedules.
2. Display in the command line next departures for multiple stops based on the static schedules.
3. Render the next departures on a monitor.
4. Implement the real-time departures.
5. Robust caching strategy of the GTFS data.
## Implemented
- (none yet)
# License
The repository is licensed under the MIT License. In short, this means:
- I retain ownership of the code, but you can use it freely under the MIT terms, and mine.
- If you find it helpful and use it in your work, a shoutout or reference would be appreciated 🙂