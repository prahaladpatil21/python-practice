#create a class movie with attribute title and rating usig the __init__() constructor

#define a method to display the movie's title and rating 
class Movie:
    def __init__(self, name, rating):
        self.name=name
        self.rating=rating
    def display(self):
        print(f"movie--> {self.name} and rating-->{self.rating}")
m1=Movie("KANTARA", 8)
M2=Movie("KGF2",8.2)
m3=Movie("premad oorali",9)

m3.display()