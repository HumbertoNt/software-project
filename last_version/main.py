students = [
    {'matricula': '0001', 'name': 'Joao', 'class': '5A', 'absence': 0, 'extra': []},
    {'matricula': '0002', 'name': 'Maria', 'class': '5A', 'absence': 0, 'extra': []},
    {'matricula': '0003', 'name': 'Pedro', 'class': '7C', 'absence': 0, 'extra': []}
]

days = [
    {'day': 'Monday', 'time': {'one': '-', 'two': '-', 'three': '-', 'four': '-', 'five': '-'}},
    {'day': 'Tuesday', 'time': {'one': '-', 'two': '-', 'three': '-', 'four': '-', 'five': '-'}},
    {'day': 'Wednesday', 'time': {'one': '-', 'two': '-', 'three': '-', 'four': '-', 'five': '-'}},
    {'day': 'Thursday', 'time': {'one': '-', 'two': '-', 'three': '-', 'four': '-', 'five': '-'}},
    {'day': 'Friday', 'time': {'one': '-', 'two': '-', 'three': '-', 'four': '-', 'five': '-'}}
]

# Materials distributed
library = ['mathlist5A.pdf']

exams = [ 
    {'class': '5A', 'subject': 'math', 'date': '27/02/2025'},
]

extraActivities = [ 
    {'activity': 'libras', 'vacancies': 4}
]

gradebook = [
    {'matricula': '0001', 'math': {'ab1': 8, 'ab2': 0}, 'science': {'ab1': 2, 'ab2': 0}},
    {'matricula': '0002', 'math': {'ab1': 7, 'ab2': 0}, 'science': {'ab1': 9, 'ab2': 0}},
    {'matricula': '0003', 'math': {'ab1': 9, 'ab2': 0}, 'science': {'ab1': 4, 'ab2': 0}}
]

payment = [
    {'matricula': '0001', 'installments': 5},
    {'matricula': '0002', 'installments': 7},
    {'matricula': '0003', 'installments': 2}
]

admin = ['admin_badu']
play = True

