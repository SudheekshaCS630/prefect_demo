from prefect import flow

@flow
def Hello_flow():
    print("Hello, world!")


if __name__ == "__main__":
    Hello_flow()