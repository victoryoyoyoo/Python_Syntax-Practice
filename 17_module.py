# Using Modules
# pip: Package Management Tool

import tool # Imports the custom 'tool.py' file located in the same directory
import sys  # 'sys' is a built-in module in Python
import numpy as np # Use 'as' to create an alias for the module name (e.g., 'np' for 'numpy')

# Note: There are three main types of modules in Python:
# 1. Built-in modules (e.g., sys)
# 2. Third-party packages installed via pip (e.g., numpy)
# 3. Custom modules you write yourself (e.g., tool)

# sys.path returns a list of directories that Python searches for modules
print(sys.path) 

print(tool.name)
print(tool.age)
print(tool.max_num(2, 3, 88))