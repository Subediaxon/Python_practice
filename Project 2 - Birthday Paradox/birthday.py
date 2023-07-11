from random import choice;
from random import randrange;
from collections import Counter;


no_bdays=int(input("How many birthdays would you like?(Max100)"))
no_sims=int(input("How many simulations would you like?(Max1000)"))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
def simulation():
    birthdays=[]
    
    for i in range(no_bdays):
        ran_month = choice(months)
        ran_date = randrange(1,30) 
        new_bday = " ".join([ran_month, str(ran_date)])
        birthdays.append(new_bday);
    
    print("Here are ",no_bdays,"birthdays: ");
    print(*birthdays, sep=', ')
    
    dup_birthday_counter = dict(Counter(birthdays))
    max_value=max(zip(dup_birthday_counter.values(), dup_birthday_counter.keys()))[1]
    #print(max_value, "has max repetation of:",dup_birthday_counter.get(max_value))
    print("In this simulation, multiple people have a birthday on ",max_value)
    
    values = dup_birthday_counter.values()
    count= 0
    for val in values:
        if (val > 1):
            count = count + 1;
    
    print(count)        
    return max_value,count
    
sim_check ={}
i=1
while i <= no_sims:
    print()
    print("running simulation", i)
    print()
    max_value,count=simulation()
    sim_check[max_value]=count
    i=i+1;

sim_check_values = sim_check.values()
total_repeat = sum(sim_check_values)
avg_percent =(total_repeat/no_sims)*100

print("Out of", no_sims,"simulations of", no_bdays,"people, there was a matching birthday in that group", total_repeat,"times.")
print("This means that", no_bdays, "people have a", avg_percent,"% chance of having a matching birthday in their group.")
print("That's probably more than you would think!")
