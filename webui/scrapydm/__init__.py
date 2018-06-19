from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()


def check_project():
    print("====")
    

def init():
    job = scheduler.add_job(check_project, 'interval', seconds=30)

    scheduler.start()