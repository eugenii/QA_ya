import datetime


class OnlineSalesRegisterCollector:
    """Working with check."""

    DISCOUNT = 0.9  # Apply discount for check more than 10 products.
    NDS_RATE_20 = 0.2  # NDS rate for some products.
    NDS_RATE_10 = 0.1  # NDS rate for some products.

    @staticmethod
    def get_telephone_number(telephone_number):
        """User's telephone number."""

        try:
            if not isinstance(telephone_number, int):
                raise ValueError('Необходимо ввести цифры')
            if len(str(telephone_number)) != 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            return f'+7{telephone_number}'

        except Exception as e:
            print(e)

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year],
        ]
        for period in date:
            interval = period[0]
            date_and_time.append(f'{interval}: {period[1](now)}')
        return date_and_time

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # Геттеры.

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    # Работа с чеком.

    def add_item_to_cheque(self, name):
        """Add product to check."""
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            self.__name_items.append(name)
            self.__number_items += 1
        except Exception as e:
            print(e)

    def delete_item_from_check(self, name):
        """Delete product from check."""

        try:
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            list.remove(self.__name_items, name)
            self.__number_items -= 1

        except Exception as e:
            print(e)

    def check_amount(self):
        """Calculate common cost."""
        total = []

        for name in self.__name_items:
            price = self.__item_price.get(name, 0)
            total.append(price)
        if len(total) > 10:
            return self.DISCOUNT * sum(total)
        return sum(total)

    # Расчёт НДС.

    def twenty_percent_tax_calculation(self):
        """Calculate 20% rate check."""

        twenty_percent_tax = [name for name in self.__name_items
                              if self.__tax_rate[name] == 20]

        total = [self.__item_price[item] for item in twenty_percent_tax]

        if len(total) > 10:
            return self.DISCOUNT * sum(total) * self.NDS_RATE_20
        return sum(total) * self.NDS_RATE_20

    def ten_percent_tax_calculation(self):
        """Calculate 10% rate check."""

        ten_percent_tax = [name for name in self.__name_items 
                           if self.__tax_rate[name] == 10]
        total = [self.__item_price[item] for item in ten_percent_tax]

        if len(total) > 10:
            return self.DISCOUNT * sum(total) * self.NDS_RATE_10
        return sum(total) * self.NDS_RATE_10

    def total_tax(self):
        """Calculate 20% + 10% rates for check."""

        return (
            self.twenty_percent_tax_calculation() + 
            self.ten_percent_tax_calculation()
        )
