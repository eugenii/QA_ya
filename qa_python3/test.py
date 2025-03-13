from time import sleep

from online_sales_register import OnlineSalesRegisterCollector


if __name__ == '__main__':
    check = OnlineSalesRegisterCollector()
    print(check.name_items)
    for punkt in ('', 'кола', 'печенье',
                'qwertyuioqwertyuiol;asdfghjklxcvbnm,exidfghjkl',
                'xbgc', 'чипсы', 'молоко', 'кефир'):
        check.add_item_to_cheque(punkt)
    print(check.name_items)
    print(check.number_items)
    check.delete_item_from_check('чапсы')
    check.delete_item_from_check('чипсы')
    print(check.number_items, check.name_items)
    print(check.check_amount())
    print(check.twenty_percent_tax_calculation())
    print(check.ten_percent_tax_calculation())
    print(check.total_tax())

    for tel in (123456, 1.22, 1234567890):
        print(check.get_telephone_number(tel))
        print(OnlineSalesRegisterCollector.get_telephone_number(tel))

    print(check.get_date_and_time())
    sleep(70)
    print(check.get_date_and_time())