import random
from abc import ABC, abstractmethod
import string
import nltk 
nltk.download("words")


class Passwordgenerator(ABC):
    @abstractmethod
    def generator(self):
        pass


class Pincodegenerator(Passwordgenerator):
    def __init__(self,lenght: int = 4):
        self.lenght = lenght
    
    def generator(self):

        return ''.join(random.choice(string.digits) for _ in range(self.lenght))
    

class Memorable(Passwordgenerator):

    def __init__(self, num_words: int = 5, separator = "-", capitalizatiion =False, vocabulary = None):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        
        self.num_words = num_words
        self.separator = separator
        self.capitalizatiion = capitalizatiion
        self.vocabulary = vocabulary

    def generator(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_words)]
        if self.capitalizatiion :
            password_words = [word.uper() for word in password_words]
        
        return self.separator.join(password_words)


class Randompassword(Passwordgenerator):
    def __init__(self, lenght = 8, include_num = False, include_symb = False):
        self.lenght = lenght
        self.character = string.ascii_letters
        if include_num:
            self.character += string.digits
        if include_symb:
            self.character += string.punctuation
    
    def generator(self):
        return ''.join(random.choice(self.character) for _ in range(self.lenght))


def pin_code():
    pincode = Pincodegenerator()
    pincode = pincode.generator()
    print(pincode)


def random_password():
    randompassword = Randompassword()
    randompassword = randompassword.generator()
    print(randompassword)


def memorable_generator():
    memorable = Memorable()
    memorable = memorable.generator()
    print(memorable)
    
def game():
    pin_code()
    random_password()
    memorable_generator()

if __name__ == "__main__":
    pin_code()
    random_password()
    memorable_generator()
