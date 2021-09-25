import subprocess

def coderunner(inputString):

    # with open("data.txt","r") as f:
    #     for line in f:
    #         inputString+=line


    output = subprocess.run(['python3', 'code_to_run.py'], stdout= subprocess.PIPE, input = inputString.encode())

    print((output).stdout.decode())
    return output.stdout.decode()
