"""Utils for creating and loading dialogue datasets."""

import logging
import json
import os
import re

from data_manager import DataManager
    
    class MultiWozDataManager(DataManager):
    """Data manager for MultiWOZ data."""

    def __init__(self):
        super().__init__()
        self.abbr_slots = {}
        self.dont_care = set()
        self.correction_map = {}

    def NormalizeText(self, text):

        return text


    def LoadRawData(self):
        """Load raw data from local data directory."""
        raw_data = LoadFile(self.data_dir+"data.json")
        test_ids = set(LoadFile(self.data_dir+"testListFile.txt"))

        return raw_data, test_ids


    def Correct(self, intent, slot, value):
        """Correct intent, slot, value tuple.

        Args:
            intent: <str> intent name.
            slot: <str> slot name.
            value: <str> slot value.
        Returns:
            intent: <str> corrected intent name.
            slot: <str> corrected slot name.
            value: <str> corrected slot value.
        """
        intent, slot, value = intent.lower(), slot.lower(), value.lower()
        # Never use an abbreviated slot name.
        if slot in self.abbr_slots:
            slot = self.abbr_slots[slot]
        # Ignore the undefined slots.
        if slot not in self.ontology[intent]:
            return intent, None, None
        # Convert values to certain tokens in the vocab.
        if value == "?":
            return intent, slot, "ASK"
        if value in self.dont_care:
            return intent, slot, "DNC"
        if (intent in self.correction_map) and (
                slot in self.correction_map[intent]):
            for before, after in self.correction_map[intent][slot].items():
                if re.search(before, value):
                    value = after
        if (self.ontology[intent][slot]["is_picklist"]) and (
                value not in self.ontology[intent][slot]["values"]):
            value = None

        return intent, slot, value


    def GetUpdates(self, turn):
        """Get gold update from a single turn."""
        updates = {}
        if "dialog_act" in turn:
            for intent_act, slot_value_pairs in turn["dialog_act"].items():
                intent, act = intent_act.lower().split("-")
                if act not in updates:
                    updates[act] = {}
                if intent == "general":
                    continue
                updates[act][intent] = {}
                for [slot, value] in slot_value_pairs:
                    intent, slot, value = self.Correct(intent, slot, value)
                    if slot and value:
                        updates[act][intent][slot] = {"value": value}
        if "span_info" in turn and len(turn["span_info"]) == 5:
            for intent_act, slot, value, start, end in turn["span_info"]:
                intent, act = intent_act.lower().split("-")
                intent, slot, value = self.Correct(intent, slot, value)
                if (act in updates) and (intent in updates[act]) and (
                  slot in updates[act][intent]):
                    updates[act][intent][slot]["span"] = [start, end]

        return updates


    def CreateData(self, save_data=True):
        """Create training and test data."""
        train_data = []
        test_data = []

        raw_data, test_ids = self.LoadRawData()
        
        for data_id, metadata in raw_data.items():
            history = []
            for i in range(len(metadata["log"])):
                raw_turn = metadata["log"][i]
                # user
                if i%2 == 0:
                    turn = {"id": data_id, "turn": i//2}
                    turn["query"] = self.NormalizeText(raw_turn["text"])
                    turn["update"] = self.GetUpdates(raw_turn)
                    turn["history"] = history[:]
                # system
                else:
                    turn["response"] = self.NormalizeText(raw_turn["text"])
                    if data_id in test_ids:
                        test_data.append(turn)
                    else:
                        train_data.append(turn)
                history.append(raw_turn["text"])

        if save_data:
            with open(self.data_dir+"train_data.json", "w") as f:
                f.write(json.dumps(train_data))
            with open(self.data_dir+"test_data.json", "w") as f:
                f.write(json.dumps(test_data))

        return train_data, test_data


    def LoadData(self):
        """Load training and test data."""
        if os.path.exist(self.data_dir+"train_data.json"):
            with open(self.data_dir+"train_data.json") as f:
                train_data = json.load(f)
            with open(self.data_dir+"test_data.json") as f:
                test_data = json.load(f)
        else:
            train_data, test_data = self.CreateData()

        return train_data, test_data


class MultiWoz21DataManager(MultiWozDataManager):
    """Creates training and test data from raw Multiwoz 2.1 data."""

    def __init__(self):
        super().__init__()
        self.data_dir = "/Users/yingdali/data/dialogue/multiwoz_2_1/"
        self.ontology = LoadFile(self.data_dir+"ontology.json")
        self.abbr_slots = {
            "addr": "address",
            "post": "postcode",
            "dest": "destination"
        }
        self.dont_care = {"do nt care", "do n't care"}
        self.correction_map = {
            "hotel": {
                "type": {
                    "hotel": "hotel",
                    "guest": "guest"
                },
                "starts": {
                    "two": "2",
                    "three": "3",
                    "four": 4
                }, 
                "price": {
                    "moderate": "moderate"
                },
                "parking": {
                    "free": "yes",
                    "n$": "no"
                },
                "internet": {
                    "free": "yes",
                    "^y$": "yes"
                },
                "day": {
                    "monda": "monday",
                    "friday": "friday"
                },
                "area": {
                    "east": "east",
                    "north": "north",
                    "we": "west"
                }
            },
            "train": {
                "day": {
                    "fr": "friday",
                    "we": "wednesday"
                }
            },
            "restaurant": {
                "area": {
                    "cent": "centre",
                    "south": "south"
                },
                "price": {
                    "ch": "cheap"
                },
                "day": {
                    "w": "wednesday"
                }
            },
            "attraction": {
                "area": {
                    "ce": "centre",
                    "we": "west"
                },
                "type": {
                    "archit": "architecture",
                    "coll": "college",
                    "concert": "concerthall",
                    "fun": "entertainment",
                    "galleria": "museum",
                    "gastropub": "nightclub",
                    "sport": "multiple sports",
                    "swimming": "swimming pool",
                    "pool": "swimming pool",
                    "night": "nightclub",
                    "mus": "museum"
                }
            }
        }


    def NormalizeText(self, text):
        text = text.lower()
        text = re.sub(r"[\*\n<>\xa0\\]", "", text)
        text = re.sub(r"#", "number", text)
        text = re.sub(r"&", "and", text)
        text = re.sub(r"@", "at", text)
        text = re.sub(r"[`]", "'", text)
        text = re.sub(r"wi-fi", "wifi", text)
        text = re.sub(r"-star", "star", text)
        text = re.sub(r"-", "'", text)
        text = re.sub(r"(?<=[0-9])(;)(?=[0-9])", ":", text)
        text = re.sub(r"(;)(?=[smlt])", "'", text)
        text = re.sub(r";", ",", text)
        text = re.sub(r"(\")(?=[md])", "'", text)
        text = re.sub(r"\"", "", text)
        text = re.sub(r"\(.*\)", "", text)
        text = re.sub(r":[\)\(]", "", text)
        text = re.sub(r"\)", "", text)
        text = re.sub(r"/$|/(?=\s)", "", text)
        text = re.sub(r"w/", "with", text)
        text = re.sub(r"20/15", "20:15", text)
        text = re.sub(r'[" "]+', " ", text)

        return text