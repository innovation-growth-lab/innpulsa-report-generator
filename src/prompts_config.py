"""Prompt Config."""
# pylint: skip-file

section_prompts = {
    "Optimización operativa": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la productividad y eficiencia operativa de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre estas interpretaciones, siguiendo la estructura del ejemplo proporcionado. El análisis debe enfocarse en dos aspectos principales:
        - Las mejoras en el proceso productivo, incluyendo eficiencia operativa y uso del espacio
        - Los factores que explican los incrementos de eficiencia, como el seguimiento de indicadores y la gestión de inventarios

        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Guía para la elaboración del análisis:
        - Mantén la estructura del ejemplo proporcionado abajo, con los mismos títulos de sección. Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Integra las interpretaciones de manera fluida y coherente
        - Al reportar cambios:
          * Verifica cuidadosamente si el cambio es un aumento o disminución
          * Si un valor baja (ej: de 10.17 a 6.78), descríbelo como una disminución o reducción
          * Si un valor sube (ej: de 6.78 a 10.17), descríbelo como un aumento o incremento
          * Limita los cambios porcentuales a un máximo de 100% (si el cambio es mayor, usa "más que duplicó" o "más que se duplicó")
          * Para disminuciones, usa el porcentaje real (ej: "disminuyó un 33%")
        - Enfatiza las mejoras más significativas y sus implicaciones, usa porcentajes solo cuando estos son relevantes
        - Establece conexiones lógicas entre los diferentes indicadores
        - Evita repetir los datos de forma aislada; en su lugar, construye una narrativa que muestre la evolución integral
        - Si los cambios porcentuales son pequeños, descártalos o menciónalos brevemente sin darles énfasis especial

        A continuación se incluye un ejemplo del formato y estilo esperado:
        '''
            ## OPTIMIZACIÓN OPERATIVA: MEJORAS EN EL PROCESO PRODUCTIVO Y LA CALIDAD DEL PRODUCTO
            En el marco del programa de ZASCA {{ciudad}} {{sector}} {{subsector}}, se implementaron varias iniciativas para optimizar la eficiencia operativa y elevar los estándares de calidad. Los resultados obtenidos demuestran avances significativos, evidenciados en los indicadores clave y métricas de éxito.

            ### Mejoras en el proceso productivo
            Al inicio del programa, las empresas se encontraban en un rango de eficiencia de {{pct}} a {{pct}}, con algunas operando cerca del nivel óptimo, pero muchas aún por debajo de su potencial. Al cierre del programa, la mayoría ha alcanzado una eficiencia entre X y Y, con más de {{pct}} empresas logrando niveles cercanos o superiores al {{pct}}, lo que evidencia una optimización significativa en sus procesos productivos.

            Estos avances en productividad están relacionados con mejoras en la distribución y utilización del espacio de planta, influyendo notablemente en la capacidad de las unidades productivas para alcanzar sus metas de producción exactamente como fueron planeadas. Esta correlación sugiere que una gestión más eficiente del espacio no solo optimiza los recursos disponibles, sino que también contribuye a una mayor conformidad con el balanceo de planta, lo que se refleja directamente en los resultados de producción.

            Inicialmente, el {{pct}} de las plantas presentaba congestión debido a una deficiente utilización del espacio, al finalizar el programa hubo una este porcentaje se redujo al {{pct}}, indicando que las empresas han logrado optimizar el uso del espacio a lo largo del programa.

            Al finalizar el programa, se observa una mejora integral en las condiciones de seguridad y organización en las plantas beneficiarias. Las zonas de tránsito, áreas de trabajo y tránsito están ahora completamente adecuadas y demarcadas, alcanzando el {{pct}} de cumplimiento. Además, la acumulación de materiales en proceso ha sido controlada, y se ha optimizado la secuencia y longitud del flujo de proceso, lo que facilita un desplazamiento más eficiente del personal y materiales. Cada planta cuenta ahora con espacios específicos para guardar elementos personales y un aislamiento completo de áreas peligrosas, contribuyendo a un entorno más seguro. Asimismo, se han instalado advertencias de peligro en todos los puestos de trabajo, logrando un ambiente laboral más seguro y organizado.

            ### ¿A qué se deben los incrementos de eficiencia? Las unidades productivas mejoraron en el seguimiento de indicadores clave y la gestión de inventarios
            En el ámbito de la gestión de inventarios se evidenció una evolución positiva. La proporción de empresas que realizan inventarios de manera constante creció del {{pct}} al {{pct}}.

            Además, se registró un aumento en el conocimiento sobre los niveles óptimos de inventario, que pasó del {{pct}} al {{pct}}, reflejando una gestión más efectiva y un mejor control de los recursos disponibles.
            
            Estos resultados en el manejo de inventarios pueden mejorar la eficiencia operativa y la capacidad de respuesta al mercado de las unidades productivas.

            Por su parte, el cálculo del tiempo estándar para la producción demostró un aumento significativo, del {{pct}} al {{pct}}. Este aumento indica una mayor precisión en la planificación, y una asignación de tiempos y recursos más eficaz, aspectos cruciales para mejorar la eficiencia operativa de la unidad productiva.

            Por otro lado, las mejoras en eficiencia y productividad también pueden ser resultado de un avance notable en la adopción de indicadores clave para mejorar el proceso productivo. De hecho, el porcentaje de unidades productivas que tienen indicador de eficiencia aumentó de un {{pct}} a un {{pct}}; aquellas que tenían indicadores de productividad experimentaron un incremento aún más impresionante, pasando de un {{pct}} a un {{pct}}. Este cambio indica una mayor eficacia en las operaciones de producción.

            Como resultado, en términos globales, el porcentaje de unidades productivas que usan indicadores presentó un incremento de {{pct_points}}. Al inicio de la intervención el {{pct}} de las unidades productivas contaban con algún tipo de indicador, mientras que, al cierre del programa este porcentaje aumentó al {{pct}}. Esto evidencia una creciente utilización de los indicadores para mejorar el proceso productivo. Las unidades productivas son más conscientes de la importancia de llevar periódicamente indicadores de desempeño.
        '''
        """
    ),
    "Mayor Calidad del Producto": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la calidad del producto y los procesos de control, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre estas interpretaciones, siguiendo la estructura del ejemplo proporcionado. El análisis debe enfocarse en cuatro aspectos principales:
        - La implementación y mejora de controles de calidad
        - La documentación y estandarización de diseños
        - El empaque y presentación del producto
        - El uso de tecnología en los procesos de diseño

        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Guía para la elaboración del análisis:
        - Mantén la estructura del ejemplo proporcionado abajo, con los mismos títulos de sección. Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Integra las interpretaciones de manera fluida y coherente
        - Al reportar cambios:
          * Verifica cuidadosamente si el cambio es un aumento o disminución
          * Si un valor baja (ej: de 10.17 a 6.78), descríbelo como una disminución o reducción
          * Si un valor sube (ej: de 6.78 a 10.17), descríbelo como un aumento o incremento
          * Limita los cambios porcentuales a un máximo de 100% (si el cambio es mayor, usa "más que duplicó" o "más que se duplicó")
          * Para disminuciones, usa el porcentaje real (ej: "disminuyó un 33%")
        - Enfatiza las mejoras más significativas y sus implicaciones, usa porcentajes solo cuando estos son relevantes
        - Establece conexiones lógicas entre los diferentes indicadores
        - Evita repetir los datos de forma aislada; en su lugar, construye una narrativa que muestre la evolución integral
        - Si los cambios porcentuales son pequeños, descártalos o menciónalos brevemente sin darles énfasis especial

        A continuación se incluye un ejemplo del formato y estilo esperado. Tu respuesta debe seguir una estructura similar, pero utilizando las interpretaciones proporcionadas arriba:

        '''
            ## MAYOR CALIDAD DEL PRODUCTO
            Paralelamente, las métricas de calidad en el producto mostraron mejoras en relación con los controles de calidad, la preparación de máquinas y el manejo de tiempos, así como la estandarización y digitalización de procesos de diseño.
            
            ### Implementación y Mejora de Controles de Calidad
            Inicialmente, el {{pct}} de las unidades productivas aplicaban algún tipo de control de calidad. Al cierre del programa, este porcentaje alcanzó el {{pct}}, demostrando un compromiso con la calidad.
            Los controles específicos de calidad en materias primas y productos finales mejoraron del {{pct}} al {{pct}}. De igual manera, la capacidad de las unidades para preparar adecuadamente las máquinas y controlar los tiempos de producción mejoró drásticamente, pasando del {{pct}} al {{pct}}. Estos cambios aseguran una consistencia mayor en los productos finales y una reducción de errores y defectos.
            
            ### Documentación y Estándares de Diseño 
            Por su parte, también se observaron avances significativos en la documentación y estandarización de nuevos diseños. El porcentaje de empresas que elaboran fichas técnicas para registrar diseños aumentó del {{pct}} al {{pct}}. Además, el porcentaje de unidades productivas que presentaban dependencia de procesos verbales disminuyó en {{pct_points}} p.p, al pasar de {{pct}} a {{pct}} al cierre de la intervención.
            Por consiguiente, las empresas han migrado a métodos más estructurados y replicables para el seguimiento de sus diseños.
            
            ### Empaque y Presentación del Producto
            El empaque del producto ha evolucionado para reflejar mejor la marca y sus valores. El uso de empaques genéricos disminuyó del {{pct}} al {{pct}} a favor de un aumento en el empaque estandarizado que aumentó del {{pct}} al {{pct}}. Esto muestra un área de mejora considerable en la identidad y presentación visual de los productos.

            ### Uso de Tecnología en Diseño
            Por último, el uso de software especializado para el diseño de productos ha visto un crecimiento considerable, la proporción de empresas que cuentan con software pasó del {{pct}} al {{pct}}. Esto facilita la precisión en los diseños y mejora la capacidad de personalización de productos.
            Además, la digitalización de patrones aumentó (al inicio del programa el {{pct}} de las unidades productivas tenían digitalizado su proceso de diseño, mientras que al cierre del programa el {{pct}} de las empresas contaban con esto).
            De igual manera, el porcentaje de unidades productivas que conservan los patrones de colecciones anteriores pasó del {{pct}} al {{pct}}, lo cual mejora la eficiencia y la capacidad de referencia histórica para el desarrollo de nuevos productos.        
        '''
    """
    ),
    "Talento Humano": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la gestión del talento humano, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre estas interpretaciones, siguiendo la estructura del ejemplo proporcionado. El análisis debe enfocarse en tres aspectos principales:
        - La estructura salarial y beneficios de los trabajadores
        - La estructura salarial del líder empresarial
        - La estabilidad y evolución del personal

        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Guía para la elaboración del análisis:
        - Mantén la estructura del ejemplo proporcionado abajo, con los mismos títulos de sección. Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Integra las interpretaciones de manera fluida y coherente
        - Al reportar cambios:
          * Verifica cuidadosamente si el cambio es un aumento o disminución
          * Si un valor baja (ej: de 10.17 a 6.78), descríbelo como una disminución o reducción
          * Si un valor sube (ej: de 6.78 a 10.17), descríbelo como un aumento o incremento
          * Limita los cambios porcentuales a un máximo de 100% (si el cambio es mayor, usa "más que duplicó" o "más que se duplicó")
          * Para disminuciones, usa el porcentaje real (ej: "disminuyó un 33%")
        - Enfatiza las mejoras más significativas y sus implicaciones, usa porcentajes solo cuando estos son relevantes
        - Establece conexiones lógicas entre los diferentes indicadores
        - Evita repetir los datos de forma aislada; en su lugar, construye una narrativa que muestre la evolución integral
        - Si los cambios porcentuales son pequeños, descártalos o menciónalos brevemente sin darles énfasis especial

        A continuación se incluye un ejemplo del formato y estilo esperado. Tu respuesta debe seguir una estructura similar, pero utilizando las interpretaciones proporcionadas arriba:

        '''
            ## GESTIÓN DE TALENTO HUMANO
            En ZASCA Manufactura, el enfoque hacia la mejora de las condiciones laborales y la formalización de las relaciones de trabajo ha llevado a cambios visibles en la cobertura de seguridad social de los trabajadores.   
            Inicialmente, la situación en muchas unidades productivas reflejaba una preocupante concentración en el {{pct}} de afiliación, con {{pct}} empresas sin formalización laboral alguna. Esto evidenciaba una carencia generalizada de acceso a beneficios básicos para los trabajadores, lo que subrayaba la urgencia de la intervención.
            Al finalizar la intervención, si bien el número de empresas con {{pct}} de afiliación se mantuvo, se evidenció un avance en los rangos intermedios, particularmente entre el {{pct}} y el {{pct}}, donde más empresas lograron aumentar su nivel de formalización. Sin embargo, el número de empresas con una proporción del {{pct}} disminuyó ligeramente de {{pct}} a {{pct}}, lo que indica un retroceso marginal en la formalización completa. Estos resultados reflejan un progreso parcial, pero también dejan claro que se requieren estrategias más específicas para incluir a las empresas menos formalizadas y consolidar los avances hacia la formalización total.

            ### Estructura Salarial del Líder Empresarial
            Se evidenció un incremento en la proporción de líderes empresariales que reciben un sueldo fijo del negocio, pasando de un {{pct}} a un {{pct}}. Este cambio no solo mejora la estabilidad financiera de los líderes, sino que también refleja una estructura de compensación más formal y equitativa.
            Además, el sueldo fijo promedio de estos líderes casi incrementó, pasando de \\${{pct}} a \\${{pct}}, mejorando sustancialmente su compensación y alineándola con las responsabilidades y el rendimiento.
            
            ### Estabilidad en el Personal
            La cantidad total de empleados se mantuvo estable, con un leve incremento en el promedio de trabajadores por unidad productiva, de {{pct}} a {{pct}}, y de {{pct}} a {{pct}} en la mediana. Esta estabilidad es un indicador de que las mejoras en compensación y beneficios no han comprometido la sostenibilidad de empleo en las unidades productivas.
        '''
    """
    ),
    "Practicas Gerenciales": (
        """A continuación, se presentan las interpretaciones de los cambios observados en las prácticas gerenciales de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre estas interpretaciones, siguiendo la estructura del ejemplo proporcionado. El análisis debe enfocarse en tres aspectos principales:
        - Los sistemas de fijación de precios y costos
        - El conocimiento y seguimiento de indicadores clave del negocio
        - La implementación de sistemas de costeo y control

        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Guía para la elaboración del análisis:
        - Mantén la estructura del ejemplo proporcionado abajo, con los mismos títulos de sección. Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Integra las interpretaciones de manera fluida y coherente
        - Al reportar cambios:
          * Verifica cuidadosamente si el cambio es un aumento o disminución
          * Si un valor baja (ej: de 10.17 a 6.78), descríbelo como una disminución o reducción
          * Si un valor sube (ej: de 6.78 a 10.17), descríbelo como un aumento o incremento
          * Limita los cambios porcentuales a un máximo de 100% (si el cambio es mayor, usa "más que duplicó" o "más que se duplicó")
          * Para disminuciones, usa el porcentaje real (ej: "disminuyó un 33%")
        - Enfatiza las mejoras más significativas y sus implicaciones, usa porcentajes solo cuando estos son relevantes
        - Establece conexiones lógicas entre los diferentes indicadores
        - Evita repetir los datos de forma aislada; en su lugar, construye una narrativa que muestre la evolución integral
        - Si los cambios porcentuales son pequeños, descártalos o menciónalos brevemente sin darles énfasis especial

        A continuación se incluye un ejemplo del formato y estilo esperado. Tu respuesta debe seguir una estructura similar, pero utilizando las interpretaciones proporcionadas arriba:

        '''
            ## PRÁCTICAS GERENCIALES: MEJORAS EN LA GESTIÓN Y TOMA DE DECISIONES

            La intervención del programa ha generado avances significativos en la profesionalización de las prácticas gerenciales, evidenciados en una mejor comprensión y aplicación de herramientas de gestión empresarial.

            ### Sistemas de Fijación de Precios y Control de Costos
            Al inicio del programa, la mayoría de las unidades productivas carecían de un sistema estructurado para la fijación de precios, con solo un {{pct}}% utilizando métodos basados en costos. La intervención logró que este porcentaje aumentara al {{pct}}%, indicando una transición hacia prácticas más profesionales de pricing.

            ### Conocimiento y Control del Negocio
            Se observaron mejoras sustanciales en el conocimiento de aspectos clave del negocio. La proporción de empresarios que conocen sus costos de producción aumentó del {{pct}}% al {{pct}}%, mientras que aquellos que manejan información detallada sobre sus márgenes de ganancia pasó del {{pct}}% al {{pct}}%. Este incremento en el conocimiento financiero permite una toma de decisiones más informada y estratégica.

            ### Implementación de Sistemas de Costeo
            En cuanto al cálculo de costos, se logró una mayor sofisticación en los métodos utilizados. El porcentaje de empresas que incluyen materiales directos en sus cálculos aumentó del {{pct}}% al {{pct}}%, mientras que la consideración de mano de obra directa se incrementó del {{pct}}% al {{pct}}%. Particularmente notable fue el aumento en la inclusión de gastos generales de fabricación, que pasó del {{pct}}% al {{pct}}%, demostrando una comprensión más integral de la estructura de costos.
        '''
        """
    ),
    "Financiero": (
        """A continuación, se presentan las interpretaciones de los cambios observados en el desempeño financiero de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre estas interpretaciones, siguiendo la estructura del ejemplo proporcionado. El análisis debe enfocarse en tres aspectos principales:
        - El desempeño en ventas y crecimiento comercial
        - La participación en ruedas comerciales y financieras
        - La formalización bancaria y sistemas contables

        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Guía para la elaboración del análisis:
        - Mantén la estructura del ejemplo proporcionado abajo, con los mismos títulos de sección. Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Integra las interpretaciones de manera fluida y coherente
        - Al reportar cambios:
          * Verifica cuidadosamente si el cambio es un aumento o disminución
          * Si un valor baja (ej: de 10.17 a 6.78), descríbelo como una disminución o reducción
          * Si un valor sube (ej: de 6.78 a 10.17), descríbelo como un aumento o incremento
          * Limita los cambios porcentuales a un máximo de 100% (si el cambio es mayor, usa "más que duplicó" o "más que se duplicó")
          * Para disminuciones, usa el porcentaje real (ej: "disminuyó un 33%")
        - Enfatiza las mejoras más significativas y sus implicaciones, usa porcentajes solo cuando estos son relevantes
        - Establece conexiones lógicas entre los diferentes indicadores
        - Evita repetir los datos de forma aislada; en su lugar, construye una narrativa que muestre la evolución integral
        - Si los cambios porcentuales son pequeños, descártalos o menciónalos brevemente sin darles énfasis especial

        A continuación se incluye un ejemplo del formato y estilo esperado. Tu respuesta debe seguir una estructura similar, pero utilizando las interpretaciones proporcionadas arriba:

        '''
            ## DESEMPEÑO FINANCIERO Y COMERCIAL

            ### Evolución de las Ventas
            El análisis del desempeño en ventas muestra una tendencia positiva. Comparando el primer trimestre de 2024 con el mismo período de 2023, se observa un crecimiento del {{pct}}% en las ventas promedio. El valor promedio mensual de ventas durante 2024 se ha mantenido en {{value}} millones de pesos, reflejando una estabilización en los niveles de ingreso.

            ### Conexiones Comerciales y Financieras
            La participación en ruedas comerciales y financieras ha sido un catalizador importante para el crecimiento. El {{pct}}% de las unidades productivas participaron en ruedas comerciales, de las cuales el {{pct}}% lograron establecer conexiones efectivas. En el ámbito financiero, la participación fue del {{pct}}%, con un {{pct}}% de empresas generando vínculos con entidades financieras, ampliando sus opciones de financiamiento.

            ### Formalización Financiera
            Se evidencia un avance significativo en la formalización financiera de las empresas. La proporción de unidades productivas con cuenta bancaria aumentó del {{pct}}% al {{pct}}%, facilitando sus transacciones comerciales y acceso a servicios financieros. En cuanto a los sistemas contables, se observa una evolución desde métodos manuales hacia herramientas más sofisticadas: el uso de Excel para contabilidad creció del {{pct}}% al {{pct}}%, mientras que la adopción de software contable pasó del {{pct}}% al {{pct}}%.
        '''
        """
    ),
    "Asociatividad": (
        """A continuación, se presentan las interpretaciones de los cambios observados en las prácticas asociativas de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre estas interpretaciones, siguiendo la estructura del ejemplo proporcionado. El análisis debe enfocarse en dos aspectos principales:
        - El conocimiento y capacidad de establecer mecanismos de asociatividad
        - Los diferentes propósitos y logros de la asociatividad (capacitaciones, maquinaria, insumos, mercados)

        Características específicas de la cohorte y centro ZASCA:
        {cohort_details}

        Guía para la elaboración del análisis:
        - Mantén la estructura del ejemplo proporcionado abajo, con los mismos títulos de sección. Evita listados de variables o subsecciones, la respuesta debería ser una serie de parágrafos conectados. 
        - Integra las interpretaciones de manera fluida y coherente
        - Al reportar cambios:
          * Verifica cuidadosamente si el cambio es un aumento o disminución
          * Si un valor baja (ej: de 10.17 a 6.78), descríbelo como una disminución o reducción
          * Si un valor sube (ej: de 6.78 a 10.17), descríbelo como un aumento o incremento
          * Limita los cambios porcentuales a un máximo de 100% (si el cambio es mayor, usa "más que duplicó" o "más que se duplicó")
          * Para disminuciones, usa el porcentaje real (ej: "disminuyó un 33%")
        - Enfatiza las mejoras más significativas y sus implicaciones, usa porcentajes solo cuando estos son relevantes
        - Establece conexiones lógicas entre los diferentes indicadores
        - Evita repetir los datos de forma aislada; en su lugar, construye una narrativa que muestre la evolución integral
        - Si los cambios porcentuales son pequeños, descártalos o menciónalos brevemente sin darles énfasis especial

        A continuación se incluye un ejemplo del formato y estilo esperado. Tu respuesta debe seguir una estructura similar, pero utilizando las interpretaciones proporcionadas arriba:

        '''
            ## ASOCIATIVIDAD Y COLABORACIÓN EMPRESARIAL

            ### Capacidad y Conocimiento Asociativo
            El programa ha logrado fortalecer significativamente la comprensión y capacidad de las unidades productivas para establecer mecanismos de asociatividad empresarial. El porcentaje de líderes que conocen cómo establecer y formalizar diferentes mecanismos de asociatividad aumentó del {{pct}}% al {{pct}}%, sentando una base sólida para futuras colaboraciones.

            ### Implementación de Prácticas Asociativas
            Este conocimiento se ha traducido en acciones concretas de colaboración. La proporción de empresas que se han asociado para tomar capacitaciones grupales creció del {{pct}}% al {{pct}}%, mientras que la colaboración para adquirir maquinaria y equipos modernos aumentó del {{pct}}% al {{pct}}%. Particularmente notable ha sido el incremento en la asociatividad para la compra conjunta de insumos, que pasó del {{pct}}% al {{pct}}%, permitiendo reducir costos operativos.

            Las unidades productivas también han mostrado avances en formas más sofisticadas de colaboración. La asociatividad para acceder a nuevos mercados aumentó del {{pct}}% al {{pct}}%, y la colaboración en procesos logísticos y de distribución se incrementó del {{pct}}% al {{pct}}%. Es importante notar que el porcentaje de empresas que no participan en ninguna forma de asociatividad se redujo del {{pct}}% al {{pct}}%, evidenciando un cambio cultural significativo hacia prácticas más colaborativas.
        '''
        """
    ),
}

executive_summary_prompt = """
A continuación, se presentan las interpretaciones detalladas de los cambios observados en las unidades productivas, organizadas por sección. Tu tarea es elaborar un resumen ejecutivo que sintetice los hallazgos más relevantes del programa:

