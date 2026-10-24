from collections import Counter

with open("V9.txt", "r", encoding="utf-8") as f:
    cipher_text = f.read().strip()

total_chars = len(cipher_text)
counts = Counter(cipher_text)

print("ЧАСТОТНИЙ АНАЛІЗ ШИФРОТЕКСТУ (ТОП-15 СИМВОЛІВ)")
for char, count in counts.most_common(15):
    print(f"Символ '{char}': {count} разів (частота: {count / total_chars:.4f})")

orig_alpha = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя,.- "
ciph_alpha = "холдний ракгтєміс,це-ьпзу.бвґжїфчщюяш"

dec_table = str.maketrans(ciph_alpha, orig_alpha)
plain_text = cipher_text.translate(dec_table)

print("\nТАБЛИЦЯ ПІДСТАНОВКИ (Таблиця 2)")
print(f"Відкритий алфавіт: {orig_alpha}")
print(f"Шифроалфавіт:      {ciph_alpha}")

print("\nРОЗШИФРОВАНИЙ ТЕКСТ")
print(plain_text)

with open("decrypted_V9.txt", "w", encoding="utf-8") as f:
    f.write(plain_text)