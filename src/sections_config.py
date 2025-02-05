from typing import List

# Variable type constants
NUMERIC = "numeric"
BOOLEAN = "boolean"
CATEGORICAL = "categorical"
ARRAY = "array"
DUMMY = "dummy"

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

def generate_prevmonth_vars(base_name: str, num_months: int = 4) -> List[str]:
    """Generate list of prevmonth variables."""
    return [f"{base_name}{i}" for i in range(1, num_months + 1)]

sections_config = {
    "Optimización operativa": [
        # Producción y metas (usando varias pre-variables)
        [
            (generate_prevmonth_vars("producedunits_prevmonth", 4), "producedunits_prevmonthc"),
            NUMERIC,
            {"description": "Número de unidades producidas por mes"},
        ],
        [
            (generate_prevmonth_vars("targetunits_prevmonth", 4), "targetunits_prevmonthc"),
            NUMERIC,
            {"description": "Meta de producción mensual"},
        ],
        [
            (generate_prevmonth_vars("defectiveunits_prevmonth", 4), "defectiveunits_prevmonthc"),
            NUMERIC,
            {"description": "Unidades defectuosas por mes"},
        ],
        [
            (generate_prevmonth_vars("estimated_prod_time", 4), "estimated_prod_timec"),
            NUMERIC,
            {"description": "Tiempo estimado de producción"},
        ],
        [
            (generate_prevmonth_vars("actual_avg_prod_time", 4), "actual_avg_prod_timec"),
            NUMERIC,
            {"description": "Tiempo real promedio de producción"},
        ],
        # Distribución y espacio
        [
            ("observ_productionplant", "observ_productionplantc"),
            CATEGORICAL,
            {
                "description": "Estado de la distribución del espacio",
                "mapping": CATEGORICAL_MAPPINGS["observ_productionplant"]
            },
        ],
        # Control de inventario
        [
            ("invent_control", "invent_controlc"),
            CATEGORICAL,
            {
                "description": "Realiza control de inventario",
                "mapping": CATEGORICAL_MAPPINGS["invent_control"]
            },
        ],
        [
            ("knowsinput", "knowsinputc"),
            BOOLEAN,
            {"description": "Conoce niveles óptimos de inventario"},
        ],
        # Eficiencia
        [
            ("knows_standardtime", "standard_timec"),
            BOOLEAN,
            {"description": "Conoce el tiempo estándar de producción"},
        ],
        # Indicadores
        [
            ("indicadores_eficiencia", "indicadores_eficienciac"),
            DUMMY,
            {"description": "Tiene indicadores de eficiencia"},
        ],
        [
            ("indicadores_productividad", "indicadores_productividadc"),
            DUMMY,
            {"description": "Tiene indicadores de productividad"},
        ],
        [
            ("index", "hasindicatorsc"),
            BOOLEAN,
            {"description": "Tiene indicadores generales"},
        ],
    ],
    "Mayor Calidad del Producto": [
        # Quality processes
        [
            ("qualityprocess_sample", "qualityprocess_samplec"),
            DUMMY,
            {"description": "Para garantizar la calidad de los productos: Realiza muestra y contramuestra"},
        ],
        [
            ("qualityprocess_set_machinery", "qualityprocess_set_machineryc"),
            DUMMY,
            {"description": "Para garantizar la calidad de los productos: Realiza preparación de máquinas"},
        ],
        [
            ("qualityprocess_control_quality", "qualityprocess_control_qualityc"),
            DUMMY,
            {"description": "Para garantizar la calidad de los productos: Tiene controles de calidad"},
        ],
        [
            ("qualityprocess_none", "qualityprocess_nonec"),
            DUMMY,
            {"description": "Para garantizar la calidad de los productos: No tiene procesos de calidad"},
        ],
        # [
        #     ("qualityprocess_other", "qualityprocess_otherc"),
        #     DUMMY,
        #     {"description": "Para garantizar la calidad de los productos: Tiene otros procesos de calidad"},
        # ],
        # Design and documentation
        [
            ("newideas_datasheet", "newideas_designc"),
            CATEGORICAL,
            {
                "description": "Las ideas de los nuevos diseños se registran en una ficha técnica",
                "mapping": CATEGORICAL_MAPPINGS["newideas_datasheet"]
            },
        ],
        # Packaging and presentation
        [
            ("packaging", "packagingc"),
            CATEGORICAL,
            {
                "description": "Cómo funciona en general el empaque en el negocio",
                "mapping": CATEGORICAL_MAPPINGS["packaging"]
            },
        ],
        # Design tools and patterns
        [
            ("software_design", "software_designc"),
            BOOLEAN,
            {"description": "El negocio utiliza algún software especializado para el diseño de sus productos"},
        ],
        [
            ("patterns_digitized", "digital_patternc"),
            BOOLEAN,
            {"description": "Los patrones están digitalizados"},
        ],
        [
            ("patterns_prevcollections", "prev_patternc"),
            BOOLEAN,
            {"description": "El negocio usualmente guarda los patrones de colecciones anteriores"},
        ],
    ],
    "Talento Humano": [
        # Employment metrics
        [
            ("emp_ft", "emp_ftc"),
            NUMERIC,
            {"description": "Empleados de nómina (afiliados por el negocio al sistema de salud y pensión)"},
        ],
        [
            ("emp_total", "emp_totalc"),
            NUMERIC,
            {"description": "Empleados totales"},
        ],
        
        # Salary information
        [
            ("hassalary", "hassalaryc"),
            BOOLEAN,
            {"description": "Postulante recibe sueldo fijo del negocio"},
        ],
        [
            ("income", "incomec"),
            NUMERIC,
            {"description": "Cuánto recibe de sueldo fijo en un mes promedio"},
        ],
    ],
    "Practicas Gerenciales": [
        # Pricing and costs
        [
            ("price_system", "price_systemc"),
            CATEGORICAL,
            {
                "description": "Los precios se fijan con base en",
                "mapping": CATEGORICAL_MAPPINGS["price_system"]
            },
        ],
        
        # Knowledge indicators
        [
            ("knows_production_cost", "knows_production_costc"),
            DUMMY,
            {"description": "En el negocio conoce: El costo de producir cada unidad de producto o servicio"},
        ],
        [
            ("knows_max_production", "knows_max_productionc"),
            DUMMY,
            {"description": "En el negocio conoce: Cantidad máxima de productos que puedes generar u ofrecer en un periodo determinado (por ejemplo: diaria, semanal, mensual)"},
        ],
        [
            ("knows_profit_margin", "knows_profit_marginc"),
            DUMMY,
            {"description": "En el negocio conoce: Porcentaje o margen de ganancia de cada producto o servicio"},
        ],
        [
            ("knows_sales_frequency", "knows_sales_frequencyc"),
            DUMMY,
            {"description": "En el negocio conoce: Periodicidad de las ventas de tus productos o servicios (ej.: diaria, semanal, mensual)"},
        ],
        [
            ("knows_detailed_income", "knows_detailed_incomec"),
            DUMMY,
            {"description": "En el negocio conoce: Ingresos del negocio de manera detallada"},
        ],
        # [
        #     ("knows_none", "knows_nonec"),
        #     DUMMY,
        #     {"description": "En el negocio conoce: No conoce ninguno de los anteriores"},
        # ],
        
        # Cost tracking
        [
            ("productcost_materials", "productcost_materialsc"),
            DUMMY,
            {"description": "Para costo de producto se calcula: Costo total materiales directos"},
        ],
        [
            ("productcost_handwork", "productcost_handworkc"),
            DUMMY,
            {"description": "Para costo de producto se calcula: Costo total mano de obra directa"},
        ],
        [
            ("productcost_fabrication", "productcost_fabricationc"),
            DUMMY,
            {"description": "Para costo de producto se calcula: Gastos generales de fabricación"},
        ],
        # [
        #     ("productcost_other", "productcost_otherc"),
        #     DUMMY,
        #     {"description": "Para costo de producto se calcula: Otros."},
        # ],
    ],
    "Financiero": [
        # Sales metrics
        [
            ("sales2023q1s", "sales2024q1s"),
            NUMERIC,
            {"description": "Ventas trimestrales, 2023T1-vs-2024T1"},
        ],
        [
            (None, "salesaverage2024"),
            NUMERIC,
            {"description": "Valor promedio mensual de las ventas del 2024"},
        ],
        
        # Financial connections
        [
            (None, "participate_commercial"),
            BOOLEAN,
            {"description": "Participó en alguna rueda comercial del programa"},
        ],
        [
            (None, "connection_commercial"),
            BOOLEAN,
            {"description": "Generó conexiones durante el desarrollo de la rueda comercial"},
        ],
        [
            (None, "participate_financial"),
            BOOLEAN,
            {"description": "Participó en alguna rueda financiera del programa"},
        ],
        [
            (None, "connection_financial"),
            BOOLEAN,
            {"description": "Generó conexiones durante el desarrollo de la rueda financiera"},
        ],
        
        # Banking and bookkeeping
        [
            ("banked", "bankedc"),
            BOOLEAN,
            {"description": "Tiene cuenta bancaria"},
        ],
        [
            ("bookkeeping", "bookkeepingc"),
            CATEGORICAL,
            {
                "mapping": CATEGORICAL_MAPPINGS["bookkeeping"],
                "description": "Forma de llevar las cuentas del negocio"
            },
        ],
    ],
    "Asociatividad": [
        [
            ("knows_associationways", "knows_associationwaysc"),
            BOOLEAN,
            {"description": "El líder del negocio conoce cómo establecer y formalizar los diferentes mecanismos de asociatividad empresarial"},
        ],
        [
            ("association_group_training", "association_group_trainingc"),
            DUMMY,
            {"description": "Se ha asociado para realizar: Sí, para tomar capacitaciones grupales"},
        ],
        [
            ("association_new_machinery", "association_new_machineryc"),
            DUMMY,
            {"description": "Se ha asociado para realizar: Sí, para adquirir maquinaria y equipos modernos"},
        ],
        [
            ("association_buy_supplies", "association_buy_suppliesc"),
            DUMMY,
            {"description": "Se ha asociado para realizar: Sí, para comprar insumos y así reducir costos"},
        ],
        [
            ("association_use_machinery_nobuy", "association_use_machinery_nobuyc"),
            DUMMY,
            {"description": "Se ha asociado para realizar: Sí, para utilizar maquinaria sin tener que comprarla"},
        ],
        [
            ("association_new_markets", "association_new_marketsc"),
            DUMMY,
            {"description": "Se ha asociado para realizar: Sí, para acceder a nuevos mercados"},
        ],
        [
            ("association_distribution", "association_distributionc"),
            DUMMY,
            {"description": "Se ha asociado para realizar: Sí, para procesos logísticos y de distribución"},
        ],
        [
            ("association_have_not", "association_have_notc"),
            DUMMY,
            {"description": "Se ha asociado para realizar: No me he asociado"},
        ],
    ],
}
