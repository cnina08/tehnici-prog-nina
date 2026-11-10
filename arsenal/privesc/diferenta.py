from arsenal.privesc.enum import citeste_linii, nume, GTFO

# B1 Două mulțimi: curat și acum
def cai(fisier):
    return set(citeste_linii(fisier))

baza = cai("arsenal/privesc/start/baza_suid.txt")
acum = cai("arsenal/privesc/start/suid.txt")
print("baza:", len(baza), " acum:", len(acum))

# B2 Diferența
noi = acum - baza
print(len(noi), "SUID noi fata de sistemul curat")
for c in sorted(noi):
    print(" ", c)

# B3 Dicționar de risc și filtrul
risc = {nume(c): ("mare" if nume(c) in GTFO else "normal") for c in noi}
periculoase = [c for c in sorted(noi) if nume(c) in GTFO]
print("periculoase NOI:", periculoase)