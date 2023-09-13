import numpy as np
w = ("Correct", "Incorrect")  # tuple of words
randomize = True
pad_input = True
max_number = 5
answers = {
    w[0]: 0,
    w[1]: 0
}
potential_numbers = []


def generate_potential_numbers():
    if not potential_numbers:
        for i in range(pow(2, max_number)):
            potential_numbers.append(i)
        np.random.shuffle(potential_numbers)


def pad_number(num, length=max_number):
    padding_needed = (length - len(num))
    return ("0" * padding_needed) + num if padding_needed else num


def game():
    generate_potential_numbers()
    decimal_number = potential_numbers.pop() if randomize else int(input("Enter a number: "))  # random/user base-10
    binary_number = pad_number("{0:b}".format(decimal_number))  # base-10 to base-2
    user_input = pad_number(input("Please enter " + str(decimal_number) + " in binary: "))  # user base-2
    correct = w[0] if user_input == binary_number else w[1]  # compares base-10 to base-2
    answers[correct] += 1  # adds to correct or incorrect answer tally
    print(
        user_input
        + " is "
        + correct
        + ". "
        + str(decimal_number)
        + " is "
        + binary_number
        + ". Accuracy: "
        + str(round((answers[w[0]] / (answers[w[0]] + answers[w[1]])) * 100, 2))
        + "%\n")  # response


while True:
    game()