while play:
    index = 0
    found = False
    case = input('(0) quit (1) Admin (2) Student ')
    
    if case == '0':
        play = False
    
    if case == '1':  # Portal do professor.
        user = input('user: ')
        while index < len(admin):

            if admin[index] == user:
                found = True
                print(f"\nAccess granted:")
                print(f"Registration: {admin[index]}")

                while True:
                    case = input('(0) quit (1) enroll students (2) list of students (3) daily attendance (4) timetables (5) exams (6) library (7) gradebook (8) manage extra activities: ')

                    if case == '0':
                        break

                    if case == '1':
                        while True:
                            name = input('Name: ')
                            clas = input('Class: ')
                            installment = int(input('installments paid: '))
                            

                            matricula_number = str(len(students) + 1).zfill(4)
                            

                            new_student = {'matricula': matricula_number, 'name': name, 'class': clas, 'absence': 0, 'extra': []}
                            new_grade = {'matricula': matricula_number, 'math': {'ab1': 0, 'ab2': 0}, 'science': {'ab1': 0, 'ab2': 0}}
                            new_payment = {'matricula': matricula_number, 'installments': 12 - installment}
                            students.append(new_student)
                            gradebook.append(new_grade)
                            payment.append(new_payment)

                            repeat = input('More registrations? (yes/ no): ')
                            if repeat.lower() == 'no':
                                break

                    if case == '2':
                        print("\nList of enrolled students:")
                        for student in students:
                            print(f"{student['matricula']} - {student['name']} ({student['class']}) ({student['absence']})")

                    if case == '3':
                        class_input = input('Class: ')

                        attendance = 0
                        while attendance < len(students):
                            if students[attendance]['class'] == class_input:
                                print(f"{students[attendance]['name']} ")
                                check = input('Present? (y/n) ')
                                if check.lower() == 'n':
                                    students[attendance]['absence'] += 1
                            attendance += 1

                    if case == '4':
                        for day in days:
                            print(f"{day['day']}:")
                            for time_slot, subject in day['time'].items():
                                print(f"  {time_slot.capitalize()}: {subject}")
                            print()
                        while True:
                            case = input('(0) quit (1) edit ')
                            if case == '0':
                                break

                            if case == '1':
                                day = input('Day of the week: ').capitalize()
                                time_slot = input('Time slot (one, two, three, four, five): ').lower()
                                new_subject = input('Subject: ')

                                for day in days:
                                    if day['day'].lower() == day.lower():
                                        if time_slot in day['time']:
                                            day['time'][time_slot] = new_subject
                                            print(f"\n{new_subject} added to {day} at {time_slot}!\n")
                                            found = True
                                            break

                                if not found:
                                    print("\n Invalid day or time slot. Please try again.\n")

                                for day in days:
                                    print(f"{day['day']}:")
                                    for time_slot, subject in day['time'].items():
                                        print(f"  {time_slot.capitalize()}: {subject}")
                                    print()                                          

                    if case == '5':
                        while True:
                            option = input('\n(0) quit (1)add: ')
                            
                            if option == '0':
                                break

                            if option == '1':
                                clas = input('Class: ')
                                subject = input('Subject: ')
                                date = input('Date :')
                                
                                exam = {'class': clas, 'subject': subject, 'date': date}
                                exams.append(exam)
                            
                    
                    if case == '6':
                        while True:
                            print("\nLibrary:", library)
                            edit = input('(0) quit (1) remove or (2) add? ')

                            if edit == '0':
                                break

                            if edit == '1':
                                for index, item in enumerate(library):
                                    print(f"{index} {item}")        

                                num = input("Delete number or no: ('num'/ no) ")

                                if num.lower() == 'no':
                                    break

                                num = int(num)
                                library.pop(num)

                            if edit == '2':
                                new_file = input('New file: ')
                                library.append(new_file)
                    
                    if case == '7':
                        while True:
                            case = input('(0) quit (1) print (2) edit: ')

                            if case == '0':
                                break

                            if case == '1':
                                for student in gradebook:
                                    print(f"Registration: {student['matricula']}")
                                    for subject, grades in student.items():
                                        if subject != 'matricula':
                                            print(f"  {subject.capitalize()}:")
                                            for evaluation, grade in grades.items():
                                                print(f"    {evaluation.upper()}: {grade}")
                                    print("-" * 30)
                            
                            if case == '2':
                                matricula = input('id aluno: ')
                                subject = input('subject: ')
                                assessment = input('assessment (ex: ab1, ab2): ')
                                new_grade = input('new grade: ')

                                for aluno in gradebook:
                                    if aluno['matricula'] == matricula:  # Encontra o aluno pela matrícula
                                        if subject in aluno:  # Verifica se a matéria existe
                                            if assessment in aluno[subject]:  # Verifica se a avaliação existe
                                                aluno[subject][assessment] = new_grade  # Atualiza a nota
                                                print(f"Changed {assessment.upper()} grade in {subject.capitalize()} to {new_grade}.")
                                            else:
                                                print(f"assessment '{assessment}' not found.")
                                        else:
                                            print(f"subject '{subject}' not found.")
                                        break  # Sai do loop após encontrar o aluno
                                else:
                                    print("Matrícula não encontrada.")

                    if case == '8':
                        print("\nManaging Extra Activities:")
                        print("Available Activities:")
                        for activity in extraActivities:
                            print(f"  - {activity['activity']} (Vacancies: {activity['vacancies']})")

                        edit = input('(0) quit (1) add or (2) student enrollment? ')
                        
                        if case == '0':
                            break

                        if edit == '1':
                            name = input('name: ')
                            vacancie = int(input('Vacancies: '))

                            new_activity = {'activity': name, 'vacancies': vacancie}
                            extraActivities.append(new_activity)

                        if edit == '2':
                            activity_name = input("Enter the name of the activity to add or 'exit' to go back: ")
                            if activity_name.lower() == 'exit':
                                continue

                            # Check if the activity exists and if there are vacancies
                            for activity in extraActivities:
                                if activity['activity'].lower() == activity_name.lower():
                                    if int(activity['vacancies']) > 0:
                                        student_matricula = input("Enter the student's registration number for enrollment: ")
                                        student = next((s for s in students if s['matricula'] == student_matricula), None)

                                        if student:
                                            if 'extra' not in student:
                                                student['extra'] = []

                                            student['extra'].append(activity_name)
                                            activity['vacancies'] = str(int(activity['vacancies']) - 1)
                                            print(f"{student['name']} has been enrolled in the activity {activity_name}. Remaining vacancies: {activity['vacancies']}")
                                        else:
                                            print("Registration number not found.")
                                    else:
                                        print(f"Sorry, no vacancies available for {activity_name}.")
                                    break
                            else:
                                print(f"Activity {activity_name} not found.")

            index += 1  # Move to next admin user
        
        # Login denied:
        if not found:
            print("User not found.\n")
    
    if case == '2':
        id = input('Registration number: ')

        while index < len(students):
            if students[index]['matricula'] == id:
                found = True
                print(f"\nStudent found:")
                print(f"Registration: {students[index]['matricula']}")
                print(f"Name: {students[index]['name']}")
                print(f"Class: {students[index]['class']}\n")
                while True:
                    case = input('(0) quit (1) attendance (2) timetables (3) exams (4) library (5) gradebook (6) payments (7) extra activities: ')
                    
                    if case == '0':
                        break

                    if case == '1':
                        print(f"\nAttendance for {students[index]['name']} is {students[index]['absence']} days.\n")

                    if case == '2':
                        for day in days:
                            print(f"{day['day']}:")
                            for time_slot, subject in day['time'].items():
                                print(f"  {time_slot.capitalize()}: {subject}")
                            print()
                    
                    if case == '3':
                        for exam in exams:
                            if exam['class'] == students[index]['class']:
                                print(f"{exam['subject']} exam scheduled for {exam['date']}")
                    
                    if case == '4':
                        print("\nLibrary files:")
                        for file in library:
                            print(file)
                    
                    if case == '5':
                        for student in gradebook:
                            if student['matricula'] == students[index]['matricula']:
                                print(f"\nGrades for {students[index]['name']}:")
                                for subject, grades in student.items():
                                    if subject != 'matricula':  # Ignore registration number
                                        print(f"  {subject.capitalize()}:")
                                        for evaluation, grade in grades.items():
                                            print(f"    {evaluation.upper()}: {grade}")
                                print("-" * 30)
                                
                    if case == '6':
                        for pay in payment:
                            if pay['matricula'] == students[index]['matricula']:
                                print(f"\nPayment status for {students[index]['name']}:")
                                print(f"Remaining installments: {pay['installments']}")
                                
                    if case == '7':  # Extra activities
                        print(f"\nExtra activities for {students[index]['name']}:")
                        for extra in students[index]['extra']:
                            print(f"  - {extra}")

            index += 1
        
        if not found:
            print("Student not found.")
