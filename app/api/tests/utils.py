from django.contrib.auth import get_user_model

from core.models import User, FriendRequest


def create_user(**params: str) -> User:
    """Creates a User with a given params"""

    return get_user_model().objects.create_user(**params)


def create_friend_request(**params: User) -> FriendRequest:
    """Creates a FriendRequest with a given params"""

    FriendRequest.objects.create(**params)