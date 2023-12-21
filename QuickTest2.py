import os

print(os.getcwd())
path = os.getcwd()
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))
print(os.path.splitext(path))
print(os.path.join(os.path.dirname(path), os.path.basename(path)))
print(os.path.exists(path))
print(os.path.isfile(path))
