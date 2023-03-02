
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_Notas = ['2','3','4','5','dos','tres','cuatro','cinco']
ALLOWED_Firma = ['35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','61','62','63','64','65','66','67','68','69','70']
class ValidateNotasForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_notas_form"

    def validate_nota_des(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value.lower() not in ALLOWED_Notas:
            dispatcher.utter_message(text=f"Las notas son del 1 al 5.")
            return {"nota_des": None}
        dispatcher.utter_message(text=f"OK! queres quitar {slot_value}.")
        return {"nota_des": slot_value}

    def validate_firma(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value not in ALLOWED_Firma:
            dispatcher.utter_message(text="La firma debe estar entre 35 y 70")
            return {"firma": None}
        dispatcher.utter_message(text=f"OK! tu firma es {slot_value}.")
        return {"firma": slot_value}

ABACO = [
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5],
]
class ActionFirma(Action):
    def name(self) -> Text:
        return "action_informar_puntaje_final"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        firma_actual = int(tracker.get_slot('firma'))
        nota_deseada = (tracker.get_slot('nota_des'))
        if nota_deseada =='dos':
            nota_deseada = 2.0
        if nota_deseada =='tres':
            nota_deseada = 3.0
        if nota_deseada =='cuatro':
            nota_deseada = 4.0
        if nota_deseada =='cinco':
            nota_deseada = 5.0 
        nota_deseada = int(nota_deseada)
        aux = [fila[firma_actual - 35] for fila in ABACO]
        aux.reverse()

        puntaje_final = aux.index(nota_deseada)+9
            #indice5 = 21 - aux.index(5)
        msg = f"Si haces {puntaje_final} en el final, quitas {nota_deseada}"
        dispatcher.utter_message(text=msg)

        return []

class ActionSaludo(Action):
    def name(self) -> Text:
        return "action_saludo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nombre = (tracker.get_slot('nombre'))
        if nombre:
            msg = f"Hola {nombre}! Soy FiunaBOT, un asistente creado para ayudarte con las preguntas frecuentes de la facultad"
        else:
            msg = f"Hola! Soy FiunaBOT, un asistente creado para ayudarte con las preguntas frecuentes de la facultad"
        dispatcher.utter_message(text=msg)    
        return []

class ActionDirector(Action):
    def name(self) -> Text:
        return "action_director_carrera"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        carrera = (tracker.get_slot('carrera'))
        if carrera:
            directores = {'Civil':' el Prof. Ing. Roberto Olmedo Bareiro, Mail: rolmedo@ing.una.py ','Industrial':'la Ing. Gisela Olmedo, Mail: golmedo@ing.una.py','Electromecanica':'el Prof. Ing. Edgar Darío Castro Núñez, Mail: ecastro@ing.una.py','Electronica':'el Prof. Ing. Oscar Dario Resquin, Mail: oresquin@ing.una.py', 'Geografica':'el Prof. Ing. Oscar Alfonso Correa, Mail: oalfonso@ing.una.py', 'Mecanica':'el Prof. Ing. Orlando David Benítez Gómez, Mail: odbenitez@fiuna.edu.py', 'Mecatronica':'el Prof. Ing. Gustavo Román Verón Alderete, Mail: gveron@ing.una.py'}
            msg = f"El director de {carrera} es {directores[carrera]}"
        else:
            msg = f"Podés tener mas información sobre los directores de carrera en el siguiente enlace http://www.ing.una.py/?page_id=629"
        dispatcher.utter_message(text=msg)    
        return []

class ActionInfoCarreras(Action):
    def name(self) -> Text:
        return "action_info_carrera"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        carrera = (tracker.get_slot('carrera'))
        if carrera:
            info = {'Civil':'http://www.ing.una.py/?page_id=1046','Industrial':'http://www.ing.una.py/?page_id=1083','Electromecanica':'http://www.ing.una.py/?page_id=1434','Electronica':'http://www.ing.una.py/?page_id=1473', 'Geografica':'http://www.ing.una.py/?page_id=1493', 'Mecanica':'http://www.ing.una.py/?page_id=1512', 'Mecatronica':'http://www.ing.una.py/?page_id=1533'}
            msg = f"Para obtener más información sobre {carrera} podés ir al siguiente link: {info[carrera]}"
        else:
            msg = f"Para obtener más información sobre las carreras de la FIUNA podés ingresar al siguiente link: http://www.ing.una.py/?page_id=629"      
        dispatcher.utter_message(text=msg)
        return []