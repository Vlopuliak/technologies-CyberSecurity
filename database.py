import sqlite3


def get_lead_by_email_secure(email_address):
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leads WHERE email = ?", (email_address,))
    result = cursor.fetchone()

    conn.close()
    return result


if __name__ == "__main__":
    setup_conn = sqlite3.connect('crm_database.db')
    setup_conn.execute("CREATE TABLE IF NOT EXISTS leads (id INTEGER PRIMARY KEY, email TEXT, name TEXT)")
    setup_conn.execute("INSERT OR IGNORE INTO leads (id, email, name) VALUES (1, 'test@example.com', 'Ivan')")
    setup_conn.commit()
    setup_conn.close()

    print("--- Тестування модуля бази даних ---")
    print("Шукаємо ліда test@example.com...")

    lead = get_lead_by_email_secure('test@example.com')
    print(f"Результат з БД: {lead}")