file = open('C:\Users\uidh3600\Desktop\poema_SE.txt', 'r+')

for line in file:
    if line.find("rosa") != -1:
        print(line)
        size = len(line)
        print size
        '''
        for char in line:
            print char
        '''
        for num in range(0,size):
            letra = line[num]
            print letra