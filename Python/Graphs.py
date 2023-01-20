class Graph:

    #Constructor converts tuple to Dictionary
    def __init__(self,edges):
        self.edges = edges

        #Dictionary stores start point as keys and possible end points as values
        #All routes dictionary
        self.graph_dict = {}
        for start, end in self.edges:
            
            #If the start point is already in the dictionary i.e Key is present
                #then append the current element as a value to it
            #If the start point is not in the dictionary, then add the end point 
                #as a key in the dictionary      
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        #print("Graph Dict: ",self.graph_dict)

    #Returns path based on start and end values
    def get_paths(self,start,end,path=[]):

        #We start with an empty list and add the start point
        path = path + [start]

        #if start and end points are same return the path
            #since its either we are not moving points
                #or we have reached the break point of the recusion
        if start == end:
            return [path]

        #Return an empty list if start point is not defined
        if start not in self.graph_dict:
            return []

        #List to holds all possible paths from start to end
        paths = []

        #Loop through the all routes dictionary with the start point as key
            #Thus we are looping through the list of possible desitnations
            #associated with the start route
        for node in self.graph_dict[start]:
            #If the current node is not in the initial path lists the we
                #we call the get_paths method recusively, thus the current node will be
                    #added to the inital path list as a new route.
            if node not in path:
                #The path variable at this point hold all the routes from the start to 
                    #current node, we assign it to a local list var
                new_paths = self.get_paths(node,end,path)
                #Loop though the local list while appending each element to the final output
                    #list
                for p in new_paths:
                    paths.append(p)

        #Return the final list of paths
        return paths

    #Returns the shortest path between two points
    def get_shortest_path(self,start,end,path=[]):
        
        #Add the start point to our path list
        path = path + [start]

        #if start and end points are same return the path
            #since its either we are not moving points
                #or we have reached the break point of the recusion
        if start == end:
            return path

        #If the start point is not in the all routes dictionary
            #return None since no such route exists
        if start not in self.graph_dict:
            return None  
        
        #Initialize a var to store the final list of shortest route
        shortest_path = None

        #Loop through the list of routes in the dictionary with the start value as the key
            #if the node is not in the initial path list, call this method recursively 
                #assign the return value of recursion to a var i.e current shortest path, if the variable has a value
                    #if the current shortest path is less than the initial final shortest path
                        #set the current shortest path as the shortest path
                            #return the shortest path
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path



if __name__ == '__main__':
    
    #Define Tuple with all possible routes
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Mumbai","Shenghai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Paris","Toronto"),
        ("Toronto","Los Angeles"),
        ("Toronto","Paris"),
        ("Dubai","New York"),
        ("Dubai","Nairobi"),
        ("Shenghai","Tokyo"),
        ("Shenghai","Nairobi"),
        ("New York","Toronto"),
        ("New York","Tokyo"),
        ("New York","Nairobi"),
        ("Tokyo","Melborne"),
        ("Melborne","Los Angeles"),
        ("Nairobi","Dubai"),
        ("Nairobi","New York"),
        ("Nairobi","Shenghai"),


    ]

    route_graph = Graph(routes)

    start = "Paris"
    end = "Melborne"

    print(f"Paths between {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest Paths between {start} and {end} is : ",route_graph.get_shortest_path(start,end))
    

