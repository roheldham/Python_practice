from sys import argv

script, user_name = argv
prompt = '>'

print (f"Hi {user_name}, I'm the {script} script")
print (f"Do you like me {user_name}?")
likes = input(prompt)

print (f"Where do you live {user_name}?")
lives = input(prompt)

print (f"""
Alright, so you said that you {likes} me 
and that you live in {lives}
""")