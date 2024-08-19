from dash import html
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("data/tabla_proj_1.csv")


column_defs = [
    {"field": "EDAD", "headerName": "Edad", "width": "55vw"},
    {"field": "DIABETES", "headerName": "Diabetes", "width": "73vw"},
    {"field": "HOSPITALIZACIÓN ULTIMO MES", "headerName": "Mes Antes", "width": "73vw"},
    {"field": "PSA", "headerName": "PSA", "width": "50vw"},
    {"field": "BIOPSIAS PREVIAS", "headerName": "Biop Prev", "width": "55vw"},
    {"field": "VOLUMEN PROSTATICO", "headerName": "Volumen", "width": "73vw"},
    {
        "field": "ANTIBIOTICO UTILIAZADO EN LA PROFILAXIS",
        "headerName": "Antibiotico utilizado",
        "width": "215vw",
    },
    {"field": "NUMERO DE MUESTRAS TOMADAS", "headerName": "Muestras", "width": "75vw"},
    {"field": "BIOPSIA", "headerName": "Examen de Biopsia", "width": "160vw"},
    {"field": "FIEBRE", "headerName": "Fiebre", "width": "70vw"},
    {"field": "HOSPITALIZACION", "headerName": "Target", "width": "65vw"},
]


default_col_def = {
    # "initialWidth": 50,
    "wrapHeaderText": True,
    "autoHeaderHeight": True,
}


proj_1_right = html.Div(
    [
        html.Div(
            html.Label(
                "Proyecto Integrador Modulo-6 (Propuesta 1) Data-PT10 Grupo 1",
                className="predictors-title",
            ),
            className="container-titulo-proyecto",
        ),
        html.Div(
            [
                html.Div(
                    html.Label("Datos de Prueba del Dataset"),
                    className="predictors-title",
                ),
                html.Br(),
                dag.AgGrid(
                    id="grid-1",
                    rowData=df.to_dict("records"),
                    # columnDefs=[{"field": i} for i in df.columns],
                    columnDefs=column_defs,
                    defaultColDef=default_col_def,
                    className="ag-theme-balham-dark",
                    # columnSize="sizeToFit",
                    style={
                        "height": "66vh",
                        "width": "98%",
                    },
                    dashGridOptions={
                        "rowSelection": "single",
                    },
                ),
            ],
            className="container-table",
        ),
    ],
    className="work-right-container",
)

"""
ag-theme-alpine
ag-theme-balham
ag-theme-balham-dark
ag-theme-material
ag-theme-fresh
ag-theme-dark
ag-theme-blue
"""
