class VivoMobile:
    def __init__(self,model,ram,rom):
        self.model=model
        self.ram=ram
        self.rom=rom

    def info(self):
        print(self.model,self.ram,self.rom)
#object
mob1=VivoMobile("x50","8gb","64gb")
mob2=VivoMobile("v20","16gb","128gb")

#function calling
mob1.info()
mob2.info()


