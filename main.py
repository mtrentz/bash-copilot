#!/usr/bin/python3
from uuid import uuid4
import subprocess
import os

# Create hidden out dir if not exists in user home
out = f"{os.path.expanduser('~')}/.bcp"

if not os.path.exists(out):
    os.makedirs(out)

uuid = uuid4()
script = f"{out}/{uuid}.sh"

# Create script with a comment as indication of type
with open(script, "w+") as f:
    f.write("#!/bin/bash")
    f.write("\n")
    f.write("# Execute bash terminal command to  ")

# Open file with cursor at the end of the file and insert mode
subprocess.run(["nvim", "-c", "normal G$", "+startinsert", script])
subprocess.run(["chmod", "+x", script])
subprocess.run(["bash", script])
