#Задача 11.1 Средний уровень Вариант 13
import struct


class Book:
    def __init__(self, title, pages,price):
        self.title = title
        self.pages = pages
        self.price = price

    def page_cost(self):
        return self.pages/self.price

    def price_multiple(self):
        if str.startswith(self.title,"Программирование"):
            self.price*=2
        return self.price
    def print_info(self):
        print('Название книги:', self.title)
        print('Количество страниц:', self.pages)
        print('Стоимость книги:',self.price)
        print('Средння стоимость страницы',self.page_cost())


book1= Book('Жопа',48,100)
book2=Book('Программирование',48,100)
book2.price_multiple()
book1.print_info()
book2.print_info()

#Задача 11.2 Средний уровень
class Library(Book):
    def __init__(self, title, pages, price, discount):
        super().__init__(title, pages, price)
        self.discount = discount

    def cost_with_discount(self):
        return self.price-(self.price*self.discount/100)

    def print_info(self):
        super().print_info()
        print('Стоимость книги со скидкой:',self.cost_with_discount())



library1 = Library('Война и мир',500,1500,15)
library1.print_info()

#Задача 11.3 Базовый уровень
class ComputerNetwork:
    def __init__(self,org_name,num_stations,avg_distance):
        self.org_name = org_name
        self.num_stations = num_stations
        self.avg_distance = avg_distance

    def quality(self):
        return (self.num_stations*self.avg_distance)

    def print_info(self):
        print('Название организации:',self.org_name)
        print('Количество станций:',self.num_stations)
        print('Среднее растояние:',self.avg_distance)
        print('Качество:',self.quality())


class College(ComputerNetwork):
    def __init__(self,org_name,num_stations,avg_distance,average_speed_of_network):
        super().__init__(org_name,num_stations,avg_distance)
        self.average_speed_of_network = average_speed_of_network
    def quality(self):
        return super().quality()*self.average_speed_of_network
    def print_info(self):
        super().print_info()
        print('Скорость интернета умноженная на качество:',self.quality())

col1 = College('Березы и сосны',20,30,100)
col1.print_info()