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

**if module is stored at non conventional loaction, python won't find it by default**
import sys
sys.path.append('/custom/path/to/modules') **to fix that adding path manually**
import mymodule 