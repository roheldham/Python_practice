class Pokemon (object):

    def __init__(self, pokemon):

        self.pokemon = pokemon 
        print (f"{self.pokemon}! {self.pokemon}! {self.pokemon}!")

class Fire_type (Pokemon):

    def __init__(self,pokemon):
        
        super().__init__(pokemon)
        print ("I am a Fire type pokemon,", pokemon)

     


Charmander = Fire_type('Charmander')



