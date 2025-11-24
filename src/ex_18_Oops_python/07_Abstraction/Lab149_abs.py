
from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass


class Browser(ExcelReader):


    def startBrowser(self):
        pass

    def stopBrowser(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Printing")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTC(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()


obj1 = TC1()
obj1.runTC()