#atur nilai
s1 = 6
s2 = 6
s3 = 6
Tinggi_prisma = 9 
tinggi = 9
luas_alas = 9
#rumus
luas_segitiga = (s1 + s2 + s3)*Tinggi_prisma
luas_prisma = (s1 + s2 + s3)*(Tinggi_prisma)+(luas_alas)+(tinggi)
volume = 1/2 * luas_alas * tinggi * Tinggi_prisma
#output
print("hasil luas:", luas_segitiga)
print("hasil luas:", luas_prisma)
print("hasil volume:", volume)