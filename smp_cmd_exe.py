import subprocess

output = subprocess.check_output("pwd", shell = True).decode("utf-8").replace("\n","")
print(output, "<-- directory")
