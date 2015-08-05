# -*- coding: utf-8 -*-
"""
@author: Ludovick S.Pelletier et Quentin Libois

Script pour Vol du polar 6 No: 9
"""


from pylab import *
from datetime import datetime
from matplotlib.dates import date2num


m300 = open("/Users/ludovick/Desktop/data_netcare/M300csv/sc9_20150420_M300.csv")
#heiko = open("/Users/ludovick/Desktop/data_netcare/Heiko/Flight8_H2O.csv")


def rh_ice(temp,vapor):
    logei = -9.09718*(273.16/temp-1)*log(10)-3.56654*log(273.16/temp)+0.876793*(1-temp/273.16)*log(10)+log(6.1071)
    ei = exp(logei)
    print temp,vapor,ei
    return vapor/ei
    
#-Heiko
#13.04.2015 15:14:23,0.31115
#vapor = []
#dates_heiko = []
#
#first = 1
#for line in heiko:
#    if first == 1:
#        first = 0
#    else:
#        line = line.replace('\r\n','')
#        data1 = line.split(",")
#        if data1[1] != "":
##            print data[0],datetime.strptime(data[0],"%d.%m.%Y %H:%M:%S")
##            raw_input()
#            dates_heiko+= [datetime.strptime(data1[0],"%d.%m.%Y %H:%M:%S")]
#            vapor+= [float(data1[1])]
#        

#-M300
grimm1 = []
grimm2 = []
grimm3 = []
grimm4 = []
grimm10 = []
grimm11 = []
grimm14 = []
grimm16 = []
rh = []
part = []
f100 = []
f300 = []
altitude = []
temp = []
dates = []
bc = []
so2 = []
lon = []
lat = []

first = 1
for line in m300:
    if first == 1:
        line = line.replace('\"','').replace('\'','').replace(' ','').replace('\n','')
        first = 0
       
        items = line.split(",")
        for k in range(len(items)):
            
            items[k]
    
        h = items.index('RH')  
        gr1 = items.index('Grimm01')   
        gr2 = items.index('Grimm02') 
        gr3 = items.index('Grimm03')   
        gr4 = items.index('Grimm04')
        gr10 = items.index('Grimm10')
        gr11 = items.index('Grimm11')
        gr14 = items.index('Grimm14')
        gr16 = items.index('Grimm16')
        p = items.index('2DCTotCn')
        fc = items.index('F100TCon')
        ft = items.index('F300TCon')
        alt = items.index('Altitude_m')
        t = items.index('Temp')
        b = items.index('SP2inc')
        s = items.index('SO2Conc')
        lo = items.index('Longitude_deg')
        la = items.index('Latitude_deg')
#        twc = items.index('TWCg/m3')
#        lwc = items.index('LWCg/m3')
 
        
    else:
        line = line.replace('\"','').replace('\n','')
        data = line.split(",")
        dates+= [datetime.strptime(data[0],"%d/%m/%Y %H:%M:%S")]
        rh+= [float(data[h])]
        grimm1+= [float(data[gr1])]
        grimm2+= [float(data[gr2])]
        grimm3+= [float(data[gr3])]
        grimm4+= [float(data[gr4])]
        grimm10+= [float(data[gr10])]
        grimm11+= [float(data[gr11])]
        grimm14+= [float(data[gr14])]
        grimm16+= [float(data[gr16])]
        part+= [float(data[p])]
        f100+= [float(data[fc])]
        f300+= [float(data[ft])]
        altitude+= [float(data[alt])]
        temp+= [float(data[t])]
        bc+= [float(data[b])]
        so2+= [float(data[s])]
        lon+= [float(data[lo])]
        lat+= [float(data[la])]
        
lat = ma.masked_less(lat,60)
lon = ma.masked_greater(lon,-70) 
##print altitude
#altitude = ma.masked_less(altitude,0)
##print altitude
#plot(dates,lon)
#ax=gca()
#ax2=ax.twinx()
#ax2.plot(dates,lat)  
##ax2.plot(dates[1000:],0.01*array(altitude)[1000:]) 
#show()      
        
#-Get RH_ice fronm Heiko and temp
        
#vapor = interp(date2num(dates),date2num(dates_heiko),vapor)  
#rhi = rh_ice(array(temp)+273.16,array(vapor))
# 
i1,i2 = searchsorted(dates,[datetime(2015,4,20,22,23),datetime(2015,4,20,23,19)])   #ascent     
#i1,i2 = searchsorted(dates,[datetime(2015,4,5,9,43),datetime(2015,4,5,13,40)])   #ascent
#i1,i2 = searchsorted(dates,[datetime(2015,04,13,18,15),datetime(2015,04,13,19,15)])   #descent
dates = dates[i1:i2]    

#-Clean data     
#rhi = ma.masked_greater(rhi[i1:i2],2.8)
#rhi = ma.masked_less(rhi[i1:i2],0.1)   
temp = ma.masked_less(temp,-40)  
temp = ma.masked_greater(temp[i1:i2],10)     
rh = ma.masked_less(rh[i1:i2],0)  
altitude = ma.masked_less(altitude[i1:i2],0) 
part = ma.masked_greater(part[i1:i2],1000) 
f100 = ma.masked_greater(f100[i1:i2],1000) 
f300 = ma.masked_greater(f300[i1:i2],1000) 
grimm1 = ma.masked_greater(grimm1[i1:i2],1000) 
grimm2 = ma.masked_greater(grimm2[i1:i2],1000) 
grimm3 = ma.masked_greater(grimm3[i1:i2],1000) 
grimm4 = ma.masked_greater(grimm4[i1:i2],1000)
grimm10 = ma.masked_greater(grimm10[i1:i2],1000) 
grimm11 = ma.masked_greater(grimm11[i1:i2],1000)  
grimm14 = ma.masked_greater(grimm14[i1:i2],1000) 
grimm16 = ma.masked_greater(grimm16[i1:i2],1000) 
bc = ma.masked_greater(bc[i1:i2],50) 
so2 = ma.masked_greater(so2[i1:i2],1000) 


#-Plot data
figure(15,figsize=(15,10))

     
plot(temp,altitude,label="Temperature (c)")
ax = gca()
ax2=ax.twiny()
ax2.plot(part,altitude,"o",markersize=4,label="> 50 $\mu$m")
ax2.plot(f100,altitude,"o",markersize=5,label="1-40$\mu$m")
ax2.plot(0.01*f300[::5],altitude[::5],"o",markersize=4,label="0.3-20 $\mu$m")
ax2.plot(grimm1,altitude,".",markersize=3,label="> 0.23 $\mu$m")
ax2.plot(grimm2,altitude,".",markersize=3,label="> 0.3 $\mu$m")
ax2.plot(grimm3,altitude,".",markersize=3,label="> 0.4 $\mu$m")
ax2.plot(grimm4,altitude,".",markersize=3,label="> 0.5 $\mu$m")
ax2.plot(grimm10,altitude,".",markersize=3,label="> 3 $\mu$m")
ax2.plot(grimm11,altitude,".",markersize=3,label="> 4 $\mu$m")
ax2.plot(0.1*bc[::5],altitude[::5],".",markersize=3,label="BC")
#ax2.plot(rhi,altitude,label="Relative humidity")
legend(loc=0)
show()        

#plot(grimm1)
#plot(grimm2)
#plot(grimm14)
#plot(grimm16)
#plot(f100,label="F100")
#plot(f300,label="F300")
#plot(part,label="2DC")
#plot(part,label="2DC")
##ylim(0,10)
#legend(loc=0)
#show()    