import csv
from collections import defaultdict
import math


data = defaultdict(list)
order = 0 

with open('output.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows_processed = 0
    total_time = 0.0

    for row_index, row in enumerate(csvreader):
        if row_index % 8 < 2:
            continue
        name, distance, width, reps, time = row
        distance = int(distance)
        width = int(width)
        time = float(time)
        reps = int(reps)
        total_time += time
        rows_processed += 1

        if rows_processed % 8 == 0:
            average_time = total_time / 6
            data.setdefault(math.log2(distance / width + 1), []).append(average_time)
            total_time = 0.0

summary_data = []

mean_times_by_id = {}
for id_value, times in data.items():
    mean_time = sum(times) / len(times)
    mean_times_by_id[id_value] = mean_time

# Write results to summary.csv
with open('summary.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['ID', 'mean time'])
    for id_value, mean_time in mean_times_by_id.items():
        formatted_id_value = "{:.3f}".format(id_value)
        formatted_mean_time = "{:.3f}".format(mean_time)
        csvwriter.writerow([formatted_id_value, formatted_mean_time])