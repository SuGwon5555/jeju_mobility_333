from flask import Flask, render_template, request, redirect, url_for, session

app=Flask(__name__) #플라스크 이름 app으로 설정
app.secret_key = 'your-secret-key'

todos = {}

@app.route('/')
def index():
    user_todos = todos.get(session['username'],[]) #username을 받아야함 #session은 메모리의 한 종류
    return render_template('todos.html',
                           username=session['username'],
                           todos=user_todos)

@app.route('/login', methods=['GET', 'POST']) 

def login():
    # 로그인 페이지 표시
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index')) #redirect는 길을 지시해주는 것
    
    return render_template('login.html')

@app.route('/add', methods=['POST']) #todo 추가
def add_todo():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    new_todo = request.form['todo']
    if new_todo: #form 내의 input data를 어딘가로 보내줌
        if session['username'] not in todos: #todo 안에 uesrname이 겹쳤는지 확인인
            todos[session['username']]=[]
        todos[session['username']].append(new_todo) #append는 list에 넣어 놓는것것

    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)