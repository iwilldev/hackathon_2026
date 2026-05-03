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
   return HttpResponse(template.render(context))

def details(request):
   roomId = request.GET.get('id',0) # Changed this variable so I can use room_id which is in the db
   # Note to Alex: The reason this wasn't working was because it's a string not an int so it wasn't equal to 0, it was equal to '0'
   # But I think it is better to also have it be greater than 0 numerically so I added some error checking here for that as well
   # also there is error checking for if the requested room isnt in the db
   error = False
   try:
      if int(roomId) <= 0:
         error = 'Room ID must be an int above zero'
   except:
      error = 'Room ID must be an int'
   
   if request.method != 'GET':
      error = 'Request must be GET'

   # filter in django is where in sql
   getName = Room.objects.filter(id=roomId).values_list('room_name')

   # Because I know Alex likes explanations I will give you big explanation here in lieu of giving a push comment
   # A user MIGHT enter a room ID that doesn't exist like 99999 so in that case also give error message
   if len(getName) == 0:
      error = 'Invalid room ID ' , roomId , '; this room does not exist'

   page = 'details'
   if error:
      page = 'error'
   
   template = loader.get_template(page + '.html')

   if error:
      return HttpResponse(template.render({
         'issue':error,
      }))
   
   # Yay no problems
   # lowkey not sure what values_list vs values is and im too lazy to look it up but sometimes they work interchangeably sometimes not :shrug:
   compList = Computers.objects.filter(room_id=roomId).values('online','comp_name')
   roomName = getName[0][0] # Not sure why it is wrapped 2 times but whatever

   data = {
      'room':roomName,
      'status':compList,
   }

   # send this to the client
   # at this point i gotta go to late night brock so i didnt quite finish this dont hate me but yeah anyway i work on the client end of this tmr
   # this SHOULD work but i havent tested it yet and things almost never work first try we will see what happens
   return HttpResponse(template.render(data))