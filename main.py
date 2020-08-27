import psutil
import time
import datetime


for x in range(5):

    ts = datetime.datetime.now().timestamp()

    now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')    
    print("\nRotina " + str(x) + " \t" + now +"\t")    
    cpu_percent = psutil.cpu_percent(interval=1)
    v_mem = psutil.virtual_memory().used
    disk_usage = psutil.disk_usage('/').percent
    io = psutil.net_io_counters()
    b_sent = io.bytes_sent
    b_recv = io.bytes_recv
    bat = psutil.sensors_battery().percent;

    print("Percentual de uso da CPU:\t " + str(cpu_percent) + "%");
    print("Memoria virtual livre:\t " + str(v_mem));
    print("Uso de disco:\t " + str(disk_usage) + "%");
    print("Bytes enviados:\t " + str(b_sent));
    print("Bytes recebidos:\t " + str(b_recv));
    print("Bateria:\t " + str(bat) + "%");
