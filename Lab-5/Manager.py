from Employee import Employee

class Manager(Employee):
    def __init__(self,id,first_name,last_name,age,department,salary,managed_department):
        super().__init__(id,first_name,last_name,age,department,salary)
        self.managed_department = managed_department


    def save(self,connection):
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO employees (first_name,last_name,age,department,salary,managed_department)
                VALUES (%s,%s,%s,%s,%s,%s)
            """,(self.first_name,self.last_name,self.age,self.department,self.salary,self.managed_department))
            connection.commit()
        except Exception as err:
            print(err)
        finally:
            cursor.close()

    def update(self,connection):
        try:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE employees
                SET first_name = %s, last_name = %s, age = %s, department = %s, salary = %s, managed_department = %s
                WHERE id = %s
            """,(self.first_name,self.last_name,self.age,self.department,self.salary,self.managed_department,self.id))
            connection.commit()
        except Exception as err:
            print(err)
        finally:
            cursor.close()

    def show(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: Confedential")

