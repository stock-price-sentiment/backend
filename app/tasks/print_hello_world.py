from app.tasks.task import Task
from app.tasks.forbes_scraper import forbes_scraper

print_hello_world = lambda : print('Running task')

search = 'Facebook'
fb = forbes_scraper(search)



task = Task(1).minutes.do(print_hello_world)
task = Task(1).minutes.do(fb)
