---
## Front matter
lang: ru-RU
title: Лабораторная работа №8
subtitle: Целочисленная арифметика многократной точности
author:
  - Доборщук В.В.
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 24 декабря 2022

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
figureTitle: "Рис."
tableTitle: "Таблица"
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
 - \usepackage{fvextra}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
---

# Информация

## Докладчик

:::::::::::::: {.columns align=center}
::: {.column width="70%"}

  * Доборщук Владимир Владимирович
  * студент группы НФИмд-02-22, студ. билет 1132223451
  * учебный ассистент кафедры прикладной информатики и теории вероятностей
  * Российский университет дружбы народов
  * [doborshchuk-vv@rudn.ru](mailto:doborshchuk-vv@rudn.ru)

:::
::: {.column width="30%"}

![](./image/doborschuk.jpeg)

:::
::::::::::::::

# Цели и задачи

**Цель** --- Изучить алгоритмы целочисленной арифметики многократной точности.  

**Задачи:**

- Реализовать представленные алгоритмы

# Выполнение лабораторной работы

\scriptsize
```python
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

```

## Выполнение лабораторной работы

\scriptsize
```python
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
```

## Выполнение лабораторной работы

\scriptsize
```python
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
```

## Результаты тестирования

\scriptsize

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