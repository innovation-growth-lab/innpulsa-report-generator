# pylint: disable=C0301
import re
from typing import List
import pandas as pd

# Variable type constants
NUMERIC = "numeric"
BOOLEAN = "boolean"
CATEGORICAL = "categorical"
ARRAY = "array"
DUMMY = "dummy"
INDICATOR = "indicator"

# Categorical value mappings for interpretation
CATEGORICAL_MAPPINGS = {
    "observ_productionplant": [
        "Hay congestión por deficiente utilización de espacio.",
        "Hay suficiente espacio para manipular los productos, materias primas e insumos.",
    ],
    "invent_control": [
        "No realiza inventario",
        "Realiza inventario de manera ocasional y sin medir la exactitud",
        "Realiza inventario constantemente y la exactitud de medición es mayor al 80%",
    ],
    "newideas_datasheet": [
        "No, el proceso se hace de manera verbal.",
        "Se toma como referencia la muestra física y se modifica.",
        "La unidad productiva ya cuenta con formatos que permitan registrar los nuevos diseños y cambios en los existentes.",
    ],
    "packaging": [
        "El empaque del producto no tiene marca, sino que se utilizan elementos genéricos como bolsas, plásticos o cartones de calidad comercial.",
        "El producto posee un empaque estándar que tiene como única función la protección de la mercancía y los datos del fabricante.",
        "La unidad productiva posee un empaque que exalta los valores de la marca y busca distinguirse en las exhibiciones ó incluso el deseo de ser conservado por el Cliente para su recordación.",
    ],
    "price_system": [
        "Ninguno - No se ha definido un mecanismo de fijación de precios",
        "Los precios de mercado de los competidores",
        "Los costos y gastos del negocio",
        "Los costos, gastos y porcentaje de ganancia de cada producto",
    ],
    "bookkeeping": [
        "A mano",
        "Excel",
        "Libro contable",
        "Software contable",
    ],
}


def find_matching_vars(
    base_pattern: str, df: pd.DataFrame, control_only: bool = False
) -> List[str]:
    """Find all variables in df that match a base pattern.

    Args:
        base_pattern: Pattern that may contain {} placeholder (e.g. 'producedunits_{}')
        df: DataFrame containing the variables
        control_only: If True, return variables ending in 'c', otherwise those not ending in 'c'

    Returns:
        List of matching variable names sorted alphabetically
    """
    pattern_parts = base_pattern.split("{}")
    if len(pattern_parts) != 2:
        raise ValueError("Dynamic patterns must contain exactly one {} placeholder")

    prefix, suffix = pattern_parts
    regex = (
        f"^{re.escape(prefix)}.*{re.escape(suffix)}{'c$' if control_only else '[^c]$'}"
    )

    # Find matching columns
    matching = [col for col in df.columns if re.match(regex, col)]
    return sorted(matching)


