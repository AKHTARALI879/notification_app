import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERT...pledge",
            message="""100 days of code in python
            Thanks for visiting & watching
            don't forget to like and subscribe
            follow for more""",
            timeout=10
        )
        time.sleep(1800)
