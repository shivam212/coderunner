import subprocess
import time

def coderunnerPython(inputString): 
    start = time.process_time()*1000
    runner = subprocess.run(['python3', 'code_to_run.py'], stdout= subprocess.PIPE, stderr=subprocess.PIPE, input = inputString.encode()) #calls a process to run the python3 code
    end = time.process_time()*1000
    # print("The time elapsed is "+ str(end-start))
    time_taken = end-start
    if(len(runner.stderr)>0):
        return [0,runner.stderr.decode()]
    return [1,runner.stdout.decode(),time_taken]  #the output from the runner is taken and decoded and returned

def coderunnerCPP(inputString): 
    start = time.process_time()*1000
    runnerPrelim = subprocess.run(['g++', 'code_to_run.cpp'], stdout= subprocess.PIPE, stderr=subprocess.PIPE, input = inputString.encode()) #calls a process to compile the c++ code 
    end = time.process_time()*1000
    # print("The time elapsed is "+ str(end-start))
    time_taken = end-start
    if(len(runnerPrelim.stderr)==0):
        runner = subprocess.run(['./a.out'], stdout= subprocess.PIPE, stderr=subprocess.PIPE, input = inputString.encode())
    else:
        return [0,runnerPrelim.stderr.decode()]
    if(len(runner.stderr)>0):
        return [0,runner.stderr.decode()]
    return [1,runner.stdout.decode(),time_taken]  #the output from the runner is taken and decoded and returned