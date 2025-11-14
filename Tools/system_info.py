# -- Modules -- #

import platform
import psutil
import cpuinfo 

import wmi # This only works on Windows.


# -- Variables -- #

pc = wmi.WMI()

uname = platform.uname()

os = f"{uname[0]} {uname[2]} {platform.architecture()[0]}"

cpu = cpuinfo.get_cpu_info()['brand_raw']

ram = f"{round(psutil.virtual_memory().total / 1024**3)} GB "

gpu = pc.Win32_VideoController()[0].name

info = {
    "Operating System: ": os,
    "CPU: ":cpu,
    "RAM: ":ram,
    "GPU: ":gpu
 }

# -- Functions -- #

