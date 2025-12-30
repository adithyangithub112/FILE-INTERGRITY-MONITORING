## Program to find the hash of a file

```python
import hashlib

def file_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

print(file_hash("D:/brocamp/week 16/textfile.txt"))
```
