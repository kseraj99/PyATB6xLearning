# Class for reading data from an Excel file
class ExcelReade:

    # Static method: can be called without creating an object
    @staticmethod
    def readExcelFile():
        print("Reading from Excel")


# Class for MySQL database connection
class MysqlDBConnection:

    # Static method: can be called without creating an object
    @staticmethod
    def readMysqlFile():
        print("Reading from MySql")


# Test case class
class TC1:

    # Method to run the test case
    def runTC(self):
        # Calling the Excel reader static method
        ExcelReade.readExcelFile()

        # Calling the MySQL reader static method
        MysqlDBConnection.readMysqlFile()

        print("Hi")  # Test case step


# Creating an object of the test case class
obj = TC1()

# Running the test case
obj.runTC()
