users = ['iker','admin','joseba','camilo']

for user in users:
    if user == 'admin':
        message = "(Admin) Hola presidente"
    else: 
        message = "Hola " + user
    print(message)