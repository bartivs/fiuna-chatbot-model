
from typing import Text, List, Any, Dict
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_Notas = ['2','3','4','5','dos','tres','cuatro','cinco']
ALLOWED_Firma = ['35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','61','62','63','64','65','66','67','68','69','70']
ALLOWED_Carreras=['Civil','Industrial','Electromecánica','Electrónica','Geográfica y Ambiental','Mecánica','Mecatrónica']
ALLOWED_Lugares=['biblioteca','atención al alumno','FIUNA','caja','CEI','DTIC','aulas H','secretaría','fotocopiadora', 'cantina','mesa de entrada']
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
            msg = f"Hola {nombre}! Soy FiunaBOT, un asistente creado para responder a las preguntas frecuentes de los alumnos sobre la facultad.\nAlgunas de estas preguntas son:\n- Horario de la caja.\n- Horario de la biblioteca\n- Aulas donde se desarrollarán las clases\n- Malla curricular de la carrera."  
        else:
            msg = f"Hola! Soy FiunaBOT, un asistente creado para responder a las preguntas frecuentes de los alumnos sobre la facultad.\nAlgunas de estas preguntas son:\n- Horario de la caja.\n- Horario de la biblioteca\n- Aulas donde se desarrollarán las clases\n- Malla curricular de la carrera."  
        dispatcher.utter_message(text=msg)    
        return []

class ActionDirector(Action):
    def name(self) -> Text:
        return "action_director_carrera"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        carrera = (tracker.get_slot('carrera'))
        if carrera not in ALLOWED_Carreras:
            msg = f"Podés tener mas información sobre los directores de carrera en el siguiente enlace http://www.ing.una.py/?page_id=629"     
        else:
            directores = {'Civil':' el Prof. Ing. Roberto Olmedo Bareiro, Mail: rolmedo@ing.una.py ','Industrial':'la Ing. Gisela Olmedo, Mail: golmedo@ing.una.py','Electromecánica':'el Prof. Ing. Edgar Darío Castro Núñez, Mail: ecastro@ing.una.py','Electrónica':'el Prof. Ing. Oscar Dario Resquin, Mail: oresquin@ing.una.py', 'Geográfica y Ambiental':'el Prof. Ing. Oscar Alfonso Correa, Mail: oalfonso@ing.una.py', 'Mecánica':'el Prof. Ing. Orlando David Benítez Gómez, Mail: odbenitez@fiuna.edu.py', 'Mecatrónica':'el Prof. Ing. Gustavo Román Verón Alderete, Mail: gveron@ing.una.py'}
            msg = f"El director de {carrera} es {directores[carrera]}"
        dispatcher.utter_message(text=msg)
        return [SlotSet("carrera",None)]

class ActionInfoCarreras(Action):
    def name(self) -> Text:
        return "action_info_carrera"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        carrera = (tracker.get_slot('carrera'))
        if carrera not in ALLOWED_Carreras: 
            msg = f"Para obtener más información sobre las carreras de la FIUNA podés ingresar al siguiente enlace http://www.ing.una.py/?page_id=629"
        else:
            info = {'Civil':'http://www.ing.una.py/?page_id=1046','Industrial':'http://www.ing.una.py/?page_id=1083','Electromecánica':'http://www.ing.una.py/?page_id=1434','Electrónica':'http://www.ing.una.py/?page_id=1473', 'Geográfica y Ambiental':'http://www.ing.una.py/?page_id=1493', 'Mecánica':'http://www.ing.una.py/?page_id=1512', 'Mecatrónica':'http://www.ing.una.py/?page_id=1533'}
            msg = f"Para obtener más información sobre {carrera} podés ir al siguiente link: {info[carrera]}"      
        dispatcher.utter_message(text=msg)
        return [SlotSet("carrera",None)]

