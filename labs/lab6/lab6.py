"""
Name: <Christopher Hamilton, II>
<lab6>.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter a first and last name: ")
    first_name, last_name = name.split(" ")
    print(last_name + ",", first_name)


def company_name():
    domain = input("Enter a 3-part domain name: ")
    domain_list = domain.split(".")
    print(domain_list[1])


def initials():
    name = int(input("How many names will be entered: "))
    for i in range(name):
        student_first = input("Enter the first name of student: " + str(i + 1) + ": ")
        student_last = input("Enter " + student_first + "'s last name: ")
        initial = student_first[0] + student_last[0]
        print(student_first + "'s initials are", initial)


def names():
    name_input = input("Enter people's names, separated by commas: ")
    name_list = name_input.split(",")
    acc = ""
    for i in range( name_input.count(",") + 1):
        first, last = name_list[i].split()
        acc = acc + " " + first[0] + last[0]
    print("The initials are" + acc)


def thirds():
    sentences = int(input("Enter how many sentences will be entered: "))
    for i in range(sentences):
        sentence_str = input("Enter sentence " + str(i + 1) + ": ")
        sentence_int = sentence_str.count("")
        print(sentence_str[2:sentence_int:3])


def word_average():
    sentence = input("Enter a sentence: ")
    word_count = sentence.count(" ") + 1
    sentence_list = sentence.split(" ")
    acc = 0
    for i in range(word_count):
        letter_total = sentence_list[i].count("") - 1
        acc = acc + letter_total
    average = acc / word_count
    print(average)


def pig_latin():
    sentence = input("Enter a sentence: ")
    sentence_list = sentence.split(" ")
    acc = ""
    for i in range(sentence.count(" ") + 1):
        word = sentence_list[i].lower()
        acc = acc + " " + word[1:] + word[0] + "ay"
    print(sentence + " ->" + acc)


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
