import sys
try:
 try:
  arg1 = sys.argv[1]
 except Exception:
  print("No file included")
 f = open(arg1)
 lines = f.readlines()
 f.close() 
 len1 = lines.index(".circuit\n")
 try:
  len2 = lines.index(".end\n")
 except Exception:
  len2 = lines.index(".end")
 for  i in range(len1+1,len2):
   try:
      y=lines[i].index('#')
      lines[i] = lines[i][:(y-len(lines[i]))]
   except Exception:
      lines[i] = lines[i]
 for i in range(len1+1,len2):
   lines[i] = lines[i].split()
 lis = lines[len1+1:len2]
 lis.reverse()
 for i in range(0,len(lis)):
   lis[i].reverse()
   lis[i] = ' '.join(lis[i])
 lis = '\n'.join(lis)   
 print(lis)  
except Exception:
 print("Invalid input") 
