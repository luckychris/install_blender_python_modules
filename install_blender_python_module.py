import sys
import subprocess
import os
import platform
import bpy

def isWindows():
    return os.name == 'nt'

def isMacOS():
    return os.name == 'posix' and platform.system() == "Darwin"

def isLinux():
    return os.name == 'posix' and platform.system() == "Linux"

def python_exec():
    
    if isWindows():
        return os.path.join(sys.prefix, 'bin', 'python.exe')
    elif isMacOS():
    
        try:
            # 2.92 and older
            path = bpy.app.binary_path_python
        except AttributeError:
            # 2.93 and later
            import sys
            path = sys.executable
        return os.path.abspath(path)
    elif isLinux():
        import sys
        return os.path.join(sys.prefix, 'bin', 'python')
    else:
        print("sorry, still not implemented for ", os.name, " - ", platform.system)


def installModule(packageName):

    try:
        subprocess.call([python_exe, "import ", packageName])
    except:
        python_exe = python_exec()
       # upgrade pip
        subprocess.call([python_exe, "-m", "ensurepip"])
        subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
       # install required packages
        subprocess.call([python_exe, "-m", "pip", "install", packageName])
        
installModule("pandas")
