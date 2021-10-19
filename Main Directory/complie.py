import subprocess

list_file = subprocess.run(["ls","-l"])
print("The exit code was: %d" % list_file.returncode)
