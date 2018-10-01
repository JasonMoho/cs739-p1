from __future__ import print_function
import matplotlib.pyplot as plt
import collections
import numpy as np

disk_read_file = open("results/disk_read_bench.out")
disk_write_file = open("results/disk_write_bench.out")

read_throughput = {}
size = 0
for line in disk_read_file:
    if "SIZE" in line:
        size = line.split(" ")[3]
        read_throughput[int(size)] = []
    elif "MB/s" in line:
        read_throughput[int(size)].append(float(line.split(" ")[9]))


od = collections.OrderedDict(sorted(read_throughput.items()))
readx = od.keys()
ready = [np.mean(x) for x in od.values()]
readstd = [np.std(x) for x in od.values()]

write_throughput = {}
size = 0
for line in disk_write_file:
    if "SIZE" in line:
        size = line.split(" ")[3]
        write_throughput[int(size)] = []
    elif "MB/s" in line:
        write_throughput[int(size)].append(float(line.split(" ")[9]))


od = collections.OrderedDict(sorted(write_throughput.items()))
writex = od.keys()
writey = [np.mean(x) for x in od.values()]
writestd = [np.std(x) for x in od.values()]

print(writex)

plt.errorbar(writex, writey, fmt="bo", yerr=writestd,linestyle='dashed', label = "write")


plt.errorbar(readx, ready, fmt="ro", yerr=readstd,linestyle='dashed', label = "read")

plt.title("Local Disk Performance")
plt.legend()
plt.xscale('log', basex=2)
plt.xlabel("Size (MB)")
plt.ylabel("Throughput (MB/s)")
plt.show()

