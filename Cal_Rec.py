import math
import time

cordinates=[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4),(4,3)]

#cordinates=[(1,3),(1,6),(2,1),(2,3),(2,6),(2,8),(6,1),(6,3),(6,6),(6,8)]

#cordinates=[(3,10),(3,8),(3,6),(3,4),(3,0),(6,0),(6,4),(6,8),(6,10)]


def calculateAngle(givenCord):
    temp=[]
    for i in cordinates:
        if i == givenCord:
           temp.append(None)
        else:
            y=i[1]-givenCord[1]
            x=i[0]-givenCord[0]
            try:
                temp.append(math.degrees(math.atan(y/x)))
            except ZeroDivisionError:
                if i[1] > givenCord[1]:
                    temp.append(90)
                elif i[1] < givenCord[1]:
                    temp.append(-90)
    #print(temp)
    angle.append(temp)

angle=[]
rectangles=[]
OppAngle = {  0.0   : 90.0,
             -0.0   : 90.0,
              90.0  : 0.0,
             -90.0  : 0.0,
              45.0  : 45.0,
             -45.0  : 45.0
            }
             

def FindRec():
    for i in cordinates:
        calculateAngle(i)
    fstside=0
    sndside=0
    trdside=0
    fhrtside=0
    fftside=0
    for fst in range(0,len(cordinates)):
        fstside=cordinates[fst]
        for snd in range(fst+1,len(cordinates)):
            ang=angle[fst][snd]
            sndside=cordinates[snd]
            ind3=-1
            for trd in angle[snd]:
                ind3=ind3+1
                if trd != None and fstside != cordinates[ind3] and OppAngle.get(ang) == abs(trd):
                    ang3=angle[snd][ind3]
                    trdside=cordinates[ind3]
                    ind4=-1
                    for fhrt in angle[ind3]:
                        ind4=ind4+1
                        if fhrt != None and sndside != cordinates[ind4] and OppAngle.get(ang3) == abs(fhrt):
                            ang4=angle[ind3][ind4]
                            fhrtside=cordinates[ind4]
                            ind5=-1
                            for fft in angle[ind4]:
                                ind5=ind5+1
                                if fft!= None and OppAngle.get(ang4) == abs(fft):
                                    ang5=angle[ind4][ind5]
                                    fftside=cordinates[ind5]
                                    if fstside == fftside:
                                        temp=[]
                                        temp.append(fstside)
                                        temp.append(sndside)
                                        temp.append(trdside)
                                        temp.append(fhrtside)
                                        temp.sort()
                                        if temp not in rectangles:
                                            rectangles.append(temp)
                    
start_time=time.time()           
FindRec()
end_time=time.time()
print(rectangles,'\n No. of rectangles: ',len(rectangles),'\nTime taken: ',end_time-start_time)


