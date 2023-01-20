class TreeNode:
    def __init__(self,name,role):
        self.name = name
        self.role = role
        self.employees = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_employee(self,child):
        child.parent = self
        self.employees.append(child)

 
    def print_tree(self,property):
        if property == "name":
            value = self.name
        elif property == "designation":
            value = self.role
        else:
            value = self.name + " (" + self.role + ")"
            
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""

        print(prefix + value)
        if self.employees:
            for employee in self.employees:
                employee.print_tree(property)

def build_management_tree():
    #Define Employes and associated roles
    e_ceo = {"name":"Brian","role":"CEO"}
    e_cto = {'name':'Jeremy',"role":"CTO"}
    e_infra_head = {'name':'Shillah',"role":"Infrastructure Head"}
    e_cm = {'name':'Lucy',"role":"Cloud Manager"}
    e_am = {'name':'Michael',"role":"Application Manager"}
    e_app_head = {'name':'Pheonah',"role":"Application Head"}
    e_hr_head = {'name':'Sharon',"role":"HR Head"}
    e_rm = {'name':'Denis',"role":"Recruitment Manager"}
    e_pm = {'name':'Shivanah',"role":"Policy Manager"}

    #Declare all parent nodes
    ceo = TreeNode(e_ceo["name"],e_ceo["role"])
    cto = TreeNode(e_cto["name"],e_cto["role"])
    infra_head = TreeNode(e_infra_head["name"],e_infra_head["role"])
    hr_head = TreeNode(e_hr_head["name"],e_hr_head["role"])

    #Add leaf nodes to branch nodes
    hr_head.add_employee(TreeNode(e_rm["name"],e_rm["role"]))
    hr_head.add_employee(TreeNode(e_pm["name"],e_pm["role"]))

    infra_head.add_employee(TreeNode(e_cm["name"],e_cm["role"]))
    infra_head.add_employee(TreeNode(e_am["name"],e_am["role"]))

    cto.add_employee(infra_head)
    cto.add_employee(TreeNode(e_app_head["name"],e_app_head["role"]))
    
    #Add branch nodes to root
    ceo.add_employee(hr_head)
    ceo.add_employee(cto)
    
    return ceo



if __name__ == '__main__':
    root_node = build_management_tree()
    print("Names ####################################################") # prints only name hierarchy
    root_node.print_tree("name") # prints only name hierarchy
    print("Roles ####################################################") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    print("All Records ####################################################") # prints both (name and designation) hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy

    