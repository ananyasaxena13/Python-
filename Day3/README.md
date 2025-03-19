# Dynamic Module Loading

1. Takes user input for the module name, function name, and argument.
2. Dynamically imports the specified module using importlib.import_module().
3. Retrieves the function from the module using getattr().
4. Converts the argument to an appropriate type using eval(), if possible.
5. Executes the function and prints the output.

