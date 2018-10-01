from __future__ import print_function
import matplotlib.pyplot as plt
import collections
import numpy as np

file = open("results/rados_bench_write.out")

write_throughput = {}
write_throughput_std = {}
write_latency = {}
write_latency_std = {}
size = 0
for line in file:
    if "SIZE" in line:
        size = line.split(" ")[3]
    elif "Bandwidth (MB/sec):" in line:
        write_throughput[int(size)] = float(line.split()[2])
    elif "Stddev Bandwidth:" in line:
        write_throughput_std[int(size)] = float(line.split()[2])
    elif "Average Latency(s):" in line:
        write_latency[int(size)] = float(line.split()[2])
    elif "Stddev Latency(s):" in line:
        write_latency_std[int(size)] = float(line.split()[2])

od = collections.OrderedDict(sorted(write_throughput.items()))

sizes = od.keys()
write_throughput = od.values()
od = collections.OrderedDict(sorted(write_throughput_std.items()))
write_throughput_std = od.values()
od = collections.OrderedDict(sorted(write_latency.items()))
write_latency = od.values()
od = collections.OrderedDict(sorted(write_latency_std.items()))
write_latency_std = od.values()

plt.errorbar(sizes, write_throughput, fmt="ro", yerr=write_throughput_std, linestyle='dashed',markersize=10)
plt.title("Ceph Write Throughput for Varying Write Sizes")
plt.xscale('log', basex=2)
plt.xlabel("Write Size (Bytes)")
plt.ylabel("Throughput (MB/s)")
plt.show()

plt.errorbar(sizes, write_latency, fmt="bo", yerr=write_latency_std, linestyle='dashed',markersize=10)
plt.title("Ceph Write Latency for Varying Write Sizes")
plt.xscale('log', basex=2)
plt.xlabel("Write Size (Bytes)")
plt.ylabel("Latency (S)")
plt.show()

plt.errorbar(sizes, write_latency, fmt="bo", yerr=write_latency_std,linestyle='dashed',markersize=10)
plt.title("Ceph Write Latency for Varying Write Sizes")
plt.xscale('log', basex=2)
plt.yscale('log', basex=2)
plt.xlabel("Write Size (Bytes)")
plt.ylabel("Latency (S)")
plt.show()
