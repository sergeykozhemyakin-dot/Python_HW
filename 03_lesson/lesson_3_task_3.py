from address import Address
from mailing import Mailing

from_address = Address("125009", "Москва", "Тверская", "7", "15")
to_address = Address("620000", "Екатеринбург", "Ленина", "50", "32")

mailing = Mailing(to_address,from_address,cost=350,track="RU123456789RU")

print(f"Отправление: {mailing.track}, {mailing.from_address.index} г.{mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")