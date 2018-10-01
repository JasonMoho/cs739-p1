from __future__ import print_function
import matplotlib.pyplot as plt
import collections
import numpy as np
from datetime import datetime

file = open("results/rados_write_trace.out")

disk_1_usage = {}
disk_2_usage = {}
disk_3_usage = {}

job_times = {}

size = 0
time = 0
t0 = 0
for line in file:
    if "SIZE = DONE" in line:
        job_times["DONE"] = time
    elif "SIZE = " in line:
        size = line.split(" ")[3]
        job_times[int(size)] = time
    elif line.startswith("1538"):
        time = int(line)
        if t0 == 0:
            t0 = time
    elif "TOTAL" not in line and "ID" not in line and "####" not in line and "MAX" not in line:
        if int(line.split()[0]) == 0:
            disk_1_usage[int(time)] = line.split()[6]
        elif int(line.split()[0]) == 1:
            disk_2_usage[int(time)] = line.split()[6]
        elif int(line.split()[0]) == 2:
            disk_3_usage[int(time)] = line.split()[6]

od = collections.OrderedDict(sorted(disk_1_usage.items()))
times = [(x - t0)/1000.0 for x in od.keys()]
disk_1_usage = od.values()

od = collections.OrderedDict(sorted(disk_2_usage.items()))
disk_2_usage = od.values()

od = collections.OrderedDict(sorted(disk_3_usage.items()))
disk_3_usage = od.values()

od = collections.OrderedDict(sorted(job_times.items()))
job_times = od.values()


node1 = plt.plot(times, disk_1_usage, "r",  marker='o', linestyle='dashed', label='Disk1')
node2 = plt.plot(times, disk_2_usage, "b",  marker='o', linestyle='dashed', label='Disk2')
node3 = plt.plot(times, disk_3_usage, "k",  marker='o', linestyle='dashed', label='Disk3')
plt.xlabel("Time (s)")
plt.ylabel("Disk Usage (%)")
plt.ylim([0,85])
plt.title("Disk Usage vs. Time for 16 Consecutive Rados Bench Writes w/ Increasing Object Size")
plt.legend()

i = 10
for time in job_times:
    plt.axvline(x=(time-t0)/1000.0, color = "g", linestyle='dashed')
    if i < 26:
        plt.text((time-t0)/1000.0, 80, 'Write Size = 2^' + str(i), rotation=90)
    i+=1


plt.show()
# od = collections.OrderedDict(sorted(seq_throughput.items()))
# sizes = od.keys()
# seq_throughput = od.values()
# od = collections.OrderedDict(sorted(seq_throughput_std.items()))
# seq_throughput_std = od.values()
# od = collections.OrderedDict(sorted(seq_latency.items()))
# seq_latency = od.values()
# od = collections.OrderedDict(sorted(seq_latency_std.items()))
# seq_latency_std = od.values()
#
# od = collections.OrderedDict(sorted(rand_throughput.items()))
# rand_throughput = od.values()
# od = collections.OrderedDict(sorted(rand_throughput_std.items()))
# rand_throughput_std = od.values()
# od = collections.OrderedDict(sorted(rand_latency.items()))
# rand_latency = od.values()
# od = collections.OrderedDict(sorted(rand_latency_std.items()))
# rand_latency_std = od.values()
#
#
# plt.plot(sizes, seq_throughput, "r",  marker='o', linestyle='dashed')
# plt.plot(sizes, rand_throughput, "b",  marker='o', linestyle='dashed')
# plt.xscale('log', basex=2)
# plt.xlabel("Write Size (Bytes)")
# plt.ylabel("Throughput (MB/s)")
# plt.show()
# plt.plot(sizes, seq_latency, "r",  marker='o', linestyle='dashed')
# plt.plot(sizes, rand_latency, "b",  marker='o', linestyle='dashed')
# plt.xscale('log', basex=2)
# plt.yscale('log', basex=2)
# plt.xlabel("Write Size (Bytes)")
# plt.ylabel("Latency (S)")
# plt.show()