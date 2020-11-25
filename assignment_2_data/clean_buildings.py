# coding: utf-8
import math
math.trunc(214)
math.trunc(214, 1)
math.trunc(214/10, 1)
math.trunc(214/10)
math.trunc(219/10)
math.trunc(219/10)
10*math.trunc(19/10)
df = pd.read_html('https://en.phorio.com/?t=projectlist&collection=5495651&type=list')
df.head()
df
len(df)
len(df[0])
get_ipython().run_line_magic('pwd', '')
df = pd.read_csv('skyscrapers1000.csv')
s = open('skyscrapers1000.csv').readlines()
s[0]
s[1]
s[2]
s[3]
s[4]
s[0].split('\t')
len(s)
bldgs = [] 
for i in range(1, 1001):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
len(bldgs)
bldgs[0]
list(map(lambda x: x.strip().rstrip(), bldgs))
list(map(lambda x: ','.join(y.strip().rstrip() for y in x), bldgs))
bldgs = [] 
for i in range(1, 2001, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
len(bldgs)
bldgs[480]
bldgs[479]
list(map(lambda x: ','.join(y.strip().rstrip() for y in x), bldgs))
bldgs = list(map(lambda x: ','.join(y.strip().rstrip() for y in x), bldgs))
df = pd.DataFrame(bldgs, headers=['Row', 'Building', 'City', 'Height m', 'Height ft', 'Floors', 'Year', 'Status'])
help(pd.DataFrame)
df = pd.DataFrame(bldgs, columns=['Row', 'Building', 'City', 'Height m', 'Height ft', 'Floors', 'Year', 'Status'])
cols = ','.join(['Row', 'Building', 'City', 'Height m', 'Height ft', 'Floors', 'Year', 'Status'])
with open('skyscrapers_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers_clean.csv')
bldgs[85:90]
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ') for y in x), bldgs))
with open('skyscrapers_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers_clean.csv')
bldgs = [] 
for i in range(1, 2001, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ') for y in x), bldgs))
with open('skyscrapers_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers_clean.csv')
df.head()
s = open('skyscrapers6000.csv').readlines()
bldgs = [] 
for i in range(1, 6001, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
len(s)
bldgs = [] 
for i in range(1, 6000, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = [] 
for i in range(1, 5999, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
s = open('skyscrapers6000.csv').readlines()
bldgs = [] 
for i in range(1, 6000, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
len(bldgs)
bldgs = [] 
for i in range(1, 12000, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = [] 
for i in range(1, 11999, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ') for y in x), bldgs))
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers6000_clean.csv')
bldgs[3:6]
bldgs = [] 
for i in range(1, 11999, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ').replace('m,1,', 'm,1') for y in x), bldgs))
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers6000_clean.csv')
bldgs[3:6]
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers6000_clean.csv')
bldgs = [] 
for i in range(1, 11999, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ').replace('m,1,', 'm,1') for y in x), bldgs))
bldgs[3:6]
'm,1,' == 'm,1,'
bldgs = [] 
for i in range(1, 11999, 2):
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ').replace(',', '') for y in x), bldgs))
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers6000_clean.csv')
bldgs[1320:1325]
s[2635:2670]
s[2645:2670]
s[2643:2670]
bldgs = [] 
for i in range(1, 11999, 2):
    if i == 2643:
        bldgs.append(s[i].strip().split('\t'))
        i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ').replace(',', '') for y in x), bldgs))
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers6000_clean.csv')
s[3665:3680]
s[3670:3680]
len(cols)
bldgs = [] 
for i in range(1, 11999, 2):
    if len(s[i]).split('\t') >= 7:
        bldgs.append(s[i].strip().split('\t'))
        i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = [] 
for i in range(1, 11999, 2):
    if len(s[i].split('\t')) >= 7:
        bldgs.append(s[i].strip().split('\t'))
        i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ').replace(',', '') for y in x), bldgs))
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers6000_clean.csv')
bldgs = [] 
for i in range(1, 11999, 2):
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = [] 
for i in range(1, 11999, 2):
    if s[i].startswith('1835'):
        print(s[i].split('\t'))
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = [] 
for i in range(1, 11999, 2):
    if s[i].startswith('1835'):
        print(s[i].split('\t'))
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        # i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = [] 
for i in range(1, 11999, 2):
    if s[i].find('1835') != -1:
        print(s[i].split('\t'))
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        # i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    
bldgs = [] 
for i in range(1, 11999, 1):
    if s[i].find('1835') != -1:
        print(s[i].split('\t'))
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        # i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    i += 1
    
bldgs = [] 
for i in range(1, 11998, 1):
    if s[i].find('1835') != -1:
        print(s[i].split('\t'))
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        # i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    i += 1
    
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ').replace(',', '') for y in x), bldgs))
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers6000_clean.csv')
s[5285:5290]
s[5284:5290]
s[5283:5290]
s[5282:5290]
bldgs[2643]
bldgs[2642]
bldgs[2644]
bldgs[1322]
bldgs[662]
bldgs[1]
bldgs[0]
bldgs = [] 
for i in range(1, 11998, 1):
    print(i)
    if s[i].find('1835') != -1:
        print(s[i].split('\t'))
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        # i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    i += 1
    
bldgs = [] 
i = 1
while i <= 11998:
    print(i)
    if s[i].find('1835') != -1:
        print(s[i].split('\t'))
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        # i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    i += 1
    
bldgs = [] 
i = 1
while i <= 11998:
    print(i)
    if s[i].find('1835') != -1:
        print(s[i].split('\t'))
    if len(s[i].split('\t')) >= 6:
        print(s[i])
        bldgs.append(s[i].strip().split('\t'))
        i += 1
        continue
    bldgs.append(s[i].strip().split('\t') + s[i+1].strip().split('\t'))
    i += 2
    
len(bldgs)
bldgs = list(map(lambda x: ','.join(y.strip().rstrip().replace(', ', ' ').replace(',', '') for y in x), bldgs))
with open('skyscrapers6000_clean.csv', 'w') as fo:
    fo.write(cols+'\n')
    for b in bldgs:
        fo.write(b + '\n')
        
df = pd.read_csv('skyscrapers6000_clean.csv')
df.head()
df.tail()
get_ipython().system('save clean_buildings.py 1-125')
