from locust import HttpLocust, TaskSet, task


# def index(l):
#     l.client.get("/")
#
# def stats(l):
#     l.client.get("/stats/requests")


class UserTasks(TaskSet):
    # 列出需要测试的任务形式一
    # tasks = [index, stats]
    # 列出需要测试的任务形式二
    @task
    def dubbo_test(self):
        pass


class WebsiteUser(HttpLocust):
    host = "http://127.0.0.1:8089"
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks
