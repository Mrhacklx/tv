import motor.motor_asyncio
from config import DB_NAME, DB_URI
from datetime import datetime

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.users = self.db.users

    def new_user(self, id, name, expiry_date):
        return dict(
            id = id,
            name = name,
            expiry_date = expiry_date,
        )
    # def new_user(self, id, name):
    #     timestamp_now = __import__('time').time()
    #     expire_seconds = 30 * 24 * 60 * 60  # 30 days in seconds
    #     expire_timestamp = timestamp_now + expire_seconds
    
    #     # Convert timestamp to readable date
    #     expire_date = __import__('time').strftime("%Y-%m-%d", __import__('time').localtime(expire_timestamp))
    
    #     return dict(
    #         id=id,
    #         name=name,
    #         expire_date=expire_date
    #     )


    async def add_user(self, id, name, expiry_date):
        user = self.new_user(id, name, expiry_date)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        return bool(user)

    # async def check_remaining_uasge(self, user_id):
    #     user_data = await self.users.find_one({"id": user_id})
    #     if user_data:
    #         expiry_time = user_data.get("expiry_date")
    #         if expiry_time is None:
    #             return 0  # No active premium
    
    #         # Ensure expiry_time is a datetime object
    #         if isinstance(expiry_time, datetime):
    #             now = datetime.now()
    #             if now <= expiry_time:
    #                 remaining = (expiry_time - now).days
    #                 return max(1, remaining)  # At least 1 day left
    #             else:
    #                 # Expired, clear it
    #                 await self.users.update_one({"id": user_id}, {"$set": {"expiry_time": None}})
    #                 return 0
    #     return 0

    async def check_remaining_uasge(self, user_id):
        user_data = await self.col.find_one({"id": int(user_id)})
        if user_data:
            expiry_str = user_data.get("expiry_date")
            if expiry_str is None:
                return 1  # No active premium
    
            try:
                expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d").date()
                today = datetime.utcnow().date()
    
                if today <= expiry_date:
                    remaining = (expiry_date - today).days
                    return max(1, remaining)
                else:
                    return 2
            except ValueError:
                # If date format is invalid
                return 3
    
        return 4

    async def check_expiry_date(self, id, today):
        user = await self.col.find_one({'id': int(id)})
        if not user or 'expiry_date' not in user:
            return False 
        expiry_date = datetime.strptime(user['expiry_date'], '%Y-%m-%d').date()
        if isinstance(today, str):
            today = datetime.strptime(today, '%Y-%m-%d').date()
        return today < expiry_date

         

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count
    
    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})





db = Database(DB_URI, DB_NAME)
