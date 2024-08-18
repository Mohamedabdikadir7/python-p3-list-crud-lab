def create_an_empty_list():
    return []

def create_a_list():
    return ["hello" , "good" , "safety", "home"]

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l
my_list = ["hello" , "good" , "safety", "home"]
my_list = add_element_to_end_of_list(my_list , 'mother')
print(my_list)


def add_element_to_start_of_list(l, element):
    l.insert(0 , element)
    return l 
my_list = ["hello" , "good" , "safety", "home"]
my_list = add_element_to_end_of_list(my_list , 'father')
print(my_list)

def remove_element_from_end_of_list(l):
    l.pop()  
    return l  

my_lists = ["hello", "good", "safety", "home"]
my_lists = remove_element_from_end_of_list(my_lists)  
print(my_lists)  

def remove_element_from_start_of_list(l):
    del l[0]  
    return l  
my_list = ["hello", "good", "safety", "home"]
modified_list = remove_element_from_start_of_list(my_list)
print(modified_list)


def retrieve_first_element_from_list(l):
    return l[0]
my_list = ["hello", "good", "safety", "home"]
first_element = retrieve_first_element_from_list(my_list)
print(first_element)


def retrieve_element_from_index(l, index):
    return l[index]
my_list = ["hello", "good", "safety", "home"]
element_at_index_2 = retrieve_element_from_index(my_list, 2)
print(element_at_index_2)


def retrieve_last_element_from_list(l):
    return l[-1]
my_list = ["hello", "good", "safety", "home"]
last_element = retrieve_last_element_from_list(my_list)
print(last_element)
