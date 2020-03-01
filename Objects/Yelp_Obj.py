class Yelp :

    def __init__ (self, country, city,  recommendations):
        self.country = country
        self.city = city
        self.recommendations = recommendations
    def __str__(self):
        return (f'Here are yelp recommendations for {self.city}:\n ----------------------------------------------\n{self.recommendations}')
