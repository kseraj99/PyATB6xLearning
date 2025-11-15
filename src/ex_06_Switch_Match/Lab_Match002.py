print("Enter: Which test you want to run")

test_type = input("Enter the test type: API, UI, Performance and Security:\n")

match test_type:
    case "API":
        print("We are running a postman API Testcases")
    case "UI":
        print("We are running selenium Testcases")
    case "Performance":
        print("We are running performance Testcases")
    case "Security":
        print("We are running security Testcases")
    case _:
        print("Invalid Testcases")

         
# print("Enter: Which test you want to run")
#
# test_type = input("Enter the test type: API, UI, Performance and Security:\n")
#
# if test_type == "API":
#     print("We are running a postman API Testcases")
# elif test_type == "UI":
#     print("We are running selenium Testcases")
# elif test_type == "Performance":
#     print("We are running performance Testcases")
# elif test_type == "Security":
#     print("We are running security Testcases")
# else:
#     print("Invalid Testcases")
