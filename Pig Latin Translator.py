import string


def Translate(englishString):

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowelSounds = ["xr", "yt"]

    translation = []

    for word in englishString.split():
        if len(word) == 2 and word[1] == "y": # Rule 4
            translation.append(word[1:]+ word[0] + "ay")
        elif len(word) <= 2:
            translation.append(word)
        else:
            if word[0] in vowels or word[0:2] in vowelSounds: # Rule 1
                translation.append(word + "ay")
            elif word[0] in consonants: # Rule 2, 3 & 4
                if word[1:3] == "qu":
                    translation.append(word[3:] + word[0:3] + "ay")
                elif word[2:4] == "qu":
                    if word[1] in consonants:
                        translation.append(word[4:] + word[0:4] + "ay")
                elif word[1] in consonants and word[1] != "y":
                    if word[2] == "y":
                        translation.append(word[2:]+ word[0:2] + "ay")
                    else:
                        translation.append(word[2:] + word[0:2] + "ay")
                else:
                    translation.append(word[1:]+ word[0] + "ay")
                        
    return translation
    
def main(): # define main function
    while True:
        try:
            englishString = input("Input an english word or sentence to translate: ")
        except TypeError:
            raise Exception("Please enter a valid word or sentence...")

        pigLatinString = Translate(englishString)
        print(" ".join(pigLatinString))

if __name__ == '__main__':
    main() # call main() function
            
