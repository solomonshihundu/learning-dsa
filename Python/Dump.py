

class ManagementHierarchy:
    def __init__(self,data):
        self.data = data
        self.employees = []
        self.parent = None

    def add_employee(self,employee):
        employee.parent = self
        self.employees.append(employee)

    def print_tree(self,tree_type): 
        if tree_type == "name":
             for employee in self.employees: 
                print(employee)
                
        elif tree_type == "designation":
            print(employee.value())
        else:
            print(employee.items())

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def build_management_tree():
    #Define Employes and associated roles
    e_ceo = {"Brian":"CEO"}
    e_cto = {'Jeremy':"CTO"}
    e_infra_head = {'Shillah':"Infrastructure Head"}
    e_cm = {'Lucy':"Cloud Manager"}
    e_am = {'Michael':"Application Manager"}
    e_app_head = {'Pheonah':"Application Head"}
    e_hr_head = {'Sharon':"HR Head"}
    e_rm = {'Denis':"Recruitment Manager"}
    e_pm = {'Shivanah':"Policy Manager"}

    #Declare all parent nodes
    ceo = ManagementHierarchy(e_ceo)
    cto = ManagementHierarchy(e_cto)
    infra_head = ManagementHierarchy(e_infra_head)
    hr_head = ManagementHierarchy(e_hr_head)

    #Add leaf nodes to branch nodes
    hr_head.add_employee(ManagementHierarchy(e_rm))
    hr_head.add_employee(ManagementHierarchy(e_pm))

    infra_head.add_employee(ManagementHierarchy(e_cm))
    infra_head.add_employee(ManagementHierarchy(e_am))

    cto.add_employee(ManagementHierarchy(infra_head))
    cto.add_employee(ManagementHierarchy(e_app_head))
    
    #Add branch nodes to root
    ceo.add_employee(ManagementHierarchy(hr_head))
    ceo.add_employee(ManagementHierarchy(cto))
    
    return ceo



if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
