from mongoengine import connect

from luckycat import luckycat_global_config
from luckycat.database.models.Job import Job


def main():
    connect(luckycat_global_config.db_name, host=luckycat_global_config.db_host)
    print("Connected to mongodbengine")
    for job in Job.objects:
        print(f"job id={job.id}, job name = {job.name}")

if __name__ == "__main__":
    main()