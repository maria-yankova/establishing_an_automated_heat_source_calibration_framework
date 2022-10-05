- This repository contains the core code used in the paper "Establishing an automated heat source calibration framework", Rissaki et al, 2023

- There are two codes in this repository. The 'efficiency.ipynb' code refers to the automatic efficiency determination process. The 'heat_source_parameters.ipynb' code refers to the automatic heat source radii determination.

- In this study (Rissaki et al 2023), the program that was used to run simulations for the heat source calibration was FEAT-WMT. In case of another program used for simulations, the code should be modified according to the format of output files.

- The many simulations of this study were run automatically with a shell script in Manchester University computational shared facility. The core code of the shell script consisted of a for loop and a 'sed' command which replaced a line of a file with another line, so to change a variable value as desired.

- For more information and any question please contact Dimitra Rissaki via email: dimrissaki@gmail.com


Wish you a nice day :)


## Instructions to use the demo Jupyter notebooks:

1) Clone this repository
2) Activate a new Python 3 virtual environment from the root of the cloned repository with:

    python -m venv <venv-name>

3) Activate the environment – see Python 3 documentation based on your operating system (https://docs.python.org/3/tutorial/venv.html)
4) Install the required packages using:

    python -m pip install -r requirements.txt

5) Start Jupyter with the command: 

	jupyter notebook

