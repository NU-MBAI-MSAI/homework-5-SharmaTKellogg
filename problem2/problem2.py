def date_format(date_form):
    mon = date_form.split('/')
    month = mon[0]
    date = mon[1]
    year = mon[2]
    new_date = year + '-' + month + '-' + date
    return new_date
