class Canteen:
    def __init__(self,temp):
        self.temp=temp
    def process(self):
        if(self.temp>=50):
            print("Table Tennis")
            print("Carroms")
            print("Pin Board")
            print("Swimming")
            print("Coconut")
            print("Go home")
        else:
            print("Coconut")
            print("Go home")
temp=float(input("Enter the Temperature="))
obj=Canteen(temp)
obj.process()
