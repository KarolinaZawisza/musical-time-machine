class UserModule:

    def __init__(self, user_id: int):
        self.user_id = user_id

    def get_user_tracks_by_time(self, sorting_type):
        # 