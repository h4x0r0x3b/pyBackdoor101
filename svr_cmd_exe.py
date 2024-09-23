import subprocess

# call method returns nothing like void
# use check_output method to store the returned value in output variable

output = subprocess.check_output("pwd", shell = True)
print(output, "<-- directory")

# convert output bytes to strings and remove newline
print(output.decode("utf-8").replace("\n",""), "<-- directory")
