class Framework:

    name:str
    language :str
    architecture:str

    def set_att(self,name,language,architecture):

        self.name = name
        self.language = language
        self.architecture = architecture

    def display(self):

        print(self.name,self.language,self.architecture)

fm_instance1 = Framework()

fm_instance1.set_att("django","python","mvt")

fm_instance1.display()
