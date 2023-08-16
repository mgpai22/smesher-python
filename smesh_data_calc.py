import math

drive_size_in_gb = 465 # change me
drive_size_in_gigie_bytes = drive_size_in_gb / 1.074 # correlates with space the smesher is using
num_units = math.floor(drive_size_in_gigie_bytes / 64)

file_cnt = num_units * 32

print(f'num units: {num_units}')
print(f'file count: {file_cnt}')

# speed in MB/sec found here: https://reports.smesh.cloud/
gpu_1_speed = 2.2 # rtx 3060 change me
gpu_2_speed = 2.52 # rtx 3070 change me
gpu_3_speed = 2.52 # rtx 3070 change me

# this needs to be adjusted according to how many gpus you have
gpu_list = [gpu_1_speed, gpu_2_speed, gpu_3_speed]

# leave everything below as is

sorted_gpu_list = sorted(gpu_list)

total_speed = sum(sorted_gpu_list)

gpu_files = [math.floor(file_cnt * (speed / total_speed)) for speed in sorted_gpu_list]

# If there are remaining files, assign them to the fastest GPU
remaining_files = file_cnt - sum(gpu_files)
gpu_files[-1] += remaining_files

if sum(gpu_files) != file_cnt:
    print("file count and gpu total file distribution do not match")

for i in range(len(gpu_files)):
    print(f'GPU {i+1} num files: {gpu_files[i]}')

file_start = 0

# Calculate and print file ranges for each GPU
for i in range(len(gpu_files)):
    file_end = file_start + gpu_files[i]
    print(f'Files to process by GPU {i+1}: from {file_start} to {file_end - 1}')
    file_start = file_end
