#file = open('C:\Users\uidh3600\Desktop\poema_SE.txt', 'r+')
file = open('C:\Users\uidh3600\Desktop\hello.dbc', 'r')

document = []

for line in file:
    if line.startswith(' SG_'):
        document.append(line)
size = len(document)
print size
for num in range(0,size):
    if document[num].find('WAKE') != -1:
        print document[num]
        signal = document[num]
        sizee = len(signal)
        print sizee
        for numm in range(0,sizee):
            if signal[numm] == "@":
                print signal[numm+1]
                print signal[numm-1]
                desde = int(signal[numm+1])
                hasta = int(signal[numm-1])

                total = (2**hasta)
                print total
'''
        if line.find("@") != -1:
            print(line)
            size = len(line)
            print size
            
            for char in line:
                print char
            
            for num in range(0,size):
                if line[num] == "@":
                    print line[num+1]
                    print line[num-1]
                    desde = int(line[num+1])
                    hasta = int(line[num-1])

                    total = (2**hasta)
                    print total
'''