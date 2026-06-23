import json
import dataclasses
from datetime import datetime, timedelta
from typing import Optional

@dataclasses.dataclass
class PasswordResetToken:
    token: str
    expires_at: datetime

class PasswordResetService:
    def __init__(self):
        self.tokens = {}
        self.users = {}

    def generate_password_reset_token(self, user_id: str) -> str:
        token = json.dumps({"user_id": user_id, "expires_at": (datetime.now() + timedelta(hours=1)).isoformat()})
        self.tokens[token] = PasswordResetToken(token, datetime.now() + timedelta(hours=1))
        return token

    def validate_password_reset_token(self, token: str) -> Optional[str]:
        if token in self.tokens:
            token_data = self.tokens[token]
            if token_data.expires_at > datetime.now():
                return token_data.token
        return None

    def reset_password(self, user_id: str, new_password: str) -> bool:
        if user_id in self.users:
            self.users[user_id]["password"] = new_password
            return True
        return False

    def send_password_reset_email(self, user_id: str, token: str) -> bool:
        # Simulate sending an email
        print(f"Sending password reset email to user {user_id} with token {token}")
        return True

    def send_password_change_confirmation_email(self, user_id: str) -> bool:
        # Simulate sending an email
        print(f"Sending password change confirmation email to user {user_id}")
        return True

    def create_user(self, user_id: str, password: str) -> bool:
        self.users[user_id] = {"password": password}
        return True
