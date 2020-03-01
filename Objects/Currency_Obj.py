class Currency:

    def __init__(self,country, denomination,  exchange_rate ):
        self.country = country
        self.denomination = denomination
        self.exchange_rate = exchange_rate
    

    def __str__(self):
        return (f'$1.00 USD is equal to ${self.exchange_rate:.2F} {self.denomination}.\n')