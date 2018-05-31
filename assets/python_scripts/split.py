import sys  

 
f=open('tmp.txt', 'r')  
fnew=open('_new.txt','w') #将结果存入新的文本中 
lines =  f.readlines()
for line in lines:   #对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0  
    #print(":"+line)
    if line.strip():   
        fnew.write(line) 
print('ok')
f.close()  
fnew.close() 
