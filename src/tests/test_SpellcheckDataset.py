import json
from typing import cast

import pytest  # noqa: F401

from main.structure.DataModels import Dataset
from main.structure.SpellcheckedDatasetCreator import SpellcheckedDatasetCreator

filename = './src/tests/komoot_reviews_1.json'
with open(filename) as f:
    json_data = json.load(f)


def test_DatasetSpeller() -> None:
    originalDataset = cast(Dataset, json_data['dataset'])
    spellcheckedDataset = SpellcheckedDatasetCreator(originalDataset).createSpellcheckedDataset()
    # test, if the originalDataset has the sentence with wrong spelled words in the first index
    assert (originalDataset['documents'][0]['text'] == 'Verry useful app for planning tripps.')
    # test, if the spellcheckedDataset has the sentence with wrong spelled words in the first index, but
    # in a spellchecked version
    assert (spellcheckedDataset['documents'][0]['text'] == 'Very useful app for planning trips.')
    # test, if originalDataset and spellcheckedDataset have the same number of docs
    assert len(originalDataset['documents']) == len(spellcheckedDataset['documents'])
    # test, if originalDataset and spellcheckedDataset are different in the second index
    # (in originalDataset is the word "behaviour" and in spellcheckedDataset is "behavior")
    assert (originalDataset['documents'][1]['text'] != spellcheckedDataset['documents'][1]['text'])  # behaviour -> behavior
    # test, if originalDataset and spellcheckedDataset are equal, since in document 3 is no spelling mistake
    assert (originalDataset['documents'][2]['text'] == spellcheckedDataset['documents'][2]['text'])

    print(spellcheckedDataset)
