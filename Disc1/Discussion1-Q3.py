def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    return if_function(cond(), true_func(), false_func())

def cond():
    return True
 
def true_func():
    print("Welcome to", "\n", "61A")

def false_func():
    print("61A")

print(with_if_function())
