import os
print(os.name)
s = input('录入路径')
files = [x for x in os.listdir(s) if os.path.splitext(x)[1] == '.md']
print(files)
for x in os.listdir(s):
    if os.path.splitext(x)[1] != '.md':
        continue
    f = open( s+'/' + x, 'r', encoding="utf-8" )
    str = f.readline()
    s2 = str.replace('#','')
    s2 = s2.strip()
    print(x, s2)
    f.close()
    s3 = s + '/' + x;
    fs = os.path.splitext(x)[0]
    try:
        os.rename(s3, s + '/' + s2 +'.md')
    except:
        None