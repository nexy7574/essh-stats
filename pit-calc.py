import re
import json
import sys
import os

if os.name == "nt":
    print("Warning: Windows may not be fully supported. Why are you using endlessh on Windows anyway?")
regex = re.compile(r"time=[0-9]+\.[0-9]{0,3}")

try:
    with open("./config.json") as config:
        cfg = json.load(config)
except:
    cfg = {
        "log_location": None
    }
    with open("./config.json", "w+") as config:
        json.dump(cfg, config, indent=2)
    print("No config found. Please edit ./config.json#log_location to be the filepath to your endlessh logs.")
    sys.exit(1)

try:
    with open(cfg["log_location"]) as logfile:
        print("Reading logs...")
        logdata = logfile.read().splitlines()
        print(f"Read {len(logdata)} lines.")
except PermissionError:
    print("Forbidden from opening file. Are you root?")
    sys.exit(1)


longest_time = 0.0
shortest_time = float("inf")
avg = []
connected = 0


for n, line in enumerate(logdata):
    if "ACCEPT" in line:
        connected += 1
    if "CLOSE" in line:
        connected -= 1
    if not regex.search(line):

        continue

    try:

        time = float(regex.search(line).group()[5:])

    except Exception as e:

        print("Failed to parse line {}: {}".format(n, str(e)))

        continue

    avg.append(time)

    if time > longest_time:

        longest_time = time

    elif time < shortest_time:

        shortest_time = time

average = round(sum(avg)/len(avg), 2)
print(f"Longest Capture Time: {round(longest_time, 2)}s\nShortest Capture Time: {round(shortest_time, 2)}s\nAverage Capture Time: {average}s\nActive Clients: {connected}")
