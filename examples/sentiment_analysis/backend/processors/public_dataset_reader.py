import csv
import time
from typing import Dict, Any, Generator

from genai_processors import processor

@processor(
    name="sentiment_analysis.public_dataset_reader",
    description="Reads data from a public dataset and yields it as a stream.",
    input_type=str,
    output_type=Dict[str, Any],
)
def public_dataset_reader(file_path: str, interval: float = 1.0) -> Generator[Dict[str, Any], None, None]:
    """
    Reads data from a public dataset and yields it as a stream.

    Args:
        file_path: The path to the dataset file.
        interval: The interval at which to yield data points, in seconds.
    """
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
            time.sleep(interval)
