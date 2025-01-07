# create a class called Order which stores items & its price
# Use Dunder function to __gt__() to convey that
# order1 > order2 if price of order1 > price of order2


class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, order2):
        return self.price > order2.price

odr1=Order("Bike",100)
odr2=Order("Car",500)

print(odr2.__gt__(odr1))
