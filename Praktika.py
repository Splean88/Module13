print('10% discount when buying more then three tickets!')
try:
    tickets = int(input("How many tickets do you want to buy?:"))
    if tickets <=0:
        print(OSError)
except ValueError as Error:
    print(Error)
sum = 0
s1 = 990
s2 = 1390
for tickets in range(tickets):
    print('How old are you?')
    age = int(input('age?'))
    if age < 18:
        sum += 0
    if 18 <= age < 25:
            sum += s1
    if age >=25:
            sum += s2
    if tickets > 3:
        sum = sum*0.9
        print(f'discount 10%: {sum}rub')
else:
    print(f'purchase amount: {sum}rub')


