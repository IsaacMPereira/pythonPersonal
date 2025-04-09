lmx = cmx = 3
mx = []
count = 1

for i in range(lmx):
    linhas = []
    for j in range(cmx):
        linhas.append(count)
        count += 1
    mx.append(linhas)

print(mx)
print()

for linhas in mx:
    print(linhas)

print()

for linha in mx:
    for elemento in linha:
        print(elemento, end=" ")
    print()