{sections_content}

Características específicas de la cohorte y centro ZASCA:
{cohort_details}

El resumen ejecutivo debe:
1. Presentar una visión integral del impacto del programa
2. Destacar las mejoras más significativas en:
   - Optimización operativa y productividad
   - Calidad del producto y estandarización
   - Gestión del talento humano
   - Prácticas gerenciales y financieras
   - Asociatividad empresarial
3. Enfocarse en cambios porcentuales relevantes y mejoras cualitativas importantes
4. Mantener un tono profesional y persuasivo
5. Evitar detalles excesivos o cambios porcentuales menores

Guía para la elaboración:
- Escribe un texto fluido de 4-5 párrafos sin subtítulos ni listados
- Comienza con una introducción que contextualice el programa
- Al reportar cambios:
  * Verifica la dirección del cambio (aumento vs. disminución)
  * Para aumentos mayores al 100%, usa "más que duplicó" en lugar de porcentajes
  * Para disminuciones, reporta el porcentaje real de reducción
  * Asegúrate de que la narrativa refleje correctamente si un cambio es positivo o negativo
- Desarrolla los logros más significativos en orden de importancia
- Concluye con una visión del impacto general y perspectivas futuras
- Usa porcentajes solo cuando sean realmente significativos
- Evita repetir datos específicos que no sean cruciales

