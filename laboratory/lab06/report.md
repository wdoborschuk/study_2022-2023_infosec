---
## Front matter
title: "Лабораторная работа №6"
subtitle: "Разложение чисел на множители"
author: "Доборщук Владимир Владимирович, НФИмд-02-22"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: /home/wdoborschuk/work/2022-2023/МОЗИиИБ/infosec/.report/pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
lol: true # List of listings
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: Fira Code Retina
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
code-block-font-size: \scriptsize
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{fvextra}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
---

# Цель и задачи работы

**Цель** --- Изучить алгоритмы разложения чисел на множители.  

**Задачи:**

- Реализовать алгоритм нахождения нетривиального сомножителя p-методом Полларда

# Теоретическая информация

Все теоретическое описание дано в описании лабораторной работы.

# Выполнение лабораторной работы

Для реализации p-метода Полларда было внесено изменение в функцию $f(x)$ - в ней у нас также выбирается случайное число от $1$ до $\sqrt{n}$ и берется по модулю $n$.

## Реалиазация и тестирование

Программный код выглядит следующим образом:

```python
# Laboratory Work
# Theme: Distribution of numbers into factors
# Author: Vladimir Doborschuk

# --- Modules ---

import numpy as np

# --- Functions ---

# --- mod(a, b) ---

def mod(a ,b):
	return a % b

# --- Pollard's P-method ---

'''
n - целое число
c - начальное значение
f - сжимающая функция
'''
def pollard(n: int, c: int, f):
    d = 1
    cnt = 0
    a, b = c, c
    
    print(f"a = {a}, b = {b}")
    
    while d == 1:
        a = mod(f(a), n)
        b = mod(f(b), n)
        d = np.gcd(a - b, n)
        
        if mod(cnt, 100) == 0 or d != 1:
            print(f"iteration {cnt+1}: a = {a}, b = {b}, d = {d}")

        cnt += 1
        
    if d == n:
        print("Делитель не найден")
        return None
    
    return d

# --- Test ---

def pollard_test(n, c):
    print(f'Поллард {n}\n---------')
    f = lambda x: np.power(x, 2) + mod(np.random.randint(1, np.floor(np.sqrt(n))), n)
    p = pollard(n, c, f)
    
    if p != None:
        print(f'Нетривиальный делитель {n}: p = {p}')
        
    print(f'---------\n')

# --- Main ---

def main():
    pollard_test(1359331, 1)
    pollard_test(137, 5)
    pollard_test(322, 12)
    
if __name__ == "__main__":
    main()
```

При запуске получаем следующие результаты:

```sh
Поллард 1359331
---------
a = 1, b = 1
iteration 1: a = 281, b = 953, d = 1
iteration 101: a = 666221, b = 55317, d = 1
iteration 201: a = 1114705, b = 242518, d = 1
iteration 250: a = 1251131, b = 205946, d = 1181
Нетривиальный делитель 1359331: p = 1181
---------

Поллард 137
---------
a = 5, b = 5
iteration 1: a = 32, b = 34, d = 1
iteration 26: a = 40, b = 40, d = 137
Делитель не найден
---------

Поллард 322
---------
a = 12, b = 12
iteration 1: a = 155, b = 146, d = 1
iteration 2: a = 200, b = 78, d = 2
Нетривиальный делитель 322: p = 2
---------
```

# Выводы

В рамках выполненной лабораторной работы мы изучили и реализовали p-метод Полларда для разложения на нетривиальные сомножители.

# Список литературы{.unnumbered}

::: {#refs}
:::
