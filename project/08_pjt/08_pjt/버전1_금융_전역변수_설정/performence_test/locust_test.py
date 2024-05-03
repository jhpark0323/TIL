from locust import HttpUser, task, between

class Test(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    @task
    def loucst(self):
        self.client.get("test/loucst/")