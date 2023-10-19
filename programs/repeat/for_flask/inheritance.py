from jinja2 import Environment, FileSystemLoader


subs = ["Физ-ра", "Математика", "Физика", "Информатика"]

file_loader = FileSystemLoader('programs/repeat/for_flask/templates')
env = Environment(loader=file_loader)

tm = env.get_template('about_us.html')
output = tm.render(my_list=subs)

print(output)