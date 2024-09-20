def format_name(f_name, l_name):
    """
    :param f_name: take a first name
    :param l_name: take a second name
    :return: formatted name + last name
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



