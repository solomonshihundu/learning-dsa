class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

 
    def print_tree(self):
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""

        print(prefix + self.data + ' ('+ str(self.get_level()) +')')
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_tree_by_level(self,level):
       
        if self.get_level() > level:
            return

        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree_by_level(level)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def build_state_tree():
    
    world = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    karnataka = TreeNode("Karnataka")
    usa = TreeNode("USA")
    jersey = TreeNode("New Jersey")
    calif = TreeNode("California")

    gujarat.add_child(TreeNode("Ahmendabad"))
    gujarat.add_child(TreeNode("Baroda"))
    india.add_child(gujarat)

    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))
    india.add_child(karnataka)

    jersey.add_child(TreeNode("Princeton"))
    jersey.add_child(TreeNode("Trenton"))

    calif.add_child(TreeNode("San Francisco"))
    calif.add_child(TreeNode("Mountain View"))
    calif.add_child(TreeNode("Palo Alto"))

    usa.add_child(jersey)
    usa.add_child(calif)

    world.add_child(india)
    world.add_child(usa)

    return world

if __name__ == '__main__':
    root = build_state_tree()
    
    print("########### Normal Tree ###########")
    root.print_tree()

    print("########### Level One ###########")
    root.print_tree_by_level(1)

    print("########### Level Two ###########")
    root.print_tree_by_level(2)

    print("########### Level Three ###########")
    root.print_tree_by_level(3)
