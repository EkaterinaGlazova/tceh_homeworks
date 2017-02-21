# Задача: реализовать веб-сервер на Flask, который бы реализовывал следующую функциональность.
# Требования:


from flask import Flask, request, jsonify, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms import ValidationError
import locale

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': 'blabla',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})

# По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']

@app.route('/locales')
def locales():
    return jsonify('ru', 'en', 'it')

# По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму

@app.route('/sum/<int:first>/<int:second>')
def flask_sum(first, second):
    return str(first + second)

# По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'

@app.route('/greet/<user_name>')
def name(user_name):
    return 'Hello, %s'% user_name


# По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля.
# #Необходимо валидировать email, что обязательно присутствует, валидировать пароли,
# #что они минимум 6 символов в длину и совпадают. Возрващать пользователю json вида: "status" - 0 или 1
# #(если ошибка валидации), "errors" - список ошибок, если они есть, или пустой список.

def password_validation(form, field):
    print(form, field)
    if form.data['password'] not in field.data:
        raise ValidationError('Passwords are different')


class UserForm(FlaskForm):
    email = StringField(validators=[
        validators.Email()
    ])
    password =StringField(validators=[
        validators.length(min = 6, max = 20)
    ])
    password_valid = StringField(validators=[
        password_validation
    ])

@app.route('/form/user', methods=['GET, POST'])
def post_form():
    print(request.method)
    print(request.form)
    print(request.args)

    if request.method == 'POST':
        user_form = UserForm(request.form)
        if user_form.validate():
            return '0', ()
        else:
            return '1 %s'%user_form.errors
    return 'Ok!'


# По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
# Файлы можно туда положить любые текстовые. А если такого нет - 404

@app.route('/serve/<path:filename>')
def files(filename):
    try:
        content = open('./files' + filename, 'r')
        return content.read()
    except:
        return '404'


if __name__ == '__main__':
    app.run()
