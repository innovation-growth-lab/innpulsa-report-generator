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
    "software_design": [
        "Diseño asistido por computadora (CAD), diseño en 3D, prototipado virtual",
        "Diseño digital o semi-digital usando software especializado de dibujo en 2D",
        "Diseño manual y dibujo a mano",
        "Otros",
    ],
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
        "Contador externo: Delegamos la gestión y registro de la información financiera a un contador externo",
        "Hojas de cálculo (Excel) o aplicación móvil para control de las cuentas del negocio",
        "Manualmente: Llevamos registros financieros utilizando métodos manuales como cuaderno, libros contables, cartillas o registros en papel.",
        "Ninguna: La gestión y registro de la información financiera no se realiza de ninguna manera y estamos buscando mejorar este aspecto.",
        "Software de contabilidad: Utilizamos software especializado de contabilidad para gestionar y registrar nuestras transacciones financieras.",
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
                    "description": "Eficiencia de la producción (unidades producidas / unidades meta).",
                    "calculation": (
                        "Calculado como la suma de unidades producidas ('producedunits_*') dividida por la suma de unidades meta ('targetunits_*') para los productos correspondientes."
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
                    "description": "Indica si el negocio calcula/conoce el tiempo estándar de producción.",
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
                    "description": "Tasa de unidades defectuosas (unidades defectuosas / unidades producidas).",
                    "calculation": (
                        "Calculado como la suma de unidades defectuosas ('defectiveunits_*') dividida por la suma total de unidades producidas ('producedunits_*') para los productos correspondientes."
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
                    "description": "Observación sobre la distribución y congestión del espacio en la planta de producción.",
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
                    "description": "Frecuencia y exactitud del control de inventario realizado por el negocio.",
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
                    "description": "Indica si el negocio conoce sus niveles óptimos de inventario de insumos/productos.",
                },
            },
            "indicadores_eficiencia": {
                "var_pairs": [
                    ("indicadores_eficiencia", "indicadores_eficienciac"),
                    # control variable might exist even if baseline doesn't
                    (None, "indicadores_eficienciac")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "indicadores_eficiencia",
                    "description": "Indica si el negocio utiliza indicadores específicos de eficiencia.",
                },
            },
            "indicadores_productividad": {
                "var_pairs": [
                    # no pre-intervention variable for some cohorts / centers
                    ("indicadores_productividad", "indicadores_productividadc"),
                    (None, "indicadores_productividadc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "indicadores_productividad",
                    "description": "Indica si el negocio utiliza indicadores específicos de productividad.",
                },
            },
            "hasindicators": {
                "var_pairs": [
                    # variable renamed between cohorts / centers
                    ("index", "hasindicatorsc"),
                    ("hasindicators", "hasindicatorsc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "hasindicators",
                    "description": "Indica si el negocio utiliza y hace seguimiento periódico de indicadores (más allá de los financieros).",
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
                    "description": "Indica si se utiliza el método de muestra y contramuestra para garantizar la calidad.",
                },
            },
            "qualityprocess_set_machinery": {
                "var_pairs": [
                    ("qualityprocess_set_machinery", "qualityprocess_set_machineryc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "qualityprocess_set_machinery",
                    "description": "Indica si se realiza preparación de máquinas y control de tiempo para garantizar la calidad.",
                },
            },
            "qualityprocess_control_quality": {
                "var_pairs": [
                    ("qualityprocess_control_quality", "qualityprocess_control_qualityc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "qualityprocess_control_quality",
                    "description": "Indica si existen controles de calidad para materias primas, producto en proceso y producto terminado.",
                },
            },
            "qualityprocess_none": {
                "var_pairs": [
                    ("qualityprocess_none", "qualityprocess_nonec")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "qualityprocess_none",
                    "description": "Indica si el negocio no aplica ningún proceso específico para garantizar la calidad.",
                },
            },
            "newideas_datasheet": {
                "var_pairs": [
                    # variable renamed between cohorts
                    ("newideas_datasheet", "newideas_designc"),
                    ("newideas_datasheet", "newideas_datasheetc")
                ],
                "type": CATEGORICAL,
                "metadata": {
                    "name": "newideas_datasheet",
                    "description": "Forma de registrar las ideas de nuevos diseños (verbal, muestra física, ficha técnica).",
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
                    "description": "Nivel de desarrollo y personalización del empaque del producto (genérico, estándar, distintivo).",
                    "mapping": CATEGORICAL_MAPPINGS["packaging"],
                },
            },
            "software_design": {
                "var_pairs": [
                    ("software_design", "software_designc")
                ],
                # Can be interpreted as boolean (uses vs not uses) or categorical (type of software) - depnds on cohort / center
                "type": [BOOLEAN, CATEGORICAL],
                "metadata": {
                    "name": "software_design",
                    "description": "Uso de software especializado para el diseño de productos (CAD, 2D, manual).",
                    "mapping": CATEGORICAL_MAPPINGS["software_design"],
                },
            },
            "patterns_digitized": {
                "var_pairs": [
                    ("patterns_digitized", "digital_patternc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "patterns_digitized",
                    "description": "Indica si los patrones de diseño están digitalizados.",
                },
            },
            "patterns_prevcollections": {
                "var_pairs": [
                    ("patterns_prevcollections", "prev_patternc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "patterns_prevcollections",
                    "description": "Indica si el negocio guarda los patrones de colecciones anteriores.",
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
                    "description": "Número de empleados de nómina (con afiliación a salud y pensión).",
                },
            },
            "emp_total": {
                "var_pairs": [
                    ("emp_total", "emp_totalc")
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "emp_total",
                    "description": "Número total de empleados del negocio (suma de todas las modalidades).",
                },
            },
            "hassalary": {
                "var_pairs": [
                    ("hassalary", "hassalaryc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "hassalary",
                    "description": "Indica si el postulante (líder) recibe un sueldo fijo del negocio.",
                },
            },
            "income": {
                "var_pairs": [
                    ("income", "incomec")
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "income",
                    "description": "Monto del sueldo fijo mensual promedio que recibe el postulante (líder).",
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
                    "description": "Método utilizado para la fijación de precios (competencia, costos, margen).",
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
                    "description": "Indica si el negocio conoce el costo unitario de producción.",
                },
            },
            "knows_max_production": {
                "var_pairs": [
                    ("knows_max_production", "knows_max_productionc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_max_production",
                    "description": "Indica si el negocio conoce su capacidad máxima de producción periódica.",
                },
            },
            "knows_profit_margin": {
                "var_pairs": [
                    ("knows_profit_margin", "knows_profit_marginc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_profit_margin",
                    "description": "Indica si el negocio conoce el margen de ganancia por producto/servicio.",
                },
            },
            "knows_sales_frequency": {
                "var_pairs": [
                    ("knows_sales_frequency", "knows_sales_frequencyc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_sales_frequency",
                    "description": "Indica si el negocio conoce la periodicidad de sus ventas.",
                },
            },
            "knows_detailed_income": {
                "var_pairs": [
                    ("knows_detailed_income", "knows_detailed_incomec")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "knows_detailed_income",
                    "description": "Indica si el negocio conoce sus ingresos de forma detallada.",
                },
            },
            "productcost_materials": {
                "var_pairs": [
                    ("productcost_materials", "productcost_materialsc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "productcost_materials",
                    "description": "Indica si se calcula el costo total de materiales directos para el costeo del producto.",
                },
            },
            "productcost_handwork": {
                "var_pairs": [
                    ("productcost_handwork", "productcost_handworkc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "productcost_handwork",
                    "description": "Indica si se calcula el costo total de mano de obra directa para el costeo del producto.",
                },
            },
            "productcost_fabrication": {
                "var_pairs": [
                    ("productcost_fabrication", "productcost_fabricationc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "productcost_fabrication",
                    "description": "Indica si se calculan los gastos generales de fabricación para el costeo del producto.",
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
                    "name": "sales2023q1s_vs_2024q1s",
                    "description": "Comparación de ventas: Enero-Abril 2023 vs Enero-Abril 2024.",
                },
            },
            "sales2023_vs_2024": {
                "var_pairs": [
                    ("sales2023", "sales2024"),
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "sales2023_vs_2024",
                    "description": "Comparación de ventas: 2023 (real/proyectado) vs 2024 (promedio mensual).",
                },
            },
            "salesaverage2024": {
                 "var_pairs": [
                    (None, "salesaverage2024")
                ],
                "type": NUMERIC,
                "metadata": {
                    "name": "salesaverage2024",
                    "description": "Valor promedio mensual de ventas reportado para 2024 (cierre).",
                },
            },
            "participate_commercial": {
                "var_pairs": [
                    (None, "participate_commercial")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "participate_commercial",
                    "description": "Indica si el negocio participó en ruedas comerciales del programa.",
                },
            },
            "connection_commercial": {
                "var_pairs": [
                    (None, "connection_commercial")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "connection_commercial",
                    "description": "Indica si se generaron conexiones comerciales durante las ruedas del programa.",
                },
            },
            "participate_financial": {
                "var_pairs": [
                    (None, "participate_financial")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "participate_financial",
                    "description": "Indica si el negocio participó en ruedas financieras del programa.",
                },
            },
            "connection_financial": {
                "var_pairs": [
                    (None, "connection_financial")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "connection_financial",
                    "description": "Indica si se generaron conexiones financieras durante las ruedas del programa.",
                },
            },
            "banked": {
                "var_pairs": [
                    ("banked", "bankedc")
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "banked",
                    "description": "Indica si el negocio posee una cuenta bancaria.",
                },
            },
            "bookkeeping": {
                "var_pairs": [
                    ("bookkeeping", "bookkeepingc"),
                    ("new_bookkeeping", "new_bookkeepingc")
                ],
                "type": CATEGORICAL,
                "metadata": {
                    "mapping": CATEGORICAL_MAPPINGS["bookkeeping"],
                    "description": "Método utilizado para llevar la contabilidad/cuentas del negocio (manual, Excel, software, etc.).",
                    "name": "bookkeeping",
                },
            },
        },
        "Asociatividad": {
            "knows_associationways": {
                "var_pairs": [
                    ("knows_associationways", "knows_associationwaysc"),
                ],
                "type": BOOLEAN,
                "metadata": {
                    "name": "knows_associationways",
                    "description": "Indica si el líder conoce mecanismos de asociatividad empresarial y cómo formalizarlos.",
                },
            },
            "association_group_training": {
                "var_pairs": [
                    ("association_group_training", "association_group_trainingc"),
                    ("dassociation_group_training", "association_group_trainingc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_group_training",
                    "description": "Indica si se ha asociado para tomar capacitaciones grupales.",
                },
            },
            "association_new_machinery": {
                "var_pairs": [
                    ("association_new_machinery", "association_new_machineryc"),
                    ("dassociation_new_machinery", "association_new_machineryc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_new_machinery",
                    "description": "Indica si se ha asociado para adquirir maquinaria/equipos modernos.",
                },
            },
            "association_buy_supplies": {
                "var_pairs": [
                    ("association_buy_supplies", "association_buy_suppliesc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_buy_supplies",
                    "description": "Indica si se ha asociado para comprar insumos y reducir costos.",
                },
            },
            "association_use_machinery_nobuy": {
                "var_pairs": [
                    ("association_use_machinery_nobuy", "association_use_machinery_nobuyc"),
                    ("dassociation_use_machinery_nobuy", "association_use_machinery_nobuyc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_use_machinery_nobuy",
                    "description": "Indica si se ha asociado para utilizar maquinaria sin comprarla.",
                },
            },
            "association_new_markets": {
                "var_pairs": [
                    ("association_new_markets", "association_new_marketsc"),
                    ("dassociation_new_markets", "association_new_marketsc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_new_markets",
                    "description": "Indica si se ha asociado para acceder a nuevos mercados.",
                },
            },
            "association_distribution": {
                "var_pairs": [
                    ("association_distribution", "association_distributionc"),
                    ("dassociation_distribution", "association_distributionc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_distribution",
                    "description": "Indica si se ha asociado para procesos logísticos y de distribución.",
                },
            },
            "association_have_not": {
                "var_pairs": [
                    ("association_have_not", "association_have_notc"),
                    ("dassociation_have_not", "association_have_notc")
                ],
                "type": DUMMY,
                "metadata": {
                    "name": "association_have_not",
                    "description": "Indica si el negocio no se ha asociado para ninguna actividad colaborativa.",
                },
            },
        },
    }