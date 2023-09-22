from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found'
    )


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')
    


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.select()  # Replace 'Employee' with your actual model name
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    try:
        employee = Employee.get(Employee.name == name)  # Replace 'Employee' with your actual model name
        print(employee)
    except Employee.DoesNotExist:
        print(f"Employee {name} not found")


def find_employee_by_id():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.get_by_id(employee_id)  # Replace 'Employee' with your actual model name
        print(employee)
    except ValueError:
        print("Invalid input for employee id")
    except Employee.DoesNotExist:
        print(f"Employee {employee_id} not found")


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")

    try:
        employee = Employee.create(name=name, job_title=job_title, department_id=department_id)  # Replace 'Employee' with your actual model name
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error creating employee: {e}")


def update_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.get_by_id(employee_id)  # Replace 'Employee' with your actual model name

        new_name = input("Enter the employee's new name: ")
        new_job_title = input("Enter the employee's new job title: ")
        new_department_id = input("Enter the employee's new department id: ")

        employee.name = new_name
        employee.job_title = new_job_title
        employee.department_id = new_department_id
        employee.save()

        print(f"Success: {employee}")
    except ValueError:
        print("Invalid input for employee id")
    except Employee.DoesNotExist:
        print(f"Employee {employee_id} not found")
    except Exception as e:
        print(f"Error updating employee: {e}")


def delete_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.get_by_id(employee_id)  # Replace 'Employee' with your actual model name
        employee.delete_instance()
        print(f"Employee {employee_id} deleted")
    except ValueError:
        print("Invalid input for employee id")
    except Employee.DoesNotExist:
        print(f"Employee {employee_id} not found")
    except Exception as e:
        print(f"Error deleting employee: {e}")


def list_department_employees():
    try:
        department_id = int(input("Enter the department's id: "))
        department = Department.get(Department.id == department_id)  # Replace 'Department' with your actual model name
        employees = department.employees
        for employee in employees:
            print(employee)
    except ValueError:
        print("Invalid input for department id")
    except Department.DoesNotExist:
        print(f"Department {department_id} not found")