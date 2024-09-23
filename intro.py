import subprocess

# call method for whoami command (user)
# shell = True is optional argument, if to be executed in shell command prompt
subprocess.call("whoami", shell = True)

# dir command (directory)
subprocess.call("dir", shell = True)
