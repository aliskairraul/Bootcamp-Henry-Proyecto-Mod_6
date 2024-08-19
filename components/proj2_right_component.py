from dash import html
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("data/tabla_proj_2.csv")

column_defs = [
    {"field": "enginesize", "headerName": "Cilindradas (in³)", "width": "110vw"},
    {"field": "curbweight", "headerName": "Peso (Kg)", "width": "110vw"},
    {"field": "horsepower", "headerName": "Potencia (HP)", "width": "110vw"},
    {"field": "carwidth", "headerName": "Ancho (In)", "width": "110vw"},
    {"field": "citympg", "headerName": "Consumo (MPG)", "width": "110vw"},
    {"field": "carlength", "headerName": "Largo (In)", "width": "110vw"},
    {"field": "Brand", "headerName": "Marca", "width": "110vw"},
    {"field": "cylindernumber", "headerName": "Cilindros", "width": "110vw"},
    {"field": "price", "headerName": "Target", "width": "110vw"},
]


default_col_def = {
    "wrapHeaderText": True,
    "autoHeaderHeight": True,
    "headerClass": "center-aligned-header",
}


proj_2_right = html.Div(
    [
        html.Div(
            html.Label(
                "Proyecto Integrador Modulo-6 (Propuesta 2) Data-PT10 Grupo 1",
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
                    id="grid-2",
                    rowData=df.to_dict("records"),
                    columnDefs=column_defs,
                    defaultColDef=default_col_def,
                    className="ag-theme-balham-dark",
                    style={
                        "height": "66vh",
                        "width": "98%",
                        "center-header": {"textAlign": "center"},
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
