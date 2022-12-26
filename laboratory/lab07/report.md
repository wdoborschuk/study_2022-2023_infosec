---
## Front matter
title: "Лабораторная работа №7"
subtitle: "Дискретное логарифмирование в конечном поле"
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

**Цель** --- Изучить алгоритмы для задач дискретного логарифмирования.  

**Задачи:**

- Реализовать алгоритм для задач дискретного логарифмирования через p-метод Полларда

# Теоретическая информация

Все теоретическое описание дано в описании лабораторной работы.

# Выполнение лабораторной работы

При выполнении лабораторной работы мы строго следовали алгоритмике, представленной в описании.

## Реалиазация и тестирование

Программный код выглядит следующим образом:

```python
# Laboratory Work
# Theme: Discrete logarthmification
# Author: Vladimir Doborschuk

# --- Modules ---

import numpy as np

# --- Functions ---

# --- mod(a, b) ---

def mod(a ,b):
	return a % b

# --- find mod order ---

def order(a, p):
    x = 1
    while mod(a**x - 1, p) != 0:
        x += 1
        
    return x

# --- Pollard's P-method for Log ---

'''
a - основание
b - значение остатка
p - простое число
'''
def po_method(a: int, b: int, p: int):
    print(f"\n{a}^(x) = {b} mod {p}")
    print("-----------------------------------------------------------------")
    print('|\tc\t|\tlog c\t|\td\t|\tlog d\t|')
    print("-----------------------------------------------------------------")
    
    u = np.random.randint(4)
    v = np.random.randint(4)
    r = order(a, p)
    
    c = mod(np.power(a, u) * np.power(b, v), p)
    d = c
    
    u_c, u_d = u, u
    v_c, v_d = v, v
    
    print(f'|\t{c}\t|\t{u_c}+{v_c}x\t|\t{d}\t|\t{u_d}+{v_d}x\t|')
    
    def f(x, u_x, v_x):
        if x < r:
            return mod(a*x, p), u_x + 1, v_x
        else:
            return mod(b*x, p), u_x, v_x + 1            

    c, u_c, v_c = f(c, u_c, v_c)
    tmp_d = f(d, u_d, v_d)
    d, u_d, v_d = f(tmp_d[0], tmp_d[1], tmp_d[2])
    
    while mod(c, p) != mod(d, p):
        print(f'|\t{c}\t|\t{u_c}+{v_c}x\t|\t{d}\t|\t{u_d}+{v_d}x\t|')
        c, u_c, v_c = f(c, u_c, v_c)
        tmp_d = f(d, u_d, v_d)
        d, u_d, v_d = f(tmp_d[0], tmp_d[1], tmp_d[2])
        
    print(f'|\t{c}\t|\t{u_c}+{v_c}x\t|\t{d}\t|\t{u_d}+{v_d}x\t|')
    print("-----------------------------------------------------------------")
    
    x = 1
    # print(v_c - v_d, u_d - u_c)
    while mod((v_c - v_d)*x, r) != mod(u_d - u_c, r):
        x += 1
        
    print(f"x = {x}")
    print(f"\n{a}^({x}) = {b} mod {p}")
    print("-----------------------------------------------------------------")
    return x

# --- Main ---

def main():
    po_method(10, 64, 107)
    po_method(2, 1, 15)
    
    
if __name__ == "__main__":
    main()
```

При запуске получаем следующие результаты:

```sh
10^(x) = 64 mod 107
-----------------------------------------------------------------
|       c       |       log c   |       d       |       log d   |
-----------------------------------------------------------------
|       101     |       0+3x    |       101     |       0+3x    |
|       44      |       0+4x    |       12      |       1+4x    |
|       12      |       1+4x    |       23      |       3+4x    |
|       13      |       2+4x    |       53      |       5+4x    |
|       23      |       3+4x    |       92      |       5+6x    |
|       16      |       4+4x    |       30      |       6+7x    |
|       53      |       5+4x    |       47      |       7+8x    |
|       75      |       5+5x    |       99      |       9+8x    |
|       92      |       5+6x    |       16      |       10+9x   |
|       3       |       5+7x    |       75      |       11+10x  |
|       30      |       6+7x    |       3       |       11+12x  |
|       86      |       7+7x    |       86      |       13+12x  |
-----------------------------------------------------------------
x = 20

10^(20) = 64 mod 107
-----------------------------------------------------------------

2^(x) = 1 mod 15
-----------------------------------------------------------------
|       c       |       log c   |       d       |       log d   |
-----------------------------------------------------------------
|       1       |       0+2x    |       1       |       0+2x    |
|       2       |       1+2x    |       4       |       2+2x    |
|       4       |       2+2x    |       4       |       2+4x    |
-----------------------------------------------------------------
x = 2

2^(2) = 1 mod 15
-----------------------------------------------------------------
```

# Выводы

В рамках выполненной лабораторной работы мы изучили и реализовали p-метод Полларда для задач дискретного логарифмирования.

# Список литературы{.unnumbered}

::: {#refs}
:::
