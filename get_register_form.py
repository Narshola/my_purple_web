def get_form(form_list):
    elem_dict = {}
    for elem in form_list:
        key = elem[0]
        value = elem[1][0]
        if len(value) == 0:
            return None
        elem_dict[key] = value
    return elem_dict

#[('fname', ['Test']), ('lname', ['Botyara']), ('age', ['87']), ('town', ['Nowt']), ('login', ['bot']), ('password', ['1']), ('password_commit', ['1']), ('img', ['https'])]