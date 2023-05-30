from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dummy data for tasks
tasks = [
    {"id": 1, "title": "python env", "description": "mata kuliah pembuka"},
    {"id": 2, "title": "dummy data", "description": "data dummy show"},
    {"id": 3, "title": "pemograman", "description": "dasar dasar algorith"}
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json['title'],
        "description": request.json['description']
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task[0])


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({"error": "Task not found"}), 404
    task[0]['title'] = request.json['title']
    task[0]['description'] = request.json['description']
    return jsonify(task[0])


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({"error": "Task not found"}), 404
    tasks.remove(task[0])
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)

