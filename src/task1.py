from abc import ABC
from abc import abstractmethod


class Orders(object):
    __value = 0

    def __init__(self, customer, waiter):
        """Order creation

        :param customer: Customer class object
        :param waiter: Waiter class object
        """
        print(20 * '-', 'New order opened', 20 * '-')
        Orders.__value += 1
        self.order_opened = True
        self.customer = customer
        self.waiter = waiter
        self.order_coast = 0
        self.order = dict()

    def food_order(self, food_name, value):
        """Food order between customer and waite

        :param food_name: string type
        :param value: number of food: integer
        :return: None
        """
        self.customer.place_order(food_name, self.waiter)
        if self.customer.food:
            self.order[food_name] = value
            self.order_coast += waiter.menu.food[food_name] * value

    def close_order(self):
        """Close order method

        :return: None
        """
        if self.order_coast == self.waiter.taken_money:
            self.order_coast = 0
            self.order_opened = False
        elif self.order_coast < self.waiter.taken_money:
            change = self.waiter.taken_money - self.order_coast
            self.waiter.give_change(change, self.customer)
            self.order_coast = 0
            self.order_opened = False
        else:
            self.order_coast -= self.waiter.taken_money
            print('Left to be paid: {}'.format(self.order_coast))

    def __str__(self):
        return (
            'Order number is: {}\n'
            'Menu type is: {}\n'
            'Waiter name is: {}\n'
            'Table number is: {}\n'
            'food in order: {}\n'
            'Total order coast: {}\n'
            '{}'.format(
                Orders.__value,
                self.waiter.menu.__class__.__name__,
                self.waiter.name,
                self.customer.table_number,
                self.order,
                self.order_coast,
                self.status(),
            ))

    def status(self):
        """Order status

        :return: Order status in string format
        """
        return 'Order opened' if self.order_opened else 'Order closed'

    @staticmethod
    def discard_orders_number():
        """Discard orders number

        :return: None
        """
        Orders.__value = 0


class OrderType(Orders):

    def __init__(self, customer, waiter, menu):
        """Order type creation

        :param customer: Customer class object
        :param waiter: Waiter class object
        :param menu: Menu class object
        """
        super().__init__(customer, waiter)
        self.waiter.menu = menu


class Customer(object):

    def __init__(self, table_number):
        """Customer type creation

        :param table_number: integer
        """
        self.table_number = table_number
        self.food = None
        self.credit = 0

    def place_order(self, food_name, waiter):
        """Place order method

        :param food_name: string
        :param waiter: Waiter class object
        :return: None
        """
        self.food = waiter.take_order(food_name)

    def pay(self, value, waiter):
        """Customer pay for order method

        :param value: integer
        :param waiter: Waiter class object
        :return: None
        """
        print('I pay you: {} !!!'.format(value))
        self.credit -= value
        waiter.take_pay(value)

    def take_change(self, value):
        """Take change method

        :param value: integer
        :return: None
        """
        self.credit += value


class Waiter(object):

    def __init__(self, name):
        """Waiter object creation

        :param name: name of waiter: string
        """
        self.name = name
        self.menu = None
        self.taken_money = 0

    def take_order(self, food_name):
        """Take order method

        :param food_name: string
        :return: food_name or None
        """
        return food_name if food_name in self.menu.food_in_menu() else None

    def take_pay(self, value):
        """Take pay method

        :param value: integer
        :return: None
        """
        self.taken_money = value

    @staticmethod
    def give_change(value, customer):
        """Give change to customer method

        :param value: integer
        :param customer: Customer class object
        :return: None
        """
        print('Give back your change: {} !!!'.format(value))
        customer.take_change(value)


class Menu(ABC):

    def __init__(self):
        self.food = dict()

    @abstractmethod
    def add_food_to_menu(self, name, price):
        """Abstract method of adding food name to menu

        :param name: string
        :param price: integer
        :return: None
        """
        self.food[name] = price

    def remove_food_from_menu(self, name):
        """Remove food name from menu

        :param name: string
        :return: None
        """
        self.food.pop(name)

    def food_in_menu(self):
        """Food in menu method

        :return: dict with
                    key: food name (string)
                    price: integer
        """
        return self.food

    def __str__(self):
        return str(self.food)


class LunchMenu(Menu):

    def add_food_to_menu(self, name, price, discount=10):
        """Add food name to lunch menu

        :param name: string
        :param price: integer
        :param discount: integer (0 <= value <= 100)
        :return: None
        """
        self.food[name] = price * (1 - discount / 100)


class DinnerMenu(Menu):

    def add_food_to_menu(self, name, price):
        """Add food to dinner menu"""
        super().add_food_to_menu(name, price)


lunch_menu = LunchMenu()
lunch_menu.add_food_to_menu('tea', 5)
lunch_menu.add_food_to_menu('milk', 10, 50)
lunch_menu.add_food_to_menu('water', 15)
print(lunch_menu)

dinner_menu = DinnerMenu()
dinner_menu.add_food_to_menu('meet', 15)
dinner_menu.add_food_to_menu('potato', 10)
dinner_menu.add_food_to_menu('cheese', 7)
print(dinner_menu)


customer = Customer(table_number=5)
waiter = Waiter('Samuel')

lunch_order = OrderType(customer, waiter, lunch_menu)
lunch_order.food_order('milk', 1)
lunch_order.food_order('water', 2)
lunch_order.food_order('meet', 1)
print(lunch_order)
customer.pay(40, waiter)
lunch_order.close_order()
print(lunch_order.status())

lunch_menu.remove_food_from_menu('water')

customer = Customer(table_number=2)

lunch_order = OrderType(customer, waiter, lunch_menu)
lunch_order.food_order('milk', 1)
lunch_order.food_order('water', 2)
lunch_order.food_order('meet', 1)
print(lunch_order)
customer.pay(4, waiter)
lunch_order.close_order()
print(lunch_order.status())
customer.pay(1, waiter)
lunch_order.close_order()
print(lunch_order.status())

Orders.discard_orders_number()

customer = Customer(table_number=9)
waiter = Waiter('Bob')

lunch_order = OrderType(customer, waiter, lunch_menu)
lunch_order.food_order('milk', 1)
lunch_order.food_order('water', 2)
lunch_order.food_order('meet', 3)
print(lunch_order)
customer.pay(25, waiter)
lunch_order.close_order()
print(lunch_order.status())

customer = Customer(table_number=1)

dinner_order = OrderType(customer, waiter, dinner_menu)
dinner_order.food_order('potato', 1)
dinner_order.food_order('meet', 1)
print(dinner_order)
customer.pay(30, waiter)
dinner_order.close_order()
print(dinner_order.status())
