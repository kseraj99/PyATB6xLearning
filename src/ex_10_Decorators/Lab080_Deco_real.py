def before_after_ui_testing(func):

    def wrapper():
        print("Before running code!")
        func()
        print("After running code!")

    return wrapper()


@before_after_ui_testing
def ui_testing():
    print("Hi,I am a UI Tester!")