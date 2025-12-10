class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Person name is {self.name}")
        print(f"Train name is {self.train}")

adminApplication = RailwayForm()
adminApplication.name = "Administrator"
adminApplication.train = "Tejas Express"
adminApplication.printData()
