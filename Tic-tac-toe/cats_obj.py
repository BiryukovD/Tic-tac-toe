from Cat import Cat
ob = Cat('Вася', 'мальчик', 12)
ob1 = Cat('Барсик', 'девочка', 3)

print(ob.get_age())

#Создайте класс Dog с помощью наследования класса Cat. Создайте метод get_pet()
#таким образом, чтобы он возвращал только имя и возраст.
#Далее сделайте вывод этой информации в консоль.

class Dog(Cat):
    def get_pet(self):
        return self.name, self.age
    def __add__(self, other):
        return self.age + other.age

ob_2 = Dog('мухтар', 'девочка', 10)
ob_3 = Dog('Бобик', 'мальчик', 5)
ob_4 = ob_2 + ob_3
print(ob_4)


