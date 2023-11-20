from handler import handler
import shutil
import datetime

if __name__ == "__main__":
    today = datetime.date.today()
    i = 10
    while 10 <= i <= 360:
        archive_date = (today - datetime.timedelta(i)).strftime("%m-%d-%Y")
        dir_path = f"data/{archive_date}"
        try:
            shutil.rmtree(dir_path)
        except FileNotFoundError:
            pass
        i += 1

    handler_results = handler(True)
