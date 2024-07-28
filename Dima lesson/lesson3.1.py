from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.sayAge()
alex.setAge(33)

card = Card("4533 4567 8800 7655", "11/28", "Alex F")
card.pay(1000)


