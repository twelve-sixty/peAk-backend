from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})






# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing


# # point the root config at the chat routing.

# # the protocoltyperouter will first inspect the type of connection.
# # if it is a websocket connection (ws:// or wss://),
# # hand it to AuthMiddleareStack
# application = ProtocolTypeRouter({

#     # AuthMiddleareStack populates the connection's scope with reference
#     # to the currently authenticated user, and hand it to URLRouter
#     'websocket': AuthMiddlewareStack(

#         # URLRouter will examine the HTTP path
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })
