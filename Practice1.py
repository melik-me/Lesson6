# Создать текстовый файл и записать в него вашу песню «la-la-la»

def naughty_boy(strings=3, nla=3, exclamation=0):
    string = ['la' for i in range(nla)]

    if exclamation:
        end_string = '!\n'
    else:
        end_string = '.\n'

    strings -= 1

    s = ("-".join(string) + "\n") * strings
    s += "-".join(string) + end_string
    return s

n = int(input('Please enter quantity of "la" in our song:\n'))
number = int(input('Please enter quantity of strings in our song:\n'))
ex = int(input('Please enter 1 if you need exclamation (otherwise string will end with a dot):\n'))

song = naughty_boy(n, number, ex)

f = open("song.txt", 'w')
f.write(song)
f.close()