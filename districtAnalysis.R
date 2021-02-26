#This project uses the csv files I made from the blue alliance api to do further analysis

#importing the csv files I will be working with

#Michigan
fim2015=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2015\\2015fim.csv",
                   sep=",", header=TRUE)
fim2016=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2016\\2016fim.csv",
                   sep=",", header=TRUE)
fim2017=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2017\\2017fim.csv",
                   sep=",", header=TRUE)
fim2018=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2018\\2018fim.csv",
                   sep=",", header=TRUE)
fim2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019fim.csv",
                   sep=",", header=TRUE)

#Indiana 
ind2015=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2015\\2015in.csv",
                   sep=",", header=TRUE)
ind2016=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2016\\2016in.csv",
                   sep=",", header=TRUE)
ind2017=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2017\\2017in.csv",
                   sep=",", header=TRUE)
ind2018=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2018\\2018in.csv",
                   sep=",", header=TRUE)
ind2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019in.csv",
                   sep=",", header=TRUE)

#Mid Atlantic
fma2015=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2015\\2015mar.csv",
                   sep=",", header=TRUE)
fma2016=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2016\\2016mar.csv",
                   sep=",", header=TRUE)
fma2017=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2017\\2017mar.csv",
                   sep=",", header=TRUE)
fma2018=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2018\\2018mar.csv",
                   sep=",", header=TRUE)
fma2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019fma.csv",
                   sep=",", header=TRUE)

#New England
ne2015=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2015\\2015ne.csv",
                 sep=",", header=TRUE)
ne2016=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2016\\2016ne.csv",
                 sep=",", header=TRUE)
ne2017=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2017\\2017ne.csv",
                 sep=",", header=TRUE)
ne2018=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2018\\2018ne.csv",
                 sep=",", header=TRUE)
ne2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019ne.csv",
                 sep=",", header=TRUE)


#Pacific North West
pnw2015=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2015\\2015pnw.csv",
                sep=",", header=TRUE)
pnw2016=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2016\\2016pnw.csv",
                sep=",", header=TRUE)
pnw2017=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2017\\2017pnw.csv",
                sep=",", header=TRUE)
pnw2018=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2018\\2018pnw.csv",
                sep=",", header=TRUE)
pnw2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019pnw.csv",
                sep=",", header=TRUE)
#chesapeake
chs2016=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2016\\2016chs.csv",
                 sep=",", header=TRUE)
chs2017=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2017\\2017chs.csv",
                 sep=",", header=TRUE)
chs2018=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2018\\2018chs.csv",
                 sep=",", header=TRUE)
chs2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019chs.csv",
                 sep=",", header=TRUE)
#North Carolina
nc2016=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2016\\2016nc.csv",
                 sep=",", header=TRUE)
nc2017=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2017\\2017nc.csv",
                 sep=",", header=TRUE)
nc2018=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2018\\2018nc.csv",
                 sep=",", header=TRUE)
nc2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019fnc.csv",
                 sep=",", header=TRUE)
#Peach Tree
pch2016=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2016\\2016pch.csv",
               sep=",", header=TRUE)
pch2017=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2017\\2017pch.csv",
                sep=",", header=TRUE)
pch2018=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2018\\2018pch.csv",
                sep=",", header=TRUE)
pch2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019pch.csv",
                sep=",", header=TRUE)
#texas
tx2019=read.csv("C:\\Users\\iboti\\Documents\\Personal Projects\\FRC-District-Analysis\\districts2019\\2019tx.csv",
                 sep=",", header=TRUE)

#lists of years in a district
fim=list(fim2019,fim2018,fim2017,fim2016,fim2015) #Michigan
ind=list(ind2019,ind2018,ind2017,ind2016,ind2015) #indiana
fma=list(fma2019,fma2018,fma2017,fma2016,fma2015) #mid atlanticn
ne=list(ne2019,ne2018,ne2017,ne2016,ne2015) #new england
pnw=list(pnw2019,pnw2018,pnw2017,pnw2016,pnw2015) #pnw
chs=list(chs2019, chs2018, chs2017,chs2016) #chesepeake
nc=list(nc2019,nc2018,nc2017,nc2016) #NC
pch=list(pch2019,pch2018,pch2017,pch2016) #peachtree 
tx=list(tx2019) #texas


#list of districts in year
dist2015=list(fim2015,ind2015,fma2015, ne2015, pnw2015)
dist2016=list(fim2016,ind2016,fma2016, ne2016, pnw2016, chs2016, nc2016, pch2016)
dist2017=list(fim2017,ind2017,fma2017, ne2017, pnw2017, chs2017, nc2017, pch2017)
dist2018=list(fim2018,ind2018,fma2018, ne2018, pnw2018, chs2018, nc2018, pch2018)
dist2019=list(fim2019,ind2019,fma2019, ne2019, pnw2019, chs2019, nc2019, pch2019,tx2019)

#colors for years in chartssss
#2015:Green 2016:grey 2017: brown  2018: cyan  2019: darkblue
colors=list('darkblue','cyan3','tan4','slategray','darkolivegreen')
years=list('2019','2018','2017','2016','2015')



#creates a function that graphs a district or set of years 
rookieIncome = function(group){
  i=1
  for (year in group){
    scatter.smooth(year$rookie_year, year$income,
                   col=as.character(colors[i]),pch=19 ,
                  ylab = "Income", xlab='Rookie Year')
    fit = lm(year$rookie_year~year$income)
    i=i+1
  }
}
#creates a function that graphs a district or set of years 
rookieTravel = function(group){
  i=1
  for (year in group){
    scatter.smooth(year$rookie_year, year$average_distance,
                   col=as.character(colors[i]),pch=19 ,
                   ylab = "Distance Traveled For Events", xlab='Rookie Year')
    fit = lm(year$rookie_year~year$income)
    i=i+1
  }
}
#creates a function that graphs a district or set of years 
rookiePoints = function(group){
  i=1
  for (year in group){
    scatter.smooth(year$rookie_year, year$points,
                   col=as.character(colors[i]),pch=19 ,
                   ylab = "District Points", xlab='Rookie Year')
    fit = lm(year$rookie_year~year$income)
    i=i+1
  }
}

incomePoints = function(group){
  i=1
  for (year in group){
    scatter.smooth(year$income, year$points,
                   col=as.character(colors[i]),pch=19 ,
                   ylab = "District Points", xlab='Median Income')
    fit = lm(year$rookie_year~year$income)
    i=i+1
  }
}

incomeTravel = function(group){
  i=1
  for (year in group){
    scatter.smooth(year$average_distance, year$income,
                   col=as.character(colors[i]),pch=19 ,
                   ylab = "income", xlab='Travel')
    fit = lm(year$rookie_year~year$income)
    i=i+1
  }
}

TravelPoints = function(group){
  i=1
  for (year in group){
    scatter.smooth(year$average_distance, year$points,
                   col=as.character(colors[i]),pch=19 ,
                   ylab = "District Points", xlab='distance')
    fit = lm(year$rookie_year~year$income)
    i=i+1
  }
}

chartDist = function(group){
  rookieIncome(group)
  rookiePoints(group)
  rookieTravel(group)
  incomePoints(group)
  incomeTravel(group)
  TravelPoints(group)
}

#district by graph
chartDist(fim)













