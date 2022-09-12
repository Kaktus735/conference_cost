def print_full_price(ticket_count):
    price_all = 0
    for i in range(1, ticket_count + 1):
        print('Билет №', i)
        attempt_count = 3
        while True:
            age_for_ticket_str = input('Укажите свой возраст\n')
            age_for_ticket, is_error = convert_to_number(age_for_ticket_str)
            if is_error:
                print('Попробуйте ввести значение снова. Осталось попыток -', attempt_count)
                attempt_count -= 1
                if attempt_count > 0:
                    continue
                else:
                    return
            break
        if age_for_ticket < 18:
            print('Билет бесплатный')
        elif age_for_ticket <= 25:
            price_all += 990
            print('Стоимость билета: 990 руб.')
        else:
            price_all += 1390
            print('Стоимость билета: 1390 руб.')
    if ticket_count > 3:
        price_all -= ((price_all / 100) * 10)
        if price_all.is_integer():
            price_all = int(price_all)
        print('Сумма к оплате', price_all, 'руб. с учетом 10%-ой скидки')
    else:
        print('Сумма к оплате', price_all, 'руб.')


def convert_to_number(number):
    is_error = False
    converted_number = 0
    try:
        converted_number = int(number)
        if converted_number <= 0:
            print('Необходимо ввести положительное число, не равное 0')
            is_error = True
    except Exception as e:
        print('Введеное значение не является целым числом')
        is_error = True
    return converted_number, is_error


if __name__ == '__main__':
    ticket_count_str = input('Введите количество билетов, которое хотите приобрести\n')
    ticket_count, is_error = convert_to_number(ticket_count_str)
    if not is_error:
        print_full_price(ticket_count)