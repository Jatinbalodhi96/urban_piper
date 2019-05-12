from celery import Celery
import time

app = Celery('tasks', broker='amqp://qtknohgh:yPqam1az0l5hKN0Kz73jc5VLpxST9Rej@shark.rmq.cloudamqp.com/qtknohgh', 
            backend='db+sqlite:///db.sqlite3')

@app.task
def reverse(self, string):
    time.sleep(20)
    return string
