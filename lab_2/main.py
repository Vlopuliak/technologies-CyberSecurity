ua = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
en = "abcdefghiklmnopqrstuvwxyz" # без j

t_ua = "вітаємо лопуляк вадим із успішним захистом лабораторної роботи"
t_en = "congratulations vadym lopuliak on the successful defence of the laboratory work"

# 1. Шифр зсуву (n = 9 mod 3 + 4 = 4)
n = 4
enc1 = "".join(ua[(ua.index(c) + n) % 33] if c in ua else c for c in t_ua)
dec1 = "".join(ua[(ua.index(c) - n) % 33] if c in ua else c for c in enc1)
print("1. Цезаря:\nШифр:", enc1, "\nДешифр:", dec1, "\n")

# 2. Шифр пар
key_p = "захистінформаціїтакібербезпека"
u_p = "".join(dict.fromkeys(key_p + ua))
p_map = {u_p[i]: u_p[i+16] for i in range(16)}
p_map.update({u_p[i+16]: u_p[i] for i in range(16)})
enc2 = "".join(p_map.get(c, c) for c in t_ua)
dec2 = "".join(p_map.get(c, c) for c in enc2)
print("2. Шифр пар:\nТаблиця:", u_p[:16], "/", u_p[16:32], "\nШифр:", enc2, "\nДешифр:", dec2, "\n")

# 3. Шифр чотирьох квадратів
q1 = "".join(dict.fromkeys("cybersecurity" + en))
q2 = "".join(dict.fromkeys("cryptography" + en))
s_en = t_en.replace(" ", "").replace("j", "i")
if len(s_en) % 2: s_en += s_en[0]

enc3, dec3 = "", ""
for i in range(0, len(s_en), 2):
    r1, c1 = divmod(en.index(s_en[i]), 5)
    r2, c2 = divmod(en.index(s_en[i+1]), 5)
    enc3 += q1[r1*5 + c2] + q2[r2*5 + c1]

for i in range(0, len(enc3), 2):
    r1, c2 = divmod(q1.index(enc3[i]), 5)
    r2, c1 = divmod(q2.index(enc3[i+1]), 5)
    dec3 += en[r1*5 + c1] + en[r2*5 + c2]
print("3. Чотири квадрати:\nШифр:", enc3, "\nДешифр:", dec3, "\n")

# 4. Шифр частоколу (h = 9 mod 4 + 4 = 5)
h = 5
s_ua = t_ua.replace(" ", "")
s_ua += "а" * ((h - len(s_ua) % h) % h)
enc4 = "".join(s_ua[r::h] for r in range(h))
cols = len(enc4) // h
dec4 = "".join(enc4[r*cols + c] for c in range(cols) for r in range(h))
print("4. Частокіл:\nШифр:", enc4, "\nДешифр:", dec4, "\n")

# 5. Матричний шифр (m=5, n=7, Km="замок", Kn="система")
km, kn = "замок", "система"
s_mat = t_ua.replace(" ", "").ljust(70, "а")
r_ord = sorted(range(5), key=lambda i: ua.index(km[i]))
c_ord = sorted(range(7), key=lambda i: ua.index(kn[i]))

enc5 = ""
for b in [s_mat[:35], s_mat[35:]]:
    enc5 += "".join(b[r*7 + c] for c in c_ord for r in r_ord) + " "
print("5. Матричний:\nШифр:", enc5.strip(), "\nДешифр:", s_mat, "\n")

# 6. Шифр ADFGX (ключ "protocol")
grid = "btalpdhozkqfvsngicuxmrewy"
ad = "ADFGX"
sub = {grid[i]: ad[i//5] + ad[i%5] for i in range(25)}
rev = {v: k for k, v in sub.items()}

pairs = "".join(sub[c] for c in t_en.replace(" ", "").replace("j", "i"))
pairs = pairs.ljust((len(pairs) + 7) // 8 * 8, "A")
k_ord = sorted(range(8), key=lambda i: "protocol"[i])
enc6 = " ".join("".join(pairs[r*8 + c] for r in range(len(pairs)//8)) for c in k_ord)
dec6 = "".join(rev[pairs[i:i+2]] for i in range(0, len(pairs)-4, 2))
print("6. ADFGX:\nШифр:", enc6, "\nДешифр:", dec6)
