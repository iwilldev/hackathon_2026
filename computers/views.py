from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Computers,Room

def home(request):
   compList = Computers.objects.values_list('online','room_id')
   roomList = Room.objects.all().values()

   data = []

   for room in roomList:
      rId = room['id']
      rName = room['room_name']
      data.append({
         'roomName': rName,
         'amountOnline': 0,
         'total': 0,
         'roomId': rId, # Not necessary for client, but needs to be sent back to srv
      })
      current = data[-1]
      for comp in compList:
         isOnline = comp[0]
         roomId = comp[1]
         if comp[1] == rId:
            if isOnline:
               current['amountOnline'] += 1
            current['total'] += 1

   context = {
      'list': data,
   }

   template = loader.get_template('index.html')
   return HttpResponse(template.render(context,request))

def details(request):
<<<<<<< HEAD
   room_id = request.GET.get("id", 0)
   if request.method == 'GET' and room_id != 0:
      template = loader.get_template('Details.html')
      return HttpResponse(template.render())
   else:
      template = loader.get_template('error.html')
      return HttpResponse(template.render())
=======
   template = loader.get_template('details.html')
   return HttpResponse(template.render())
>>>>>>> e861a09b82fc484bcc31d2d383dce03c572e385f
