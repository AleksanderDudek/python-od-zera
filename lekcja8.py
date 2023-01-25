# konto bankowe : wypisuj balans, wplac pienaidze, wyplac pieniadze, konto przypisane do wlasciciela, okreslona waluta konta
# okreslona waluta - przewalutowanie konta z np. PLN na EURO, api (currency name, balance zmienone)
# obsluga bledow i udokumentowana klasa, autodocstring

# slownik albo modul enum
# enum Currencies = {
#     PLN = 'PLN',
# }

# Currencies.PLN
import requests

# kurs walut z api nbp
apiUrl = 'https://api.nbp.pl/api/exchangerates/tables/a'

# słownik dostępnych walut
availableCurrencies = ['PLN', 'USD', 'EUR']

def check_currency(currencyName: str):
    try:
       return True if availableCurrencies.index(currencyName) >= 0 else False
    except ValueError:
        return False

class BankAccount:
    # balance = 0
    # currencyName = ''
    # owner = ''

    def __init__ (self, owner: str, currencyName: str = "PLN",balance: float = 0 ):
        """Creates instance of an object of BankAccount class

        Args:
            owner (str): Name of the owner of the account
            currencyName (str, optional): Name of the currency the account holds. Defaults to "PLN".
            balance (float, optional): Balance of the account. Defaults to 0.
        """
        self.__balance = balance
        self.__currencyName = currencyName
        self.__owner = owner

    def deposit_money(self, currencyAmount: float):
        self.__balance += currencyAmount
        return True

    def withdraw_money(self, currencyAmount: float):
        if self.__balance < currencyAmount:
            return False
        else:
            self.__balance -= currencyAmount
            return True

    def __str__(self):
        return f'''
            Owner: {self.__owner}
            Currency: {self.__currencyName}
            Balance: {self.__balance}
        '''
    def convert_account(self, newCurrencyName: str):
        # sprawdzanie czy mozna obsluzyc dana walute w tym banku
        if check_currency(newCurrencyName):
            # connect to api
            try:
                r = requests.get(apiUrl).json()[0]['rates']
                try:
                    currencies = dict()
                    for currency in r:
                        currencies[currency['code']] = currency['mid']

                    # z PLN na obcą lub z obcej na obca 
                    if newCurrencyName != 'PLN':
                        if self.__currencyName == 'PLN':
                            self.__balance = self.__balance * currencies[newCurrencyName]
                            self.__currencyName = newCurrencyName
                        else:
                            # najpierw z powrotem na zlotowki 
                            self.__balance = self.__balance / currencies[self.__currencyName]
                            self.__currencyName = newCurrencyName

                            # potem wedlug przelicznika 
                            self.__balance = self.__balance * currencies[newCurrencyName]
                    # z obcej na PLN 
                    else:
                        
                        # najpierw z powrotem na zlotowki 
                        self.__balance = self.__balance / currencies[self.__currencyName]
                        self.__currencyName = newCurrencyName

              
                except:
                    print('Cos sie spsulo')
            except:
                print('Ups. Cos nie tak z api')
            # baza wartosci jest stosunek waluta / zloty polski
        else:
            print('Konto w danej walucie niedostępne')
        # strzal do api i konwersja waluty

# ======================================================

# oprocentowanie, dodaje odsetki, konto oszczednosciowe

class BankAccountForYoung(BankAccount):
    def __init__ (self, owner: str, percentage: float, currencyName: str = "PLN",balance: float = 0):
        super().__init__(owner, currencyName, balance)
        self.__percentage = percentage
    
    def add_interest(self) -> None: 
        self._BankAccount__balance = round(self._BankAccount__balance*(100+self.__percentage)/100, 2)

# ======================================================

# account = BankAccount('Aleksander')
account = BankAccountForYoung('Aleksander', 10, "PLN", 1000)
print(account)
account.convert_account('USD')
print(account)

account.convert_account('PLN')
print(account)

account.convert_account('USD')
print(account)

account.convert_account('EUR')
print(account)



# print(vars(account))

# print(account)

# account.deposit_money(123.12)

# print(account)

# print(account) if account.withdraw_money(20.12) else print('Za mało środków')

# print(account) if account.withdraw_money(1220.12) else print('Za mało środków')

# account.add_interest()

# print(account)

# account.add_interest()

# print(account)

# account.add_interest()

# print(account)