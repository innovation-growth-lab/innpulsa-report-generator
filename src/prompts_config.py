"""Prompt Config."""
# pylint: skip-file

section_prompts = {
    "Optimización operativa": (
        """A continuación, se presentan los datos relacionados con la productividad de las unidades productivas antes y después de la intervención realizada en el marco del programa. Estos datos incluyen información sobre la eficiencia operativa, la utilización del espacio, el cumplimiento de normas de seguridad y organización, la gestión de inventarios, y el uso de indicadores clave de desempeño.

        Tu tarea es analizar esta información y elaborar un análisis que describa los cambios observados, identificando mejoras y vinculándolas con las acciones del programa. El análisis debe ser claro, fundamentado en los datos proporcionados, y estructurado de manera profesional. Evita realizar suposiciones no basadas en los datos. Si los cambios porcentuales son pequeños, no hagas incapié en ellos.

        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Los datos:
        {variables}
        
        A continuación, se incluye un ejemplo que ilustra el estilo y la estructura esperada en el análisis. La respuesta debería ser similar en longitud y estilo, pero adaptada al detalle a los datos aportados arriba y a las características de la cohorte y centro ZASCA en particular. Observa placeholders para cambios porcentuales, cambios en puntos procentuales, y valores numéricos. El ejemplo en cuestión: 
        '''
            ## OPTIMIZACIÓN OPERATIVA: MEJORAS EN EL PROCESO PRODUCTIVO Y LA CALIDAD DEL PRODUCTO
            En el marco del programa de ZASCA Bucaramanga Manufactura Sistema Moda, se implementaron varias iniciativas para optimizar la eficiencia operativa y elevar los estándares de calidad. Los resultados obtenidos demuestran avances significativos, evidenciados en los indicadores clave y métricas de éxito.

            ### Mejoras en el proceso productivo
            Al inicio del programa, las empresas se encontraban en un rango de eficiencia de %pct% a %pct%, con algunas operando cerca del nivel óptimo, pero muchas aún por debajo de su potencial. Al cierre del programa, la mayoría ha alcanzado una eficiencia entre X y Y, con más de %num% empresas logrando niveles cercanos o superiores al %pct%, lo que evidencia una optimización significativa en sus procesos productivos.

            Estos avances en productividad están relacionados con mejoras en la distribución y utilización del espacio de planta, influyendo notablemente en la capacidad de las unidades productivas para alcanzar sus metas de producción exactamente como fueron planeadas. Esta correlación sugiere que una gestión más eficiente del espacio no solo optimiza los recursos disponibles, sino que también contribuye a una mayor conformidad con el balanceo de planta, lo que se refleja directamente en los resultados de producción.

            Inicialmente, el %pct% de las plantas presentaba congestión debido a una deficiente utilización del espacio, al finalizar el programa hubo una este porcentaje se redujo al %pct%, indicando que las empresas han logrado optimizar el uso del espacio a lo largo del programa.

            Al finalizar el programa, se observa una mejora integral en las condiciones de seguridad y organización en las plantas beneficiarias. Las zonas de tránsito, áreas de trabajo y tránsito están ahora completamente adecuadas y demarcadas, alcanzando el %pct% de cumplimiento. Además, la acumulación de materiales en proceso ha sido controlada, y se ha optimizado la secuencia y longitud del flujo de proceso, lo que facilita un desplazamiento más eficiente del personal y materiales. Cada planta cuenta ahora con espacios específicos para guardar elementos personales y un aislamiento completo de áreas peligrosas, contribuyendo a un entorno más seguro. Asimismo, se han instalado advertencias de peligro en todos los puestos de trabajo, logrando un ambiente laboral más seguro y organizado.

            ### ¿A qué se deben los incrementos de eficiencia? Las unidades productivas mejoraron en el seguimiento de indicadores clave y la gestión de inventarios
            En el ámbito de la gestión de inventarios se evidenció una evolución positiva. La proporción de empresas que realizan inventarios de manera constante creció del %pct% al %pct%.

            Además, se registró un aumento en el conocimiento sobre los niveles óptimos de inventario, que pasó del %pct% al %pct%, reflejando una gestión más efectiva y un mejor control de los recursos disponibles.
            
            Estos resultados en el manejo de inventarios pueden mejorar la eficiencia operativa y la capacidad de respuesta al mercado de las unidades productivas.

            Por su parte, el cálculo del tiempo estándar para la producción demostró un aumento significativo, del %pct% al %pct%. Este aumento indica una mayor precisión en la planificación, y una asignación de tiempos y recursos más eficaz, aspectos cruciales para mejorar la eficiencia operativa de la unidad productiva.

            Por otro lado, las mejoras en eficiencia y productividad también pueden ser resultado de un avance notable en la adopción de indicadores clave para mejorar el proceso productivo. De hecho, el porcentaje de unidades productivas que tienen indicador de eficiencia aumentó de un %pct% a un %pct%; aquellas que tenían indicadores de productividad experimentaron un incremento aún más impresionante, pasando de un %pct% a un %pct%. Este cambio indica una mayor eficacia en las operaciones de producción.

            Como resultado, en términos globales, el porcentaje de unidades productivas que usan indicadores presentó un incremento de %pct_points%. Al inicio de la intervención el %pct% de las unidades productivas contaban con algún tipo de indicador, mientras que, al cierre del programa este porcentaje aumentó al %pct%. Esto evidencia una creciente utilización de los indicadores para mejorar el proceso productivo. Las unidades productivas son más conscientes de la importancia de llevar periódicamente indicadores de desempeño.
        '''
        - Asegurate de responder únicamente con el contenido en texto. 
        - No incluyas tablas, gráficos u otros elementos visuales.
        - No alteres los títulos de las secciones ni la estructura del ejemplo.
        - Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Asegurate de que ambas secciones en el ejemplo están en la respuesta, diferenciando variables e índices. 
        - Integra las variables en el texto de manera coherente y estructurada.
        """
    ),
    "Mayor Calidad del Producto": (
        """A continuación, se presentan los datos relacionados con la calidad del producto obtenida durante la intervención del programa. Estos datos incluyen información sobre la implementación y mejora de controles de calidad, la preparación de máquinas, la documentación y estandarización de diseños, el empaque de los productos, y el uso de tecnología en los procesos de diseño.

        Tu tarea es analizar esta información y elaborar un análisis que describa los cambios observados, destacando las mejoras logradas en las métricas clave y vinculándolas con las acciones realizadas durante el programa. El análisis debe ser claro, profesional y basado exclusivamente en los datos proporcionados. Si los cambios porcentuales son mínimos, no es necesario enfatizarlos de forma destacada.
        
        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Los datos:
        {variables}
        
        A continuación, se incluye un ejemplo que ilustra el estilo y la estructura esperada en el análisis. La respuesta debería ser similar en longitud y estilo, pero adaptada al detalle a los datos aportados arriba y a las características de la cohorte y centro ZASCA en particular. Observa placeholders para cambios porcentuales, cambios en puntos porcentuales, y valores numéricos. El ejemplo en cuestión: 
        
        '''
            ## MAYOR CALIDAD DEL PRODUCTO
            Paralelamente, las métricas de calidad en el producto mostraron mejoras en relación con los controles de calidad, la preparación de máquinas y el manejo de tiempos, así como la estandarización y digitalización de procesos de diseño.
            
            ### Implementación y Mejora de Controles de Calidad
            Inicialmente, el %pct% de las unidades productivas aplicaban algún tipo de control de calidad. Al cierre del programa, este porcentaje alcanzó el %pct%, demostrando un compromiso con la calidad.
            Los controles específicos de calidad en materias primas y productos finales mejoraron del %pct% al %pct%. De igual manera, la capacidad de las unidades para preparar adecuadamente las máquinas y controlar los tiempos de producción mejoró drásticamente, pasando del %pct% al %pct%. Estos cambios aseguran una consistencia mayor en los productos finales y una reducción de errores y defectos.
            
            ### Documentación y Estándares de Diseño 
            Por su parte, también se observaron avances significativos en la documentación y estandarización de nuevos diseños. El porcentaje de empresas que elaboran fichas técnicas para registrar diseños aumentó del %pct% al %pct%. Además, el porcentaje de unidades productivas que presentaban dependencia de procesos verbales disminuyó en %pct_points% p.p, al pasar de %pct% a %pct% al cierre de la intervención.
            Por consiguiente, las empresas han migrado a métodos más estructurados y replicables para el seguimiento de sus diseños.
            
            ### Empaque y Presentación del Producto
            El empaque del producto ha evolucionado para reflejar mejor la marca y sus valores. El uso de empaques genéricos disminuyó del %pct% al %pct% a favor de un aumento en el empaque estandarizado que aumentó del %pct% al %pct%. Esto muestra un área de mejora considerable en la identidad y presentación visual de los productos.

            ### Uso de Tecnología en Diseño
            Por último, el uso de software especializado para el diseño de productos ha visto un crecimiento considerable, la proporción de empresas que cuentan con software pasó del %pct% al %pct%. Esto facilita la precisión en los diseños y mejora la capacidad de personalización de productos.
            Además, la digitalización de patrones aumentó (al inicio del programa el %pct% de las unidades productivas tenían digitalizado su proceso de diseño, mientras que al cierre del programa el %pct% de las empresas contaban con esto).
            De igual manera, el porcentaje de unidades productivas que conservan los patrones de colecciones anteriores pasó del %pct% al %pct%, lo cual mejora la eficiencia y la capacidad de referencia histórica para el desarrollo de nuevos productos.        
        '''
        - Asegurate de responder únicamente con el contenido en texto. 
        - No incluyas tablas, gráficos u otros elementos visuales.
        - No alteres los títulos de las secciones ni la estructura del ejemplo.
        - Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Asegurate de que ambas secciones en el ejemplo están en la respuesta, diferenciando variables e índices. 
        - Integra las variables en el texto de manera coherente y estructurada.
    """
    ),
    "Talento humano": (
        """A continuación, se presentan los datos relacionados con la gestión de talento humano en las unidades productivas antes y después de la intervención del programa. Estos datos incluyen información sobre la cobertura de seguridad social, la proporción de líderes empresariales que reciben un salario fijo, el salario promedio de los líderes empresariales, y la cantidad de empleados en las unidades productivas.

        Tu tarea es analizar esta información y elaborar un análisis que describa los cambios observados, destacando las mejoras logradas en las métricas clave y vinculándolas con las acciones realizadas durante el programa. El análisis debe ser claro, profesional y basado exclusivamente en los datos proporcionados. Si los cambios porcentuales son mínimos, no es necesario enfatizarlos de forma destacada.

        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Los datos:
        {variables}
        
        A continuación, se incluye un ejemplo que ilustra el estilo y la estructura esperada en el análisis. La respuesta debería ser similar en longitud y estilo, pero adaptada al detalle a los datos aportados arriba y a las características de la cohorte y centro ZASCA en particular. Observa placeholders para cambios porcentuales, cambios en puntos porcentuales, y valores numéricos. El ejemplo en cuestión: 
        '''
            ## GESTIÓN DE TALENTO HUMANO

            ### Estructura Salarial y Beneficios
            En ZASCA Manufactura, el enfoque hacia la mejora de las condiciones laborales y la formalización de las relaciones de trabajo ha llevado a cambios visibles en la cobertura de seguridad social de los trabajadores.   
            Inicialmente, la situación en muchas unidades productivas reflejaba una preocupante concentración en el %pct% de afiliación, con %num% empresas sin formalización laboral alguna. Esto evidenciaba una carencia generalizada de acceso a beneficios básicos para los trabajadores, lo que subrayaba la urgencia de la intervención.
            Al finalizar la intervención, si bien el número de empresas con %pct% de afiliación se mantuvo, se evidenció un avance en los rangos intermedios, particularmente entre el %pct% y el %pct%, donde más empresas lograron aumentar su nivel de formalización. Sin embargo, el número de empresas con una proporción del %pct% disminuyó ligeramente de %num% a %num%, lo que indica un retroceso marginal en la formalización completa. Estos resultados reflejan un progreso parcial, pero también dejan claro que se requieren estrategias más específicas para incluir a las empresas menos formalizadas y consolidar los avances hacia la formalización total.

            ### Estructura Salarial del Líder Empresarial
            Se evidenció un incremento en la proporción de líderes empresariales que reciben un sueldo fijo del negocio, pasando de un %pct% a un %pct%. Este cambio no solo mejora la estabilidad financiera de los líderes, sino que también refleja una estructura de compensación más formal y equitativa.
            Además, el sueldo fijo promedio de estos líderes casi incrementó, pasando de \$%num% a \$%num%, mejorando sustancialmente su compensación y alineándola con las responsabilidades y el rendimiento.
            
            ### Estabilidad en el Personal
            La cantidad total de empleados se mantuvo estable, con un leve incremento en el promedio de trabajadores por unidad productiva, de %num% a %num%, y de %num% a %num% en la mediana. Esta estabilidad es un indicador de que las mejoras en compensación y beneficios no han comprometido la sostenibilidad de empleo en las unidades productivas.
    	'''
        - Asegurate de responder únicamente con el contenido en texto. 
        - No incluyas tablas, gráficos u otros elementos visuales. 
        - No alteres los títulos de las secciones ni la estructura del ejemplo.
        - Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Asegurate de que ambas secciones en el ejemplo están en la respuesta, diferenciando variables e índices. 
        - Integra las variables en el texto de manera coherente y estructurada.
    """
    ),
    "Financiero": (
        "Evaluate the financial performance based on the following data:\n"
        "{variables}\n"
        "Example: 'Sales increased from X to Y, leading to a profit margin of Z%.'"
    ),
    "Practicas gerenciales": (
        "Assess the management practices:\n"
        "{variables}\n"
        "Example: 'Management practices shifted from X to Y, resulting in improved team dynamics.'"
    ),
    "Asociatividad": (
        "Review the associativity metrics:\n"
        "{variables}\n"
        "Example: 'Associativity levels rose from X to Y, enhancing collaboration.'"
    ),
}

