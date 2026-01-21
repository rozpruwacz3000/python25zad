# class Character:
#     def __init__(self, name, health, items):
#         self.name = name
#         if health > 0:
#             self.health = health
#         else: # Postać nie może mieć mniej niż 0 punktów życia
#             self.health = 0
#         self.items = items
#
#     def introduce(self):
#         print("Hello,my name is " + self.name + "and I have: ")
#
#         for item  in self.items:
#             print("- " + item)
#
#     def is_alive(self):
#         return self.health > 0
#
#     def take_damage(self, damage):
# #         self.health -= damage #self.health = self.health - demage (to jest to samo)
# #         if self.health <= 0:
# #             self.health = 0
# #             #self.health = max(0,self.health) ---> to jest to samo!
# #             #lub wszystko zastapic self.health = max(0, self.health - damage)
# #
# #
# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imaginary = imag
#
#     # Zdefiniowanie metody __add__ pozwala na dodawanie dwóch obiektów klasy ComplexNumber korzystając z operatora +
#     def __add__(self, other):
#         # Zwracamy nowy obiekt klasy ComplexNumber, z częścią rzeczywistą równą sumie części rzeczywistych obu obiektów i częścią urojoną równą sumie części urojonych obu obiektów
#         return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
#
#
# # c1 = ComplexNumber(0,5)
# # c2 = ComplexNumber(-3,5)
# # c3 = c1 + c2
# # print(str(c3.real) + " " +str( c3.imaginary))
#
#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, other):
#         return Vector(self.x * other.x, self.y * other.y)
#
#     def __str__(self):
#         return f"Vector(x: {self.x}, y: {self.y})"
#
#
# v1 = Vector(5, 10)
# # v2 = Vector(2, 3)
# #
# # print("Wektor 1:", v1)
# # print("Wektor 2:", v2)
# # print("Suma:", v1 + v2)
# # print("Różnica:", v1 - v2)
# # print("Mnożenie:", v1 * v2)
#
# class Character:
#     def __init__(self, name, health, items):
#         self.name = name
#         self.health = health
#         self.items = items
#
#     def introduce(self):
#         print("Hello!")
#
#     def is_alive(self):
#         return self.health > 0
#
# class Wizard(Character):
#     def __init__(self, name, health, items, mana):
#         super().__init__(name, health, items)
#         self.mana = mana
#
#     def cast_spell(self):
#       if self.mana > 0:
#         print("Fireball!")
#         self.mana -= 1
#       else:
#         print("Not enough mana!")
#
# class Warrior(Character):
#     def __init__(self, name, health, items,strength):
#         super().__init__(name,health,items)
#         self.strength = strength
#     def attack(self):
#         print("Attack!")
#         return self.strength
#
# c1 = Wizard("Gandalf",100,["Wand","Cape","Hobbit"],20)
# c1.cast_spell()
# c1.introduce()
#
# c2 = Warrior("John",200,["Sword","Shield"],10)
# print(c2.attack())
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __add__(self, amount):
        return self.__class__(self.account_number, self.balance + amount, *self._get_extra_args())

    def __sub__(self, amount):
        return self.__class__(self.account_number, self.balance - amount, *self._get_extra_args())

    def _get_extra_args(self):

        return []

    def __str__(self):
        return f"Account number: {self.account_number}, balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def _get_extra_args(self):
        return [self.interest_rate]

    def add_interest(self):

        self.balance += self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number, balance, free_transfers, transfer_fee):
        super().__init__(account_number, balance)
        self.free_transfers = free_transfers
        self.transfer_fee = transfer_fee

    def _get_extra_args(self):
        return [self.free_transfers, self.transfer_fee]

    def transfer(self, other_account, amount):
        # Sprawdzenie czy darmowe przelewy się skończyły
        if self.free_transfers <= 0:
            fee = self.transfer_fee
        else:
            fee = 0

        total_cost = amount + fee


        if self.balance >= total_cost:
            if fee > 0:
                self.balance -= fee

            self.balance -= amount
            other_account.balance += amount

            if self.free_transfers > 0:
                self.free_transfers -= 1
        else:
            print("Insufficient funds")
account1 = SavingsAccount("1234", 1000, 0.05)
account2 = CheckingAccount("5678", 500, 3, 5)
account1 = account1 + 50
print(account1)
account1 = account1 - 50
print(account1)
account1.add_interest()
print(account1)
account2.transfer(account1, 100)
print(account2)
print(account1)