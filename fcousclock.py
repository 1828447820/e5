import time

def start_focus_timer(duration):
    print("专注计时开始！")
    time.sleep(duration)
    print("专注计时结束！")

if __name__ == "__main__":
    focus_duration = 25 * 60  # 专注时长（以秒为单位）
    start_focus_timer(focus_duration)
