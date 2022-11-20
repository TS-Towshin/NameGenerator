import random
def NameGeneration():

    alphabets = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
                 'v', 'w', 'x', 'y', 'z']
    Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    last = ['a', 'e', 'i', 'o', 'u', 'h', 'm', 'n', 'v', 'w', 'z']
    names = open('Name.txt', 'a')
    x = 1
    rdnames = open('Name.txt', 'r')
    try:
        where = rdnames.readlines()[-1]
        f1 = where.find('[') + 1
        f2 = where.find(']')
        fnd = where[f1:f2]
        x += int(fnd)
    except:
        pass
    names.write(f'[{x}]')
    i = random.randint(6, 10)
    Alp = random.choice(Alphabets)
    names.write(Alp)
    num = i - 2
    remainder = num % 2
    if remainder == 0:
        while True:
            snd = random.choice(last)
            names.write(snd)
            num -= 1
            vow = random.choice(vowels)
            alp = random.choice(alphabets)
            names.write(vow)
            num -= 1
            names.write(alp)
            num -= 1
            if num <= 0:
                char = random.choice(last)
                names = open('Name.txt', 'a')
                names.write(f'{char}\n')
                names = open('Name.txt', 'r')
                print(names.readlines()[-1])
                break
    elif remainder == 1:
        while True:
            snd = random.choice(last)
            num -= 1
            names.write(snd)
            char = random.choice([vowels, alphabets])
            char = random.choice(char)
            num -= 1
            names.write(char)
            if num <= 0:
                char = random.choice(last)
                names.write(f'{char}\n')
                names = open('Name.txt', 'r')
                print(names.readlines()[-1])
                break

try:
    if __name__ == '__main__':
        while True:
            NameGeneration()
            input()
    else:
        NameGeneration()
except Exception as why:
    print(why)
