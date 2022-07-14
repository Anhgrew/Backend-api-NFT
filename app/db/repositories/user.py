from db.models.user import UserHistory

user_history_collection = UserHistory


async def create_user_history(new_user_history: UserHistory) -> UserHistory:
    user = await new_user_history.create()
    return user


async def retrieve_user_history(user_id: str) -> UserHistory:
    user_history = await user_history_collection.find(
        UserHistory.user_id == user_id
    ).to_list()
    return user_history

