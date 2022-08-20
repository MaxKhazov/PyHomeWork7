from dis import dis
from controller import name_view
from controller import surname_view
from controller import number_view
from controller import discription_view

def create():
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '      <p {}>Surname: {} </p>\n'\
        .format(style, surname_view())
    html += '      <p {}>Name: {} </p>\n'\
        .format(style, name_view())
    html += '      <p {}>Number: {} </p>\n'\
        .format(style, number_view())
    html += '      <p {}>Discription: {} </p>\n'\
        .format(style, discription_view())
    html += '  </body>\n</html>'

    with open('index.html', 'a') as page:
        page.write(html)

    return html