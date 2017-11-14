


products = [
   ("Ultrasonic range finder", 2.50, 4)
 , ("Servo motor", 14.99, 10)
 , ("Servo controller", 44.95, 5)
 , ("Microcontroller Board",34.95, 7)
 , ("Laser range finder", 149.99, 2)
 , ("Lithium polymer battery", 8.99, 8)
 ]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i] :#names       prices
            print(str(i)+")",products[i].name, "$", products[i].price)
    print()
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
         printStock()

         vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

         if vals[0] == "quit": break

         prodId = int(vals[0])
         count = int(vals[1])


         if products[prodId].instock(count):#quantities and count
             if cash >= products[prodId].cost(count):#prices
                 products[prodId].remove(ammount) #subtracting from count
                 cash -= products[prodId].cost(count)  #subtractinf cash for ammount taken
                 print("You purchased", count, products[prodId].name+".")#saying product name
                 print("You have $", "{0:.2f}".format(cash), "remaining.")
             else:
                 print("Sorry, you cannot afford that product.")
         else:
             print("Sorry, we are sold out of", products.name[prodId])#saying that the store is sold out of a certain item

class Product:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def instock(self, desiredQuantity):
        if self.quantity >= desiredQuantity:
            return True
        else:
            return False

    def cost(self, ammount):
        return self.price * ammount
    
    def remove(self, ammount):
       self.quantity = self.quantity - ammount  




main()


        
     
