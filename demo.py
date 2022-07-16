import sys
import subprocess
import schedule


platform = sys.platform
result = subprocess.run('pip install selenium', check=True, text=True, shell=True, stdout=open('output.txt', 'a'))
while result.returncode != 0:
    result = subprocess.run('pip install selenium', check=True, text=True, shell=True, stdout=open('output.txt', 'a'))

print('Successfully installed Selenium...')
