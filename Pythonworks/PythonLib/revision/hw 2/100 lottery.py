import random
lottery_tickets=[]
print("genrating 100 random lottery tickets:")
for i in range(100):
    lottery_tickets.append(random.randrange(1000000000,9999999999))
winners=random.sample(lottery_tickets,2)
print("two lucky tickets are:",winners)
