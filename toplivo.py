import os
def toplivo(path):
    num_files = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
    return num_files