# Guido van Rossum?
import os

# Use a raw string to avoid escape sequences
directory = r"C:\Users\FakeUser\Targetfolder"
file = r"C:\Users\FakeUser\Targetfolder\targetfile.txt"
fileDest = r"C:\Users\FakeUser\Targetfolder\newname.md"

# Loop through the files in the directory and print them
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        print(f"File: {filename}")
        
# Rename a file        
os.rename(file, fileDest)
print("Source file has been renamed.")

# Another way to print a directory
files = os.listdir(directory)
print(files)
        
"""
Using the os module:
An easy and efficient way to interact with 
the operating system across various platforms,
such as Windows, macOS, and Linux.

Empowers developers to leverage system
resources without dealin with low-level, 
platform-specific programming.

- Python, widely used for automating 
  repetitive tasks. The  module provides
  tools to navigate directories,
  manage files, and execute
  system commands—all essential
  features for automation. 
   
- Integration with the operating system,
  allows developers to
  access environment variables,
  control file permissions,
  manage processes, and more.
   
- the module offers
  straightforward functions for
  system-level tasks that otherwise
  requires complex code.
  
- Instead of writing system-specific
  code for tasks: file manipulation 
  or process management, the module
  abstracts these operations,
  allowing code
  that works flawless 
  across different platforms
"""