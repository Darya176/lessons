"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""
class BankAccount:

    def __init__(self, name, balance, passport, password):
        self._name = name
        self.__balance = balance
        self.__passport = passport
        self.__password = password

    def getbalance(self):
        return self.__balance

    def setbalance(self, newbalance):
        if self.__balance + newbalance >= 0:
            self.__balance += newbalance
            print('баланс изменен: ', self.getbalance())
        else:
            print('баланс меньше 0')

    def getpassword(self):
        return self.__password

    def getpassport(self):
        return self.__passport

    def setpassport(self, new_passport, password):
        if password == self.getpassword():
            self.__passport = new_passport
            print('номер паспорта изменен')
        else:
            print('Неверный пароль')

    def delpassport(self, password):
        if password == self.getpassword():
            del self.__passport
        else:
            print('неверный пароль')



account1 = BankAccount('Dasha', 1000, 111, 123)
print(account1.getbalance())
account1.setbalance(2000)
account1.setpassport(222, 123)
print(account1.getpassport())
account1.delpassport(123)
try:
    print(account1.getpassport())
except:
    print('паспорт был удален')
