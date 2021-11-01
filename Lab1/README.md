# Lab. nr 1 - "Powtórka operacji na tablicach i macierzach"

Zadaniem labolatorium było rozwiązanie następujących zadań z użyciem odpowiednich funkcji pakietu NumPy.
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_1.png?raw=true)

## Realizacja zadań
1. Utwórz tablicę zawierającą 10 zer
```python
tenZeros = np.zeros(10)
print('1. Tablica zer -', tenZeros)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_2.png?raw=true)

2. Utwórz tablicę zawierającą 10 piątek
```python
tenFives = np.full(10, 5)
print('2. Tablica piatek -', tenFives)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_3.png?raw=true)

3. Utwórz tablicę zawierającą liczby od 10 do 50
```python
arrangeTheRange = np.arange(10, 51)
print('3. Tablica zawierająca liczby od 10 do 50 -', arrangeTheRange)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_4.png?raw=true)

4. Utwórz macierz (tablica wielowymiarowa) o wymiarach 3x3 zawierającą liczby od 0 do 8
```python
reshaped = np.arange(0, 9, 1).reshape(3, 3)
print('4. Macierz (tablica wielowymiarowa) o wymiarach 3x3 zawierająca liczby od 0 do 8 - \n', reshaped)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_5.png?raw=true)

5. Utwórz macierz jednostkową o wymiarach 3x3,
```python
identity = np.eye(3)
print('5. Macierz jednostkowa o wymiarach 3x3 - \n', identity)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_6.png?raw=true)

6. Utwórz macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej (Gaussa),
```python
gauss = np.random.normal(size=(5,5))
print('6. Macierz o wymiarach 5x5 zawierająca liczby z dystrybucji normalnej (Gaussa) - \n', gauss)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_7.png?raw=true)

7. Utwórz macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01
```python
tensMat = np.linspace(0.01, 1, 100)
print('7. Macierz o wymiarach 10x10 zawierająca liczby od 0,01 do 1 z krokiem 0,01 - \n', tensMat)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_8.png?raw=true)

8. Utwórz tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1)
```python
twentyMat = np.linspace(0, 1, 20)
print('8. Tablica zawierająca 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1) - \n', twentyMat)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_9.png?raw=true)

9. Utwórz tablicę zawierającą losowe liczby z przedziału (1, 25), następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami:
```python
ran = np.random.randint(1, 25, size = (5,5))
print('9. Tablica zawierająca losowe liczby z przedziału (1, 25), następnie zamieniona na macierz o wymiarach 5 x 5 z tymi samymi liczbami: \n', ran)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_10.png?raw=true)

-- oblicz sumę wszystkich liczb w ww. macierzy,
```python
suma = ran.sum()
print('-> 9a. Sumę wszystkich liczb w ww. macierzy - \n', suma)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_11.png?raw=true)

-- oblicz średnią wszystkich liczb w ww. macierzy,
```python
avg = ran.mean()
print('-> 9b. Średnia wszystkich liczb w ww. macierzy - \n', avg)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_12.png?raw=true)

-- oblicz standardową dewiację dla liczb w ww. macierzy,
```python
dv = np.std(ran)
print('-> 9c. Standardową dewiacja dla liczb w ww. macierzy - \n', dv)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_13.png?raw=true)

-- oblicz sumę każdej kolumny ww. macierzy i zapisz ją do tablicy.
```python
sumsum = np.sum(ran, axis = 0)
print('-> 9d. Suma każdej kolumny ww. macierzy, zapisana do tablicy - \n', sumsum)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_14.png?raw=true)

10. Utwórz macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) oraz:
```python
fivemat = np.random.randint(100, size = (5, 5))
print('10. Macierz o wymiarach 5x5 zawierająca losowe liczby z przedziału (0, 100)  - \n', fivemat)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_15.png?raw=true)

-- oblicz medianę tych liczb,
```python
med = np.median(fivemat)
print('-> 10a. Mediana tych liczb - \n', med)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_16.png?raw=true)

-- znajdź najmniejszą liczbę tej macierzy,
```python
minF = np.min(fivemat)
print('-> 10b. Najmniejsza liczba tej macierzy - \n', minF)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_17.png?raw=true)

-- znajdź największą liczbę tej macierzy.
```python
maxF = np.max(fivemat)
print('-> 10c. Największa liczba tej macierzy - \n', maxF)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_18.png?raw=true)

11. Utwórz macierz o wymiarach różnych od siebie i większych od 1, zawierającą losowe liczby z przedziału (0, 100) i dokonaj jej transpozycji
```python
rann = np.random.randint(0, 100, size = (3, 5))
rant = rann.transpose()
print('11. Macierz o wymiarach różnych od siebie i większych od 1, zawierająca losowe liczby z przedziału (0, 100): \n', rann, '\n\n po transpozycji: \n', rant)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_19.png?raw=true)

12. Utwórz dwie macierze o odpowiednich wymiarach, większych od 2x2 i dodaj je do siebie
```python
mat1 = np.random.randint(0, 100, size = (4, 6))
mat2 = np.random.randint(0, 100, size = (4, 6))
print('12. Dwie macierze o odpowiednich wymiarach, większych od 2x2:\n', mat1, '\n oraz \n', mat2, '\n\n po dodaniu do siebie: \n', mat1 + mat2)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_20.png?raw=true)

13. Utwórz dwie macierze o odpowiednich wymiarach różnych od siebie i większych od 2, a następnie pomnóż je przez siebie za pomocą dwóch różnych funkcji (np. ‘matmul’ i ‘multiply’, proszę poczytać o różnicach w obliczaniu wyników mnożenia).
```python
mat3 = np.random.randint(0, 100, size = (5, 6))
mat4 = np.random.randint(0, 100, size = (6, 5))
matmuled = np.matmul(mat3, mat4)
dotted = np.dot(mat3, mat4)
multiplied = np.multiply(mat3, mat4.reshape(5, 6))
print('13. Dwie macierze o odpowiednich wymiarach różnych od siebie i większych od 2, następnie pomnożone przez siebie za pomocą dwóch różnych funkcji. \n')
print('a) matmul: \n', matmuled)
print('b) dot: \n', dotted)
print('c) multiply: \n', multiplied)
```
![](https://github.com/jagodalewandowska/wstep-do-ml-lewandowska/blob/main/Lab1/screenshots/Screenshot_21.png?raw=true)