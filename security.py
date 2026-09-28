import bcrypt


def hash_employee_password(plain_text_password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed_password


if __name__ == "__main__":
    test_password = "MySuperSecretPassword123"
    hashed = hash_employee_password(test_password)

    print("--- Тестування модуля шифрування ---")
    print(f"Оригінальний пароль: {test_password}")
    print(f"Захешований пароль (те, що йде в БД): {hashed}")