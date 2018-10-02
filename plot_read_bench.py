from __future__ import print_function
import matplotlib.pyplot as plt
import collections
import numpy as np

# file_seq = open("results/rados_bench_seq.out")
# file_rand = open("results/rados_bench_rand.out")

file_seq = open("results/aff_seq_bench.out")
file_rand = open("results/aff_rand_bench.out")

seq_throughput = {}
seq_throughput_std = {}
seq_latency = {}
seq_latency_std = {}

rand_throughput = {}
rand_throughput_std = {}
rand_latency = {}
rand_latency_std = {}
size = 0
for line in file_seq:
    if "SIZE" in line:
        size = line.split(" ")[3]
    elif "Bandwidth (MB/sec):" in line:
        seq_throughput[int(size)] = float(line.split()[2])
    elif "Stddev Bandwidth:" in line:
        seq_throughput_std[int(size)] = float(line.split()[2])
    elif "Average Latency(s):" in line:
        seq_latency[int(size)] = float(line.split()[2])
    elif "Stddev Latency(s):" in line:
        seq_latency_std[int(size)] = float(line.split()[2])

for line in file_rand:
    if "SIZE" in line:
        size = line.split(" ")[3]
    elif "Bandwidth (MB/sec):" in line:
        rand_throughput[int(size)] = float(line.split()[2])
    elif "Stddev Bandwidth:" in line:
        rand_throughput_std[int(size)] = float(line.split()[2])
    elif "Average Latency(s):" in line:
        rand_latency[int(size)] = float(line.split()[2])
    elif "Stddev Latency(s):" in line:
        rand_latency_std[int(size)] = float(line.split()[2])



od = collections.OrderedDict(sorted(seq_throughput.items()))
sizes = od.keys()
seq_throughput = od.values()
od = collections.OrderedDict(sorted(seq_throughput_std.items()))
seq_throughput_std = od.values()
od = collections.OrderedDict(sorted(seq_latency.items()))
seq_latency = od.values()
od = collections.OrderedDict(sorted(seq_latency_std.items()))
seq_latency_std = od.values()

od = collections.OrderedDict(sorted(rand_throughput.items()))
rand_throughput = od.values()
od = collections.OrderedDict(sorted(rand_throughput_std.items()))
rand_throughput_std = od.values()
od = collections.OrderedDict(sorted(rand_latency.items()))
rand_latency = od.values()
od = collections.OrderedDict(sorted(rand_latency_std.items()))
rand_latency_std = od.values()


plt.plot(sizes, seq_throughput, "r",  marker='o', linestyle='dashed', label = "SEQ")
plt.plot(sizes, rand_throughput, "b",  marker='o', linestyle='dashed', label = "RAND")
plt.legend()
plt.title("Adjusted AFF 2 SSDs 1 PERS: Ceph Read Throughput for Varying Read Sizes")
plt.xscale('log', basex=2)
plt.xlabel("Read Size (Bytes)")
plt.ylabel("Throughput (MB/s)")
plt.show()
plt.plot(sizes, seq_latency, "r",  marker='o', linestyle='dashed', label = "SEQ")
plt.plot(sizes, rand_latency, "b",  marker='o', linestyle='dashed', label = "RAND")
plt.title("Adjusted AFF 2 SSDs 1 PERS: Ceph Read Latency for Varying Read Sizes")
plt.legend()
plt.xscale('log', basex=2)
plt.xlabel("Read Size (Bytes)")
plt.ylabel("Latency (S)")
plt.show()