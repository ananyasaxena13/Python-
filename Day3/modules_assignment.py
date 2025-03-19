#Fix the circular import problem between module_a.py and module_b.py.

#module_a.py:

#


#Dynamic Module Loading

import importlib

def dynamic_import_and_execute():
    module_name = input("Enter module name: ")
    function_name = input("Enter function name: ")
    argument = input("Enter argument: ")

    try:
        module = importlib.import_module(module_name)  # Dynamically import module
        func = getattr(module, function_name)  # Get function from module

        if callable(func):
            # Convert input to appropriate type (int, float, etc.)
            try:
                argument = eval(argument)
            except:
                pass  # Keep as string if eval fails

            result = func(argument)  # Execute function
            print("Output:", result)
        else:
            print(f"'{function_name}' is not a callable function in {module_name}.")
    except (ModuleNotFoundError, AttributeError) as e:
        print("Error:", e)

# Run the function
dynamic_import_and_execute()


