import user_interface as ui
import txt_creator as tc
import publisher as pu

a = int(input('нажмите 1 для добавления в справочник,\nнажмите 2 для просмотра справочника:\n'))


if a == 1:
    tc.name_create(ui.name_view())
    tc.first_name_create(ui.first_name_view())
    tc.number_phone_create(ui.number_phone_view())
    tc.description_create(ui.description_view())
elif a == 2:
    b = int(input('Выберите формат вывода 1 - 2:\n'))
    if b == 1:
        pu.show_v1()
    elif b == 2:
        pu.show_v2()
    else:
        print('!!Неверное значение!!')
else:
    print('!!Неверное значение!!')

