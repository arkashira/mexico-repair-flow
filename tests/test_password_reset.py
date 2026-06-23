from datetime import datetime, timedelta
from password_reset import PasswordResetService

def test_generate_password_reset_token():
    service = PasswordResetService()
    token = service.generate_password_reset_token("user1")
    assert token in service.tokens

def test_validate_password_reset_token():
    service = PasswordResetService()
    token = service.generate_password_reset_token("user1")
    validated_token = service.validate_password_reset_token(token)
    assert validated_token == token

def test_reset_password():
    service = PasswordResetService()
    service.create_user("user1", "old_password")
    token = service.generate_password_reset_token("user1")
    validated_token = service.validate_password_reset_token(token)
    assert service.reset_password("user1", "new_password")
    assert service.users["user1"]["password"] == "new_password"

def test_send_password_reset_email():
    service = PasswordResetService()
    token = service.generate_password_reset_token("user1")
    assert service.send_password_reset_email("user1", token)

def test_send_password_change_confirmation_email():
    service = PasswordResetService()
    assert service.send_password_change_confirmation_email("user1")

def test_create_user():
    service = PasswordResetService()
    assert service.create_user("user1", "password")

def test_invalid_token():
    service = PasswordResetService()
    assert service.validate_password_reset_token("invalid_token") is None

def test_expired_token():
    service = PasswordResetService()
    token = service.generate_password_reset_token("user1")
    service.tokens[token].expires_at = datetime.now() - timedelta(hours=1)
    assert service.validate_password_reset_token(token) is None
