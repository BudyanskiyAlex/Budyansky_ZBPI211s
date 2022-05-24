
#1
def fact(x):
    if type(x) != int:
        return "Тип числа не соответствует тз"
    if x == 1:
        return 1
    return fact(x-1) * x


print(fact(23))

#2
def filter_even(li):
    if type(li) != list:
        return "Ошибка типа пармаетра"
    if len(li) == 0:
        return "Список пуст"
    return list(filter(lambda x: x % 2 == 0, li)) 

print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#3
def square(li):
    if type(li) != list:
        return "Ошибка типа пармаетра"
    if len(li) == 0:
        return "Список пуст"
    return list(map(lambda x: x ** 2, li))

print(square([10,11,12,13,14,15,16,17]))

#4
def bin_search(li, element):

    if type(element) != int:
        return "Ошибка типа пармаетра"
    if type(li) != list:
        return "Ошибка типа пармаетра"
    if len(li) == 0:
        return "Список пуст"
          

    low = 0
    high = len(li)

    while high > low:
        sr = (low+high)//2

        if(li[sr] == element):
            return sr

        if(li[sr] < element):
            low = sr 
        else:
            high = sr 

    if(li[sr] != element):
        return -1

print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))

#5
def is_palindrome(string):
    if type(string) != str:
        return "Ошибка типа пармаетра"
    string = string.replace(" ", "")
    string = string.lower()
    string1 = []
    for i in string:
       if i.isalpha():
          string1.append(i) 
    left = 0
    right = len(string1)-1 
    while left != right:
        if(string1[left] != string1[right]):
            return "NO"
        left+=1
        right-=1
    return "YES"

print(is_palindrome("Madam, I'm Adam"))

#6
def calculate(path2file):

    if type(path2file) != str:
        return "Ошибка типа пармаетра"


    file = open(path2file,'r')

        
    operations = ["%", "-", "**", "//","+","*"]  
    result = []

    for stroka in file.readlines():

        stroka2 = stroka.split("    ")

        result2 = eval(stroka2[1] + stroka2[0] + stroka2[2])
        result.append(str(result2))

    result3 = ",".join(result)

    f_result = open('output1.txt','w')
    f_result.write(result3)
    f_result.close()

    file.close()

    return result3


print(calculate('C:\\Users\\Admin\\Desktop\\test_input_file_1.txt'))


#8
def decode_ch(sting_of_elements):

    if type(sting_of_elements) != str:
        return "Ошибка типа пармаетра"


    table = json.load(open('periodic_table.json',"r", encoding = "utf-8"))
   

    const  = 0 
    res1 = [] 
    stroka  = ""
    for i in sting_of_elements:
        if i.isupper():
            const += 1
            if const == 2:
                res1.append(stroka)
                const = 1
                stroka = ""
        stroka += i
        
    res1.append(stroka) 

    res2 = ""
    for i in res1:
        res2 += periodic_table.get(i)
  

    return res2 

print(decode_ch("NOTiFICaTiON"))

#9
class Student:
    def __init__(self, name, surname, grades = [3,4,5]):

        self.name     = name 
        self.surname  = surname
        self.fullname = name + " " + surname
        self.grades   = grades
    
    def greeting(self):
        return "Hello, I am Student"

    def mean_grade(self):
        sr = 0
        for i in self.grades:
            sr = sr + i
        sr = sr/len(self.grades)
        return round(sr, 2)

    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return "YES"
        else:
            return "NO"

    def __add__(self, other):
        return self.name + " is friends with " + other.name
 

    def __str__(self):
        if hasattr(self, "fullname"): 
            return self.fullname
       



student_1 = Student("Будянский", "Александр", [4, 5, 5])
print(student_1)
print(student_1.greeting())
print(student_1.mean_grade())
print(student_1.is_otlichnik())

student_2 = Student("Будянскиц", "Alexander", [3, 3, 3])
print(student_2)
print(student_2.greeting())
print(student_2.mean_grade())
print(student_2.is_otlichnik())

print(student_1+student_2)
