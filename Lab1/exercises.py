# %%

import numpy as np

# %%
tenZeros = np.zeros(10)
print('1. Tablica zer -', tenZeros)

# %%
tenFives = np.full(10, 5)
print('2. Tablica piatek -', tenFives)

# %%
arrangeTheRange = np.arange(10, 51)
print('3. Tablica zawierająca liczby od 10 do 50 -', arrangeTheRange)

# %%
reshaped = np.arange(0, 9, 1).reshape(3, 3)
print('4. Macierz (tablica wielowymiarowa) o wymiarach 3x3 zawierająca liczby od 0 do 8 - \n', reshaped)

# %%
identity = np.eye(3)
print('5. Macierz jednostkowa o wymiarach 3x3 - \n', identity)

# %%
gauss = np.random.normal(size=(5,5))
print('6. Macierz o wymiarach 5x5 zawierająca liczby z dystrybucji normalnej (Gaussa) - \n', gauss)

# %%
tensMat = np.linspace(0.01, 1, 100)
print('7. Macierz o wymiarach 10x10 zawierająca liczby od 0,01 do 1 z krokiem 0,01 - \n', tensMat)

# %%
twentyMat = np.linspace(0, 1, 20)
print('8. Tablica zawierająca 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1) - \n', twentyMat)

# %%
ran = np.random.randint(1, 25, size = (5,5))
print('9. Tablica zawierająca losowe liczby z przedziału (1, 25), następnie zamieniona na macierz o wymiarach 5 x 5 z tymi samymi liczbami: \n', ran)

# %%
suma = ran.sum()
print('-> 9a. Sumę wszystkich liczb w ww. macierzy - \n', suma)

# %%
avg = ran.mean()
print('-> 9b. Średnia wszystkich liczb w ww. macierzy - \n', avg)

# %%
dv = np.std(ran)
print('-> 9c. Standardową dewiacja dla liczb w ww. macierzy - \n', dv)

# %%
sumsum = np.sum(ran, axis = 0)
print('-> 9d. Suma każdej kolumny ww. macierzy, zapisana do tablicy - \n', sumsum)

# %%
fivemat = np.random.randint(100, size = (5, 5))
print('10. Macierz o wymiarach 5x5 zawierająca losowe liczby z przedziału (0, 100)  - \n', fivemat)

# %%
med = np.median(fivemat)
print('-> 10a. Mediana tych liczb - \n', med)

# %%
minF = np.min(fivemat)
print('-> 10b. Najmniejsza liczba tej macierzy - \n', minF)

# %%
maxF = np.max(fivemat)
print('-> 10c. Największa liczba tej macierzy - \n', maxF)

# %%
rann = np.random.randint(0, 100, size = (3, 5))
rant = rann.transpose()
print('11. Macierz o wymiarach różnych od siebie i większych od 1, zawierająca losowe liczby z przedziału (0, 100): \n', rann, '\n\n po transpozycji: \n', rant)

# %%
mat1 = np.random.randint(0, 100, size = (4, 6))
mat2 = np.random.randint(0, 100, size = (4, 6))
print('12. Dwie macierze o odpowiednich wymiarach, większych od 2x2:\n', mat1, '\n oraz \n', mat2, '\n\n po dodaniu do siebie: \n', mat1 + mat2)

# %%
mat3 = np.random.randint(0, 100, size = (5, 6))
mat4 = np.random.randint(0, 100, size = (6, 5))
matmuled = np.matmul(mat3, mat4)
dotted = np.dot(mat3, mat4)
multiplied = np.multiply(mat3, mat4.reshape(5, 6))
print('13. Dwie macierze o odpowiednich wymiarach różnych od siebie i większych od 2, następnie pomnożone przez siebie za pomocą dwóch różnych funkcji. \n')
print('a) matmul: \n', matmuled)
print('b) dot: \n', dotted)
print('c) multiply: \n', multiplied)




