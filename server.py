import time
import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def my_home():
    # return 'Hello, Earth!, Yellow What! if thats the earth, where the heck am I?'
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/about.html')
# def aboutme():
#     return render_template('about.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/work.html')
# def work():
#     return render_template('works.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

def save_to_file(data):
    with open('datab2.txt', 'a') as dbase:
        email = data['email']
        subject = data['subject']
        message = data['message']
        time = data['time']
        file = dbase.write(f'\n {email},{subject},{message},{time}')


def save_to_csv(data):
    with open('database.csv', 'a') as dbase2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        time = data['time']
        csv_writer = csv.writer(
            dbase2, delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message, time])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        current_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())
        data['time'] = current_time
        save_to_csv(data)

        # def append_dict_to_file(file_path, data):
        #     """ Appends a dictionary to a file.

        #         Args:
        #         file_path (str): The path to the file.
        #         new_dict (dict): The dictionary to append.

        #     """

        # file_path = 'datab.txt'
        # try:
        #     with open(file_path, 'r+') as file:
        #         try:
        #             existing_data = json.load(file)
        #             if isinstance(existing_data, list):
        #                 existing_data.append(data)
        #             else:
        #                 existing_data = [existing_data, data]
        #         except json.JSONDecodeError:
        #             existing_data = [data]
        #         file.seek(0)
        #         json.dump(existing_data, file, indent=0)
        #         file.truncate()

        # except FileNotFoundError:
        #     with open(file_path, 'w') as file:
        #         json.dump([data], file,  indent=4)

        # new_data = data
        # append_dict_to_file(file_path, new_data)

        return redirect('/thanks.html')
    else:
        return 'something went wrong'
