from PIL import Image
import pandas as pd
import psutil

path = f"/home/tombalak/Desktop/s/Train/"
yollar = [f'{path}/{id}.png' for id in range(1,663,1)]
temp = {i: '' for i in range(1,663,1)}
id = 0
while True:
    temp[id+1] = input("Enter the content: ")
    im = Image.open(yollar[id])
    im.show()
    
    
    
    if temp[id+1] == 'exit':
        break
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()
    id+=1

df = pd.DataFrame(temp)

df.to_csv('./my.csv')