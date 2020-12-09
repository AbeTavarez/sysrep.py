# sysrep.py

Python System Disk Situation Report 

## Getting Started

### Prerequisites

- Python
- Pandas


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
