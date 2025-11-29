
eg = ExceptionGroup("Multiple Exp", [
    ValueError("Invalid value"),
    TypeError("Type Error"),
    ZeroDivisionError("Zero div error")
])

def check_div(a):
    if a == 0:
        raise eg