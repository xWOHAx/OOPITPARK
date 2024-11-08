""" Абстракция """

# class Vehicle:
#     def start_engine(self):
#         pass

#     def stop_engine(self):
#         pass

#     def drive(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         return "Двигатель автомобиля заведен"
    
#     def stop_engine(self):
#         return "Двигатель автомобиля заглушен"
    
#     def drive(self):
#         return "Автомобиль едет"
    

# class Bicycle(Vehicle):
#     def start_engine(self):
#         return "у велосипеда нету двигателя"
    
#     def stop_engine(self):
#         return "У велосипеда нету двигателя"
    
#     def drive(self):
#         return "Велосипед едет"
    


class Employee:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def calculate_salary(self):
        return 0

    def display_info(self):
        print(f"Имя: {self.name}, Базовая ставка: {self.rate}")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.rate * 1.2


class PartTimeEmployee(Employee):
    def __init__(self, name, rate, worked):
        super().__init__(name, rate)
        self.worked = worked
        
    def calculate_salary(self):
        return self.rate * 0.5 * self.worked


def process_salary(employee):
    employee.display_info()
    salary = employee.calculate_salary()
    print(f"Зарплата: {salary:.2f}")


full_time = FullTimeEmployee("Сергей", 25000)
part_time = PartTimeEmployee("Аня", 900, 17)

process_salary(full_time)
process_salary(part_time)









# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev 

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" , ")
#             current = current.next
#         print("None")


# linked_list = LinkedList()
# linked_list.append(1) 
# linked_list.append(2) 
# linked_list.append(3) 
# print("Исходный список:") 
# linked_list.print_list()  
# linked_list.reverse() 
# print("Разворот списка:") 
# linked_list.print_list()  