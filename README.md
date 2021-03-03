# Resharer

> A small utility for automating of photo converting and resharing.

## Description

This small tool enables me to convert HEIC photos into JPEG.

## Installation

All that's needed to install resharer is to download the source code from github and do following guide:

```
git clone https://github.com/krutijan1/resharer.git
cd resharer
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

Now you are able to run the program by python main.py command, inside your virtual environment.


## Available Commands

Resharer supports several commands, each accessible through the `python main.py` command. For help on individual commands, add `--help` following the command name. The commands are:

### `converter`

Converts HEIC files from local folder to local folder into JPEGs.
