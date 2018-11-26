# inputs:
# total cost of the bill
# month of the year
# year
# number of Rosario's days abroad

# singleDayCost_perCapita = tot amount / (giorni del mese * 2)
# RosDayInHouse = giorni mese - giorni fuori
# RosAmount = singleDayCost_perCapita * RosDayInHouse
# LandLordAmount = BillTOT - RosAmount

import sys
import calendar
from datetime import date as dt

supportEmail = 'enrico.pascai@gmail.com'

class Bill:
    def __init__(self):
        self.amount = None
        self.month = None
        self.year = None
        self.daysAbroad = None
    def calculate_amountPerCapita(self, totAmount, month, year, daysAbroad):
        amount_perCapita = [0, 0]
        daysInMonth = calendar.monthrange(year, month)[1]
        singleDayCost_perCapita = totAmount / (daysInMonth * 2)
        RosDaysInHouse = daysInMonth - daysAbroad
        amount_perCapita[0] = singleDayCost_perCapita * RosDaysInHouse #RosAmount
        amount_perCapita[1] = totAmount - amount_perCapita[0] #LandLordAmount
        return amount_perCapita

bill = Bill()
bill.amount = float(input('Please, enter the total amount of the bill: '))
bill.month = int(input('Please, enter the month of the bill '
                    '(1 = January; 12 = December): '))
bill.year = int(input('Please, enter the year of the bill: '))
bill.daysAbroad = int(input('Please, enter your number of days abroad: '))

print('------------------------------------------------------\nRECAP')
print('Amount of the bill: ' + str(bill.amount) + '€')
print('Month&Year of the bill: ' + calendar.month_name[bill.month] + ' ' + str(bill.year))
print('Number of days abroad: ' + str(bill.daysAbroad) + ' / ' + str(calendar.monthrange(bill.year, bill.month)[1]))

amount_perCapita = bill.calculate_amountPerCapita(bill.amount, bill.month, bill.year, bill.daysAbroad)

print('------------------------------------------------------\nAMOUNT DUE')
print('Your amount (Rosario) is equal to ' + str(round(amount_perCapita[0], 1)) + '€')
print('Landlord\'s amount is equal to ' + str(round(amount_perCapita[1], 1)) + '€')
