from Person import Person  # ����������� ����� Person �� ����� Person
from Employee import Employee  # ����������� ����� Person �� ����� Person
from Models.ORG_DTO import ORG_DTO


    
    
def CreateOrganization():
    GOKL = ORG_DTO()
    GOKL.ORG_id = 1
    GOKL.ORG_name = "GOKL"    
    print(f"{GOKL.ORG_name}")

def main():
    CreateOrganization()
    
    
if __name__ == "__main__":
    main()
    