from tweepy import OAuthHandler, API
from tweepy.models import List


class Twitter:
    def __init__(
        self,
        consumer_key: str,
        consumer_secret: str,
        access_token: str,
        access_token_secret: str,
    ):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = API(auth)

    def create_list(
        self, name: str, description: str = "", is_private: bool = False
    ) -> List:
        return self.api.create_list(
            name=name,
            description=description,
            mode="private" if is_private else "public",
        )
