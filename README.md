# networktools_py
一个用python写的网络工具箱

### ping_check
用于检测到目标站点的延迟，丢包，抖动，每分钟ping20次，每分钟生成一次结果到目标文件，按天进行汇总

### winsysinfo
cookbook
http://timgolden.me.uk/python/wmi/cookbook.html
用于获取windows的信息,执行后打印出来信息如下：
```python
型号: LENOVO_MT_20U2_BU_Think_FM_ThinkPad L14 Gen 1
系统: Microsoft Windows 10 企业版 LTSC
CPU型号: Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz
主板: L1HF19V00A4
内存插槽 1 容量: 16.00 GB
内存插槽 2 容量: 16.00 GB
显卡: Intel(R) UHD Graphics
硬盘型号: KBG40ZNT512G TOSHIBA MEMORY 硬盘大小: 476.94 GB 硬盘接口: SCSI
Intel(R) Ethernet Connection (10) I219-V 84:A9:38:3C:61:XX ('192.168.x.x', 'fe80::a362:6010:2804:xxxx')
MediaTek Wi-Fi 6 MT7921 Wireless LAN Card 38:D5:7A:44:EA:XX None
TAP-Windows Adapter V9 for OpenVPN Connect 00:FF:AB:22:25:XX None
Array Networks TAP-Windows Adapter 00:FF:F5:E9:5E:XX None
Bluetooth Device (Personal Area Network) 38:D5:7A:44:EA:XX None
```

### ap_check
用于检测思科无线控制器（wlc）的无线AP在线状态，联动了smtp.py

### smtp
发送邮件通知，可在一些检测的脚本中调用此模块

### east_west_bandwith
东西流量统计，把汇聚、核心交换机下联端口的端口数据信息过滤出来放入到脚本中，然后算出东西流量带宽

<<<<<<< HEAD

### pubulic_ip
判断一个地址是否是公网ip（192.168.0.0/16,172.16.0.0/12,10.0.0.0/8）

=======

### check_port
判断设备是否打开了某个端口

(bili) PS E:\SynologyDrive\python script\测试> python .\check_port.py
Port 22 is closed on 172.16.255.1
Port 22 is closed on 172.16.255.2
Port 22 is closed on 172.16.255.3
Port 22 is closed on 172.16.255.4
<<<<<<< HEAD

### get_url

解析google浏览器开发者模式har文件，har文件与脚本放在同一个目录并执行脚本
'''shell
pip install haralyzer
PS E:\SynologyDrive\python script\测试> python .\url.py
assets-global.website-files.com
geolocation.onetrust.com
discord.com
www.googletagmanager.com
ajax.googleapis.com
global.localizecdn.com
d3e54v103j8qbb.cloudfront.net
www.youtube.com
assets.website-files.com
'''
=======
