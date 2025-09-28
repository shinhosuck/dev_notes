from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        try:
            token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
        except ValueError:
            token_key = None
        scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
        return await super().__call__(scope, receive, send)



from django.urls import path

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from yourapp.consumers import SocketCostumer
from yourapp.token_auth import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddlewareStack(
        URLRouter([
            path("socket/", SocketCostumer),
        ]),
    ),

})


async def connect(self):
    user_data = self.scope.get('query_string').decode().split('&')
    self.user = {i.split('=')[0]:i.split('=')[1] for i in user_data}
    self.is_authenticated = await database_sync_to_async(self.get_users)()

    if not self.is_authenticated:
        await self.send(json.dumps({'error': 'Please login first to access websocket'}))
        await self.close()
    else:
        await self.accept()

def get_users(self):
    token_obj = Token.objects.get(key=self.user.get('token'))
    return token_obj.user.username == self.user.get('user')
