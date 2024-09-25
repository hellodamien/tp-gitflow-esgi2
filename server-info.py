import psutil

# Get the memory usage information
memory = psutil.virtualMemory()

# Print the memory usage details
print("Total Memory: {:.2f} GB".format(memory.total / (1024 ** 3)))
print("Used Memory: {:.2f} GB".format(memory.used / (1024 ** 3)))
print("Memory Percent: {:.2f}%".format(memory.percent))