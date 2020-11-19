import random

def GhiFile(tk, mk):
    file = open('ghifiletk.txt', 'a', encoding ='utf-8')
    file.write(tk)
    file.write('|')
    file.write(mk)
    file.write('\n')
    file.close()


# name = ['quyet', 'van', 'nguyen', 'long', 'hiep', 'trung', 'hang', 'nga']
# sorandom = str(random.randrange(999,10000))
# user ='nvq' + random.choice(name) + sorandom
#
# GhiFile(user)