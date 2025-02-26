import re
from typing import List
import pandas as pd

# Variable type constants
NUMERIC = "numeric"
BOOLEAN = "boolean"
CATEGORICAL = "categorical"
ARRAY = "array"
DUMMY = "dummy"
INDICATOR = "indicator"  # New variable type for efficiency calculations

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
        Dictionary containing the sections configuration
    """
    return {
        "Optimización operativa": [
            # Production efficiency indicator
            [
                (
                    (
                        find_matching_vars("producedunits_{}", df),
                        find_matching_vars("targetunits_{}", df),
                    ),
                    (
                        find_matching_vars("producedunits_{}", df, control_only=True),
                        find_matching_vars("targetunits_{}", df, control_only=True),
                    ),
                ),
                INDICATOR,
                {
                    "name": "production_efficiency",
                    "description": "Eficiencia de producción",
                    "calculation": (
                        "El ratio de eficiencia de producción es el ratio entre el"
                        " número de unidades producidas y el número de unidades objetivo."
                    ),
                },
            ],
            # 2 - Eficiencia
            [
                ("knows_standardtime", "standard_timec"),
                BOOLEAN,
                {
                    "name": "knows_standardtime_old",
                    "description": "Conoce el tiempo estándar de producción",
                },
            ],
            [
                ("knows_standardtime", "knows_standardtimec"),
                BOOLEAN,
                {
                    "name": "knows_standardtime",
                    "description": "Conoce el tiempo estándar de producción",
                },
            ],
            # Unidades Defectuosas
            [
                (
                    (
                        find_matching_vars("defectiveunits_{}", df),
                        find_matching_vars("producedunits_{}", df),
                    ),
                    (
                        find_matching_vars("defectiveunits_{}", df, control_only=True),
                        find_matching_vars("producedunits_{}", df, control_only=True),
                    ),
                ),
                INDICATOR,
                {
                    "name": "defective_units_rate",
                    "description": "Tasa de Unidades defectuosas",
                    "calculation": (
                        "La tasa de unidades defectuosas es el ratio entre el número de "
                        "unidades defectuosas y el número total de unidades producidas."
                    ),
                },
            ],
            # Distribución y espacio
            [
                ("observ_productionplant", "observ_productionplantc"),
                CATEGORICAL,
                {
                    "name": "observ_productionplant",
                    "description": "Estado de la distribución del espacio",
                    "mapping": CATEGORICAL_MAPPINGS["observ_productionplant"],
                },
            ],
            # Control de inventario
            [
                ("invent_control", "invent_controlc"),
                CATEGORICAL,
                {
                    "name": "invent_control",
                    "description": "Realiza control de inventario",
                    "mapping": CATEGORICAL_MAPPINGS["invent_control"],
                },
            ],
            [
                ("knowsinput", "knowsinputc"),
                BOOLEAN,
                {
                    "name": "knowsinput",
                    "description": "Conoce niveles óptimos de inventario",
                },
            ],
            # Indicadores
            [
                ("indicadores_eficiencia", "indicadores_eficienciac"),
                DUMMY,
                {
                    "name": "indicadores_eficiencia",
                    "description": "Tiene indicadores de eficiencia",
                },
            ],
            [
                ("indicadores_productividad", "indicadores_productividadc"),
                DUMMY,
                {
                    "name": "indicadores_productividad",
                    "description": "Tiene indicadores de productividad",
                },
            ],
            [
                ("index", "hasindicatorsc"),
                BOOLEAN,
                {"name": "index", "description": "Tiene indicadores generales"},
            ],
        ],
        "Mayor Calidad del Producto": [
            # Quality processes
            [
                ("qualityprocess_sample", "qualityprocess_samplec"),
                DUMMY,
                {
                    "name": "qualityprocess_sample",
                    "description": "Para garantizar la calidad de los productos: Realiza muestra y contramuestra",
                },
            ],
            [
                ("qualityprocess_set_machinery", "qualityprocess_set_machineryc"),
                DUMMY,
                {
                    "name": "qualityprocess_set_machinery",
                    "description": "Para garantizar la calidad de los productos: Realiza preparación de máquinas",
                },
            ],
            [
                ("qualityprocess_control_quality", "qualityprocess_control_qualityc"),
                DUMMY,
                {
                    "name": "qualityprocess_control_quality",
                    "description": "Para garantizar la calidad de los productos: Tiene controles de calidad",
                },
            ],
            [
                ("qualityprocess_none", "qualityprocess_nonec"),
                DUMMY,
                {
                    "name": "qualityprocess_none",
                    "description": "Para garantizar la calidad de los productos: No tiene procesos de calidad",
                },
            ],
            # Design and documentation
            [
                ("newideas_datasheet", "newideas_designc"),
                CATEGORICAL,
                {
                    "name": "newideas_datasheet",
                    "description": "Las ideas de los nuevos diseños se registran en una ficha técnica",
                    "mapping": CATEGORICAL_MAPPINGS["newideas_datasheet"],
                },
            ],
            # Packaging and presentation
            [
                ("packaging", "packagingc"),
                CATEGORICAL,
                {
                    "name": "packaging",
                    "description": "Cómo funciona en general el empaque en el negocio",
                    "mapping": CATEGORICAL_MAPPINGS["packaging"],
                },
            ],
            # Design tools and patterns
            [
                ("software_design", "software_designc"),
                BOOLEAN,
                {
                    "name": "software_design",
                    "description": "El negocio utiliza algún software especializado para el diseño de sus productos",
                },
            ],
            [
                ("patterns_digitized", "digital_patternc"),
                BOOLEAN,
                {
                    "name": "patterns_digitized",
                    "description": "Los patrones están digitalizados",
                },
            ],
            [
                ("patterns_prevcollections", "prev_patternc"),
                BOOLEAN,
                {
                    "name": "patterns_prevcollections",
                    "description": "El negocio usualmente guarda los patrones de colecciones anteriores",
                },
            ],
        ],
        "Talento Humano": [
            # Employment metrics
            [
                ("emp_ft", "emp_ftc"),
                NUMERIC,
                {
                    "name": "emp_ft",
                    "description": "Empleados de nómina (afiliados por el negocio al sistema de salud y pensión)",
                },
            ],
            [
                ("emp_total", "emp_totalc"),
                NUMERIC,
                {"name": "emp_total", "description": "Empleados totales"},
            ],
            # Salary information
            [
                ("hassalary", "hassalaryc"),
                BOOLEAN,
                {
                    "name": "hassalary",
                    "description": "Postulante recibe sueldo fijo del negocio",
                },
            ],
            [
                ("income", "incomec"),
                NUMERIC,
                {
                    "name": "income",
                    "description": "Cuánto recibe de sueldo fijo en un mes promedio",
                },
            ],
        ],
        "Practicas Gerenciales": [
            # Pricing and costs
            [
                ("price_system", "price_systemc"),
                CATEGORICAL,
                {
                    "name": "price_system",
                    "description": "Los precios se fijan con base en",
                    "mapping": CATEGORICAL_MAPPINGS["price_system"],
                },
            ],
            # Knowledge indicators
            [
                ("knows_production_cost", "knows_production_costc"),
                DUMMY,
                {
                    "name": "knows_production_cost",
                    "description": "En el negocio conoce: El costo de producir cada unidad de producto o servicio",
                },
            ],
            [
                ("knows_max_production", "knows_max_productionc"),
                DUMMY,
                {
                    "name": "knows_max_production",
                    "description": "En el negocio conoce: Cantidad máxima de productos que puedes generar u ofrecer en un periodo determinado (por ejemplo: diaria, semanal, mensual)",
                },
            ],
            [
                ("knows_profit_margin", "knows_profit_marginc"),
                DUMMY,
                {
                    "name": "knows_profit_margin",
                    "description": "En el negocio conoce: Porcentaje o margen de ganancia de cada producto o servicio",
                },
            ],
            [
                ("knows_sales_frequency", "knows_sales_frequencyc"),
                DUMMY,
                {
                    "name": "knows_sales_frequency",
                    "description": "En el negocio conoce: Periodicidad de las ventas de tus productos o servicios (ej.: diaria, semanal, mensual)",
                },
            ],
            [
                ("knows_detailed_income", "knows_detailed_incomec"),
                DUMMY,
                {
                    "name": "knows_detailed_income",
                    "description": "En el negocio conoce: Ingresos del negocio de manera detallada",
                },
            ],
            # Cost tracking
            [
                ("productcost_materials", "productcost_materialsc"),
                DUMMY,
                {
                    "name": "productcost_materials",
                    "description": "Para costo de producto se calcula: Costo total materiales directos",
                },
            ],
            [
                ("productcost_handwork", "productcost_handworkc"),
                DUMMY,
                {
                    "name": "productcost_handwork",
                    "description": "Para costo de producto se calcula: Costo total mano de obra directa",
                },
            ],
            [
                ("productcost_fabrication", "productcost_fabricationc"),
                DUMMY,
                {
                    "name": "productcost_fabrication",
                    "description": "Para costo de producto se calcula: Gastos generales de fabricación",
                },
            ],
        ],
        "Financiero": [
            # Sales metrics
            [
                ("sales2023q1s", "sales2024q1s"),
                NUMERIC,
                {
                    "name": "sales2023q1s",
                    "description": "Ventas trimestrales, 2023T1-vs-2024T1",
                },
            ],
            [
                (None, "salesaverage2024"),
                NUMERIC,
                {
                    "name": "salesaverage2024",
                    "description": "Valor promedio mensual de las ventas del 2024",
                },
            ],
            # Financial connections
            [
                (None, "participate_commercial"),
                BOOLEAN,
                {
                    "name": "participate_commercial",
                    "description": "Participó en alguna rueda comercial del programa",
                },
            ],
            [
                (None, "connection_commercial"),
                BOOLEAN,
                {
                    "name": "connection_commercial",
                    "description": "Generó conexiones durante el desarrollo de la rueda comercial",
                },
            ],
            [
                (None, "participate_financial"),
                BOOLEAN,
                {
                    "name": "participate_financial",
                    "description": "Participó en alguna rueda financiera del programa",
                },
            ],
            [
                (None, "connection_financial"),
                BOOLEAN,
                {
                    "name": "connection_financial",
                    "description": "Generó conexiones durante el desarrollo de la rueda financiera",
                },
            ],
            # Banking and bookkeeping
            [
                ("banked", "bankedc"),
                BOOLEAN,
                {"name": "banked", "description": "Tiene cuenta bancaria"},
            ],
            [
                ("bookkeeping", "bookkeepingc"),
                CATEGORICAL,
                {
                    "mapping": CATEGORICAL_MAPPINGS["bookkeeping"],
                    "description": "Forma de llevar las cuentas del negocio",
                    "name": "bookkeeping",
                },
            ],
        ],
        "Asociatividad": [
            [
                ("knows_associationways", "knows_associationwaysc"),
                BOOLEAN,
                {
                    "name": "knows_associationways",
                    "description": "El líder del negocio conoce cómo establecer y formalizar los diferentes mecanismos de asociatividad empresarial",
                },
            ],
            [
                ("association_group_training", "association_group_trainingc"),
                DUMMY,
                {
                    "name": "association_group_training",
                    "description": "Se ha asociado para realizar: Sí, para tomar capacitaciones grupales",
                },
            ],
            [
                ("association_new_machinery", "association_new_machineryc"),
                DUMMY,
                {
                    "name": "association_new_machinery",
                    "description": "Se ha asociado para realizar: Sí, para adquirir maquinaria y equipos modernos",
                },
            ],
            [
                ("association_buy_supplies", "association_buy_suppliesc"),
                DUMMY,
                {
                    "name": "association_buy_supplies",
                    "description": "Se ha asociado para realizar: Sí, para comprar insumos y así reducir costos",
                },
            ],
            [
                ("association_use_machinery_nobuy", "association_use_machinery_nobuyc"),
                DUMMY,
                {
                    "name": "association_use_machinery_nobuy",
                    "description": "Se ha asociado para realizar: Sí, para utilizar maquinaria sin tener que comprarla",
                },
            ],
            [
                ("association_new_markets", "association_new_marketsc"),
                DUMMY,
                {
                    "name": "association_new_markets",
                    "description": "Se ha asociado para realizar: Sí, para acceder a nuevos mercados",
                },
            ],
            [
                ("association_distribution", "association_distributionc"),
                DUMMY,
                {
                    "name": "association_distribution",
                    "description": "Se ha asociado para realizar: Sí, para procesos logísticos y de distribución",
                },
            ],
            [
                ("association_have_not", "association_have_notc"),
                DUMMY,
                {
                    "name": "association_have_not",
                    "description": "Se ha asociado para realizar: No me he asociado",
                },
            ],
        ],
    }
