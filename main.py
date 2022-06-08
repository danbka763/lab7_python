import random
from itertools import *


class Board:
    def __init__(self):
        self.board = []

    def get_items(self):
        return self.board

    def get_variant(self):
        lenght = len(self.board)
        return [self.board[0][0], self.board[lenght-1][1]]

    def first(self, item):
        self.board.append(item)

    def next(self, item, variant):
        if variant[0] == item[1]:
            self.board.insert(0, item)
        elif variant[0] == item[0]:
            item_reverse = [item[1], item[0]]
            self.board.insert(0, item_reverse)
        elif variant[1] == item[0]:
            self.board.append(item)
        else:
            item_reverse = [item[1], item[0]]
            self.board.append(item_reverse)

    def get_len(self):
        return len(self.board)


class Collection:
    def __init__(self, variation):
        self.collection = []

        for i in range(7):
            rand = random.randint(0, variation.get_len() - 1)
            self.collection.append(variation.get(rand))

    def get_domino(self, index):
        domino = self.collection[index]
        self.collection.pop(index)
        return domino

        return domino

    def get_collection(self):
        return self.collection

    def get(self, index):
        return self.collection[index]


class Variation:
    def __init__(self):
        self.variation = []

        for i in product('0123456', repeat=2):
            self.variation.append([int(i[0]), int(i[1])])

    def get(self, index):
        variation = self.variation[index]
        self.variation.pop(index)

        return variation

    def get_len(self):
        return len(self.variation)


def search_repeat(coll, num):
    for i in range(len(coll)):
        if num == coll[i][0] and num == coll[i][1]:
            return True


def step_player(coll_player, not_first, variant) -> int:
    if not_first:
        while True:
            index = get_input("индекс домино, которой хотите походить. Сдаться [0]")

            if 1 <= index <= 7:
                if (coll_player[index - 1][0] == variant[0]
                        or coll_player[index - 1][0] == variant[1]
                        or coll_player[index - 1][1] == variant[0]
                        or coll_player[index - 1][1] == variant[1]):
                    return index - 1

            if index == 0:
                return -1
            print("введены некоректные значения или требуется выбрать другую карту")

    index = get_input("индекс домино, которой хотите походить")

    if index > 7 or index < 1 or coll_player[index - 1][0] == 0 and coll_player[index - 1][1] == 0:
        while True:
            print("введены некоректные значения или требуется выбрать другую карту")
            index = get_input("индекс домино, которой хотите походить")

            if 1 <= index <= 7:
                if not coll_player[index - 1][0] == 0 and not coll_player[index - 1][1] == 0:
                    return index - 1

    return index - 1


def step_computer(coll_comp, not_first, variant) -> int:

    for i in range(len(coll_comp) - 1):
        if not_first:
            if (coll_comp[i][0] == variant[0]
                    or coll_comp[i][0] == variant[1]
                    or coll_comp[i][1] == variant[0]
                    or coll_comp[i][1] == variant[1]):
                return i
        elif not coll_comp[i][0] == 0 and not coll_comp[i][1] == 0:
            return i

    return -1


def visible_board(board_collection):
    print("Фигуры на столе: ", end="")
    for item in range(len(board_collection)):
        print(board_collection[item], end=" ")
    print()


def start():
    variation = Variation()
    collection = Collection(variation)
    collection_computer = Collection(variation)
    board = Board()

    player_first = True

    while True:
        coll_comp = collection_computer.get_collection()
        coll_player = collection.get_collection()

        print("\nВаша коллекция", end=": ")
        for i in range(len(coll_player)):
            print(f"{i + 1}.", coll_player[i], end=" ")
        print("")

        if board.get_len() == 0:
            if ((search_repeat(coll_comp, 0)
                 or search_repeat(coll_comp, 6))
                    and not search_repeat(coll_player, 0)):
                player_first = False

            if player_first:
                step = collection.get_domino(step_player(coll_player, False, []))
                board.first(step)

                variant = board.get_variant()
                step = step_computer(coll_comp, True, variant)
                if exit_game(step, "Вы выиграли!"):
                    return
                data = collection_computer.get_domino(step)
                board.next(data, variant)
            else:
                step = collection_computer.get_domino(step_computer(coll_comp, False, []))
                board.first(step)

                board_collection = board.get_items()
                visible_board(board_collection)

                variant = board.get_variant()
                step = step_player(coll_player, True, variant)
                if exit_game(step, "Вы проиграли!"):
                    return
                data = collection.get_domino(step)
                board.next(data, variant)

            continue

        board_collection = board.get_items()

        if player_first:
            visible_board(board_collection)

            variant = board.get_variant()
            player_step = step_player(coll_player, True, variant)
            if exit_game(player_step, "Вы проиграли!"):
                return
            data = collection.get_domino(player_step)
            board.next(data, variant)

            variant = board.get_variant()
            comp_step = step_computer(coll_comp, True, variant)
            if exit_game(comp_step, "Вы выиграли!"):
                return
            data = collection_computer.get_domino(comp_step)
            board.next(data, variant)
        else:
            variant = board.get_variant()
            comp_step = step_computer(coll_comp, True, variant)
            if exit_game(comp_step, "Вы выиграли!"):
                return
            data = collection_computer.get_domino(comp_step)
            board.next(data, variant)

            board_collection = board.get_items()
            visible_board(board_collection)

            variant = board.get_variant()
            player_step = step_player(coll_player, True, variant)
            if exit_game(player_step, "Вы проиграли!"):
                return
            data = collection.get_domino(player_step)
            board.next(data, variant)


def exit_game(step, message):
    if (step == -1):
        print(message)
        return True

    return False


def get_input(param) -> int:
    while True:
        print(f"Введите {param}:", end=" ")
        try:
            return int(input())
        except ValueError as exc:
            print(f"Введеная строка не является целым числом. Попробуйте заново.\nПодробнее: {exc}")


def menu():
    print("\n\n")
    print("1. Начать игру")
    print("0. Выйти\n")


def main():
    while True:
        menu()
        variant = get_input("номер действия")

        if variant == 0:
            return
        elif variant == 1:
            start()
        else:
            print("Попробуем ещё-раз...\n")


if __name__ == '__main__':
    main()
