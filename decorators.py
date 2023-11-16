from datetime import datetime
import time

def logger(func):
    def wrapper():
        print("-"*50)
        print("> Execution Started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        func()
        print("> Execution Completed {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("-"*50)
    return wrapper

@logger
def demo_function():
    print("Executing Task!")
    # simulating execution
    time.sleep(3)
    print("Task Completed.")

def logger_args(func):
    def wrapper(*args, **kwargs):
        print("-"*50)
        print("> Execution Started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        func(*args, **kwargs)
        print("> Execution Completed {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("-"*50)
    return wrapper

@logger_args
def demo_function_args(sleep_time):
    print("Executing Task!")
    time.sleep(sleep_time)
    print("Task Completed.")

demo_function_args(1)
demo_function_args(2)
demo_function_args(3)
