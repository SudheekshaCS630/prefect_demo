import json
from prefect import flow
from prefect import get_run_logger
from pathlib import Path
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from orchestrator.tasks import greet

def load_config(config_path: str) -> dict:
    print("load_config() invoked!!")
    config_file = Path.cwd() / config_path
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
        print(f"Loaded config: {config}")  # Debugging output
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at {config_file}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in config file {config_file}")


@flow
def hello_flow(config_path):
    logger = get_run_logger()
    try:
        logger.info("Starting flow execution")
        
        config = load_config(config_path)
        
        if not isinstance(config, dict):
            raise ValueError("Config is not a dictionary!")
            
        result = greet.say_hello(config["name"])
        logger.info(f"Task result: {result}")
        return result
    except Exception as e:
        logger.error(f"Flow failed: {str(e)}")
        raise

if __name__ == "__main__":
    hello_flow()
