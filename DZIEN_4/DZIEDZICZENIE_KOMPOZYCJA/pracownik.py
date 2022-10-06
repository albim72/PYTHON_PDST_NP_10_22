class Salary:

    def __init__(self,pay):
        self.pay = pay

    def get_total(self):
        return (self.pay*12)


class Pracownik:

    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)

    def annual_salary(self):
        return f"Do wypłaty: {self.obj_salary.get_total() + self.bonus}"


prac1 = Pracownik(789,1500)
print(f"{prac1.annual_salary()} zł")
