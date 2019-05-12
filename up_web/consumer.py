# from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import redirect
from channels.db import database_sync_to_async
from .models import Task
import json


class BroadCastConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'abc'
        self.room_group_name = 'def'
        print('@'*5, 'connected to websocket.')
        ''' 
        1. on connect to socket create a websocket instance
        2. 
         '''
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()


    async def disconnect(self, close_code):
        print('@'*5, 'Disconnected.')
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await redirect('/')

    async def receive(self, text_data):
        '''
        1. creates task on getting new data.
        2. 
        '''
        task = json.loads(text_data)
        await self.create_task(task)

    @database_sync_to_async
    def create_task(self, data):
        created_by = data['created_by']
        title = data['title']
        priority = data['priority']
        status = 'new'
        task = Task(title=title, priority=priority, created_by=created_by, status=status)
        task.save()
