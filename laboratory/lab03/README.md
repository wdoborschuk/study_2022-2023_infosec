# Цель работы

Изучить методы шифрования гаммированием.

**Задачи:**

- Реализовать алгоритм шифрования гаммированием конечной гаммы.

# Теоретическая информация

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

*Гаммирование* - процедура наложения при помощи некоторой функции $F$ на исходный текст *гаммы* шифра, т.е. *псевдослучайной последователыюсти (ПСП)* с выходов генератора $\mathbb{G}$. Псевдослучайная последовательность по своим статистическим свойствам неотличима от случайной последовательности, но является детерминированной, т.е. известен алгоритм ее формирования. Чаще Обычно в качестве функции $F$ берется операция поразрядного сложения по модулю два или по модулю $N$ ($N$ - число букв алфавита открытого текста).

Простейший генератор псевдослучайной последовательности можно представить рекуррентным соотношением: 

$$
\gamma_i = a\cdot\gamma_{i-1} + b\:\mathnormal{mod(m)}, i = \overline{1,m}
$$

где $y_i$ - $i$-й член последовательности псевдослучайных чисело, $a,y_0,b$ - ключевые параметры.

При использовании генератора ПСП получаем бесконечную гамму. Однако, возможен режим шифрования конечной гаммы. В роли конечной гаммы может выступать фраза. Как и ранее, используется алфавитный порядок букв.

> ## Замечание
> В примере, данном в описании лабораторной работы, допущена ошибка - берется алфавит без буквы "**ё**", т.е. алфавит длины 32, хотя указан алфавит длины 33.