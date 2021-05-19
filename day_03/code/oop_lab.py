class employee:


    # Data/attributes
    def __init__(self, empname, empage, empcompany):
        print('SELF:', self)
        self.name    = empname
        self.age     = empage
        self.salary  = ''
        self.company = empcompany
        self.country = ''
        self.tax     = 0


    # Member functions/methods

    def printstatus(self):
        pass

    # setter
    def setsalary(self, empsal):
        pass

    # getter
    def getsalary(self):
        pass

    # logic
    def calctax(self):
        pass

    def gettax(self):
        pass
# -------------------------------------------------------------------------

# Test Code

if __name__ == "__main__":

    e1 = employee('Anil', 30, 'oracle')
    e2 = employee('Sunil', 21, 'genpact')

    # -------------------------------------------------------------------------


    e1.printstatus()
    e2.printstatus()

    # e1.salary = '1000000'
    e1.setsalary('1000000')
    e2.setsalary('2000000')

    e1.printstatus()
    e2.printstatus()

    print('E1 :', e1.getsalary())
    print('E2 :', e2.getsalary())

    e1.calctax()
    e2.calctax()

    e1.printstatus()
    e2.printstatus()


