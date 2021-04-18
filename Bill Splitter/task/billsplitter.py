import random

guest_list = {}
guest_number = int(input('Enter the number of friends joining (including you):\n'))
print('\nEnter the name of every friend (including you), each on a new line:')
for i in range(guest_number):
    guest_name = input()
    guest_list[guest_name] = 0
bill_value = int(input('\nEnter the total bill value:\n'))
lucky_option = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if lucky_option == 'Yes':
    lucky_name = random.choice(list(guest_list.keys()))
    print(f'\n{lucky_name} is the lucky one!\n')
    try:
        bill_share = round((bill_value / (guest_number - 1)), 2)
        for k in guest_list:
            guest_list[k] = bill_share
            guest_list[lucky_name] = 0
    except ZeroDivisionError as e:
        pass
else:
    print('\nNo one is going to be lucky\n')
    try:
        bill_share = round((bill_value / guest_number), 2)
        for k in guest_list:
            guest_list[k] = bill_share
    except ZeroDivisionError as e:
        pass
print(guest_list)
