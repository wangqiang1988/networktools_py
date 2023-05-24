import wmi
import platform
import os

memory_index= 1

def convertFileSize(size):
    # 定义单位列表
    units = 'Bytes', 'KB', 'MB', 'GB', 'TB'
    # 初始化单位为Bytes
    unit = units[0]
    # 循环判断文件大小是否大于1024，如果大于则转换为更大的单位
    for i in range(1, len(units)):
        if size >= 1024:
            size /= 1024
            unit = units[i]
        else:
            break
    # 格式化输出文件大小，保留两位小数
    return '{:.2f} {}'.format(size, unit)

# 创建 WMI 对象
c = wmi.WMI()

device = c.Win32_ComputerSystem()[0]
system = c.Win32_OperatingSystem()[0]
cpu = c.Win32_Processor()[0]
board = c.Win32_BaseBoard()[0]
memory = c.Win32_PhysicalMemory()[1]
vedio = c.Win32_VideoController()[0]
disk = c.Win32_DiskDrive()[0]

print("型号:",device.SystemSKUNumber)
print("系统:",system.Caption)
print("CPU型号:",cpu.Name.strip())
print("主板:",board.SerialNumber.strip())
for mem in c.Win32_PhysicalMemory():
    print("内存插槽",memory_index,"容量:",convertFileSize(int(memory.Capacity)))
    memory_index +=1
print("显卡:",vedio.Name.strip())
print("硬盘型号:",disk.Model.strip() ,"硬盘大小:",convertFileSize(int(disk.Size)),"硬盘接口:",disk.InterfaceType)
for netinfo in c.Win32_NetworkAdapterConfiguration():
    if ':' in str(netinfo.MACAddress) and 'VMnet' not in str(netinfo.Description) and 'Virtual' not in str(netinfo.Description) and 'WAN' not in str(netinfo.Description):
        print(netinfo.Description,netinfo.MACAddress,netinfo.IPAddress)

