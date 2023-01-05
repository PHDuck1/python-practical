from random import shuffle


def randomWord(ls):
    random_words = ls.copy()
    shuffle(ls)
    shuffle(random_words)

    while True:
        if random_words:
            yield random_words.pop()

        elif ls:
            random_words = ls.copy()
            shuffle(random_words)
            yield random_words.pop()

        else:
            yield None


def main():
    words = [3, 4, 7]
    rand = randomWord([3, 2, 90])
    list1 = []
    list2 = []
    for i in range(len(words)):
        list1.append(next(rand))

    for i in range(len(words)):
        list2.append(next(rand))
    print(list1 != list2)
    print(list1)
    print(list2)


if __name__ == '__main__':
    main()
