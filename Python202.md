## Python 201

**Decorators**
1. Allows modification of a function's behaviour without modifying the function
2. Requires an nested function

> from datetime import datetime\
> import time\

> def logger(func):\
    > def wrapper():\
        > print("-"*50)\
        > print(">>> Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))\
        > print(">>> Execution completed {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))\
        > print("-"*50)\
    return wrapper\

@logger #name of decorator\
> def demo_function():\
    > print("Executing task!")\
    > time.sleep(3)\
    > print("Task completed!")\

demo_function()\

logger(demo_function()) # alternative way of running\