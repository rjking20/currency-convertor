from django.shortcuts import render,redirect,HttpResponse
from forex_python.converter import CurrencyRates,CurrencyCodes



def convertor(request):
    context = {
        'val':'1',
        'display':'hidden'
    }
    return render(request,'currency.html',context)

def buttonAction(request):
    status = request.POST.get('status')
    if 'convert' in request.POST and '1' == status:
        return convert(request)
    elif 'clean' in request.POST:
        return clean(request)
    else:
        return render(request,'currency.html',{'val':'0','display':'show','click':'none'})



def convert(request):
    result = None
    try:
        if request.method == 'POST':
            currency = int(request.POST.get('inpt'))
            inpt = request.POST.get('curInput')
            oupt = request.POST.get('curOutput')
            rates = CurrencyRates()
            codes = CurrencyCodes()
            result = rates.convert(inpt,oupt,currency)
            symb1 = codes.get_symbol(inpt)
            symb2 = codes.get_symbol(oupt)

        print(inpt,oupt,result)

        if result:
            context = {
            'input':currency,
            'result':result,
            'val':'0',
            'opt1': inpt,
            'opt2': oupt,
            'symb1':symb1,
            'symb2':symb2

            }


    except:
        context = {
            'input': currency,
            'result': 'This conversion is not available',
            'val':'1',
        }

    return render(request,'currency.html',context)

def clean(request):
    context = {
        'val':'1'
    }
    return render(request,'currency.html',context)
