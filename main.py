#!/usr/bin/python3
# Import uuid generator
from uuid import uuid4
import subprocess
import os

# Create out dir if not exists
out = f"{os.path.expanduser('~')}/.bcp"

if not os.path.exists(out):
    os.makedirs(out)

# Execute nvim
uuid = uuid4()
script = f"{out}/{uuid}.sh"

# Create script with a comment
with open(script, "w+") as f:
    f.write("#!/bin/bash")
    f.write("\n")
    f.write("# Execute bash terminal command to  ")

# Open with cursor at the end of the file
subprocess.run(["nvim", "-c", "normal G$", "+startinsert", script])
subprocess.run(["chmod", "+x", script])
subprocess.run(["bash", script])
