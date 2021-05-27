
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from pfc.models import pfc 
from django.shortcuts import render, get_object_or_404
from pfc.serializers import pfcSerializer
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from pfc import pfcscript
import json
from json import dumps
from rest_framework import status
import csv, calendar
import io
import numpy
from django.views.decorators.csrf import csrf_protect
# Create your views here.
    

final = []
weekday = []
weekend = []

@csrf_protect
def home(request):
    data = pfc.objects.all()
    return render(request, 'upload_csv.html')


@api_view(["POST"])
def get_data(request):
    d = dict(request.POST)
    #print("data",d)
    main = []
    for k in d :
        main.append(d[k])

    N = len(main)-1
    for i in range(2,N):
        final.append(main[i]) 

    #print(final)    #prints all the data in date- 1..2..3..4..24 format
    
    filter = pfcscript.task(final)
    #print(filter)   #prints data in date-hour-price format
   
    year = 2017
    fyear = 2023
    filter2 = pfcscript.task1(filter,year)
    #print(filter2)
    input_year = pfcscript.yearcreation(filter2,year,fyear)  #copied to forwarded year
    #print(input_year)
    sep_input = input_year
    # R,T = pfcscript.seperate1(sep_input) #to forwarding ex 2024
    # Y,Z = pfcscript.seperate1(filter2)  #from forwarding ex 2017
   
    res1 = pfcscript.day_to_day_mapping(year, fyear) #diff bet years
    additional_days = pfcscript.add_on(filter,year,res1) #diff bet year and last days
    #print(res1)

    day_map = pfcscript.mapping(filter2,input_year,res1,additional_days)
    # weekday_map = pfcscript.mapping(Y,R)
    #print(day_map)
    new_day_map = pfcscript.date_format_sol(day_map)
    # year_unsorted =  weekday_map + weekend_map
    # #print(year_unsorted)
    # monthly_sep_unsort = pfcscript.monthlseparation(year_unsorted)

    # arr1 = monthly_sep_unsort[0]
    # # arr2 = arr1[0]
    # #print(len(arr1))
    # # str1 = arr2[0]
    # # date1 = str1[0:2]
    # # print(date1)
    # #print(monthly_sep_unsort)
    # sorted_year = pfcscript.sort_monthly(monthly_sep_unsort)
    # #print(sorted_year)
    convert = pfcscript.convert_integer(new_day_map)
    # #print(convert)

    # full_year_avg = pfcscript.full_year_avg(convert)
    # #print(convert)
    # r1, r2, r3, r4 = pfcscript.quarter_avg(convert)
    # dateList=[1,2,3]
    # # print(full_year_avg)
    # # print("Quarterly average -" )
    # # print(r1, r2, r3, r4)

    
    # # # a = numpy.array(Z)
    # # numpy.savetxt("data3.csv", a, delimiter=",")
    
    # # with open('file.csv', 'w', newline='') as f:
    # #     writer = csv.writer(f)
    # #     writer.writerows(convert)
    
    # # print(weekend_map)
    # # A, B = pfcscript.seperate(final)
    # # weekday = pfcscript.roundingyear(A)
    # # weekend = pfcscript.roundingyear(B)
    # # mat = pfcscript.YM(weekday)   #print it and see the results
    # # mat1 = pfcscript.YM(weekend)

    # # print(mat1)
    # # print("weekday")
    # # print(mat)
    data={'date1':convert}
    # dict1={'date1':dateList}
    return HttpResponse(json.dumps(data))
        # print(dict1)
    
    # data = dumps(convert)

    # return HttpResponse({'data': data})
    # data = dumps(convert)
    # return render(request, "upload_csv.html", {"data": data})
    
    # return JsonResponse({"Message":'Hi Post'})











# def check_weekday(date):
#     day = ""
#     month = ""
#     year = ""  
#     day += date[0:2]
#     month += date[3:5]
#     year += date[6:10]
#     week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#     week_num = calendar.weekday(int(year),int(month),int(day))
   
#     if(week_num > 4):
#         return 0
#     else:
#         return 1


# def seperate(final):     #seperates the weekday and weekend data
#     size = len(final)
#     for i in range(size):
#         if (check_weekday(final[i][0]) == 1):
#             weekday.append(final[i])
#         else:
#             weekend.append(final[i])
#     print(weekday)
    














# class pfcViewset(viewsets.ModelViewSet):
#     queryset = pfc.objects.all()
#     serializer_class = pfcSerializer
#     http_method_names = ('get', 'post', 'patch', 'delete')
#    # permission_classes = [pfcPermission]

#     def create(self, request):
#         print(self.request)
#         d = dict(request.POST)
#         print("data",d)
#         # fileName = request.data['file']
#         # print("file name",fileName)
#         # csvfile = request.FILES['file'].read().decode("UTF-8")
       
#         # print("type",type(csvfile))
#         # print("csvfile",csvfile)

#         # io_string=io.StringIO(csvfile)
#         # next(io_string)
        
       
#         # for column in csv.reader(io_string,delimiter=","):
#         #     print(column[0])
                

#         return Response(status=status.HTTP_204_NO_CONTENT)


# with open('filepath/filename.csv', "rt", encoding='ascii') as infile:
#     read = csv.reader(infile)
#     for row in read :
#         print (row)








