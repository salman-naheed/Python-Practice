import mycode as person

print(person.name)
person.greet()
person.toFile('test.txt')

person.name='salman naheed'
person.greet()

person.fromFile('test.txt')
person.greet()