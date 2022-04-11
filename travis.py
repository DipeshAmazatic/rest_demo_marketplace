'''
Script to check maintainabilty on travis CI
'''
from subprocess import Popen, PIPE
import re

def get_file_paths():
    proc = Popen('find ./src/ -type f -name "*.py"', stdout=PIPE, stderr=PIPE, shell=True)
    out, err = proc.communicate()
    return out.decode('ascii').split('\n')

def run_wily_report(paths):
    for path in paths:
        if path:
            proc = Popen('wily report {} mi --console-format 4 --number 1'.format(path[2:]),
                         stdout=PIPE, stderr=PIPE, shell=True)
            out, err = proc.communicate()
            out = out.decode('utf-8').split('\n')
            result = re.findall(r' ([0-9.]+) ', out[2])
            if result:
                if float(result[0]) < 90:
                    print('Exception: Maintainability Index for file '\
                    '{} is {} which is lesser than threshold value(90).'.format(path, result[0]))
                    exit(1)

if __name__ == '__main__':
    file_paths = get_file_paths() 
    run_wily_report(file_paths)
    
