import sys

#word = sys.argv[1]

phrase = "iliuminatainball"
letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def main():
    decode()
    encode()


def decode():
    #decodeWord = input("what do you want to decode: ") 
    decodeWord = "lolxplqdwdlqedoo"
    print(decodeWord)
    for ch in decodeWord:
        count = 0
        print(ch)
        while count < len(letterList):
            if letterList[count] == ch:
                newCount = count - 3
                print(ch, newCount, letterList[newCount])
                break
            count = count + 1        
                
def encode():
    pass

main()