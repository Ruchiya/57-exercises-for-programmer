current_employee = ['John Smith',
                    'Jackie Jackson',
                    'Chris Jones',
                    'Amanda Cullen',
                    'Jeremy Goodwin']

def remove(employee):
    if employee in current_employee:
        current_employee.remove(employee)
        return True
    else:
        return False

    
print(f'There are {len(current_employee)} employees:')

for employee in current_employee:
        print(employee)

employee = input('Employee remove?:')
remove(employee)
print(f'There are {len(current_employee)} employees:')
for employee in current_employee:
    print(employee)
