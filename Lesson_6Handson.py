# Part 1

class Stadium:
    """"This defines a stadium"""

    def __init__(self, name, city_state, capacity, sport, seats):
        """"This shows the properties of each stadium"""
        self.name = name        
        """This is the stadium name"""
        self.city_state = city_state 
        """This is where the stadium is located"""
        self.capacity = capacity
        """This is the capacity of the stadium"""
        self.sport = sport
        """This is defines the sport"""
        self.seats = seats
        """This defines the amount of seats available"""

    def describe_stadium(self):
        print("The", self.name, "is located in", self.city_state, "and holds", self.capacity, "fans.")


#Part 2
    def sport_played(self):
        print("The following sport is mainly played in this statium:", self.sport + ".")

    def seats_available(self):
        print("There are", self.seats, "seats still available for tonight's game.")
    

stadium1 = Stadium('Mercedes Benz Arena', 'Atlanta, Ga', "70,000", 'Football', '15000')
stadium1.describe_stadium() 
stadium1.sport_played()
stadium1.seats_available()