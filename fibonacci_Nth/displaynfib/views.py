from django.shortcuts import render

def return_n_fib(request):                          #function returing the html and displaying the result with time
    return render(request, 'index.html')

