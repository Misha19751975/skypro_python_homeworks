from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Nokia", "E-38", "+7911112"))
catalog.append(Smartphone("Samsung", "A-40","+791112"))
catalog.append(Smartphone("Samsung", "A-18", "+791113"))
catalog.append(Smartphone("Infinix", "X-669", "+791114"))
catalog.append(Smartphone("Infinix", "X-669D", "+791115"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")