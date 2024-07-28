from adress import Address
from mailing import Mailing

to_adress = Address("344092", "Rostov-on-Don", "Komarova", "16" ,"70")
from_adress = Address("143980", "Balashiha", "Babkina Dacha", "94", "2")

mailing = Mailing(to_adress, from_adress, 750, "trak12-B")
print(mailing)
