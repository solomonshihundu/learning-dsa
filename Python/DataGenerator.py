class Generator:
    def __init__(self,min,max):
        self.min = min
        self.max = max
        self.data_set = []

    def generate_data(self,code = None):

        if code == "ODD":
            for i in range(self.min,self.max):
                if not i % 2 == 0:
                    self.data_set.append(i)
            return self.data_set
            
        elif code == "EVEN":
            for i in range(self.min,self.max):
                if i % 2 == 0:
                    self.data_set.append(i)
            return self.data_set
        else:
            for i in range(self.min,self.max):
                self.data_set.append(i)
            return self.data_set
        
    
    def print_data(self):
        for i in self.data_set:
            print(i)
        return

def data_gen():
    gen = Generator(1,100)
    return gen

if __name__ == '__main__':
    test = data_gen()
    print(test.generate_data())
    #test.print_data()
            

        

