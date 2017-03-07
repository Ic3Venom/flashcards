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

        random = list(range(length))
        shuffle(random)
        #random also carries its own index integer
        random.insert(1, 1)
    except:
        print 'Unknown file name \'%s\'. Exiting program.' % fileName
        exit(1)

    with open(fileName, 'r') as f:

        while True:
            i = 0
            for line in f:
                if i == random[random[0]]:

                    j = 0
                    for char in line.split():
                        if char == fileSplit:
                            term = ' '.join(line.split()[:j])
                            definition = ' '.join(line.split()[j+1:])
                        j += 1

                    userInput = raw_input(term)
                    if userInput.lower is not definition.lower:
                        print 'Wrong! It should be %s' % definition
                        random[i] = definition, fileSplit, term

                    random[0] = int(random[0]) + 1
                    break
            if i is length:
                break


if __name__ == '__main__':
    main()
    exit(0)
