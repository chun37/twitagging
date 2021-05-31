from dataclasses import dataclass

from tweepy import API, OAuthHandler, models
import typedjson


@dataclass(frozen=True)
class User:
    id: int
    id_str: str
    name: str
    screen_name: str
    location: str
    url: str
    description: str
    protected: bool
    verified: bool
    followers_count: int
    friends_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int
    created_at: str
    profile_banner_url: str
    profile_image_url_https: str
    default_profile: bool
    default_profile_image: bool


class TwitterAPI:
    def __init__(
        self, consumer_key, consumer_secret, access_token, access_token_secret
    ):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = API(auth)

    def get_user_from_id(self, user_id) -> tuple[User, dict]:
        tweepy_user: models.User = self.api.get_user(user_id=user_id)
        return typedjson.decode(User, tweepy_user._json), tweepy_user._json
