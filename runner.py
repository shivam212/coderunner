import subprocess

def coderunnerPython(inputString): 
    runner = subprocess.run(['python3', 'code_to_run.py'], stdout= subprocess.PIPE, input = inputString.encode()) #calls a process to run the python3 code
    return runner.stdout.decode()  #the output from the runner is taken and decoded and returned
