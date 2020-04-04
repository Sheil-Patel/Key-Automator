# Key-Automator

Hello Welcome to key-automator program! In this program you
## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Setup

### Repo-Setup
Use the GitHub.com online interface to create a new remote project repository called something like "robo-advisor". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like `https://github.com/YOUR_USERNAME/key-logger`.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/key-logger
```
### Environment Setup
Use Anaconda to create and activate a new virtual environment, perhaps called "key-env":

```sh
conda create -n key-env python=3.7 # (first time only)
conda activate key-env
```
### Installation of Packages
From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)


## Running the program

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python app/key-automator.py
```

## Stopping Python Scripts

After you run the program, you will see python scripts running in the task manager. After you are done, be sure to deactivate those scripts. 