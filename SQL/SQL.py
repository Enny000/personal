import sqlite3

class TODO:
    def __init__(self):
        self.connect = sqlite3.connect("Todo.db")
        self.cursor = self.connect.cursor()
        self.create_task_table()

    def create_task_table(self): 
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks ( 
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL, 
        priority INTEGER NOT NULL );
    ''') 

    def add_task(self, name , priority):  
        self.cursor.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.connect.commit()
        
    def find_task(self, taskname):
        self.cursor.execute('''
            SELECT * FROM tasks WHERE name = ?;                    
                           ''', (taskname,))
        
        return self.cursor.fetchone()

    def show_tasks(self):
        self.cursor.execute('''
            SELECT * FROM tasks ;                    
                           ''')
        
        result = self.cursor.fetchall()

        for row in result:
            print(row)

    def change_priority(self, change_priority, id ):
        self.cursor.execute('''
        UPDATE tasks SET priority = ? WHERE id = ?
                            ''', (change_priority, id))
        self.connect.commit()

    def delete_task(self, id):
        self.cursor.execute('''
        DELETE FROM tasks WHERE id = ?
                            ''', (id,))
        self.connect.commit()

todo = TODO()

todo.change_priority(100, 2)
todo.show_tasks()

todo.delete_task(1)
todo.show_tasks()

# print(todo.find_task("test"))
# todo.show_tasks()
# todo.add_task("test", 2)
# todo.add_task("token", 4)
# print(todo.find_task("test"))
# todo.show_tasks()