current_users = ['John', 'Andy', 'Maria', 'Victor', 'Sandy'];
new_users = ['Marie', 'nelson', 'john', 'julian', 'VictOr'];

current_user_lower = [];
for user in current_users :
    current_user_lower.append(user.lower());

for user in new_users:
    if user.lower() in current_user_lower :
        print(user + " is invalid. Please enter a new username.");
    else :
        print(user + " is available.");
