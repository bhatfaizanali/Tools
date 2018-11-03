import sys
inFile = sys.argv[1]
outFile = sys.argv[2]


with open(inFile, 'r+') as rf:
    content = rf.read()
    rf.seek(0, 0)
    rf.write('\n'.rstrip('\r\n') + '\n' + content)

with open(inFile, 'r') as rf:
    for line in rf:
        ip_list = rf.read().splitlines()
        for i in ip_list:
            splited = i.split('/')
            ip = splited[0].split('.')
            with open(outFile, 'a') as wf:
                for i in range(1, int(splited[1])+1):
                    ip[3] = str(i)
                    new = ''
                    for x in range(0, int(len(ip))):
                        new += ip[x]
                        if x < int(len(ip)-1):
                            new += '.'
                    wf.write(new+'\n')

with open(inFile, 'r') as fin:
    data = fin.read().splitlines(True)
with open(inFile, 'w') as fout:
    fout.writelines(data[1:])
