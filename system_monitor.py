#2023-09-07 15:30:00, <cpu-usage>, <number-of-logical-CPUs-used>,<used-memory>, <used-disk-space>, <current-host-ip>
import psutil
from datetime import datetime
from math import floor
memory_max_usage = input("please enter the memory max usage in percent example(write 80 to check if it reach 80'%' or more)): ")
refresh_time = input("please enter in seconds the period to check: ")
iterations = input("please enter the number of needed samples: ")
memory_max_usage = int(memory_max_usage)
refresh_time = int(refresh_time)
iterations = int(iterations)
current_date = datetime.now()
filenamedate = current_date.strftime('%Y-%m-%d')
def warning():
    with open(f"{filenamedate}-notification.log" , 'w') as errorF:
        errorF.write(" the system is running a low memory")
file = open(f"log_{filenamedate}.txt" , 'w')
for i in range(iterations):
    mem = psutil.virtual_memory()
    memUsage = (mem.used) / (1024 * 1024 * 1024) # to print usage in gigabytes
    memUsage = round(memUsage , 3)
    if mem.percent >= memory_max_usage:
        warning()
############################################################################    
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
############################################################################
    cpuS_usage = psutil.cpu_percent( interval = refresh_time ,percpu = True )
    av_cpu_usage = sum(cpuS_usage) / len(cpuS_usage)
    av_cpu_usage = floor(av_cpu_usage)
############################################################################
    Lcpu_num = psutil.cpu_count(logical=True)  #the logical number of the CPU cores
############################################################################
    disk = psutil.disk_usage('/')
    disk = (disk.used) / (1024 * 1024 * 1024)
    disk = round(disk,3)
############################################################################
    
    network_interfaces = psutil.net_if_addrs()
    default_interface = list(psutil.net_if_stats().keys())[1]
    host_ip = network_interfaces[default_interface][1].address

    output_data = f"{formatted_date} , {av_cpu_usage} , {Lcpu_num} , {memUsage} , {disk} , {host_ip}" 
    
    file.write(output_data)
    file.write("\n")
file.close()
'''
Lcpu_num = psutil.cpu_count()
print("the logical CPUs is: ")
print(Lcpu_num)
print("\n")
print(Rcpu_num)
print (cpuS_usage)
'''
