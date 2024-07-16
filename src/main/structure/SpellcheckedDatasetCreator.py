from copy import deepcopy

import language_tool_python

from main.structure.DataModels import Dataset
from main.tooling.Logger import logging_setup

logger = logging_setup(__name__)


class SpellcheckedDatasetCreator():
    """
        Description: The class for creating a spellchecked dataset.
    """

    def __init__(self, originalDataset: Dataset):
        self.spellcheckedDataset = deepcopy(originalDataset)

    def createSpellcheckedDataset(self) -> Dataset:
        """
            Description:
                This method performs a spellcheck on an original dataset and generates a new,
                spelling corrected dataset.
            Args:
                None: Uses the dataset class variable
            Returns:
                Dataset: The new spellchecked dataset
        """

        logger.info(f"-------Start spellchecking original dataset: {self.spellcheckedDataset['name']}-------")

        # use context manager to explicitly control when the server is started and stopped:
        # with language_tool_python.LanguageToolPublicAPI('en-US') as tool: # remote_server='https://languagetool.org/api/'
        with language_tool_python.LanguageTool('en-US') as tool:  # local_server

            for index, value in enumerate(self.spellcheckedDataset["documents"]):
                self.spellcheckedDataset["documents"][index]["text"] = tool.correct(value["text"])

        logger.info("-------Finished spellchecking!-------")

        return self.spellcheckedDataset
