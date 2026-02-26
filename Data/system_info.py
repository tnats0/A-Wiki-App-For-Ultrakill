# -- Modules -- #

import platform
import psutil
import cpuinfo 

import wmi # This only works on Windows.


# -- Variables -- #

pc = wmi.WMI()

cnm = platform.node()

uname = platform.uname()

os = f"{uname[0]} {uname[2]} {platform.architecture()[0]}"

cpu = cpuinfo.get_cpu_info()['brand_raw']

ram = f"{round(psutil.virtual_memory().total / 1024**3)} GB "

ram_usage = f"{round(psutil.virtual_memory().percent)}%"

ram_info = (ram,ram_usage)

gpu = pc.Win32_VideoController()[0].name

sys_info = {

    "Computer Network Name: ": cnm,
    "Operating System: ": os,
    "CPU: ":cpu,
    "RAM Info: ": f"{ram_info[0]}  {ram_info[1]}",
    "GPU: ":gpu
 }

# -- Functions -- #