class ActionInformarHorario(Action):
    def name(self) -> Text:
        return "action_horario"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = (tracker.get_slot('lugar'))
        if place not in ALLOWED_Lugares:
            msg = f"Aún no cuento con esa información, espero poder ayudarte pronto" 
        else:
            info = {'biblioteca':'El horario de atención de la biblioteca es de Lunes a Viernes desde las 7:00 hasta las 20:00 y los sabados desde las 7:00 hasta las 12:00. La biblioteca de Citec abre de lunes a viernes de 7:15 a 19:00hs.',
                    'atención al alumno':'El horario de atención al alumno es de Lunes a Viernes de 8:00 a 18:00. Para mas información podes consultar llamar al 021 585584/1102',
                    'FIUNA':'La FIUNA abre de Lunes a Viernes de 07:00 a 22:15 y los sábados de 07:00 a 18:00 hs.',
                    'caja':'El horario de atención de la caja es de Lunes a Viernes de 07:30 a 19:00 y los Sábados de 08:00 a 12:00 hs.',
                    'CEI':'El horario del CEI es; Lunes a Viernes de 7:30 a 12:00 - 14:30 a 20:45 y los Sábados de 7:30 a 12:00 hs.',
                    'DTIC':'El horario de DTIC es de Lunes a Viernes de 7:00 a 17:00 y los Sábados de 7:00 a 18:00 hs. ',
                    'aulas H': 'El horario de las aulas H es de Lunes a Viernes de 8:00 a 19:00 y los Sábados de 8:00 a 12:00 hs. ',
                    'secretaría': 'El horario de secretaría es de Lunes a Viernes de 8:00 a 12:00 - 13:00 a 17:00 y los Sábados de 8:00 a 12:00 hs. ',
                    'fotocopiadora':'El horario de la fotocopiadora es de Lunes a Viernes de 7:00 a 19:00 y los Sábados de 7:00 a 14:00 hs. ',
                    'cantina':'El horario de la cantina es de Lunes a Viernes de 7:00 a 20:30 y los Sábados de 7:00 a 15:00 hs.',
                    'mesa de entrada':'El horario de mesa de entrada es de Lunes a Viernes de 08:00 a 18:30 y los Sábados de 08:00 a 12:00 hs.'
                    }
            msg = f"{info[place]}"     
        dispatcher.utter_message(text=msg)
        return [SlotSet("lugar",None)]
class ActionMallaCurricular(Action):
    def name(self) -> Text:
        return "action_malla_curricular"
    
    def run(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        carrera = (tracker.get_slot('carrera'))    
        if carrera not in ALLOWED_Carreras: 
            msg = f"Podés ver la malla curricular de tu carrera en el siguiente enlace: https://drive.google.com/drive/u/1/folders/1uphtj7-73YaAFhZmWX3mIDZbDFQPYlgo"
        else:
            info = {'Civil':'https://drive.google.com/file/d/1GiLXzY7Z9Y9dv_nRWL74I-SMWJyoqc8c/view','Industrial':'http://www.ing.una.py/pdf2013/mallaindustrial2013.JPG','Electromecánica':'https://drive.google.com/drive/folders/1BKwQLFdu7O1wTyXddubx1w-w-3Dd-n63','Electrónica':'http://www.ing.una.py/pdf2017/carreras/electronica/malla-Curricular2013-electronica.pdf', 'Geográfica y Ambiental':'http://www.ing.una.py/wp-content/uploads/2022/10/Malla_GyA_Actualizada.pdf', 'Mecánica':'https://drive.google.com/drive/folders/1KsIi87G1BziKuq5ZP_FRF-2_pJQpnKl0', 'Mecatrónica':'http://www.ing.una.py/pdf2022/Academico/Malla_actualizada_MCT2013.pdf'}
            msg = f"Podés ver la malla curricular de {carrera} en el siguiente enlace: {info[carrera]}"      
        dispatcher.utter_message(text=msg)
        return [SlotSet("carrera",None)]
