from smartphone import Smartphone
catalog = [
Smartphone("Nokia", "3310", "89213423455"),
Smartphone("Moto", "1122", "89991234543" ),
Smartphone("Iphone","13", "89227896534"),
Smartphone("Samsung","s12", "89773451222"),
Smartphone("Fly", "1012", "89435674433")]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")



