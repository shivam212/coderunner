import subprocess

def coderunnerPython(inputString): 
    runner = subprocess.run(['python3', 'code_to_run.py'], stdout= subprocess.PIPE, stderr=subprocess.PIPE, input = inputString.encode()) #calls a process to run the python3 code
    if(len(runner.stderr)>0):
        return [0,runner.stderr.decode()]
    return [1,runner.stdout.decode()]  #the output from the runner is taken and decoded and returned

def coderunnerCPP(inputString): 
    runnerPrelim = subprocess.run(['g++', 'code_to_run.cpp'], stdout= subprocess.PIPE, stderr=subprocess.PIPE, input = inputString.encode()) #calls a process to compile the c++ code 
    if(len(runnerPrelim.stderr)==0):
        runner = subprocess.run(['./a.out'], stdout= subprocess.PIPE, stderr=subprocess.PIPE, input = inputString.encode())
    else:
        return [0,runnerPrelim.stderr.decode()]
    if(len(runner.stderr)>0):
        return [0,runner.stderr.decode()]
    return [1,runner.stdout.decode()]  #the output from the runner is taken and decoded and returned