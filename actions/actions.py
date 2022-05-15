#actions
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionFirma(Action):
    def name(self) -> Text:
        return "puntos_necesarios"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        firma_actual = tracker.get_slot("puntos_firma")
        msg = f"Tenes que hacer 18 para pasar con tu firma de {firma_actual}. Buena suerte!"
        dispatcher.utter_message(text=msg)

        return []