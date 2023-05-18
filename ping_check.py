import subprocess
import time
import statistics
from datetime import datetime, timedelta

hosts = ['google.com', 'bing.com', 'yahoo.com'] # 在这里添加你想要ping的主机
ping_count = 20 # 每分钟ping的次数

while True:
    results = []
    for host in hosts:
        ping_times = []
        for i in range(ping_count):
            ping = subprocess.Popen(
                ["ping", "-c", "1", host],
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, error = ping.communicate()
            if "bytes from" in out.decode('utf-8'):
                time_taken = float(out.decode('utf-8').split("time=")[1].split(" ")[0])
                ping_times.append(time_taken)
            else:
                ping_times.append(None)

        # 计算每分钟的平均延迟、丢包率和抖动
        avg_time = sum([x for x in ping_times if x is not None]) / len(ping_times)
        packet_loss = len([x for x in ping_times if x is None]) / len(ping_times)
        jitter = statistics.pstdev([x for x in ping_times if x is not None])

        results.append(("主机:"+str(host), "平均延迟:"+str(avg_time), "丢包率:"+str(packet_loss),"抖动:"+str(jitter)))

    # 将结果写入文件
    now = datetime.now()
    if now.hour == 0 and now.minute == 0:
        file_name = "ping_results_" + now.strftime("%Y-%m-%d") + ".txt"
        with open(file_name, "w") as f:
            f.write("time, host, avg_time, packet_loss, jitter\n")
    else:
        file_name = "ping_results_" + now.strftime("%Y-%m-%d") + ".txt"
    with open(file_name, "a") as f:
        for result in results:
            f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}, {result[0]}, {result[1]}, {result[2]}, {result[3]}\n")

    time.sleep(60) # 每分钟执行一次ping操作
