from dataclasses import dataclass, field
@dataclass
class Employee:
    name:str
    id:str
    base:float
    bonuses: dict=field(default_factory=dict)
    deductions: dict=field(default_factory=dict)
    def net_salary(self)->float:
        return self.base+sum(self.bonuses.values()) - sum(self.deductions.values())
    def payslip(self)->str:
        return (
            f"Employee: {self.name} ({self.id})\n"
            f"Base: ${self.base:,.2f}\n"
            f"Bonuses: ${sum(self.bonuses.values()):,.2f}\n"
            f"Deductions: ${sum(self.deductions.values()):,.2f}\n"
            f"Net Pay: ${self.net_salary():,.2f}"
        )
if __name__=="__main__":
    emp=Employee("Jane Doe", "E1024", 5000.0)
    emp.bonuses["Performance"]=500.0
    emp.deductions["Tax"]=650.0
    print(emp.payslip())
