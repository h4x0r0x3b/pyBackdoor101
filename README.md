<h2 align="center">Introduction to subprocess module</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

- - - - - - - - - - - - - - - - - - - - - -
- [Introduction to subprocess module](#introduction-to-subprocess-module)
- [Saving result of command execution](#saving-result-of-command-execution)
- [Simplify the command execution](#simplify-the-command-execution)
---
#### Introduction to subprocess module

> [intro.py](intro.py)
```python
import subprocess

# call method for whoami command (user)
# shell = True is optional argument, if to be executed in shell command prompt
subprocess.call("whoami", shell = True)

# dir command (directory)
subprocess.call("dir", shell = True)
```
---
#### Saving result of command execution

> [svr_cmd_exe.py](svr_cmd_exe.py)
```python
import subprocess

# call method returns nothing like void
# use check_output method to store the returned value in output variable

output = subprocess.check_output("pwd", shell = True)
print(output, "<-- directory")

# convert output bytes to strings and remove newline
print(output.decode("utf-8").replace("\n",""), "<-- directory")
```
---
#### Simplify the command execution

> [simplified_cmd_exe.py](simplified_cmd_exe.py)
```python
import subprocess

output = subprocess.check_output("pwd", shell = True).decode("utf-8").replace("\n","")
print(output, "<-- directory")
```