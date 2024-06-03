from django.shortcuts import render
import datetime
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request


def index(request):
    x=datetime.datetime.now()
    time = x.strftime("%I"+":"+"%M"+" "+"%p")
    day = x.strftime("%a")
    date = x.strftime("%d")
    month = x.strftime("%b")
    year = x.strftime("%Y")
    
    if request.method == 'POST':
        city = request.POST.get('city')
        ''' api key might be expired use your own api_key
            place api_key in place of appid="your api_key here "  '''

        # source contain json data from api

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=48a90ac42caa09f90dcaeee4096b9e53').read()
        list_of_data = json.loads(source)
        # converting json data to dictionary
        
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
          
            "location_name": str(list_of_data['name']),
            
            "temp": round(int((list_of_data['main']['temp']))-273.15),
            'sky': str(list_of_data['weather'][0]['description']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'visibility':int(str(list_of_data["visibility"]))/1000,
            "wind": int(list_of_data['wind']["speed"]),
            "cloud": int(list_of_data['clouds']['all']),
            "time": time,
            "day": day,
            "date": date,
            "month": month,
            "year" : year

        }
       
    else:
        data={"location_name": 'pataudi',
            
            "temp":30,
            'sky': 'sunny',
            "pressure": 1008,
            "humidity": 25,
            'visibility':10,
            "wind": 5,
            "cloud": 20,
             "time": time,
            "day": day,
            "date": date,
            "month": month,
            "year" : year
}
    return render(request, "weather/template/index.html",data) 
