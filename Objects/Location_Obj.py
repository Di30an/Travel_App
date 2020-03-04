class Location:

    
    def __init__(self,country,  city, country_code):
        self.country = country
        self.city = city
        self.country_code = country_code
    def __str__(self):
        return (f'{self.country},{self.city}, {self.country_code}' )
