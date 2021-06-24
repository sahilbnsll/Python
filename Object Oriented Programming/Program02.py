class RailwayForm:
    def data(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

sahilsApplication = RailwayForm()
sahilsApplication.name = "Sahil"        
sahilsApplication.train = "Satabadi Express"        

sahilsApplication.data()