import requests
from requests.exceptions import ConnectionError

from main.structure.DataModels import Dataset
from main.tooling.Logger import logging_setup

logger = logging_setup(__name__)


BASE_URL = "https://feed-uvl.ifi.uni-heidelberg.de"

DATASET_POST_ENDPOINT = f"{BASE_URL}/hitec/repository/concepts/store/dataset/"


# DATASET_POST_ENDPOINT = "http://localhost:9684/hitec/repository/concepts/store/dataset/"


class ForeignComponentSpellcheckerRestConnectoRequester():
    """
        Description: REST calls to foreign services.
    """

    def __init__(self) -> None:
        pass

    def storeDatasetRequest(self, dataset: Dataset) -> int:
        """
            Description:
                This method sends a POST request to the uvl-storage-concepts service to store a dataset.
            Args:
                Dataset: The dataset, which has to be stored
            Returns:
                int: The status of the POST request
        """

        logger.info(f"-------Store new generated Dataset with the Name: {dataset['name']}-------")

        try:
            response = requests.post(DATASET_POST_ENDPOINT, json=dataset)
        except ConnectionError as e:
            print(f"ConnectionError: Failed to connect to the uvl-storage-concepts service: {e}")

        return response.status_code
