class Table:
    def __init__(self,l,w,h):
        self.long = l
        self.width = w
        self.height = h
    def outing(self):
        print (self.long,self.width,self.height)


class Kitchen(Table):
    def howplaces(self,n):
        if n < 2:
            print ("It is not kitchen table")
        else:
            self.places = n
    def outplases(self):
        print (self.places)


class Coffee(Table):
    def relax(self):
        if self.height <= 50:
            print('Comfortable Coffee Table')
        else:
            print('Uncomfortable Coffee Table')


t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
t_2 = Table(1,3,0.7)
t_2.outing()

t_coffee1 = Coffee(10, 10, 60)
t_coffee1.relax()
t_coffee2 = Coffee(10, 10, 10)
t_coffee2.relax()