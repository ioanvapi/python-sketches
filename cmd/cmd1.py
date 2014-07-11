#!/usr/bin/python
# executes 'free -m', calculates and display free memory

import commands

output = commands.getoutput("free -m")
output_array = output.split()
total = int(output_array[7])
free = int(output_array[9])
buffers = int(output_array[11])
cached = int(output_array[12])

actual_free = free + buffers + cached
print("Real free: {0}".format(actual_free))

percent_free = actual_free * 100 / total
print("Percent free: {0}%".format(percent_free))
