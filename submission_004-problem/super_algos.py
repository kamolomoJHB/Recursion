import random

def find_min(element):
    """TODO: complete for Step 1"""
    for i in element:
        if type(i) != int:
            return -1
    if (len(element) == 0):
        return -1
    if len(element) == 1:
        return element[0]
    if len(element) > 1:
        if element[0]> element[1]:
            element.pop(0)
        else:
            element.pop(1)
        return find_min(element)   

def sum_all(element):
    """TODO: complete for Step 2"""
    for i in element:
        if type(i) != int:
            return -1
    if len(element) == 0:
        return -1
    if len(element) == 1:
        return element[0]
    if len(element) > 1: 
        element[0] = element[0] + element[1]
        element.pop(1)
        return sum_all(element)

def strings(character_set, n, generated_strings):
    num_possibilities = (len(character_set))**n
    single_string = ""

    if not(len(generated_strings) == num_possibilities):
        for i in range(0,n):
            single_string = single_string + ''.join(random.choices(character_set))
        
        if single_string not in generated_strings:
            generated_strings.append(single_string)
    else:
        print("Input:\nset[] = " + str(set(character_set))+ ", k = " + str(n) + "\n\nOutput:")
        strings_output = ""
        generated_strings = sorted(generated_strings)
        for i in range(0, len(generated_strings)):
            strings_output = strings_output + generated_strings[i] + "\n"
        print(strings_output)
        return  generated_strings

    return strings(character_set,n,generated_strings)

    
def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    set_characters = set(character_set)
    if len(set_characters) == len(character_set):
        for i in character_set:
            if type(i) == int:
                return []
        return strings(character_set,n,list())
    else:
        return -1

if __name__ == '__main__':
    print(find_possible_strings(['x','y'], 3))


