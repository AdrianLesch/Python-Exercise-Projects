# Testprogramm Python Kurs
name = input('Bitte gebe hier den Namen des Vermieters ein: ')
mein_name = 'Adrian Lesch'
age = '32'

city = 'München'
job = 'Sales Consultant'
newJob = "Software Developer"
new_City= 'Benjendorf'

is_woman = True

if is_woman:
    print('Sehr geehrte Frau ' + name + ',')
else:
    print('Sehr geehrter Herr ' + name + ',')

print('Mein Name ist ' + mein_name + '.')
print('Ich bin ' + age + ' Jahre alt und ich wohne in momentan in ' + city + '.')
print('Momentan arbeite ich als ' + job + ' beginne aber einen neuen Job als ' + newJob + ' in ' + new_City + '.')

input('Bitte beliebige Taste drücken.')