def before_after_ui_test(func):

    def wrapper():
        print("Before running code!")
        func()
        print("After running code!")

    return wrapper()


@before_after_ui_test
def test_ui():
    print("Hi,I am a UI Tester!")