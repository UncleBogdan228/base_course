import sys, os

print(os.getcwd())
os.system('echo hi!')
#os.system('/home/codespace/.python/current/bin/python3 /workspaces/base_course/lec_sys_os.py')
print(sys.platform)
print('Python version is:', sys.version)
print(sys.path)

print(dir(sys))
print(dir(0))