A continuación se incluye un ejemplo del estilo y estructura esperados:

'''
El programa ZASCA {{ciudad}} {{sector}} - {{subsector}} ha generado un impacto significativo en la optimización operativa y la calidad del producto de las empresas participantes. Las unidades productivas han logrado mejoras sustanciales en su eficiencia operativa, evidenciadas por reducciones en tiempos de producción y mejor aprovechamiento del espacio. Particularmente notable ha sido el incremento en el uso de indicadores de gestión, que ahora son implementados por más del {{pct}}% de las empresas, permitiendo un control más efectivo de sus procesos.
En términos de calidad y estandarización, se observan avances importantes en la implementación de controles de calidad y la documentación de procesos. La proporción de empresas que utilizan fichas técnicas para el registro de diseños se ha duplicado, mientras que la adopción de empaques estandarizados y distintivos refleja una mayor profesionalización en la presentación de productos.
La gestión del talento humano muestra mejoras significativas en la formalización laboral y la estructura salarial. El {{pct}}% de los líderes empresariales ahora reciben un sueldo fijo, y la cobertura de seguridad social ha aumentado considerablemente. En el ámbito financiero, la adopción de herramientas contables estructuradas y la participación en ruedas comerciales han fortalecido la capacidad de gestión y el acceso a nuevos mercados.
Las prácticas gerenciales han evolucionado hacia métodos más profesionales, con un incremento notable en el uso de sistemas de costeo y fijación de precios basados en datos. La asociatividad empresarial también ha mostrado avances significativos, con más empresas participando en iniciativas colaborativas para capacitación, compra de insumos y acceso a mercados.
En conclusión, el programa ZASCA {{ciudad}} {{sector}} ha catalizado una transformación integral en las unidades productivas participantes, sentando bases sólidas para su crecimiento sostenible. Los avances en eficiencia operativa, calidad, gestión del talento humano y prácticas empresariales posicionan a estas empresas para competir más efectivamente en sus respectivos mercados.
'''
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
