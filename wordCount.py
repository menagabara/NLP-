# a function to return 10 most common and uncommon words i a text.

import re


def word_count():
    txt = "As I was waiting, a man came out of a side room, and at a glance I was sure he must be Long John. His left " \
          "leg was cut off close by the hip, and under the left shoulder he carried a crutch, which he managed with " \
          "wonderful dexterity, hopping about upon it like a bird. He was very tall and strong, with a face as big as " \
          "a ham—plain and pale, but intelligent and smiling. Indeed, he seemed in the most cheerful spirits, " \
          "whistling as he moved about among the tables, with a merry word or a slap on the shoulder for the more " \
          "favoured of his guests. "

    # convert all to lower case.
    txt = txt.casefold()

    # split and add to list, then sort the words.

    # remove special characters from the text.
    txt = re.sub('\,|\.|\:|\;|\"|\{|\}|\[|\]|\\|\/|\+|\-|\(|\)|\*|\&|\^|\%|\$|\#|\@|\!|\~|>|\<|\?', '', txt)

    # split text and add it to a list.
    split = txt.split()

    word_count_dict = {}

    # append word and its count to a dictionary.
    for word in split:
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
            # word_count_dict.update(i=counter+1)
        else:
            word_count_dict[word] = 1

    # sort dictionary's values.
    sorted_count = sorted(word_count_dict.items(), key=lambda pair: pair[1], reverse=True)

    # print the top common 10 words.
    print("\n10 top common words:\nWord\tCount")
    for word, count in sorted_count[:10]:
        print("{}\t{}".format(word, count))

    # print the least common 10 words.
    print("10 least common words:\nWord\tCount")
    for word, count in sorted_count[-10:]:
        print("{}\t{}".format(word, count))


word_count()
