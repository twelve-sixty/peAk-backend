# from channels.generic.websocket import WebsocketConsumer
# import json


# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         self.send(text_data=json.dumps({
#             'message': message
#         }))


from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import datetime
from board.models import Message, MessageBoard, PeakUser, User
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # obtain from URL route in chat/routing.py
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # create a channels group based on user-specified room name
        self.room_group_name = 'chat_%s' % self.room_name

        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # accepts websocket connection.
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    def chat_message(self, event):
        message = event['message']
        print('message magic from chat_message: ', dir(self))
        print(self.scope['user'])
        print(self.room_name)
        user = PeakUser.objects.filter(user__username=self.scope['user'])
        # message_board=MessageBoard.objects.filter()
        print("*"*25)
        print('user created: ', list(user)[0])
        print('user type: ', type(user))
        print('user type: ', type(user.distinct()))

        model = Message(
            message_user=list(user)[0],
            message=message,
            # message_board=message_board
            message_date=datetime.date.today().strftime('%Y-%m-%d'))
        print('model created: ', model)
        model.save()

        self.send(text_data=json.dumps({
            'message': message
        }))
