list_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


def find_person(this_name, names):
    while True:
        name = names.pop()
        if name == this_name:
            print('%s, настрало твое время' % this_name)
            break


find_person("Валера", list_names)


def ask_user():
    while True:
        print('Как дела?')
        answer = input()
        if answer == "Хорошо":
            break
        else:
            get_answer(answer)

def get_answer(answer):
    print("google в помощь")


ask_user()
