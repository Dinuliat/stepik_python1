n = int(input())
    # Имена всех команд
names = set()

    # Имя команды -> Количество игр команды
total = dict()
    # Имя команды -> Количество побед команды
win = dict()
    # Имя команды -> Количество ничьих команды
draw = dict()
    # Имя команды -> Количество проигрышей команды
lose = dict()
    # Имя команды -> Количество очков команды
score = dict()

for i in range(n):
    line = input()
    values = line.split(';')

    first_name = values[0]
    first_score = int(values[1])
    second_name = values[2]
    second_score = int(values[3])

    names.add(first_name)
    names.add(second_name)

        # Считаем количество игр
    if first_name not in total:
        total[first_name] = 1
    else:
        total[first_name] = total[first_name] + 1

    if second_name not in total:
        total[second_name] = 1
    else:
        total[second_name] = total[second_name] + 1

        # Считаем количество побед
    if first_score > second_score:
            # Увеличиваем число побед для 1 команды
        if first_name not in win:
            win[first_name] = 1
        else:
            win[first_name] = win[first_name] + 1

            # Увеличиваем число проигрышей для 2 команды
        if second_name not in lose:
            lose[second_name] = 1
        else:
            lose[second_name] = lose[second_name] + 1

            # Увеличиваем число очков для 1 команды
        if first_name not in score:
            score[first_name] = 3
        else:
            score[first_name] = score[first_name] + 3
    elif second_score > first_score:
            # Увеличиваем число побед для 2 команды
        if second_name not in win:
            win[second_name] = 1
        else:
            win[second_name] = win[second_name] + 1

            # Увеличиваем число проигрышей для 1 команды
        if first_name not in lose:
            lose[first_name] = 1
        else:
            lose[first_name] = lose[first_name] + 1

            # Увеличиваем число очков для 2 команды
        if second_name not in score:
            score[second_name] = 3
        else:
            score[second_name] = score[second_name] + 3
    elif first_score == second_score:
            # Увеличиваем число ничьих для 1 команды
        if first_name not in draw:
            draw[first_name] = 1
        else:
            draw[first_name] = draw[first_name] + 1

            # Увеличиваем число ничьих для 2 команды
        if second_name not in draw:
            draw[second_name] = 1
        else:
            draw[second_name] = draw[second_name] + 1

            # Увеличиваем число очков для 1 команды
        if first_name not in score:
            score[first_name] = 1
        else:
            score[first_name] = score[first_name] + 1

            # Увеличиваем число очков для 2 команды
        if second_name not in score:
            score[second_name] = 1
        else:
            score[second_name] = score[second_name] + 1

for name in names:
    print(
        f"{name}:{total.get(name, 0)} {win.get(name, 0)} {draw.get(name, 0)} {lose.get(name, 0)} {score.get(name, 0)}")