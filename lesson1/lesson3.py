class User:
	age = 0;

	def __init__(self, name):
		print("я создался")
		self.username = name

	def sayName(self):
		print("меня зовут ", self.username)

	def sayAge(self): #создали метод
		print(self.age) #создали тело метода

	
	def setAge(self, newAge):
		self.age = newAge

alex = User("Alex")
mark = User("Mark")
marta = User("Marta")

alex.sayName()
alex.sayAge() #создали запрос
alex.setAge(33)
alex.sayAge()