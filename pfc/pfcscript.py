import sys
import calendar
import datetime

weekday = []
weekend = []

# def __init__(self, name):   
#         self.name = name   

def task(arr):        #retuns task 1
    final = []

    for i in range(2,len(arr)):
        for j in range(1,25):
            temp = []
            temp.append(arr[i][0])
            temp.append(j)
            temp.append(arr[i][j])
            final.append(temp)
    return final

def task1(arr, year):
    result = []
    for i in range(len(arr)):
        date = arr[i][0]
        if date[6:10] == str(year):
            result.append(arr[i])

    return result

def yearcreation(arr,tyear,year):
    result = []
    diff = year-tyear
    # res = leap(year)
    # res1= leap(tyear)
    # if res == 1 and res1 == 0: 
    #     for i in range(0, len(arr)):
    #         for j in range(1,3):
    #             temp = []
    #             tt = arr[i][0]
    #             t = tt[0:6]
    #             ttt = int(tt[6:10])+diff
    #             tttt = t+str(ttt)
    #             temp.append(tttt)
    #             temp.append(arr[i][1])
    #             temp.append(arr[i][j])
    #         result.append(temp)
    #     k = 1
    #     for j in range(1416,1440):
    #         tt = ["29/02/"+str(year),k,32]
    #         result.insert(j, tt)
    #         k+=1
    #     return result
    
    for i in range(0, len(arr)):
        for j in range(1,3):
            temp = []
            tt = arr[i][0]
            t = tt[0:6]
            ttt = int(tt[6:10])+diff
            tttt = t+str(ttt)
            temp.append(tttt)
            temp.append(arr[i][1])
            temp.append(arr[i][j])
        result.append(temp)
        
    return result


def convert_integer(arr):
    result = []
    for i in range(len(arr)):
        temp = []
        temp.append(arr[i][0])
        temp.append(int(arr[i][1]))
        temp.append(float(arr[i][2]))
        result.append(temp)

    return(result)

def check_weekday(date):
    day = ""
    month = ""
    year = ""  
    day += date[0:2]
    month += date[3:5]
    year += date[6:10]
    week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    week_num = calendar.weekday(int(year),int(month),int(day))
   
    if(week_num > 4):
        return 0
    else:
        return 1


def seperate(final1):     #seperates the weekday and weekend data
    size = len(final1)
    for i in range(size):
        if (check_weekday(final1[i][0]) == 1):
            weekday.append(final1[i])
        else:
            weekend.append(final1[i])
    return weekday, weekend


def check_weekday1(date):
    day = ""
    month = ""
    year = ""  
    day += date[0:2]
    month += date[3:5]
    year += date[6:10]
    week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    week_num = calendar.weekday(int(year),int(month),int(day))
   
    if(week_num > 4):
        return 0
    else:
        return 1


def seperate1(final1):     #seperates the weekday and weekend data
    size = len(final1)
    weekday1 = []
    weekend1 = []
    for i in range(size):
        if (check_weekday1(final1[i][0]) == 1):
            weekday1.append(final1[i])
        else:
            weekend1.append(final1[i])
    return weekday1, weekend1




def monthlseparation(arr):
    jan = []
    feb = []
    march = []
    aprl = []
    may = []
    june = []
    july = []
    aug = []
    sep = []
    octo = []
    nov = []
    dec = []
    numb = ['01','02','03','04','05','06','07','08','09','10','11','12']
    align = [jan,feb,march,aprl,may,june,july,aug,sep,octo,nov,dec]

    for j in range(12):
        for i in range(len(arr)):
            temp = arr[i][0]
    
            if temp[3:5] == numb[j]:
                (align[j]).append(arr[i])
    temp1 = arr[0][0]
   # print("The data of year",temp1[6:10])
    return align        #returns array of array contains all months of a year


def roundingyear(arr):
    nwarr = []      #year wise separation
    start = arr[0][0]   
    y = 0
    if (start[3:5] != '01'):
        y = int(start[6:10])
       # print(y)

    for i in range(len(arr)):
        temp = arr[i][0]

        if temp[6:10] ==str(y):
            continue
        else:
            nwarr.append(arr[i])
    return nwarr

