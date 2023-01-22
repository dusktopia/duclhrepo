import csv
import random
import time

time_ms = 0
encoder_a = 0
encoder_b = 0
headers = ['time_ms', 'encoder_a', 'encoder_b']
csv_path = 'sample_data.csv'

with open(csv_path, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
    csv_writer.writeheader()

while True:
    with open(csv_path, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        info = {
            'time_ms': time_ms,
            'encoder_a': encoder_a,
            'encoder_b': encoder_b,
        }
        csv_writer.writerow(info)
        print(time_ms, encoder_a, encoder_b)
        time_ms += 1
        encoder_a = random.randint(0, 1023)
        encoder_b = random.randint(0, 512)
    time.sleep(0.5)
    if time_ms > 100:
        break
    else:
        pass