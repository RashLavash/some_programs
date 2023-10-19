from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('programs/repeat/for_flask/templates')
envir = Environment(loader=file_loader)

tm = envir.get_template('content.html')
message = tm.render(title='Моя страница')

print(message)