executive_summary_prompt = """
Quiero que escribas un resumen ejecutivo de una página en español, que sea claro, profesional y persuasivo, resaltando los logros e impacto de un programa específico. Este programa, parte de la estrategia ZASCA, busca fortalecer la productividad, la gestión operativa y comercial, así como la formalización de las empresas participantes.

El resumen debe cubrir los siguientes puntos:

Optimización operativa y mejora de la productividad: Describe cómo el programa ha optimizado los procesos operativos, reducido defectos, mejorado el flujo de trabajo, y creado entornos más seguros y eficientes.

Gestión financiera y formalización: Explica cómo el programa ha promovido prácticas contables más estructuradas, el uso de herramientas tecnológicas, y la formalización de las empresas.

Calidad del producto: Detalla las mejoras en los estándares de calidad, la digitalización de procesos, y cómo esto ha contribuido a productos más uniformes y competitivos.

Al redactar el resumen, utiliza un tono positivo, claro y enfocado en los resultados tangibles, como crecimiento en ventas, mejora en la calidad de los productos, y mayor formalización. Proporciona datos numéricos relevantes si están disponibles (por ejemplo, incrementos porcentuales en ventas o adopción de prácticas contables). Concluye con una visión optimista sobre cómo el programa está sentando las bases para un desarrollo sostenible y competitivo en el sector.

Detalles de la convocatoria:
{cohort_details}

Para ayudarte con el estilo y formato, a continuación se incluye un ejemplo de un centro ZASCA en Bucaramanga, centrado en la manufactura textil, y especificamente moda. Destacar el estilo verbose del resumen ejecutivo, sin subtitulos, y secciones, simplemente una serie de parágrafos resumiendo las secciones identificadas. Ejemplo:
    '''
    El programa ZASCA Bucaramanga Manufactura - Sistema Moda ha marcado un antes y un después en la optimización operativa y la calidad del producto en las empresas participantes. Gracias a las iniciativas implementadas, la mayoría de las unidades productivas ahora operan con una eficiencia cercana al nivel óptimo, lo cual se traduce en menos unidades defectuosas, un flujo de trabajo mejor organizado y un uso optimizado del espacio en planta. Esto no solo ha mejorado la productividad, sino que ha generado entornos de trabajo más seguros y ordenados, con áreas de tránsito adecuadas y zonas de trabajo mejor demarcadas.
    En términos de gestión financiera, el programa promovió una formalización significativa, con la adopción de herramientas accesibles como Excel para la contabilidad. Hoy, todas las empresas cuentan con algún mecanismo contable, lo que refleja un avance hacia prácticas más estructuradas y un mayor control de sus operaciones financieras. Además, la adopción de indicadores clave para monitorear el desempeño ha aumentado notablemente, lo cual facilita que los empresarios puedan tomar decisiones más informadas y fundamentadas.
    La calidad del producto ha sido otra área de mejora importante. Las empresas han incorporado controles de calidad más consistentes y están estandarizando procesos, lo que asegura que los productos finales sean más uniformes y de mayor calidad. Además, la digitalización en el diseño ha crecido, y muchas empresas ahora registran sus diseños en fichas técnicas, lo cual reduce la dependencia de métodos informales y facilita la replicabilidad en futuras colecciones.
    En el ámbito comercial, el impacto también ha sido positivo. Las empresas participantes han logrado un crecimiento promedio del 37% en ventas en el primer trimestre de 2024 comparado con el mismo período en 2023. Este incremento se atribuye en parte a su participación en eventos comerciales, aunque las ruedas financieras todavía presentan un área de oportunidad para generar más conexiones significativas.
    El programa también ha puesto un fuerte énfasis en mejorar la estructura laboral de las empresas, asegurando condiciones de trabajo más estables y equitativas. Se ha incrementado el número de líderes empresariales que reciben un sueldo fijo, y un
    mayor número de empleados ahora cuenta con beneficios de seguridad social, lo cual contribuye a la formalización del empleo en el sector.
    En conclusión, el programa ZASCA Bucaramanga Manufactura ha logrado mejoras tangibles en eficiencia, calidad y profesionalización de la gestión en el sector de la moda. Estos avances no solo fortalecen la capacidad de las empresas para competir en el mercado, sino que también establecen una base sólida para el crecimiento sostenido y el desarrollo a largo plazo de las empresas beneficiadas en el Sistema Moda.
    '''

A continuación tienes el contenido de las secciones que deberías incluir en tu resumen ejecutivo:
{sections_content}
"""


