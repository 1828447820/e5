import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("倒计时结束！")

# 设置倒计时时间（以秒为单位）
seconds = 10

countdown(seconds)
