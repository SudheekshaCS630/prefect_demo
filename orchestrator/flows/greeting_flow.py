from prefect import flow, task

@task
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@task
def print_message(message: str):
    print(message)

@flow(name="hello-world-flow")
def hello_flow():
    greeting = say_hello("Sudheeksha")
    print_message(greeting)

if __name__ == "__main__":
    hello_flow()
