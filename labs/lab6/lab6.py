"""
Name: Steve Ford
lab6.py
"""


def name_reverse():
    full_name = input("What name are we reversing? ")
    name_split = full_name.split()
    print(name_split[1] + ", " + name_split[0])


def company_name():
    full_website = input("What is the website? ")
    company = full_website.split(".")
    print(company[1])


def initials():
    name_count = int(input("How many names are in the list? "))
    for _ in range(name_count):
        first = str(input("What is the first name? "))
        last = str(input("What is the last name? "))
        print(first + "'s initials are: " + first[0].capitalize() + last[0].capitalize())


def names():
    all_names = str(input("Enter people's names, separated by commas: ")).upper()
    all_names = all_names.split(", ")
    initials_acc = ""
    for i in range(len(all_names)):
        parts = all_names[i].split()
        initials_acc += parts[0][0] + parts[1][0] + " "
    print("The initials are: " + initials_acc)


def thirds():
    total_sentences = int(input("How many sentences are we computing? "))
    sentence_acc = ""
    for i in range(total_sentences):
        new_sentence = str(input("What is sentence #" + str(i + 1) + "? "))
        for letter in range(2, len(new_sentence), 3):
            sentence_acc += new_sentence[letter]
    print(sentence_acc)


def word_average():
    sentence = str(input("Type the sentence you want to return its average word length: "))
    words = sentence.split()
    average_acc = 0
    for i in range(len(words)):
        average_acc += len(words[i])
    average_acc = average_acc / len(words)
    print(average_acc)


def pig_latin():
    message = str(input("Type the message you want converted into pig latin: "))
    message_pig = ""
    message = message.split()
    for i in range(len(message)):
        word = message[i]
        first = word[0]
        body = word[1:]
        message_pig += body + first + "ay "
    print(message_pig)


def main():
    initials()
    name_reverse()
    company_name()
    names()
    thirds()
    word_average()
    pig_latin()


main()