def seperateyear(arr):
    cyear=[]       #seperated year data
    remain = []     #remainning data which exclude cyear
    start1 = arr[0][0]
    y = start1[6:10]
    for i in range(len(arr)):
        start = arr[i][0]
        if start[6:10] == y: 
            cyear.append(arr[i])
        else:
            remain.append(arr[i])

    return cyear

def monthlyavg(month):
    arr = []
    for i in range(24):
        sum = 0
       # temp = []
        aver = 0
        for j in range(len(month)):
            sum = sum + float(month[j][i+1])
        aver = sum/len(month)
        #temp.append(round(aver,2))
        arr.append(round(aver,2))
    return arr

def YM(arr):
    curyear = seperateyear(arr)
    monthsofyear = monthlseparation(curyear)   #gives data in the form of months of cyear

    res = []
    for i in range(len(monthsofyear)):
        temp = monthlyavg(monthsofyear[i])
        res.append(temp)
    return res


def leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 1
            else:
                return 0
        else:
           return 1
    else:
        return 0




def mapping(arr1,arr2, d,add_days):
    diff= d*24
    n = min(len(arr1),len(arr2))
    for i in range(0,n):
        arr2[i-diff][2] = arr1[i][2]
    
    y = arr2[0][0]
    ye = y[6:10]
   
    if(leap(int(ye)) == 1):
        k = 1
        for j in range(1416,1440):
            tt = ["29/02/"+ ye,k,32]
            arr2.insert(j, tt)    
            k+=1
        for kp in range(1416,1440):
             arr2[kp][2] = arr2[kp-24][2]
    
    start = len(arr2) - diff
    for k in range(diff):
        arr2[start][2] = add_days[k][2]
        start+=1
    
    return arr2

def add_on(arr,year,d):
    diff = d*24
    fin = [] # has final output
    result = []
    for i in range(len(arr)):
        date = arr[i][0]
        if date[6:10] == str(year+1):
            result.append(arr[i])
    # res2 = task(result)
    #print(res2)
    for j in range(diff):
        fin.append(result[j])

    return fin


def date_format_sol(arr):
    for i in range(len(arr)):
        day = arr[i][0]
        day1 = day[0:2]
        month = arr[i][0]
        month1 = month[3:5]
        year = month[6:10]
        date = month1+"/"+day1+"/"+year
        arr[i][0] = date
    print((arr))
    return arr


def full_year_avg(arr):
    total = 0
    avg = 0
    n = len(arr)
    for i in range(len(arr)):
        total += arr[i][2]
    avg = total//n
    return avg  


def day_to_day_mapping(cyear, fyear):
    diff = fyear-cyear
    for i in range(cyear,fyear):
        if(leap(i) == 1):
            diff += 1
        
    
    print(diff)
    return diff


def quarter_avg(arr):
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    total = 0
    for i in range(0,2160):
        total += arr[i][2]
    r1 = total//2160

    total1 = 0
    for j in range(2160,4344):
        total1 += arr[j][2]
    r2 = total1//2184

    total2 = 0
    for j in range(4344,6552):
        total2 += arr[j][2]
    r3 = total2//2208

    total3 = 0
    for j in range(6552,8760):
        total3 += arr[j][2]
    r4 = total3//2208
    return r1, r2, r3, r4

def sort_monthly1(arr):
    temp = []
    k=1
    while(k <= len(arr)//24):
        for i in range(0,len(arr)):
            arr2 = arr[i]
            str1 = arr2[0]
            date1 = str1[0:2]
        
            if (int(date1) == k):
                temp.append(arr2)

        k+=1
    
                
    return temp
    

def sort_monthly(arr5):
    temp = []
    simple = []
    for i in range(0,12):
        res = sort_monthly1(arr5[i])
        temp.append(res)
    
    for j in range(0,len(temp)):
        for k in range(0,len(temp[j])):
            simple.append(temp[j][k])

   
    return simple

