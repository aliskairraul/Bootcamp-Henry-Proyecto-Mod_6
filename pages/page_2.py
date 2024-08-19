import dash
from dash import html, Output, Input, callback
import pandas as pd
import joblib
import locale

from components.proj2_left_component import returned_comp_left2
from components.proj2_right_component import proj_2_right

locale.setlocale(locale.LC_ALL, "es_VE.utf8")

dash.register_page(__name__, path="/project-2", name="🚘 Propuesta-2 🚘")


layout = html.Div(
    [
        html.Div(
            [
                html.Div([], className="left-container", id="left-proj-2"),
                html.Div([proj_2_right], className="right-container"),
            ],
            className="inner-container",
        )
    ],
    className="work-container",
)


@callback(Output("left-proj-2", "children"), Input("grid-2", "selectedRows"))
def update_left2(rowselected: list[dict]) -> html.Div:
    """update_left2: La app en ambas propuestas de Proyectos esta mostrada en una pantalla que se divide
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
        html.Div: Es el componente que recibe de la funcion 'returned_comp_left2` que a su vez inserta en el componente
                  cuyo id es 'left-proj-2` para mostrar la parte izquierda de la pantalla
    """
    df = pd.DataFrame()
    if rowselected:
        df = pd.DataFrame(rowselected[0], index=[0])
        component = returned_comp_left2(df=df)

    component = returned_comp_left2(df=df)
    return component


@callback(
    Output("prediccion-2", "children"),
    [
        Input("predecir-2", "n_clicks"),
        Input("drop-marca", "value"),
        Input("drop-cilindros", "value"),
        Input("drop-cilindrada", "value"),
        Input("drop-hp", "value"),
        Input("drop-largo", "value"),
        Input("drop-ancho", "value"),
        Input("drop-peso", "value"),
        Input("drop-consumo", "value"),
    ],
)
def predicion_2(
    n_clicks: int,
    marca: str,
    cilindros: str,
    cilindrada: int,
    hp: int,
    largo: float,
    ancho: float,
    peso: int,
    consumo: int,
) -> html.Label:
    """prediccion_2: Esta Funcion se encarga de recibir los distintos valores de las variables predictoras, y crear
                     el dataframe con la estructura adecuada para luego usarla en el modelo que hace la prediccion
                     del proyecto 2

    Args:
        n_clicks (int): variable que escucha cuando se hace click en el boton
        marca (str): Variable predictora 'BRAND'
        cilindros (str): Variable predictora 'cylindernumber'
        cilindrada (int): Variable predictora 'enginesize'
        hp (int): Variable predictora 'horsepower'
        largo (float): Variable predictora 'carlength'
        ancho (float): Variable predictora 'carwidth'
        peso (int): Variable predictora 'curbweight'
        consumo (int): Variable predictora 'citympg'

    Returns:
        html.Label: Componente Label que muestra el resultado de la Prediccion
    """
    componente = None
    if n_clicks:
        modelo = joblib.load("models/modelo_proyecto_02.pkl")

        inputs = {}
        inputs["enginesize"] = cilindrada
        inputs["curbweight"] = peso
        inputs["horsepower"] = hp
        inputs["carwidth"] = ancho
        inputs["citympg"] = consumo
        inputs["carlength"] = largo
        inputs["Brand"] = marca
        inputs["cylindernumber"] = cilindros

        df_inputs = pd.DataFrame(inputs, index=[0])
        predicion = modelo.predict(df_inputs)
        resultado = locale.format_string("%d", round(predicion[0]), grouping=True)
        componente = html.Label(f"El resultado de la Prediccion es {resultado} $")

    return componente
