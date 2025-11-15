
def validate_status_code(response_code):
    if response_code == 200:
        print("Request is success")
    else:
        print("Error in the request")

validate_status_code(200)

validate_status_code(int(input("Enter the status code:\n")))