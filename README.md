# sysrep.py 📁 💿 📊

Python System Disk Situation Report

## Getting Started

### Prerequisites

- Python
- Pandas

### Runing the program

1. Fork repo.

2. Open it inn your favorite editor.

3. From the project's directory, run the following code in your terminal:

```
python3 disk_report path/to/directory/to/analyze
```

4- If everything was successful a new disk_usage.csv file shold be created in the same directory of the project.

### Sample Code

```
# Get directory size

def get_size(path):
    # accumulator
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                # recurvise call for each sub/directory
                total += get_size(entry.path)
            else:
              # get size in the total accumulator
                total += entry.stat(follow_symlinks=False).st_size
        except Exception as e:
            print('Exeption: ', e)
            total += 0
    return total
```
