# tests division
dv = '\n' + '-' * 42 + '\n'

# Start of the learning Journey
message = "\nHello Python World! the lack of main and ';' is unsettling\n"
message_2 = "Python Zero to One"
print(message + message_2 + dv)

# Flexible String test
test = "Test of Dynamic strings\n"
print(test)
test = "A smaller string"
print(test + dv)

# Strings...
test1 = 'this is a string\n'
test2 = "this is also a string"
print(test1);
print(test2 + dv);

test3 = 'I told my friend, "Python is my favorite language!"\n'
test4 = "The language 'Python' is named after Monty Python, not the snake."
print(test3)
print(test4 + dv)

#Case and Methods
name = "seiji python/ "
print('$name + title() => ' + name.title())
print('$name + upper() => ' + name.upper())
print('$name + lower() => ' + name.lower() + dv)

#combining/concatenating strings + Special
first_name = 'seiji'
last_name = 'python'
full_name = first_name + " " + last_name
print("Languages:\n\tPython\n\tC\n\tJava\n")
print(full_name + dv)

#stripping Whitespace
language = "                            Python                                 \n"
print("Normal = " + language + "With strip()  = " + language.strip() + dv)

#numbers

number = 42
print ("this is not a " + str(number) + " project")

#end
