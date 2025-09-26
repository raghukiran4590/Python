import os
from datetime import datetime

def get_datetime_from_timestamp(timestamp):
    """Convert a timestamp to a datetime object."""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_file_attributes(file_path):
    with os.scandir(file_path) as entries:
        for entry in entries:
            if entry.is_file():
                stats = entry.stat()
                file_info = {
                    'name': entry.name,
                    'size': stats.st_size,
                    'created': get_datetime_from_timestamp(stats.st_ctime),
                    'modified': get_datetime_from_timestamp(stats.st_mtime),
                    'accessed': get_datetime_from_timestamp(stats.st_atime)
                }
                print(file_info)


get_file_attributes(".")