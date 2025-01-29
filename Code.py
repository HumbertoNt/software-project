user = True
students = []
week = []

while user:
    case = input('(1) matricula (2) aulas (0) quit')

    if case == '1':
        # Matricula de alunos.
        
        enrollment = True

        while enrollment:
            name = input('Name ')
            clas = input('Class ')
            
            new_aluno = {'name': name, 'class': clas}
            students.append(new_aluno)
            
            repeat = input("More registration? (yes/ no) ")
            if repeat == 'no':
                enrollment = False
                
        print(f"{students}")

# Gestão de aulas.

    if case == '2':
        enrollment = 'true'

        while enrollment:
            print("1 monday 2 tusday 3 wednesday 4 thursday 5 friday 0 quit")
            day = input('What day of the week do you want to change? ')
            
            if day == '1':
                print("Monday: ")
                one = input('time 1: ')
                two = input('time 2: ')
                three = input('time 3: ')
                four = input('time 4: ')
                five = input('time 5: ')
                new_time = {'day': "monday", 'time1': one, 'time2': two, 'time3': three, 'time4': four, 'time5': five}
                week.append(new_time)
            elif day == '2':
                print("tusday: ")
                one = input('time 1: ')
                two = input('time 2: ')
                three = input('time 3: ')
                four = input('time 4: ')
                five = input('time 5: ')
                new_time = {'day': "tusday", 'time 1': one, 'time 2': two, 'time 3': three, 'time 4': four, 'time 5': five}
                week.append(new_time)
            elif day == '3':
                print("wednesday: ")
                one = input('time 1: ')
                two = input('time 2: ')
                three = input('time 3: ')
                four = input('time 4: ')
                five = input('time 5: ')
                new_time = {'day': "wednesday", 'time 1': one, 'time 2': two, 'time 3': three, 'time 4': four, 'time 5': five}
                week.append(new_time)
            elif day == '4':
                print("thursday: ")
                one = input('time 1: ')
                two = input('time 2: ')
                three = input('time 3: ')
                four = input('time 4: ')
                five = input('time 5: ')
                new_time = {'day': "thursday", 'time 1': one, 'time 2': two, 'time 3': three, 'time 4': four, 'time 5': five}
                week.append(new_time)
            elif day == '5':
                print("friday: ")
                one = input('time 1: ')
                two = input('time 2: ')
                three = input('time 3: ')
                four = input('time 4: ')
                five = input('time 5: ')
                new_time = {'day': "friday", 'time 1': one, 'time 2': two, 'time 3': three, 'time 4': four, 'time 5': five}
                week.append(new_time)
            elif day == '0':
                enrollment = False
            
            print(f"{week}")
    if case == '0':
        user = False 
