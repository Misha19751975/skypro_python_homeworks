class User:
    age = 0;

    def __init__(self, name):
        print("я создался")
        self.username = name

    def sayName(self):
        print("меня зовут ", self.username)

    def sayAge(self):
        print(self.age) 

    def setAge(self, newAge):
        self.age = newAge
    
    def addCard(self, card): #создали метод с параметрами
        self.card = card #добавили карточку в тело метода

    def getCard(self): #метод для распознавания карты
        return self.card #возвращение значения переменной в скрипт