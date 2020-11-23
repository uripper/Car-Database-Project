class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self.m = make
        self.mo = model
        self.c = color
        self.y = year
        self.mi = mileage

    def __str__(self):
        s = [" - "
            f"-Make: {self.m}"
            f"-Model: {self.mo}"
            f"-Color: {self.c}"
            f"-Year: {self.y}"
            f"-Mileage: {self.mi}"
            " - "
            " - "]
        return " ".join(s)

    def addnew(self):
            self.m = input("What is the make of your car: ").title()
            self.mo = input("What is the model of your car: ").title()
            self.c = input("What is the color of your car: ").title()
            while True:
                try: 
                    self.y = int(input("What is the year of your car: "))
                    break
                except ValueError:
                    print("Please enter a number.")
            while True:
                try:
                    self.mi = int(input("What is the mileage of your car: "))
                    break
                except ValueError:
                    print("Please enter a number.")
vlist = []

#To make list readable and clean, and adding numbers in front
def vlistclean():
    x =  list(enumerate(vlist,1))
    x = str(x)
    vlistclean = x.replace("(","").replace("('","").replace("[","").replace("'","").replace("]","").replace("')","").replace(")","")
    print(vlistclean.replace("-","\n").replace(" , ", "").replace('"',"").replace(", ",":").replace(" :","").replace(",",""))
    
def change(vlist):
    idx = int(input("Type the position of the car you'd like to update: "))
    vlist.pop(idx-1)
    updatedcar = Automobile("","","","","")
    updatedcar.addnew()
    vlist.insert(idx-1, updatedcar.__str__())
    print("Your changes have been saved.")


#sample inventory before additions
Toyota = Automobile("Toyota","Camry Hybrid XLE", "White", "2012", "106,000")
Honda = Automobile("Honda","CRV", "Green", "2016", "56,000")

vlist.append(Toyota.__str__())
vlist.append(Honda.__str__())


while True:
    print("""
          1. View inventory
          2. Add a vehicle
          3. Remove a vehicle
          4. Update vehicle attributes
          5. Quit and export inventory
          """)
    usera = input("Please enter a number: ")

    if usera == "1":
        print("\n")
        vlistclean()

    elif usera == "2":
        print("\n")
        usercar = Automobile("","","","","")
        usercar.addnew()
        vlist.append(usercar.__str__())

    elif usera == "3":
        while True:
            userb = input("\nType the position of the car you would like to delete. \nType 1 if you know the position. \nType 2 if you need a list.\nType 3 to return to the Main Menu.\n")
            if userb == "1":
                print("\n")
                userc = (int(input("Type the position of the car \n")))
                vlist.pop(userc-1)
                print("New list after removal: ")
                vlistclean()
                break

            elif userb == "2":
                print("\n")
                vlistclean()

            elif userb == "3":
                break

    elif usera == "4":
        while True:
            userb = input("\nType the position of the car you would like to change. \nType 1 if you know the position. \nType 2 if you need a list.\nType 3 to return to the Main Menu.\n")
            if userb == "1":
                print("\n")
                change(vlist)
                break

            elif userb == "2":
                print("\n")
                vlistclean()

            elif userb == "3":
                break

    elif usera == "5":
        print("\nExporting file and closing program...")
        x =list(enumerate(vlist,1))
        x = str(x)
        vlistclean = x.replace("(","").replace("('","").replace("[","").replace("'","").replace("]","").replace("')","").replace(")","")
        vlistclean = vlistclean.replace("-","\n").replace(" , ", "").replace('"',"").replace(", ",":").replace(" :","").replace(",","")
        with open("PortfolioOutput.txt", "w") as file:
            file.write(vlistclean)
            file.close()

        break

    else:
        print("\nPlease try again.")
                
                

                
                        
                      
        
        
        
    

