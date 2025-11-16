
import time

def print_logs(func):

    def wrapper():
        print("Start of the logs")
        func()
        print("End of the logs")
    return wrapper    # <-- FIXED


def time_decorator(func):

    def wrapper():
        start_time = time.time()
        print("Start time:", start_time)
        func()
        end_time = time.time()
        print("End time:", end_time)
        print("Total time taken:", end_time - start_time)
    return wrapper    # <-- FIXED



@time_decorator
@print_logs
def ui_testing_1():
    print("add a function, time taken by this function-1")
    time.sleep(2)

@time_decorator
@print_logs
def ui_testing_2():
    print("add a function, time taken by this function-2")
    time.sleep(2)


# Call the functions to actually run them
ui_testing_1()
ui_testing_2()
