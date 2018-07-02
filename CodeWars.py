# Create a function that takes a list of strings & numbers, only returns numbers
def filter_list(l):
    # "return a new list with the strings filtered out"
    temp_list = [i for i in l if type(i) is int]
    print(temp_list)
    #return temp_list
#filter_list([1,2,'a','b'])
#filter_list([1,'a','b',0,15])
#filter_list([1,2,'aasf','1','123',123])
#l.assert_equals(filter_list([1,2,'a','b']),[1,2])
#l.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
#l.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])


# Create a function that returns 5 without using 0123456789+-*/
def five():
    return len("afive")
#print(five())


# Create a function that returns whether you will have sufficient change to provide a movie ticket customer
def tickets(people):
    money = 0
    counter = range(len(people)-1)
    print(counter)
    for tick in counter:
        money += people[tick]
        print("money: {} minus ticket: {}".format(money, people[tick+1]))
        temp = money - people[tick+1]
        if temp < 0:
            return "NO"
    return "YES"
#print(tickets([25, 25, 50]))
#print(tickets([25, 100]))


# Create a function that calculates principle and returns what year you will hit your desired balance
def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        years += 1
        principal += ((principal * interest) - ((principal * interest) * tax))
    print(years)
calculate_years(1000, 0.05, 0.18, 1100)

# Create a function that calculates if you can make a triangle or not.
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Create a function that replaces unique characters as one thing, and non-unique characters as another, case insensitive
def duplicate_encode(word):
    temp_word = [i.lower() for i in word]
    new_word = []
    for character in temp_word:
        count = temp_word.count(character)
        if count > 1:
            new_word.append(")")
        else:
            new_word.append("(")
    new_string = "".join(new_word)
    return new_string

# Create a function that corrects mistakes in a string
def correct(string):
    new_word = []
    for character in string:
        if "0" in character:
            new_word.append("O")
        elif "1" in character:
            new_word.append("I")
        elif "5" in character:
            new_word.append("S")
        else:
            new_word.append(character)
    new_string = "".join(new_word)
    return new_string

# Create a function that alternates every other letter of a string to the opposite of its current case
def to_alternating_case(string):
    new_word = []
    for character in string:
        if character == character.lower():
            new_word.append(character.upper())
        else:
            new_word.append(character.lower())
    return "".join(new_word)
print(to_alternating_case("TesT"))

# Create a function that sorts and array, and returns the first index in the array with *** in-between each character
def two_sort(array):
    array.sort()
    first = array[0]
    new = []
    for character in first:
        new.append(character)
    return "***".join(new)

# Create a function that takes a number, generates a range, then outputs the range backwards
def reverse_seq(n):
    new_list = [i for i in range(1,n+1)]
    return new_list[::-1]

# Create a function that makes string upper(), then splits it by empty space into list, then outputs first characters
def abbrevName(name):
    words = name.upper().split()
    initials = []
    for i in words:
        initials.append(i[0])
    return ".".join(initials)

# Create a function that encodes
def duplicate_encode(word):
    temp_word = [i.lower() for i in word]
    print(word)
    print(temp_word)
    new_word = []
    for character in temp_word:
        count = temp_word.count(character)
        if count > 1:
            new_word.append(")")
        else:
            new_word.append("(")
    new_string = "".join(new_word)
    return new_string

print(duplicate_encode("Supralapsarian"))
print(duplicate_encode("eyJ(!xw(xHkwHx(HOlll"))
#'((()()))))()))))()))'
print(duplicate_encode("dklbQH(@mJ@zF) lSHdnuP"))