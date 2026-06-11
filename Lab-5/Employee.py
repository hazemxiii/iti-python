class Employee:
    employess = []
    def __init__(self,id,first_name,last_name,age,department,salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        # Disabled both methods to prevent adding new user with the same data as an old one when retreiving from database
        # Employee.employess.append(self)
        # self.save(connection)

    def transfere(self,new_dept):
        self.department = new_dept

    def fire(self):
        Employee.employess.remove(self)
        del self

    def show(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}")

    def save(self,connection):
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO employees (first_name,last_name,age,department,salary)
                VALUES (%s,%s,%s,%s,%s)
            """,(self.first_name,self.last_name,self.age,self.department,self.salary))
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
                SET first_name = %s, last_name = %s, age = %s, department = %s, salary = %s
                WHERE id = %s
            """,(self.first_name,self.last_name,self.age,self.department,self.salary,self.id))
            connection.commit()
        except Exception as err:
            print(err)
        finally:
            cursor.close()

    def delete(self,connection):
        try:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM employees
                WHERE id = %s
            """,(self.id,))
            connection.commit()
        except Exception as err:
            print(err)
        finally:
            cursor.close()

    @staticmethod
    def find(emp_id,connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * from employees where id = %s",(emp_id,))
            result = cursor.fetchone()
            return result
        except Exception as err:
            print(err)
        finally:
            cursor.close()

    @staticmethod
    def findAll(connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * from employees")
            result = cursor.fetchall()
            return result
        except Exception as err:
            print(err)
        finally:
            cursor.close()

    @staticmethod
    def list_employees():
        for emp in Employee.employess:
            emp.show()

