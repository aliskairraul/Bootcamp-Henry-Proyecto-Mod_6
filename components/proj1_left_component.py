from dash import dcc, html
import pandas as pd
import numpy as np

edades = list(range(35, 101, 1))
psa_s = np.arange(0.4, 100.01, 0.1)
psa_s = np.round(psa_s, 2)
num_muestras = list(range(1, 31, 1))
volumen_prostatico = ["Menor a 40 cm³", "Mayor o igual a 40 cm³"]

antibioticos = [
    "FLUOROQUINOLONA_AMINOGLICOSIDO",
    "CEFALOSPORINA_AMINOGLUCOCIDO",
    "OROQUINOLONAS",
    "FLUOROQUINOLONA_AMINOGLICÓSIDO",
    "OTROS",
]

biopsias = [
    "NEG",
    "ADENOCARCINOMA GLEASON 6 ",
    "ADENOCARCINOMA GLEASON 7 ",
    "ADENOCARCINOMA GLEASON 6",
    "ADENOCARCINOMA GLEASON 10 ",
    "ADENOCARCINOMA GLEASON 9 ",
    "ADENOCARCINOMA GLEASON 8 ",
    "PROSTATITIS",
    "ADENOCARCINOMA GLEASON 7",
    "HIPERPLASIA PROSTATICA",
    "CARCINOMA INDIFERENCIADO DE CELULAS CLARAS",
]


def returned_comp_left1(df: pd.DataFrame) -> html.Div:
    """returned_comp_left1: Esta Funcion se encarga de crear y retornar los distintos componentes que se
                            mostraran en la parte izquierda de la pantalla del proyecto 1.

    Args:
        df (pd.DataFrame): Dataframe de Pandas que contendra los distintos Valores que tendrán los componentes
                           de la parte izquierda de la pantalla del proyecto 1, en caso de que el usuario haya
                           seleccinado una fila de la tabla que aparece la parte derecha de la pantalla

    Returns:
        html.Div: Componente global que encierra a todos los comopnentes que se muestran en la parte izquierda de
                  la pantalla del proyecto 1
    """
    if len(df) > 0:
        edad = df.iloc[0, 0]
        diabetes = "Si" if df.iloc[0, 1] == 1 else "No"
        hosp_ultimo_mes = "Si" if df.iloc[0, 2] == 1 else "No"
        psa = df.iloc[0, 3]
        biopsias_previas = "Si" if df.iloc[0, 4] == 1 else "No"
        vol_prostatico = (
            "Mayor o igual a 40 cm³" if df.iloc[0, 5] == 1 else "Menor a 40 cm³"
        )
        antibiotico = df.iloc[0, 6]
        muestras = df.iloc[0, 7]
        biopsia = df.iloc[0, 8]
        fiebre = "Si" if df.iloc[0, 9] == 1 else "No"
    else:
        edad = edades[0]
        diabetes = "No"
        hosp_ultimo_mes = "No"
        psa = psa_s[0]
        biopsias_previas = "No"
        vol_prostatico = volumen_prostatico[0]
        antibiotico = antibioticos[0]
        muestras = num_muestras[0]
        biopsia = biopsias[0]
        fiebre = "No"

    proj_1_left = html.Div(
        [
            html.Div(html.Label("Variables Predictoras"), className="predictors-title"),
            html.Div(
                [
                    html.Div(
                        [
                            html.Label(
                                "Edad del Paciente", className="label-drops-proj"
                            ),
                            dcc.Dropdown(
                                id="drop-edad",
                                className="height",
                                options=edades,
                                value=edad,
                                placeholder="Seleccione la Edad",
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
                            html.Label("PSA en sangre", className="label-drops-proj"),
                            dcc.Dropdown(
                                id="drop-psa",
                                options=psa_s,
                                value=psa,
                                placeholder="PSA en Sangre",
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
                className="two-minidrop",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Label(
                                "Volumen Prostático", className="label-drops-proj"
                            ),
                            dcc.Dropdown(
                                id="drop-volumen",
                                className="height",
                                options=volumen_prostatico,
                                value=vol_prostatico,
                                placeholder="Seleccione la Edad",
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
                                "Muestras Tomadas", className="label-drops-proj"
                            ),
                            dcc.Dropdown(
                                id="drop-muestras",
                                options=num_muestras,
                                value=muestras,
                                placeholder="PSA en Sangre",
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
                className="two-minidrop",
                id="two-minidrop-2",
            ),
            html.Div(
                [
                    html.Label(
                        "Antibiotico Utilizado en la Profilaxis",
                        className="label-drops-proj",
                    ),
                    dcc.Dropdown(
                        id="drop-antibiotico",
                        options=antibioticos,
                        value=antibiotico,
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
                    html.Label(
                        "Examen de Biopsia practicado",
                        className="label-drops-proj",
                    ),
                    dcc.Dropdown(
                        id="drop-biopsia",
                        options=biopsias,
                        value=biopsia,
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
                            html.Label("Diabetes", className="label-drops-proj"),
                            dcc.RadioItems(
                                ["Si", "No"],
                                value=diabetes,
                                id="radio-diabetes",
                                style={"color": "rgb(240, 240, 240)"},
                            ),
                        ],
                        className="one-radio-container",
                    ),
                    html.Div(
                        [
                            html.Label("Fiebre", className="label-drops-proj"),
                            dcc.RadioItems(
                                ["Si", "No"],
                                value=fiebre,
                                id="radio-fiebre",
                                style={"color": "rgb(240, 240, 240)"},
                            ),
                        ],
                        className="one-radio-container",
                    ),
                ],
                className="two-radios-container",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Label(
                                "Hosp. Mes Anterior", className="label-drops-proj"
                            ),
                            dcc.RadioItems(
                                ["Si", "No"],
                                value=hosp_ultimo_mes,
                                id="radio-ultimo_mes",
                                style={"color": "rgb(240, 240, 240)"},
                            ),
                        ],
                        className="one-radio-container",
                    ),
                    html.Div(
                        [
                            html.Label(
                                "Biopsias Previas", className="label-drops-proj"
                            ),
                            dcc.RadioItems(
                                ["Si", "No"],
                                value=biopsias_previas,
                                id="radio-biopsias_previas",
                                style={"color": "rgb(240, 240, 240)"},
                            ),
                        ],
                        className="one-radio-container",
                    ),
                ],
                className="two-radios-container",
            ),
            html.Div(
                html.Button("Predecir", className="btn-predecir", id="predecir-1"),
                className="btn-container",
            ),
            html.Div(className="predictors-title", id="prediccion-1"),
        ],
        className="work-left-container",
    )
    return proj_1_left
