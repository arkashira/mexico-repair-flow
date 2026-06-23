# Password Reset Service
A simple password reset service implemented in Python.

## Usage
1. Create a user: `service.create_user("user1", "password")`
2. Generate a password reset token: `service.generate_password_reset_token("user1")`
3. Validate the token: `service.validate_password_reset_token(token)`
4. Reset the password: `service.reset_password("user1", "new_password")`
5. Send a password reset email: `service.send_password_reset_email("user1", token)`
6. Send a password change confirmation email: `service.send_password_change_confirmation_email("user1")`
