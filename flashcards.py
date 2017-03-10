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
    fileName  = str(raw_input('What is the flashcard file name? (include file type) '))
    fileSplit = str(raw_input('What character separates the term and definition? '))

    try:
        #Used to create random card order
        with open(fileName, 'r') as f:
            rngLen = 0
            for line in f:
                rngLen+= 1
            f.close()

        rng = list(range(rngLen))
        shuffle(rng)
        del rngLen

        #rng also carries its own index integer
        rng.insert(0, 1)
    except:
        print 'Unknown file name \'%s\'. Exiting program.' % fileName
        exit(1)

    with open(fileName, 'r') as f:
        #Alternatives to 'while True' require 2+ variables
            while True:
                i = 0
                f.seek(0)
                for line in f:
                    if i == rng[rng[0] + 1]:
                        j = 0

                        for char in line.split():
                            if char == fileSplit:
                                term = ' '.join(line.split()[:j])
                                definition = ' '.join(line.split()[j+1:])
                            j += 1

                        userInput = str(raw_input(term + ': '))
                        if userInput.lower() != definition.lower():
                            print '\t- Wrong! It should be %s' % definition
                            rng[rng[0] + 1] = 'You typed ' + str(userInput) + 'for ' + str(term) + ', should be ' + str(definition)
                        rng[0] += 1
                        break
                    i += 1
                if rng[0] == (len(rng) - 1):
                    break

            print 'You have finished all the cards! Would you like to know which ones you got wrong?',
            userInput = raw_input("Yes or No: ")
            if userInput.lower() in ['yes', 'y']:
                wrongCount = 0
                for i in rng:
                    if type(i) is str:
                        wrongCount += 1
                        print i
                print 'You got %d cards wrong' % wrongCount

            f.close()

if __name__ == '__main__':
    main()
    exit(0)
