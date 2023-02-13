from DataGenerator import Generator

def swap(a,b,arr):
    if a != b:
        arr[a],arr[b] = arr[b],arr[a]

def partition(low,high,elements):
    
    pivot = elements[high]
    #The first element is the partion index
    p_index = 0
    
    i = low - 1

    for p_index in range(low,high):
        if(elements[p_index] <= pivot):
            i += 1
            swap(i,p_index,elements)
    swap(i+1,high,elements)
    return (i + 1)


def quick_sort(low,high,elements):
    if low < high:
        pi = partition(low,high,elements)
        quick_sort(low,pi-1,elements)
        quick_sort(pi+1,high,elements)

if __name__ == '__main__':
    #Initialize test data
    gen = Generator(1,10)
    #data_set = gen.generate_data("RAND") 
    data_set = [2, 4, 6, 3, 9, 8, 5, 1, 7]

    print(data_set)
    quick_sort(0,len(data_set) - 1, data_set)
    print(data_set)