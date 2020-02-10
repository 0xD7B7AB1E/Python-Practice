import time


def main():
    pass


if __name__ == '__main__':
    # string op
    s = "Hello World!"
    print(type(s))
    t = " Sample program."
    r = s + t
    print(r, len(r))
    x = '100'
    print(type(x))
    y = int(x)
    print(y, type(y))
    print('This string (%s) has %d chars' % (s, len(s)))
    print(s.upper())
    print(s.lower())
    print(s[0])
    print(s[6:])
    print(s[6:-1])
    print(s.strip('!'))

    # lists
    fruits = ['apple', 'orange', 'banana', 'mango']
    print(type(fruits), len(fruits))
    print(fruits[1])
    print(fruits[1:3])
    print(fruits[1:])
    fruits.append('pear')
    print(fruits)
    fruits.remove('mango')
    print(fruits)
    fruits.insert(1, 'mango')
    print(fruits)
    veg = ['potato', 'carrot', 'onion', 'beans', 'radish']
    print(veg)
    eatables = fruits + veg
    print(eatables)
    mixed = ['data', 5, 100.1, 8287398]  # py 8 doesn't support trailing I or L
    print(type(mixed), mixed)
    for mix in mixed:
        print(type(mix))
    nested = [fruits, veg]
    print(nested)

    # tuples
    fruits = ('apple', 'mango', 'banana', 'pineapple')
    print(fruits, type(fruits), len(fruits))
    print(fruits[0])
    print(fruits[:2])
    veg = ('potato', 'carrot', 'onion', 'radish')
    eatables = fruits + veg
    print(eatables)

    # dict
    student = {
        'name': 'Mary',
        'id': '8776',
        'major': 'CS'
    }
    print(student, type(student), len(student))
    print(student['name'])
    print(student.items())
    print(student.keys())
    print(student.values())
    print(student)
    student1 = {
        'name': 'David',
        'id': '9876',
        'major': 'ECE'
    }
    students = {'1': student, '2': student1}
    print(students)
    print('name' in student.keys())
    print('grade' in student.keys())

    # type conv
    a = 10000
    print(str(a))
    print(int(a))
    print(float(a))
    # print(long(a))  # invalid
    s = 'aeiou'
    print(list(s))
    x = ['mango', 'apple', 'banana', 'mango', 'banana']
    print(set(x))

    # if
    a = 25 ** 5
    if a > 10000:
        print('More')
    else:
        print('Less')
    if a > 10000:
        if a < 100000:
            print('Betweeen 10k and 100k')
        else:
            print('More than 100k')
    elif a == 10000:
        print('Equal to 10k')
    else:
        print('Less than 10k')
    s = 'Hello World'
    if 'World' in s:
        s += '!'
        print(s)
    student = {
        'name': 'Mary',
        'id': '8776'
    }
    if 'major' not in student.keys():
        student['major'] = 'CS'
    print(student)

    # for
    hS = "Hello World"
    fruits = ['apple', 'orange', 'banana', 'mango']
    student = {
        'name': 'Mary',
        'id': '8776',
        'major': 'CS'
    }
    for c in hS:
        print(c)
    i = 0
    for item in fruits:
        print('Fruit-%d: %s' % (i, item))
        i += 1
    for key in student:
        print('%s: %s' % (key, student[key]))

    # while
    i = 0
    while i <= 100:
        if i % 2 == 0:
            print(i)
        i += 1

    # range
    print(list(range(10)))
    print(list(range(10, 110, 10)))

    # break continue
    y = 1
    for x in range(4, 256, 4):
        y = y * x
        if y > 512:
            break
        print(y)
    fruits = ['apple', 'orange', 'banana', 'mango']
    for item in fruits:
        if item == 'banana':
            continue
        else:
            print(item)

    # pass
    fruits = ['apple', 'orange', 'banana', 'mango']
    for item in fruits:
        if item == 'banana':
            pass
        else:
            print(item)

    # functions
    students = {'1': {'name': 'Bob', 'grade': 2.5},
                '2': {'name': 'Mary', 'grade': 3.5},
                '3': {'name': 'David', 'grade': 4.2},
                '4': {'name': 'John', 'grade': 4.1},
                '5': {'name': 'Alex', 'grade': 3.8}}


    def average_grade(_students):
        _sum = 0.0
        for _key in _students:
            _sum = _sum + _students[_key]['grade']
        average = _sum / len(_students)
        return average


    avg = average_grade(students)
    print("The average garde is: %0.2f" % avg)


    def display_fruits(_fruits=['apple', 'orange']):
        print("There are %d fruits in the list" % (len(_fruits)))
        for _item in fruits:
            print(_item)


    display_fruits()
    display_fruits(fruits)


    def print_student_records(name, age=20, major='CS'):
        print("Name: " + name)
        print("Age: " + str(age))
        print("Major: " + major)


    # print_student_records() # error
    print_student_records(name='Alex')
    print_student_records(name='Bob', age=22, major='ECE')
    print_student_records(name='Alan', major='ECE')


    def student(name, **kwargs):
        print("Student Name: " + name)
        for _key in kwargs:
            print(_key + ': ' + kwargs[_key])


    student(name='Bob', age='20', major='CS')


    def student(name, *varargs):
        print('Name: ' + name)
        for _item in varargs:
            print(_item)


    student('Nav')
    print('')
    student('Amy', 'Age: 24')
    print('')
    student('Bob', 'Age: 20', 'Major: CS')

    import email

    dir(email)
    import email

    dir(email)
    import email

    dir(email)
    fruit = ['mango', 'banana']
    veg = ['potato', 'tomato']

    food = fruit + veg
    with open('file.txt', 'w') as food_fp:
        for f in food:
            food_fp.write(f+'\n')
    food_fp = open('file.txt', 'r')
    content = food_fp.read()
    print(content)
    fp = open('file.txt', 'r')
    content = fp.read()
    print(content)
    fp = open('file.txt', 'r')
    content = fp.read()
    print(content)
    fp = open('file.txt', 'r')
    print("Line-1 : " + fp.readline())
    fp = open('file.txt', 'r')
    print("Line-1 : " + fp.readline())
    fp = open('file.txt', 'r')
    print("Line-1 : " + fp.readline())
    fp = open('file.txt', 'r')
    lines = fp.readlines()
    for line in lines:
        print(line)
    fp = open('file.txt', 'r')
    lines = fp.readlines()
    for line in lines:
        print(line)
    fp = open('file.txt', 'r')
    lines = fp.readlines()
    for line in lines:
        print(line)
    fp = open('file.txt', 'r')
    lines = fp.readlines()
    for line in lines:
        print(line)
    fruit = ['mango', 'banana']
    veg = ['potato', 'tomato']

    food = fruit + veg
    food_fp = open('file.txt', 'r')
    fp.read(10)
    fp = open('file.txt', 'r')
    fp.read(10)
    fp = open('file.txt', 'r')
    fp.seek(10, 0)
    content = fp.read(10)
    print(content)
    fp = open('file.txt', 'r')
    fp.seek(10, 0)
    content = fp.read(10)
    print(content)
    fp = open('file.txt', 'r')
    fp.seek(10, 0)
    content = fp.read(10)
    print(content)
    fp = open('file.txt', 'w')
    content = 'assasasadsafsdasd'
    fp.write(content)
    fp.close()
    fp = open('file.txt', 'w')
    content = 'assasasadsafsdasd'
    fp.write(content)
    fp.close()
    fp = open('file.txt', 'w')
    content = 'assasasadsafsdasd'
    fp.write(content)
    fp.close()
    fp = open('file.txt', 'w')
    content = 'assasasadsafsdasd'
    fp.write(content)
    fp.close()

    now_time = time.time()
    time.localtime(now_time)
    time.asctime(time.localtime(now_time))


    class Student:
        studentCount = 0
        grades = {}

        def __init__(self, name, _id):
            self.name = name
            self.id = _id
            Student.studentCount = Student.studentCount + 1

        @staticmethod
        def get_student_count():
            return Student.studentCount

        def get_grade(self, _key):
            return self.grades[_key]

        def add_grade(self, _key, value):
            self.grades[_key] = value


    s = Student('Steve', '8789')
    s.add_grade('Math', '90')
    s.add_grade('English', '89')
    s.get_grade('Math')


    class Shape:
        def __init__(self):
            self.color = 'Green'
            self.lineWeight = 10.0

        @staticmethod
        def draw():
            print("Draw-to be implemented")

        def set_color(self, _c):
            self.color = _c

        def get_color(self):
            return self.color

        def set_line_weight(self, lwt):
            self.lineWeight = lwt

        def get_line_weight(self):
            return self.lineWeight


    class Point:
        def __init__(self, _x, _y):
            self.xCoordinate = _x
            self.yCoordinate = _y

        def set_x(self, _x):
            self.xCoordinate = _x

        def set_y(self, _y):
            self.yCoordinate = _y

        def get_x(self):
            return self.xCoordinate

        def get_y(self):
            return self.yCoordinate


    class Circle(Shape):
        def __init__(self, _p, _r):
            super().__init__()
            self.center = _p
            self.radius = _r

        def set_center(self, _c):
            self.center = _c

        def get_center(self):
            return self.center

        def set_radius(self, _r):
            self.radius = _r

        def get_radius(self):
            return self.radius

        def draw(self):
            print("Draw Circle (overriden function)")


    p = Point(2, 6)
    cir = Circle(p, 9)
    cir.get_color()
    cir.set_color('red')
    cir.get_color()
    cir.get_line_weight()
    cir.draw()
    print(cir.radius)
