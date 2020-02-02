　　带浏览器的：
　　　　locust -f locust_test.py -—host=‘http://localhost:5000/board/daily_fail_list’ -c 1000 -r 10 -n 1000
　　不带浏览器的：
　　　　locust -f start_locust.py ——host=‘http://localhost:5000/board/daily_fail_list’ —no-web -c 1000 -r 10 -n 1000
　　参数意义：
　　　　--no-web是用来选择无浏览器模式，
　　　　-c后面接的是模拟用户数，
　　　　-r后面接的每秒模拟用户并发数，
　　　　-n后面接的是模拟请求数