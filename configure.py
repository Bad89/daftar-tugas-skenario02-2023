from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Belajar Python',
        'description': 'Belajar pemrograman Python dasar.',
        'done': False
    },
    {
        'id': 2,
        'title': 'Beli bahan makanan',
        'description': 'Beli sayuran dan daging di pasar.',
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run()
