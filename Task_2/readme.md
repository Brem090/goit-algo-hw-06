# Порівняння алгоритмів пошуку в соціальній мережі

У цьому аналізі порівнюються два алгоритми пошуку в графі на прикладі соціальної мережі "Online Forever":

- Пошук в глибину (DFS)
- Пошук у ширину (BFS)

___

## Граф соціальної мережі

Розглядається **неорієнтований граф** з 9 вершинами та 16 ребрами:

- Вершини - користувачі мережі 
- Ребра - наявність зв'язку між користувачами (друзі, колеги, взаємодія в мережі)

Початкова вершина - користувач 1.

___

## Результати пошуку

DFS: 1, 2, 4, 3, 6, 7, 5, 8, 9

BFS: 1, 2, 3, 4, 5, 6, 7, 8, 9

___

## Пояснення результатів

**DFS** спочатку рухається "вглиб" по мережі друзів обраного користувача.
**BFS** спочатку охоплює "в ширину" - спочатку друзів користувача, потім їхніх друзів і т.д.
Тому DFS може піти далеко в одну гілку зв'язків, в той час як BFS дає уявлення про ближнє оточення користувача.

___

## Висновок

В соціальній мережі **BFS краще підходить** для аналізу кола зв'язків та оточення заданого користувача.
**DFS** корисний для знаходження окремих "ланцюжків друзів" та гілок мережі.