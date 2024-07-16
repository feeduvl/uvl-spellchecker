from datetime import datetime
from typing import Dict, cast

from main.connector.ForeignComponentSpellcheckerRestConnectoRequester import ForeignComponentSpellcheckerRestConnectoRequester
from main.structure.DataModels import Dataset
from main.structure.SpellcheckedDatasetCreator import SpellcheckedDatasetCreator
from main.tooling.Logger import logging_setup

logger = logging_setup(__name__)


class Spellchecker():
    """
        Description: This is the behavior class, that uses the classes in the structure package to delegate the program.
    """

    def __init__(self) -> None:
        self.foreignComponentRequester = ForeignComponentSpellcheckerRestConnectoRequester()

    def startSpellchecking(self, content: Dict[str, str]) -> str:
        """
            Description:
                This method delegates the spellchecking.
            Args:
                Dict[str, str]: The selected configuration from the user (comes from the ri-visualization service)
            Returns:
                str: A message outlining, that the spellchecked dataset has been created
        """

        logger.info("-------Spellchecker requested-------")

        originalDataset = cast(Dataset, content["dataset"])

        spellcheckedDataset = SpellcheckedDatasetCreator(originalDataset).createSpellcheckedDataset()

        spellcheckedDataset["uploaded_at"] = datetime.now().astimezone().isoformat()
        spellcheckedDataset["name"] = content['params']['new_dataset_name']  # type: ignore[index]

        self.foreignComponentRequester.storeDatasetRequest(spellcheckedDataset)

        return "New spellchecked dataset successfully created!"
