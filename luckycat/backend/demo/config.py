import logging
import os

# Lucky CAT configs
host = '127.0.0.1'
port = 11300
job_name = 'ph7'
crash_queue = 'crashes'
stats_queue = 'stats'
sleep = 10
log_level = logging.DEBUG

# afl configs
base_path = '/tmp/afl-ramdisk'
cmd = os.path.join(base_path, 'ph7/ph7') + ' @@'
fuzzers = 2
collect_threads = 4
memory_limit = 1024
input_dir = os.path.join(base_path, 'ph7/fuzzing_in/')
output_dir = os.path.join(base_path, 'ph7/fuzzing_out/')
crashes_dir = os.path.join(base_path, 'ph7/crashes/')
