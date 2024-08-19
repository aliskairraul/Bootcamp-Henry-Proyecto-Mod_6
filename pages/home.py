import dash
from dash import html, Input, Output, callback
import pandas as pd

import joblib

from components.proj1_left_component import returned_comp_left1
from components.proj1_right_component import proj_1_right

dash.register_page(
    __name__, path="/", name="🚑 Propuesta-1 🏩", suppress_callback_exceptions=True
)


layout = html.Div(
    [
        html.Div(
            [
                html.Div([], className="left-container", id="left-proj-1"),
                html.Div([proj_1_right], className="right-container"),
            ],
            className="inner-container",
        )
    ],
    className="work-container",
)


@callback(Output("left-proj-1", "children"), Input("grid-1", "selectedRows"))
def update_left1(rowselected: list[dict]) -> html.Div:
    """update_left1: La app en ambas propuestas de Proyectos esta mostrada en una pantalla que se divide
                     en dos partes.  En la parde la Izquierda se desglozan los valores que tendrán las
                     variables predictoras. Para facilidad del usuario se da la opcion de cargar datos
                     desde una tabla que esta en la parte derecha de la pantalla (datos provenientes
                     del set de prueba suministrado para el proyecto) Esta funcion se activa cuando el
                     usuario a selecciona una fila (row) de la tabla, recogiendo los datos de la misma
                     y enviandolo a la funcion que devuelve el componente COMPLETO de la parte izquierda
                     de la pantalla


    Args:
        rowselected (list[dict]): Fila seleccionada por el usuario en este caso viene una lista de diccionarios
                                  donde cada diccionario es una fila seleccionada. Como esta activada la opcion
                                  de `single` solo se puede seleccionar una sola Fila a la vez, por lo que la
                                  posicion cero(0) de esta lista es el diccionario que contiene los valores de
                                  los campos

    Returns:
        html.Div: Es el componente que recibe de la funcion 'returned_comp_left1` que a su vez inserta en el componente
                  cuyo id es 'left-proj-1` para mostrar la parte izquierda de la pantalla
    """
    df = pd.DataFrame()
    if rowselected:
        df = pd.DataFrame(rowselected[0], index=[0])
        component = returned_comp_left1(df=df)

    component = returned_comp_left1(df=df)
    return component


@callback(
    Output("prediccion-1", "children"),
    [
        Input("predecir-1", "n_clicks"),
        Input("drop-edad", "value"),
        Input("drop-psa", "value"),
        Input("drop-volumen", "value"),
        Input("drop-muestras", "value"),
        Input("drop-antibiotico", "value"),
        Input("drop-biopsia", "value"),
        Input("radio-diabetes", "value"),
        Input("radio-fiebre", "value"),
        Input("radio-ultimo_mes", "value"),
        Input("radio-biopsias_previas", "value"),
    ],
)
def predicion_1(
    n_clicks: int,
    edad: int,
    psa: float,
    volumen: str,
    muestras: int,
    antibiotico: str,
    biopsia: str,
    diabetes: str,
    fiebre: str,
    ultimo_mes: str,
    biopsias_previas: str,
) -> html.Label:
    """prediccion_1: Esta Funcion se encarga de recibir los distintos valores de las variables predictoras, y crear
                     el dataframe con la estructura adecuada para luego usarla en el modelo que hace la prediccion
                     del proyecto 1

    Args:
        n_clicks (int): variable que escucha cuando se hace click en el boton
        edad (int): Variable predictora 'EDAD'
        psa (float): Variable predictora 'PSA'
        volumen (str): Variable predictora 'VOLUMEN PROSTATICO'
        muestras (int): Variable predictora 'NUMERO DE MUESTRAS TOMADAS'
        antibiotico (str): Variable predictora 'ANTIBIOTICO UTILIAZADO EN LA PROFILAXIS'
        biopsia (str): Variable predictora 'BIOPSIA'
        diabetes (str): Variable predictora 'DIABETES'
        fiebre (str): Variable predictora 'FIEBRE'
        ultimo_mes (str): Variable predictora 'HOSPITALIZACIÓN ULTIMO MES'
        biopsias_previas (str): Variable predictora 'BIOPSIAS PREVIAS'

    Returns:
        html.Label: Componente Label que muestra el resultado de la Prediccion
    """
    componente = None
    if n_clicks:
        modelo = joblib.load("models/modelo_proyecto_01.pkl")

        inputs = {}
        inputs["EDAD"] = edad
        inputs["DIABETES"] = 1 if diabetes == "Si" else 0
        inputs["HOSPITALIZACIÓN ULTIMO MES"] = 1 if ultimo_mes == "Si" else 0
        inputs["PSA"] = psa
        inputs["BIOPSIAS PREVIAS"] = 1 if biopsias_previas == "Si" else 0
        inputs["VOLUMEN PROSTATICO"] = 1 if volumen == "Mayor o igual a 40 cm³" else 0
        inputs["ANTIBIOTICO UTILIAZADO EN LA PROFILAXIS"] = antibiotico
        inputs["NUMERO DE MUESTRAS TOMADAS"] = muestras
        inputs["BIOPSIA"] = biopsia
        inputs["FIEBRE"] = 1 if fiebre == "Si" else 0

        df_inputs = pd.DataFrame(inputs, index=[0])
        predicion = modelo.predict(df_inputs)

        componente = html.Label(f"El resultado de la Prediccion es {predicion[0]}")

    return componente
