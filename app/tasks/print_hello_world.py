from app.tasks.task import Task

print_hello_world = lambda : print('Running task')

task = Task(1).minutes.do(print_hello_world)