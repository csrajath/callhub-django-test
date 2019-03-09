import time                                         # used to calculate time consumed for execution
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from displaynfib.models import FibOutput

def calculatefibonacci(num):                           #fibonacci logic
    if num < 2:
        return 1                                        # if input value is less than 2, 1 is the result
    else:
        n1 = 1                                          #initializing first and second position values to 1
        n2 = 1
        for i in range(2, num):                         #looping through the numbers from 2nd number to nth
            t = n1 + n2
            n1 = n2
            n2 = t
        return n2

def return_n_fib(request):                          #function returing the html and displaying the result with time
    num = 0
    result = 0
    time_taken = 0

    if request.GET.get('number'):
        start = time.time()
        number = request.GET.get('number')
        num = int(number)
        result = calculatefibonacci(num)
        end = time.time() - start
        time_taken = str(end)[0:5]                  #calculating the time consumed for execution

        pt = FibOutput.objects.create(number=num, result=result, time_taken=time_taken)
        pt.save()

    return render(request, 'index.html',{'number': num, 'result': result, 'time_taken': time_taken})
