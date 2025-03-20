# Dynamic Module Loading

1. Takes user input for the module name, function name, and argument.
2. Dynamically imports the specified module using importlib.import_module().
3. Retrieves the function from the module using getattr().
4. Converts the argument to an appropriate type using eval(), if possible.
5. Executes the function and prints the output.

# Module Creation and Distribution

1. Created a package structure **mypackage**.
2. Added functions to **__init__.py**.
3. Created **setup.py** to make the package installable.
4. Installed the package locally using **pip install .**.
5. Imported and tested the package in **check.py**.

#  Investigate sys.path

- **sys.path** list defines the **directories** where Python searches **for modules when using import**

- If your **module** is in an **unconventional location**, you can manually add the path using **sys.path.append()**.

**if module is stored at non conventional location, python won't find it by default**
import sys
sys.path.append('/custom/path/to/modules') **to fix that adding path manually**
import mymodule 


# Mocking Modules for Testing
**is used to temporarily replace an object(function, class or module) with a mock object during a test**

from unittest import mock   **unittest.mock.patch is used to temporarily replace math.sqrt with a mock function that always returns 100**

**unittest.mock.patch allows us to replace dependencies in tests.**
with mock.patch('math.sqrt', return_value=100): 
    print(math.sqrt(25)) **normally return 5.0, but since we patched math.sqrt, it now returns 100.**


# Investigate Python’s Import Caching

- **sys.modules** is a dictionary that stores all imported modules.
- When you import a module, Python first checks **sys.modules** to see if it has already been loaded.
- If the module is found in sys.modules, it is not reloaded—instead, Python simply returns the cached version.
- If the module is not in sys.modules, Python loads and executes it, then stores it in sys.modules.