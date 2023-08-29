print('Achtung: Es handelt sich hierbei um Bruttobeträge!')

gehaltswunsch = input('Bitte gib hier dein gewünschtes Stundengehalt ein: ')
stdpw = input('Wie viele Stunden pro Woche arbeitest du? ')


monthlySalary = (float(gehaltswunsch) * float(stdpw)) * 4
weeklySalary = float(gehaltswunsch) * float(stdpw)
dailySalary = float(gehaltswunsch) * (float(stdpw) / 5)
yearlySalary = float(monthlySalary) * 12

print('Pro Tag verdienst du ' + str(dailySalary) + '€.')
print('Du verdienst ' + str(weeklySalary) + '€ pro Woche!')
print('Im Monat macht das dann ' + str(monthlySalary) + '€!')
print('Dein Brutto-Jahresgehalt ist also ' + str(yearlySalary) + '€!')

if (float(gehaltswunsch) * float(stdpw)) <= 600:
    print('Fauler Sack, arbeite mehr!')
else:
    print('Davon kann man doch ganz gut leben.')

input('Drücke eine beliebige Taste um das Programm zu schließen.')
