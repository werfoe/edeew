import random
from words import adjective1, noun1

class FunRandomName():  
    def __start(self): 
        self.__adjective = adjective1
        self.__noun = noun1
    def __get_random_adjective(self):
        return random.choice(self.__adjective)
    def __get_random__noun(self): 
        return random.choice(self.__noun)
    def get_name(self):
        adjective = self.__get_random_adjective()
        noun = self.__get_random__noun()
        return f"{adjective} {noun}"

a = FunRandomName()
print(a.get_name())
