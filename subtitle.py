import os,  time

filename='srt.txt'


file = open(filename, "r")

def caltime(str):
    return 3600*str[0]+60*str[1]+str[2]


# hello world
for x in range(1,3) :


    line= file.readline()
    if line[1] =='':
        time=file.readline();
        times=split(time,'-->')
        time1=split( times[0],':')
        time2=split(times[1], ':')
        t1=caltime(time1)
        t2=caltime(time2)
        delay=t2-t1

        print file.readline()
        time.sleep(delay)
        
    
# end of code
