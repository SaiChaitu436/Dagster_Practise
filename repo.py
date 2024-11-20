from dagster import job, op

@op
def hello_op():
    print("Hello, Dagster!")

@job
def hello_job():
    hello_op()

if __name__ == "__main__":
    hello_job.execute_in_process()