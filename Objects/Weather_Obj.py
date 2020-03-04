class Weather:

    def __init__(self, country, city, date, temp):
        self.country = country
        self.date = date
        self.temp = temp
        self.city = city
    def __str__(self):
        return (f'| In {self.city} the temperature is {self.temp:.1f}°F.')


