---
title: Reading and Writing to Files in Python
layout: default
nav_exclude: true
---

We have already seen how to use the read_csv commands (in R and python/pandas) to read data from files into dataframes/tibbles.  But sometimes
we need to work directly with text files. 

## The basics


```python
#with open("path","r") as f:
#    (put logic to read file here)
```

This structure guarantees that the file will be properly closed when you're done. 

#### Slurp up the whole file into a string.


```python
with open("data/gettysburg.txt","r") as f:
    data = f.read()
len(data)
```


```python
lines = data.split('\n')
for x in lines[:10]:
    print(x)
```

#### Read the file line by line


```python
with open("data/gettysburg.txt","r") as f:
    for line in f:
        print(line) 
```

#### Read a line from the file


```python
with open("data/gettysburg.txt","r") as f:
    line = f.readline()
    print(line)
```

#### Slurp the file into a list


```python
with open("data/gettysburg.txt","r") as f:
    line_list = f.readlines()

lowercase = [x.lower() for x in line_list]
lowercase
```

## Writing to a file

An entire string to the file. **This will overwrite what is in the file.**


```python
with open("data/gettysburg_lower.txt","w") as f:
    f.write('\n'.join(lowercase))
```

One line at a time.
**This will overwrite what is in the file.**


```python
with open("data/gettysburg_lower.txt","w") as f:
    for x in lowercase:
        f.write(x+"\n")
```

## Appending to a file


```python
with open("data/gettysburg_lower.txt","a") as f:
    f.write("This goes at the end\n")
```

## Working with directories (folders)


```python
import os
import shutil
#os.getcwd()
#os.chdir('/home/jet08013')
#os.getcwd()
#files = os.listdir('.')
#os.rename()
#shutil.copy()
```
