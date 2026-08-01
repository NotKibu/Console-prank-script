import random
import subprocess
from time import sleep

time = random.randint(5,5)
sleep(time)

for i in range(3):
    subprocess.Popen(
        ["cmd","/c","exit"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )