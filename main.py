# Import uuid generator
from uuid import uuid4
import subprocess

# Execute nvim
uuid = uuid4()
script = f"{uuid}.sh"

# Create script with a comment
with open(script, "w") as f:
    f.write("#!/bin/bash")
    f.write("\n")
    f.write("# Execute bash terminal command to  ")

# Open with cursor at the end of the file
subprocess.run(["nvim", "-c", "normal G$", "+startinsert", script])
subprocess.run(["chmod", "+x", script])
subprocess.run(["bash", script])
