from locust import TaskSet, task, between

from protocol import DubboLocust


class TestUser(DubboLocust):
    # host = "192.168.20.4"
    host = "192.168.10.29"
    port = 23882
    # port = 23888
    # min_wait = 2000
    # max_wait = 2000
    wait_time = between(0, 5)

    class task_set(TaskSet):

        @task
        def send_data1(self):
            response = self.client.invoke('com.biz.soa.service.product.frontend.ProductService',
                                          'getProductCustomFacesByProductId',
                                          346840940184473616,
                                          # 468866659321397248
                                          )
            print(response)


if __name__ == '__main__':
    user = TestUser()
    user.run()  # msg = 'invoke com.biz.soa.service.promotion.backend.game.getCurrentConfig()'
