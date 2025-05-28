import subprocess
obj = subprocess.Popen('ls /root',shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 )

res = obj.stderr.read()

# ls / ; echo 123 ; ls / ; ls /root