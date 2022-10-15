---
## Front matter
title: "Лабораторная работа №3"
subtitle: "Шифрование гаммированием"
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
monofont: PT Mono
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
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{fvextra}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
---

# Цель работы

Цель данной работы --- изучить методы шифрования гаммированием.

# Задание

Заданием является:

- Реализовать алгоритм шифрования гаммированием конечной гаммы.

# Теоретическое введение

Из всех схем шифрования простейшей и наиболее надежной является схема однократного использования. Формируется $m$-разрядная случайная двоичная последовательность - ключ шифра. Отправитель производит побитовое сложение по модулю два ($mod$ 2) ключа

$$
k = k_1 k_2 \dots k_i \dots k_m
$$

и $m$-разрядной двоичной последовательности

$$
p = p_1 p_2 \dots p_i \dots p_m
$$

соответствующей посылаемому сообщению

$$
c_i = p_i \oplus k_i, i = \overline{1,m} 
$$

*Гаммирование* - процедура наложения при помощи некоторой функции $F$ на исходный текст *гаммы* шифра, т.е. *псевдослучайной последователыюсти (ПСП)* с выходов генератора $\mathbb{G}$ [@сокол2019шифрование]. Псевдослучайная последовательность по своим статистическим свойствам неотличима от случайной последовательности, но является детерминированной, т.е. известен алгоритм ее формирования. Чаще Обычно в качестве функции $F$ берется операция поразрядного сложения по модулю два или по модулю $N$ ($N$ - число букв алфавита открытого текста).

Простейший генератор псевдослучайной последовательности можно представить рекуррентным соотношением: 

$$
\gamma_i = a\cdot\gamma_{i-1} + b\:\mathnormal{mod(m)}, i = \overline{1,m}
$$

где $y_i$ - $i$-й член последовательности псевдослучайных чисело, $a,y_0,b$ - ключевые параметры.

При использовании генератора ПСП получаем бесконечную гамму. Однако, возможен режим шифрования конечной гаммы. В роли конечной гаммы может выступать фраза. Как и ранее, используется алфавитный порядок букв.

**Замечание**

В примере, данном в описании лабораторной работы, допущена ошибка - берется алфавит без буквы "**ё**", т.е. алфавит длины 32, хотя указан алфавит длины 33.

# Выполнение лабораторной работы

Для реализации шифров мы будем использовать Python, так как его синтаксис позволяет быстро реализовать необходимые нам алгоритмы.

## Модули и вспомогательные фукнции

Дополнительно мы используем библиотеку `numpy` и импортируем её.

```python
import numpy as np
```

Также, реализовали функцию получения английского и русского алфавита.

```python
# Cyrillic or Latin alphabet getter
def get_alphabet(option="eng"):
    if option == "eng":
        return list(map(chr, range(ord("a"), ord("z")+1)))
    elif option == "rus":
        return list(map(chr, range(ord("а"), ord("я")+1)))

```

## Реализация шифрования гаммированием

Шифрование гаммированием реализуем в виде функции `gamma_encryption` следующего вида:

```python
  # Gamma Encryption
  def gamma_encryption(message: str, gamma: str):
      alphabet = get_alphabet()
      if message.lower() not in alphabet:
          alphabet = get_alphabet("rus")
      
      print(alphabet)
      m = len(alphabet)

      def encrypt(letters_pair: tuple):
          idx = (letters_pair[0] + 1) + (letters_pair[1] + 1) % m
          if idx > m:
              idx = idx - m

          return idx - 1
          
      message_cleared = list(filter(lambda s: s.lower() in alphabet, message))
      gamma_cleared = list(filter(lambda s: s.lower() in alphabet, gamma))
      
      message_indices = list(map(lambda s: alphabet.index(s.lower()), message_cleared))
      gamma_indices = list(map(lambda s: alphabet.index(s.lower()), gamma_cleared))
      
      for i in range(len(message_indices) - len(gamma_indices)):
          gamma_indices.append(gamma_indices[i])

      print(f'{message.upper()} -> {message_indices}\n{gamma.upper()} -> {gamma_indices}')

      encrypted_indices = list(map(lambda s: encrypt(s), zip(message_indices, gamma_indices)))
      print(f"ENCRYPTED FORM: {encrypted_indices}\n")
      
      return ''.join(list(map(lambda s: alphabet[s], encrypted_indices))).upper()
```

На вход она принимает переменные `message` (передаваемое сообщение), `gamma` (гамма-ключ).

В ходе обработке мы работаем с индексами элементов массива-строки, предварительно проверяя, является ли первый элемент сообщения частью передаваемого алфавита.

Далее, мы очищаем сообщений от символов, не входящих в алфавит, что дает нам возможность сделать соответствие индексов гаммы-ключа и самого сообщения.

В результате, каждый из символов проходит процедуру шифрованию, и мы получаем зашифрованное сообщение по определенной гамме. 

## Тестирование

Для тестирования мы создали следующую функцию, которую вызываем в блоке *Main*:

```python
# --- Tests ---
def test_encryption(message: str, gamma: str):
    print(f'ENCRYPTION RESULT: {gamma_encryption(message, gamma)}')
```

Данные тесты возвращают строку шифро-текста в качестве результата.

Для их вызова, реализуем функцию `main` следующим образом:

```python
# --- Main function ---
def main():
    message = "приказ"
    gamma = "гамма"

    print("TEST 1\n")
    test_encryption(message, gamma)

    message = "Шла Саша по шоссе и сосала сушку"
    gamma = "Котопес"

    print("TEST 2\n")
    test_encryption(message, gamma)
```

## Результаты тестирования

Запустив наш программный код, получим результат, изображенный на рисунке [-@fig:001].

![Вывод программы с реализованным шифром гаммирования конечной гаммы](image/python_output.png){ #fig:001 width=100% }

Явно получим вот такой результат:

```sh
TEST 1

['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
ПРИКАЗ -> [15, 16, 8, 10, 0, 7]
ГАММА -> [3, 0, 12, 12, 0, 3]
ENCRYPTED FORM: [19, 17, 21, 23, 1, 11]

ENCRYPTION RESULT: УСХЧБЛ

TEST 2

['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
ШЛА САША ПО ШОССЕ И СОСАЛА СУШКУ -> [24, 11, 0, 17, 0, 24, 0, 15, 14, 24, 14, 17, 17, 5, 8, 17, 14, 17, 0, 11, 0, 17, 19, 24, 10, 19]
КОТОПЕС -> [10, 14, 18, 14, 15, 5, 17, 10, 14, 18, 14, 15, 5, 17, 10, 14, 18, 14, 15, 5, 17, 10, 14, 18, 14, 15]
ENCRYPTED FORM: [3, 26, 19, 0, 16, 30, 18, 26, 29, 11, 29, 1, 23, 23, 19, 0, 1, 0, 16, 17, 18, 28, 2, 11, 25, 3]
```

Сравнивая результат шифрования с примером из описания лабораторной работы, можем убедиться, что наша реализация корректна.

# Выводы

В рамках выполненной лабораторной работы мы изучили и реализовали алгоритм шифрования гаммированием конечной гаммы.

# Список литературы{.unnumbered}

::: {#refs}
:::