# Impacto comercial: Menciona el incremento en ventas, la participación en eventos comerciales, y los avances en estrategias de mercado.

# Condiciones laborales y equidad: Enfatiza los avances en estabilidad laboral, formalización del empleo, y la profesionalización de las estructuras salariales.



final_edit_prompt = """
Actúa como un editor profesional especializado en informes técnicos y de gestión. Tu tarea es revisar y perfeccionar el contenido de las secciones del informe proporcionado. Asegúrate de que:

1. **Contenido y Estructura**:
   - El contenido sea claro, lógico y fácil de entender.
   - Toda la información original se conserve íntegramente, sin eliminar detalles.
   - Los títulos de las secciones permanezcan exactamente como están.

2. **Estilo y Consistencia**:
   - El tono sea profesional, homogéneo y adecuado para un informe técnico.
   - El estilo sea uniforme a lo largo de todas las secciones, evitando discrepancias en redacción o formato.
   - Mejores el flujo narrativo para que las ideas fluyan naturalmente y estén conectadas de forma lógica.

3. **Contexto y Precisión**:
   - Realices ajustes contextuales para mejorar la precisión y relevancia de la información.
   - Agregues claridad cuando sea necesario, pero sin expandir excesivamente el contenido ni reducir su extensión.

Realiza solo las correcciones necesarias para mejorar la coherencia, claridad y presentación del texto, sin cambiar la estructura general del informe ni modificar los títulos de las secciones.

Contenido de las secciones:
{sections_content}

Por favor, devuelve el contenido editado de las secciones con las mejoras implementadas.
"""


