from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# لیست وظایف
tasks = []

# صفحه اصلی
@app.route('/')
def home():
    return render_template('tasks.html', tasks=tasks)

# ایجاد وظیفه
@app.route('/tasks', methods=['POST'])
def create_task():
    title = request.form.get('title')
    if title:
        new_task = {
            'id': len(tasks) + 1,
            'title': title,
            'completed': False
        }
        tasks.append(new_task)
    return redirect(url_for('home'))

# ویرایش وظیفه
@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return "Task not found", 404

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['completed'] = 'completed' in request.form
        return redirect(url_for('home'))

    return render_template('edit_task.html', task=task)

# حذف وظیفه
@app.route('/tasks/<int:task_id>/delete', methods=['GET'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
