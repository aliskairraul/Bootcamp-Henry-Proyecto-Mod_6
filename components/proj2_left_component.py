from dash import dcc, html
import pandas as pd
import numpy as np

enginesizes = list(range(61, 327))
horspowers = list(range(48, 289))
curbweights = list(range(1488, 4067))
citympgs = list(range(13, 50))

carlenght = np.arange(141.1, 208.2, 0.1)
carlenght = np.round(carlenght, 2)

carwidths = np.arange(60.3, 72.3, 0.1)
carwidths = np.round(carwidths, 2)

cylindernumbers = ["two", "three", "four", "five", "six", "eight", "twelve"]
brands = [
    "Bmw",
    "Volvo",
    "Plymouth",
    "Mitsubishi",
    "Buick",
    "Subaru",
    "Volkswagen",
    "Toyota",
    "Jaguar",
    "Dodge",
    "Mazda",
    "Porsche",
    "Alfa-romeo",
    "Audi",
    "Nissan",
    "Isuzu",
    "Chevrolet",
    "Mercury",
    "Saab",
    "Renault",
    "Peugeot",
    "Honda",
]


def returned_comp_left2(df: pd.DataFrame) -> html.Div:
    """returned_comp_left2: Esta Funcion se encarga de crear y retornar los distintos componentes que se
                            mostraran en la parte izquierda de la pantalla del proyecto 2.

    Args:
        df (pd.DataFrame): Dataframe de Pandas que contendra los distintos Valores que tendrán los componentes
                           de la parte izquierda de la pantalla del proyecto 2, en caso de que el usuario haya
                           seleccinado una fila de la tabla que aparece la parte derecha de la pantalla

    Returns:
        html.Div: Componente global que encierra a todos los comopnentes que se muestran en la parte izquierda de
                  la pantalla del proyecto 2
    """
    if len(df) > 0:
        cilindrada = df.iloc[0, 0]
        peso = df.iloc[0, 1]
        hp = df.iloc[0, 2]
        ancho = df.iloc[0, 3]
        consumo = df.iloc[0, 4]
        largo = df.iloc[0, 5]
        marca = df.iloc[0, 6]
        cilindros = df.iloc[0, 7]
    else:
        cilindrada = enginesizes[0]
        peso = curbweights[0]
        hp = horspowers[0]
        ancho = carwidths[0]
        consumo = citympgs[0]
        largo = carlenght[0]
        marca = brands[0]
        cilindros = cylindernumbers[0]
    proj_2_left = html.Div(
        [
            html.Div(html.Label("Variables Predictoras"), className="predictors-title"),
            html.Div(
                [
                    html.Label(
                        "Marca del Automovil",
                        className="label-drops-proj",
                    ),
                    dcc.Dropdown(
                        id="drop-marca",
                        options=brands,
                        value=marca,
                        style={
                            "backgroundColor": "rgb(112, 194, 232)",
                            "fontSize": 14,
                            "color": "rgb(51, 51, 51)",
                            "border-radius": "1vh",
                        },
                    ),
                ],
                className="drop-grande-proj",
                id="container-drop-marca",
            ),
            html.Div(
                [
                    html.Label(
                        "Número de Cilindros del Motor del Automovil",
                        className="label-drops-proj",
                    ),
                    dcc.Dropdown(
                        id="drop-cilindros",
                        options=cylindernumbers,
                        value=cilindros,
                        style={
                            "backgroundColor": "rgb(112, 194, 232)",
                            "fontSize": 14,
                            "color": "rgb(51, 51, 51)",
                            "border-radius": "1vh",
                        },
                    ),
                ],
                className="drop-grande-proj",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Label(
                                "Tamaño del Motor (in³)", className="label-drops-proj"
                            ),
                            dcc.Dropdown(
                                id="drop-cilindrada",
                                className="height",
                                options=enginesizes,
                                value=cilindrada,
                                style={
                                    "backgroundColor": "rgb(112, 194, 232)",
                                    "fontSize": 14,
                                    "color": "rgb(51, 51, 51)",
                                    "border-radius": "1vh",
                                },
                            ),
                        ],
                        className="mini-drop",
                    ),
                    html.Div(
                        [
                            html.Label(
                                "Caballos de Fuerza (HP)", className="label-drops-proj"
                            ),
                            dcc.Dropdown(
                                id="drop-hp",
                                options=horspowers,
                                value=hp,
                                style={
                                    "backgroundColor": "rgb(112, 194, 232)",
                                    "fontSize": 14,
                                    "color": "rgb(51, 51, 51)",
                                    "border-radius": "1vh",
                                },
                            ),
                        ],
                        className="mini-drop",
                    ),
                ],
                id="minidrops-proj2",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Label(
                                "Largo del Auto (in)", className="label-drops-proj"
                            ),
                            dcc.Dropdown(
                                id="drop-largo",
                                className="height",
                                options=carlenght,
                                value=largo,
                                style={
                                    "backgroundColor": "rgb(112, 194, 232)",
                                    "fontSize": 14,
                                    "color": "rgb(51, 51, 51)",
                                    "border-radius": "1vh",
                                },
                            ),
                        ],
                        className="mini-drop",
                    ),
                    html.Div(
                        [
                            html.Label(
                                "Ancho del Auto (in)", className="label-drops-proj"
                            ),
                            dcc.Dropdown(
                                id="drop-ancho",
                                options=carwidths,
                                value=ancho,
                                style={
                                    "backgroundColor": "rgb(112, 194, 232)",
                                    "fontSize": 14,
                                    "color": "rgb(51, 51, 51)",
                                    "border-radius": "1vh",
                                },
                            ),
                        ],
                        className="mini-drop",
                    ),
                ],
                id="minidrops-proj2",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Label(
                                "Peso del Auto (Kg)", className="label-drops-proj"
                            ),
                            dcc.Dropdown(
                                id="drop-peso",
                                className="height",
                                options=curbweights,
                                value=peso,
                                style={
                                    "backgroundColor": "rgb(112, 194, 232)",
                                    "fontSize": 14,
                                    "color": "rgb(51, 51, 51)",
                                    "border-radius": "1vh",
                                },
                            ),
                        ],
                        className="mini-drop",
                    ),
                    html.Div(
                        [
                            html.Label("Consumo (MPG)", className="label-drops-proj"),
                            dcc.Dropdown(
                                id="drop-consumo",
                                options=citympgs,
                                value=consumo,
                                style={
                                    "backgroundColor": "rgb(112, 194, 232)",
                                    "fontSize": 14,
                                    "color": "rgb(51, 51, 51)",
                                    "border-radius": "1vh",
                                },
                            ),
                        ],
                        className="mini-drop",
                    ),
                ],
                id="minidrops-proj2",
            ),
            html.Div(
                html.Button("Predecir", className="btn-predecir", id="predecir-2"),
                className="btn-container",
                id="btn-container-2",
            ),
            html.Div(className="predictors-title", id="prediccion-2"),
        ],
        className="work-left-container",
    )
    return proj_2_left
