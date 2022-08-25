
import numpy as np

def random_predict(number:int=1)-> int:
    """Функция угадывает число не более, чем за 20 попыток
    
     Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # устанавливаем счетчик
    min = 1 # устанавливаем минимальное значение интервала чисел для загадывания
    max = 101 # устанавливаем максимальное значение интервала чисел для загадывания
    
    predict_number = np.random.randint(1, 101) # загадываем число
    
    # запускаем цикл
    while True:
        count += 1
        if predict_number > number: # если загаданное число больше предполагаемого,
                                    # максимальное значение интервала меняется и
                                    # сужается диапазон поиска
           max = predict_number
           predict_number = round((max + min) / 2)
        elif predict_number < number: # аналогично, за исключением замены минимального значения
           min = predict_number
           predict_number = round((max + min) / 2)
        elif number == predict_number:
            break # выход из цикла при угадывании
    
    return count


def score_game(random_predict) -> int:
    """Фнукция определяет количество попыток на 1000 подходов

    Args:
        random_predict (_type_): Загаданное число

    Returns:
        int: Количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадываем число
    
    for number in random_array:
        count_ls.append(int(random_predict(number)))
    
    score = int(np.mean(count_ls)) # вычисление среднего количества попыток
    
    return score

print(f'количество попыток: {random_predict(10)}')