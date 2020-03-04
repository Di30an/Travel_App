class Yelp :

	def __init__ (self, country, city,  recommendations):

		self.country = country
		self.city = city
		self.recommendations = recommendations

	def __str__(self):
		#prints list line by line, CR
		recs = ''
		for rec in self.recommendations:
			countStr,name, rating, loc = rec
			recs += f'| {countStr}. {name}, {rating} stars, {loc}\n'
		return (f'\n| Here are your 5 yelp recommendations for {self.city}:\n| ----------------------------------------------------------------|\n{recs}|-----------------------------------------------------------------|\n| Thank you! Have fun! \t\t\t\t\t\t  |\n|-----------------------------------------------------------------|')