SYSTEM_PROMPT = """
Eres un asistente especializado en la generación de informes analíticos y ejecutivos para programas de intervención multisectorial, como ZASCA, que promueven el desarrollo económico, la reindustrialización y el fortalecimiento de micro, pequeñas y medianas empresas en Colombia. Tu enfoque abarca la productividad, la sostenibilidad, la innovación, y la inclusión social y económica.

- Propósito: Tu objetivo principal es elaborar informes claros, estructurados y relevantes, basados exclusivamente en los datos y parámetros proporcionados. Todo contenido debe estar fundamentado en la información recibida, evitando suposiciones infundadas.
- Estilo de comunicación: Mantén un tono profesional, objetivo y directo. Explica conceptos de manera clara, evitando tecnicismos innecesarios, pero sin perder profundidad analítica. Cada afirmación o conclusión debe estar sustentada.
- Enfoque en datos: Interpreta los datos proporcionados y tradúcelos en análisis significativos. No inventes datos ni supongas valores. Si algún porcentaje (que no cambio porcentual) es de más del 100%, explica porqué.
- Adaptabilidad: Ajusta la estructura y el enfoque del análisis según el contexto o los requerimientos específicos del usuario, pero siempre respetando el marco profesional.
- Formato: Proporciona respuestas en texto plano, enfocándote en la claridad y la lógica del contenido, sin recurrir a formatos como tablas, gráficos u otros elementos visuales.

Tu prioridad es entregar contenido de alta calidad, estructurado y directamente útil para la toma de decisiones basada en datos.
"""
