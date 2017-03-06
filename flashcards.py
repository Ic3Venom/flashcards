#-------------------------------------------------------------------------------
# Name:        flashcards.py
# Purpose:     Virtual flashcards on a command prompt
#
# Author:      Julian Meyn
#
# Created:     05/03/2017
# (This was generated with PyScripter)
#-------------------------------------------------------------------------------

from random import shuffle

def main():
    fileName  = raw_input('What is the flashcard file name? (include file type)')
    fileSplit = raw_input('What character separates the term and definition?')

    try:
        #Used to create random card order
        with open(fileName, 'r') as f:
            length = 0
            for line in f:
                length += 1
        wrong = [i for i in range(length)]
        shuffle(wrong)

    except:
        print 'Unknown file name \'%s\'. Exiting program.' % fileName
        exit(1)

    with open(fileName, 'r') as f:
        i = 0
        j = 0
        print wrong

        while True:

            for line in f:
                if j == wrong[i]:

                    for char in line.split():
                        j += 1

                        if char == fileSplit:
                            term = ' '.join(line.split()[:j])
                            definition = ' '.join(line.split()[j-1:])


                    userInput = raw_input(term)
                    if userInput is not definition:
                        print 'Wrong! It should be %s' % definition
                        wrong.append(i)
                    i += 1
                    j = 0
                j += 1
            break



if __name__ == '__main__':
    main()

    exit(0)