def get_sections_config(df: pd.DataFrame) -> dict:
    """Generate sections configuration based on available variables in DataFrame.

    Args:
        df: DataFrame containing all variables

    Returns:
        Dictionary containing the sections configuration where each section contains
        a dictionary of variables with their possible column name combinations
    """
    return {
        "Optimización operativa": {
            "production_efficiency": {
                "var_pairs": [
                    (
                        (
                            find_matching_vars("producedunits_{}", df),
                            find_matching_vars("targetunits_{}", df),
                        ),
                        (
                            find_matching_vars("producedunits_{}", df, control_only=True),
                            find_matching_vars("targetunits_{}", df, control_only=True),
                        ),
                    )
                ],
                "type": INDICATOR,
                "metadata": {
                    "name": "production_efficiency",
                    "description": "Eficiencia de producción",
                    "calculation": (
                        "El ratio de eficiencia de producción es el ratio entre el"
                        " número de unidades producidas y el número de unidades objetivo."
                    ),
                },
            },
            "knows_standardtime": {
                "var_pairs": [
                    ("knows_standardtime", "standard_timec"),
                    ("knows_standardtime", "knows_standardtimec"),
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "knows_standardtime",
                    "description": "Conoce el tiempo estándar de producción",
                },
            },
            "defective_units_rate": {
                "var_pairs": [
                    (
                        (
                            find_matching_vars("defectiveunits_{}", df),
                            find_matching_vars("producedunits_{}", df),
                        ),
                        (
                            find_matching_vars("defectiveunits_{}", df, control_only=True),
                            find_matching_vars("producedunits_{}", df, control_only=True),
                        ),
                    )
                ],
                "type": INDICATOR,
                "metadata": {
                    "name": "defective_units_rate",
                    "description": "Tasa de Unidades defectuosas",
                    "calculation": (
                        "La tasa de unidades defectuosas es el ratio entre el número de "
                        "unidades defectuosas y el número total de unidades producidas."
                    ),
                },
            },
            "observ_productionplant": {
                "var_pairs": [
                    ("observ_productionplant", "observ_productionplantc")
                ],
                "type": CATEGORICAL,
                "metadata": {
                    "name": "observ_productionplant",
                    "description": "Estado de la distribución del espacio",
                    "mapping": CATEGORICAL_MAPPINGS["observ_productionplant"],
                },
            },
            "invent_control": {
                "var_pairs": [
                    ("invent_control", "invent_controlc")
                ],
                "type": CATEGORICAL,
                "metadata": {
                    "name": "invent_control",
                    "description": "Realiza control de inventario",
                    "mapping": CATEGORICAL_MAPPINGS["invent_control"],
                },
            },
            "knowsinput": {
                "var_pairs": [
                    ("knowsinput", "knowsinputc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "knowsinput",
                    "description": "Conoce niveles óptimos de inventario",
                },
            },
            "indicadores_eficiencia": {
                "var_pairs": [
                    ("indicadores_eficiencia", "indicadores_eficienciac")
                ],
                "type": [DUMMY, BOOLEAN],
                "metadata": {
                    "name": "indicadores_eficiencia",
                    "description": "Tiene indicadores de eficiencia",
                },
            },
            "indicadores_productividad": {
                "var_pairs": [
                    ("indicadores_productividad", "indicadores_productividadc")
                ],
                "type": [DUMMY, BOOLEAN],
                "metadata": {
                    "name": "indicadores_productividad",
                    "description": "Tiene indicadores de productividad",
                },
            },
            "index": {
                "var_pairs": [
                    ("index", "hasindicatorsc")
                ],
                "type": [DUMMY, BOOLEAN],
                "metadata": {
                    "name": "index",
                    "description": "Tiene indicadores generales",
                },
            },
        },
        "Mayor Calidad del Producto": {
            "qualityprocess_sample": {
                "var_pairs": [
                    ("qualityprocess_sample", "qualityprocess_samplec")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "qualityprocess_sample",
                    "description": "Para garantizar la calidad de los productos: Realiza muestra y contramuestra",
                },
            },
            "qualityprocess_set_machinery": {
                "var_pairs": [
                    ("qualityprocess_set_machinery", "qualityprocess_set_machineryc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "qualityprocess_set_machinery",
                    "description": "Para garantizar la calidad de los productos: Realiza preparación de máquinas",
                },
            },
            "qualityprocess_control_quality": {
                "var_pairs": [
                    ("qualityprocess_control_quality", "qualityprocess_control_qualityc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "qualityprocess_control_quality",
                    "description": "Para garantizar la calidad de los productos: Tiene controles de calidad",
                },
            },
            "qualityprocess_none": {
                "var_pairs": [
                    ("qualityprocess_none", "qualityprocess_nonec")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "qualityprocess_none",
                    "description": "Para garantizar la calidad de los productos: No tiene procesos de calidad",
                },
            },
            "newideas_datasheet": {
                "var_pairs": [
                    ("newideas_datasheet", "newideas_designc")
                ],
                "type": CATEGORICAL,
                "metadata": {
                    "name": "newideas_datasheet",
                    "description": "Las ideas de los nuevos diseños se registran en una ficha técnica",
                    "mapping": CATEGORICAL_MAPPINGS["newideas_datasheet"],
                },
            },
            "packaging": {
                "var_pairs": [
                    ("packaging", "packagingc")
                ],
                "type": CATEGORICAL,
                "metadata": {
                    "name": "packaging",
                    "description": "Cómo funciona en general el empaque en el negocio",
                    "mapping": CATEGORICAL_MAPPINGS["packaging"],
                },
            },
            "software_design": {
                "var_pairs": [
                    ("software_design", "software_designc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "software_design",
                    "description": "El negocio utiliza algún software especializado para el diseño de sus productos",
                },
            },
            "patterns_digitized": {
                "var_pairs": [
                    ("patterns_digitized", "digital_patternc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "patterns_digitized",
                    "description": "Los patrones están digitalizados",
                },
            },
            "patterns_prevcollections": {
                "var_pairs": [
                    ("patterns_prevcollections", "prev_patternc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "patterns_prevcollections",
                    "description": "El negocio usualmente guarda los patrones de colecciones anteriores",
                },
            },
        },
        "Talento Humano": {
            "emp_ft": {
                "var_pairs": [
                    ("emp_ft", "emp_ftc")
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "emp_ft",
                    "description": "Empleados de nómina (afiliados por el negocio al sistema de salud y pensión)",
                },
            },
            "emp_total": {
                "var_pairs": [
                    ("emp_total", "emp_totalc")
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "emp_total",
                    "description": "Empleados totales",
                },
            },
            "hassalary": {
                "var_pairs": [
                    ("hassalary", "hassalaryc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "hassalary",
                    "description": "Postulante recibe sueldo fijo del negocio",
                },
            },
            "income": {
                "var_pairs": [
                    ("income", "incomec")
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "income",
                    "description": "Cuánto recibe de sueldo fijo en un mes promedio",
                },
            },
        },
        "Practicas Gerenciales": {
            "price_system": {
                "var_pairs": [
                    ("price_system", "price_systemc")
                ],
                "type": CATEGORICAL,
                "metadata": {
                    "name": "price_system",
                    "description": "Los precios se fijan con base en",
                    "mapping": CATEGORICAL_MAPPINGS["price_system"],
                },
            },
            "knows_production_cost": {
                "var_pairs": [
                    ("knows_production_cost", "knows_production_costc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_production_cost",
                    "description": "En el negocio conoce: El costo de producir cada unidad de producto o servicio",
                },
            },
            "knows_max_production": {
                "var_pairs": [
                    ("knows_max_production", "knows_max_productionc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_max_production",
                    "description": "En el negocio conoce: Cantidad máxima de productos que puedes generar u ofrecer en un periodo determinado (por ejemplo: diaria, semanal, mensual)",
                },
            },
            "knows_profit_margin": {
                "var_pairs": [
                    ("knows_profit_margin", "knows_profit_marginc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_profit_margin",
                    "description": "En el negocio conoce: Porcentaje o margen de ganancia de cada producto o servicio",
                },
            },
            "knows_sales_frequency": {
                "var_pairs": [
                    ("knows_sales_frequency", "knows_sales_frequencyc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_sales_frequency",
                    "description": "En el negocio conoce: Periodicidad de las ventas de tus productos o servicios (ej.: diaria, semanal, mensual)",
                },
            },
            "knows_detailed_income": {
                "var_pairs": [
                    ("knows_detailed_income", "knows_detailed_incomec")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_detailed_income",
                    "description": "En el negocio conoce: Ingresos del negocio de manera detallada",
                },
            },
            "productcost_materials": {
                "var_pairs": [
                    ("productcost_materials", "productcost_materialsc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "productcost_materials",
                    "description": "Para costo de producto se calcula: Costo total materiales directos",
                },
            },
            "productcost_handwork": {
                "var_pairs": [
                    ("productcost_handwork", "productcost_handworkc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "productcost_handwork",
                    "description": "Para costo de producto se calcula: Costo total mano de obra directa",
                },
            },
            "productcost_fabrication": {
                "var_pairs": [
                    ("productcost_fabrication", "productcost_fabricationc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "productcost_fabrication",
                    "description": "Para costo de producto se calcula: Gastos generales de fabricación",
                },
            },
        },
        "Financiero": {
            "sales2023q1s": {
                "var_pairs": [
                    ("sales2023q1s", "sales2024q1s")
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "sales2023q1s",
                    "description": "Ventas trimestrales, 2023T1-vs-2024T1",
                },
            },
            "salesaverage2024": {
                "var_pairs": [
                    (None, "salesaverage2024")
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "salesaverage2024",
                    "description": "Valor promedio mensual de las ventas del 2024",
                },
            },
            "participate_commercial": {
                "var_pairs": [
                    (None, "participate_commercial")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "participate_commercial",
                    "description": "Participó en alguna rueda comercial del programa",
                },
            },
            "connection_commercial": {
                "var_pairs": [
                    (None, "connection_commercial")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "connection_commercial",
                    "description": "Generó conexiones durante el desarrollo de la rueda comercial",
                },
            },
            "participate_financial": {
                "var_pairs": [
                    (None, "participate_financial")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "participate_financial",
                    "description": "Participó en alguna rueda financiera del programa",
                },
            },
            "connection_financial": {
                "var_pairs": [
                    (None, "connection_financial")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "connection_financial",
                    "description": "Generó conexiones durante el desarrollo de la rueda financiera",
                },
            },
            "banked": {
                "var_pairs": [
                    ("banked", "bankedc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "banked",
                    "description": "Tiene cuenta bancaria",
                },
            },
            "bookkeeping": {
                "var_pairs": [
                    ("bookkeeping", "bookkeepingc")
                ],
                "type": CATEGORICAL,
                "metadata": {
                    "mapping": CATEGORICAL_MAPPINGS["bookkeeping"],
                    "description": "Forma de llevar las cuentas del negocio",
                    "name": "bookkeeping",
                },
            },
        },
        "Asociatividad": {
            "knows_associationways": {
                "var_pairs": [
                    ("knows_associationways", "knows_associationwaysc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "knows_associationways",
                    "description": "El líder del negocio conoce cómo establecer y formalizar los diferentes mecanismos de asociatividad empresarial",
                },
            },
            "association_group_training": {
                "var_pairs": [
                    ("association_group_training", "association_group_trainingc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_group_training",
                    "description": "Se ha asociado para realizar: Sí, para tomar capacitaciones grupales",
                },
            },
            "association_new_machinery": {
                "var_pairs": [
                    ("association_new_machinery", "association_new_machineryc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_new_machinery",
                    "description": "Se ha asociado para realizar: Sí, para adquirir maquinaria y equipos modernos",
                },
            },
            "association_buy_supplies": {
                "var_pairs": [
                    ("association_buy_supplies", "association_buy_suppliesc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_buy_supplies",
                    "description": "Se ha asociado para realizar: Sí, para comprar insumos y así reducir costos",
                },
            },
            "association_use_machinery_nobuy": {
                "var_pairs": [
                    ("association_use_machinery_nobuy", "association_use_machinery_nobuyc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_use_machinery_nobuy",
                    "description": "Se ha asociado para realizar: Sí, para utilizar maquinaria sin tener que comprarla",
                },
            },
            "association_new_markets": {
                "var_pairs": [
                    ("association_new_markets", "association_new_marketsc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_new_markets",
                    "description": "Se ha asociado para realizar: Sí, para acceder a nuevos mercados",
                },
            },
            "association_distribution": {
                "var_pairs": [
                    ("association_distribution", "association_distributionc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_distribution",
                    "description": "Se ha asociado para realizar: Sí, para procesos logísticos y de distribución",
                },
            },
            "association_have_not": {
                "var_pairs": [
                    ("association_have_not", "association_have_notc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_have_not",
                    "description": "Se ha asociado para realizar: No me he asociado",
                },
            },
        },
    }
