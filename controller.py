import view
import process
import log

def button_click():
    mode = view.inp_mod()

    if mode.lower() == 'импорт':
        surname = view.inp_import()
        res_search = process.search(surname)

        if isinstance(res_search, str):
            view.view_import_no()
        else:
            view.view_import(res_search)

        log.log_cash(mode, res_search)

    elif mode.lower() == "экспорт":
        result = view.inp_export()
        process.export(result)
        log.log_cash(mode, result[1:])

