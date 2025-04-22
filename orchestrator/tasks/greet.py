from prefect import task
from prefect import get_run_logger
from prefect.artifacts import create_markdown_artifact

@task
def say_hello(name: str) -> str:
    print("say_hello() invoked")
    logger = get_run_logger()
    logger.info("say_hello() invoked")

    greeting = f"Hello {name}...!"
    
    create_markdown_artifact(
        key="greeting-markdown",
        markdown=greeting
    )
    
    return greeting