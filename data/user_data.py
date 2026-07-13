import time

timestamp = int(time.time())

REGISTER_USER = {
    "first_name": "Тест",
    "last_name": "Тестов",
    "username": f"test_user_{timestamp}",
    "email": f"test_{timestamp}@mail.ru",
    "password": "TestPass123!"
}