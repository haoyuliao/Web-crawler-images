import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
#Learning references
#https://www.learncodewithmike.com/2020/09/download-images-using-python.html

data = pd.read_excel('dataset.xlsx')
output = {}
NumImgs = []
deviceType = 'SmartPhone'
if not os.path.exists("./%sTeardownImages" %(deviceType)): #Create folders to save images.
    os.mkdir("./%sTeardownImages" %(deviceType))
    
for i in range(len(data)):
    br = data['Brand'][i]
    mo = data['mode'][i].replace('"', "")
    rep = data['repairability'][i]
    linkd = data['link'][i]
    '''
    posMo = []
    posMo.append(mo.capitalize())
    posMo.append(mo.lower())
    posMo.append(mo.replace(' ','_').capitalize())
    posMo.append(mo.replace(' ','_').lower())
    posMo.append(mo.replace(' ','').capitalize())
    posMo.append(mo.replace(' ','').lower())
    '''
    if not os.path.exists("./%sTeardownImages/%s" %(deviceType, br)):
        os.mkdir("./%sTeardownImages/%s" %(deviceType, br))
        
    if not os.path.exists("./%sTeardownImages/%s/%s" %(deviceType, br,rep)):
        os.mkdir("./%sTeardownImages/%s/%s" %(deviceType, br,rep))


    savePath = "./%sTeardownImages/%s/%s/%s" %(deviceType, br,rep,mo)
    if not os.path.exists(savePath):
        os.mkdir(savePath)  

    response = requests.get(f"%s" %(linkd))

    soup = BeautifulSoup(response.text, "lxml")

    results = soup.find_all("img")
    image_links1 = [result.get("data-src") for result in results]  # Get src of image
    image_links2 = [result.get("src") for result in results]  # Get src of image
    image_links = image_links1 + image_links2

    filesName = []
    index = 0
    for link in image_links:
        if link == None:
            continue
        fileName = link.split('/')[-1]
        #judSum = sum([1 for x in posMo if x in fileName])
        if link[-6:] == 'medium' and fileName not in filesName:
            #print(link)
            #print(fileName)
            filesName.append(fileName)
            img = requests.get(link)  # Download images
            with open(savePath +'/'+ str(index+1) + ".jpg", "wb") as file:  # Create new image file
                file.write(img.content)  # Write to the image file
            index+=1
            continue
        if link[-3:] in ['jpg','png'] and fileName not in filesName \
           and ('scaled' in fileName or 'outof' in fileName):# and judSum > 0:
            #print(link)
            #print(fileName)
            filesName.append(fileName)
            img = requests.get(link)  # ????????????
            with open(savePath +'/'+ str(index+1) + ".jpg", "wb") as file:  # Create new image file
                file.write(img.content)  # Write to the image file
            index+=1
            continue
    NumImgs.append(index)
output['NumImgs'] = NumImgs
pd.DataFrame(output).to_excel("output.xlsx")
            



