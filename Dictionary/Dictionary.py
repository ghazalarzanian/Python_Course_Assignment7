def Menu():
    print('1-add new word')
    print('2-translation english2persian')
    print('3-translation persian2english')
    print('4-exit')
def Add_New_Word():
    New={}
    English_word=input("Enter English words: ")
    New['english']=English_word
    Persian_word=input("Enter Translation in persian: ")
    New['persian']=Persian_word
    WORDS.append(New)
def Translation_English2Persian():
    Senctence=input('Enter Your Sentence[for new senctence->space+.+space]:')
    Senctence1=Senctence.split(' ')
    flag =0
    for i in range(len(Senctence1)):
        flag =0
        if Senctence1[i]!=' ' and Senctence1[i]!='.':
            for j in range(len(WORDS)):
                if Senctence1[i]==WORDS[j]['english']:
                    print(WORDS[j]['persian'],end=' ')
                    flag =1
                elif Senctence1[i]==',':
                    print(Senctence1[i])
            if flag==0:
                print(' Not Found',end=' ')
        if Senctence1[i]=='.':
            print('.',end='')
    print()
def Translation_Persian2English():
    Senctence=input('Enter Your Sentence[for new senctence->space+.+space]:')
    Senctence1=Senctence.split(' ')
    flag =0
    for i in range(len(Senctence1)):
        flag =0
        if Senctence1[i]!=' ' and Senctence1[i]!='.':
            for j in range(len(WORDS)):
                if Senctence1[i]==WORDS[j]['persian']:
                    print(WORDS[j]['english'],end=' ')
                    flag =1
                elif Senctence1[i]==',':
                    print(Senctence1[i])
            if flag==0:
                print(' Not Found',end=' ')
        if Senctence1[i]=='.':
            print('.',end='')
    print()
def Exit():
    myfile=open('translate.txt','w')
    for i in range(len(WORDS)):
        rows =str(WORDS[i]['english'])+'\n'+str(WORDS[i]['persian'])
        myfile.write(rows)
        if i!=(len(WORDS)-1):
            myfile.write('\n')
    myfile.close()
    exit()
def Load():
    print('Loading...')
    Myfile=open('translate.txt','r')
    Data=Myfile.read()
    words=Data.split('\n')
    for i in range(0,len(words)-1,2):
        WORDS.append({'english':words[i],'persian':words[i+1]})
#######Main
WORDS=[]
Load()
while True:
    Menu()
    Choice=int(input(":"))
    if Choice==1:
        Add_New_Word()
    if Choice==2:
        Translation_English2Persian()
    if Choice==3:
        Translation_Persian2English()
    if Choice==4:
        Exit()