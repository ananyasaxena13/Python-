def func_a():
    return "Function A"
#to resolve the circular dependencies we will import module where we need it not at the top of the file
import module_b
print(module_b.func_b())