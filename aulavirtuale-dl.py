import os
from bs4 import BeautifulSoup
import urllib


#Base link to the lessons page
edunovaLink = "https://davy04.edunova.it/presentation/"
#Relative path to the slides video
videoSuffix = "/deskshare/deskshare.webm"
#Relative path to the presentation audio
audioSuffix = "/video/webcams.mp4"
#slides = "https://davy04.edunova.it/presentation/17d59e4eb742c498e605406fd441c1a2d7eb4bf0-1601024050226/shapes.svg"

os.makedirs("VideoLezioni", exist_ok=True)
os.chdir("VideoLezioni")

#Dictionary containing the id of the saved lessons
meetingsID = {
    '021020': '17d59e4eb742c498e605406fd441c1a2d7eb4bf0-1601628738707',
    '290920': '17d59e4eb742c498e605406fd441c1a2d7eb4bf0-1601380547311',
    '250920': '17d59e4eb742c498e605406fd441c1a2d7eb4bf0-1601024050226',
    '061020': '17d59e4eb742c498e605406fd441c1a2d7eb4bf0-1601984780753'
            }

for (date, meetId) in meetingsID.items():
    if(os.path.exists(f"Gestione{date}joinedWithSlide.mp4")):
        continue

    #Assemblo il comando ffmpeg con i riferimenti web a video e audio della presentazione con id {meetId}
    downloadAndJoin = f"ffmpeg -i {edunovaLink}{meetId}{videoSuffix} -i {edunovaLink}{meetId}{audioSuffix} -map 0:v -map 1:a -c:v copy -shortest Gestione{date}joined.mp4"
    os.system(downloadAndJoin)
    svgSlide = urllib.request.urlopen(f"{edunovaLink}{meetId}/shapes.svg").read()

    soup = BeautifulSoup(svgSlide, 'html.parser')
    usefulImg = []
    for img in soup.find_all('image'):
        
        start = img.get('in')
        end = img.get('out')
        imgLink = img.get('xlink:href')
        if(not imgLink.endswith("deskshare.png")):
            usefulImg.append([float(start), float(end), imgLink])

    imgSorted = sorted(usefulImg)
    print(imgSorted)
    if(len(imgSorted)==0):
        os.rename(f"Gestione{date}joined.mp4", f"Gestione{date}joinedWithSlide.mp4")
        continue

    slideBase = f"{edunovaLink}{meetId}/"

    imgLinkList = ''
    imgScaleList = ''
    for l in imgSorted:
        imgLinkList += f"-i \"{slideBase}{l[2]}\" "

    for i in range(len(imgSorted)):
        imgScaleList += f"[{i+1}:v] scale=1280:720 [ol{i}]; "

    imgOverlayList = f"[0:v] [ol0] overlay=0:0:enable='between(t,{int(imgSorted[0][0])},{int(imgSorted[0][1])})' [olo0]; "

    for i in range(1, len(imgSorted)-1):
        imgOverlayList += f"[olo{i-1}] [ol{i}] overlay=0:0:enable='between(t,{int(imgSorted[i][0])},{int(imgSorted[i][1])})' [olo{i}]; "

    imgOverlayList += f"[olo{len(imgSorted)-1-1}] [ol{len(imgSorted)-1}] overlay=0:0:enable='between(t,{int(imgSorted[len(imgSorted)-1][0])},{int(imgSorted[len(imgSorted)-1][1])})'"
    
    #Informazioni di debug sulle immagini e sui momenti nei quali inserirle nel video
    print(imgLinkList)
    print(imgScaleList)
    print(imgOverlayList)

    #Comando di esempio di utilizzo di ffmpeg per incollare diverse immagini in diversi momenti su un video
    #ffmpeg -i Untitled.mp4 -i slide-1.png -i slide-2.png -filter_complex "[1:v] scale=640:480 [ol]; [2:v] scale=640:480 [ol2]; [0:v] [ol] overlay=0:0:enable='between(t,0,20)' [ol1]; [ol1] [ol2] overlay=0:0:enable='between(t, 30,40)'" -codec:a copy example_marked.mp4

    ffmpegCommand = f'ffmpeg -i Gestione{date}joined.mp4 {imgLinkList} -filter_complex "{imgScaleList}{imgOverlayList}" -codec:a copy Gestione{date}joinedWithSlide.mp4'

    os.system(ffmpegCommand)
    #Rimuovo il file intermedio senza slide
    os.remove(f"Gestione{date}joined.mp4")
