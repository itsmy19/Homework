S = str(input("Введите строку S: "))

print("Строка \'%s\' \nДлина строки %d сиволов." % (S, len(S)))

subs_set = set()
for i in range(len(S)):
    for j in range(len(S)-1 if i == 0 else len(S), i, -1):
        subs_set.add(hash(S[i:j]))

print("Количество подстрок:", len(subs_set))