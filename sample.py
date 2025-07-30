import os
from celery import Celery


project_id = "cto-tinaa-pltf-svc-lab-159cfb"


topic_name = "celery-tasks"
subscription_name = "celery-taskssub"


print(f"Using project: {project_id}")
print(f"Using topic: {topic_name}")
print(f"Using subscription: {subscription_name}")


app = Celery('tasks')
app.conf.update(
   
    broker_url=f'gcpubsub://projects/{project_id}',
    broker_transport_options={
        'project': project_id,
        'topic_name': topic_name,
        'subscription_name': subscription_name,
        
        'create_topic': True, 
        'create_subscription': True, 
    },
    result_backend=None,  
    task_serializer='json',
    accept_content=['json'],
   
    worker_enable_remote_control=False,
    worker_concurrency=1,
)

@app.task
def add(x, y):
    """A simple task that adds two numbers."""
    result = x + y
    print(f"Task executed: {x} + {y} = {result}")
    return result

@app.task
def hello(name):
    """A simple task that prints a greeting."""
    message = f"Hello, {name}!"
    print(message)
    return message

if __name__ == '__main__':
    app.start()

