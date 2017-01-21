class Person(object):
        def __init__(self, name, age, status='child'):
            self.name = name
            self.age = age
            self.status = status
        show_msg = "Hi! I am {}, I am {}, I am a {}."

        def show(self, msg=None):
            if not msg:
                print Person.show_msg.format(self.name, self.age, self.status)
            else:
                print msg.format(self.name, self.status)


family = [Person('Patrick', 46), Person('Jane', 42), Person('Jimmy', 8),
          Person('Mandy', 17)]

print 'Hello, we are the Bloomberg family!'

for person in family:
        person.show()
        if person.age > 18:
            person.status = 'adult'
            person.show('> {} is in fact an {}.')
        elif person.age > 12:
            person.status = 'teenager'
            person.show('> {} is actually a {}.')
