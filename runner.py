import subprocess

def coderunnerPython(inputString): 
    runner = subprocess.run(['python3', 'code_to_run.py'], stdout= subprocess.PIPE, stderr=subprocess.PIPE, input = inputString.encode()) #calls a process to run the python3 code
    if(len(runner.stderr)>0):
        return [0,runner.stderr.decode()]
    return [1,runner.stdout.decode()]  #the output from the runner is taken and decoded and returned
