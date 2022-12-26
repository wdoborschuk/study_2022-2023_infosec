---
## Front matter
title: "Лабораторная работа №8"
subtitle: "Целочисленная арифметика многократной точности"
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

**Цель** --- Изучить алгоритмы целочисленной арифметики многократной точности.  

**Задачи:**

- Реализовать представленные алгоритмы

# Теоретическая информация

Все теоретическое описание дано в описании лабораторной работы.

# Выполнение лабораторной работы

При выполнении лабораторной работы мы строго следовали алгоритмике, представленной в описании.

## Реалиазация и тестирование

Программный код выглядит следующим образом:

```python
# Laboratory Work
# Theme: Arithmetic for big numbers
# Author: Vladimir Doborschuk

# --- Functions ---

def mod(a ,b):
	return a % b

def big_sum(u, v, b):
    u_ = str(u)
    v_ = str(v)
    
    j = len(u_) - 1
    
    if j != len(v_) - 1:
        print("bad N")
        return None
    
    k = 0
    
    w = ""
    
    while j >= 0:
        w_ = mod(int(u_[j]) + int(v_[j]) + k, b)
        w += str(w_)
        k = (int(u_[j]) + int(v_[j]) + k) // b
        j = j - 1
    
    w += str(k)
    return int(w[::-1])

def big_differ(u, v, b):
    u_ = str(u)
    v_ = str(v)
    
    j = len(u_) - 1
    
    if j != len(v_) - 1:
        print("bad N")
        return None
    
    k = 0
    
    w = ""
    
    while j >= 0:
        w_ = mod(int(u_[j]) - int(v_[j]) + k, b)
        w += str(w_)
        k = (int(u_[j]) - int(v_[j]) + k) // b
        j = j - 1

    return int(w[::-1])

def big_multiple(u, v, b):
    u_ = str(u)
    v_ = str(v)
    
    j = len(v_) - 1
    w = [0] * (j * len(u_))
    
    while j >= 0:
        if v_[j] == 0:
            w[j] = 0
            j = j - 1
        else:
            i = len(u_) - 1
            k = 0
            while i >= 0:
                t = int(u_[i]) * int(v_[j]) + w[i+j] + k
                w[i+j] = mod(t, b)
                k = t // b
                i = i - 1
            w[j] = k
            j = j - 1

    return int("".join(list(map(str, w))))

# --- Main ---

def main():
    x = 874
    y = 775
    
    print(f"Sum: {x} + {y} (10)")
    print(big_sum(x, y, 10))
    
    print(f"Differ: {x} - {y} (10)")
    print(big_differ(x, y, 10))
    
    print(f"Multiplication: {x} * {y} (10)")
    print(big_multiple(x, y, 10))
    
if __name__ == "__main__":
    main()
```

При запуске получаем следующие результаты:

```sh
Sum: 874 + 775 (10)
1649
Differ: 874 - 775 (10)
99
Multiplication: 874 * 775 (10)
684500
```

# Выводы

В рамках выполненной лабораторной работы мы изучили и реализовали представленные алгоритмы целочисленной арифметики многократной точности.

# Список литературы{.unnumbered}

::: {#refs}
:::
