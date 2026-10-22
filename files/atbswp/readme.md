# READING AND WRITING FILES

Variables are a fine way to store data while
your program is running, but if you want
your data to persist even after your program
has finished, you need to save it to a file. You
can think of a file’s contents as a single string value,
potentially gigabytes in size.

## Files and File Paths

A file has two key properties:

1. filename (usually written as one word)

    `project.docx`

2. path = specifies the location of a file on the computer.

    `C:\Users\Al\Documents`

3. The `C:\` part of the path is the root folder, which contains all other folders.

## Backslash on Windows and Forward Slash on macOS and Linux

On Windows, paths are written using backslashes `(\)` as the separator between
folder names.

The macOS and Linux operating systems, however, use the
forward slash `(/)` as their path separator.

If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases.

We can use `Path()` function in the `pathlib` module.

```python
from pathlib import Path
Path('spam', 'bacon', 'eggs')

Windows: WindowsPath('spam/bacon/eggs')
str(Path('spam', 'bacon', 'eggs'))
'spam\\bacon\\eggs'

Linux: PosixPath('spam/bacon/eggs')
```
