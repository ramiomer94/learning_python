sandwich_orders = ['tuna', 'meatball', 'steak & cheese', 'turkey breast']
sandwich_orders.append('chicken and bacon ranch')
sandwich_orders.insert(2,'pastrami');
sandwich_orders.insert(5, 'pastrami');
sandwich_orders.append('pastrami')

finished_sandwiches = []

print("Sorry, we ran out of pastrami")

while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')


while sandwich_orders :
    current_order = sandwich_orders.pop()
    print("I made your " + current_order.title() + " sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following orders have been completed: ")
for finished_sandwich in finished_sandwiches :
    print(finished_sandwich.title());