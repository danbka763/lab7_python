# lab7_python

## Седьмая лабораторная работа по python (ООП)

## Задание

"Домино". Двум игрокам раздаются по 7 косей домино. Игроки поочерёдно делают ход. Компьютер контролирует правильность ходов игроков. В качестве одного из игроков можно взять "компьютер". Игра заканчивается, если у одного из игроков закончились кости или у всех игроков нет подходящих вариантов.

## Реализация

1. В начале игрока встречает меню, в котором он может начать игру и выйти из приложения.
2. Если игрок выбирает "Начать игру" - вызывается класс variation, в котором иннициализируются все возможные комбинации домино. 
3. При "раздаче" домино игроку и компьютеру - обращаемся к variation, вытаскиваем оттуда один из вариантов из комбинации и этот вариант удаляется из массива variation.
4. Каждый ход игрока или компьютера проверяется на правильность, в случае с компьютером реализован самый простой вариант, он выбирает "первую попавшуюся" домино из его коллекции.
5. Игра заканчивается, в случае, если у кого-то закончились домино "на руках", или если у бота не осталось вариантов хода. Игрок может в любой момент сдаться. 
6. Завершается игра сопроводительным сообщением для игрока о том, выграл он или проиграл.
