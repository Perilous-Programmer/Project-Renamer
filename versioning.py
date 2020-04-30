import os 

print("path = ",os.getcwd())
files = []
for x in os.listdir():
    if ('.zip' in x):
        files.append(x)

count = len(files)-1
if count < 10 :
    os.rename(os.getcwd()+"\\"+files[-1],os.getcwd()+"\\"+str(count).zfill(2)+'-'+files[-1])
else:
    files[-1] = str(count)+'-'+files[-1]
    os.rename(os.getcwd()+"\\"+files[-1],os.getcwd()+"\\"+str(count)+'-'+files[-1])

for x in os.listdir():
    if ('.zip' in x):
        files.append(x)
print("zip list :",)
print(*files, sep = ", ")