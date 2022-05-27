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

        firma_actual = int(tracker.get_slot("puntos_firma"))
        nota_des = int(tracker.get_slot("nota_deseada"))
        abaco=[
            [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5],
            ]    
        aux = [fila[firma_actual-35] for fila in abaco]
        aux.reverse()
        nota5 = aux.index(5)+9
        indice5 = 21-aux.index(5)

        nota4 = aux.index(4)+9
        indice4 = 21-aux.index(4)

        nota3 = aux.index(3)+9
        indice3 = 21-aux.index(3)

        nota2 = aux.index(2)+9
        indice2 = 21-aux.index(2)
            
        notas = [nota2,nota3,nota4,nota5]

        if nota_des==0:
            msg = f"Para pasar con 2 tenes que hacer {nota2}\nPara quitar 3, {nota3}\nPara quitar 4,{nota4}\n y para quitar 5 {nota5}"
            dispatcher.utter_message(text=msg)
        else:
            msg = f"Si haces {puntos_final} en el final, quitas {aux[puntos_final-9]}"
            dispatcher.utter_message(text=msg)
        return []