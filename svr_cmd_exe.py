import subprocess

output = subprocess.check_output("pwd", shell = True)
print(output, "<-- directory")

print(output.decode("utf-8").replace("\n",""), "<-- directory")
