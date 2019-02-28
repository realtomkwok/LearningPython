from sys import argv

script, user_name = argv
prompt = '>'

print(f"hi {user_name}, im the {script} script.")
print("id like to ask you a few questions.")
print(f"do you like me {user_name}")
likes = input(prompt)

print(f"where do ya live {user_name}?")
lives = input(prompt)

print("what kind of computer do ya have")
computer = input(prompt)

print(f"""
Alright, so you said {likes} bout liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")