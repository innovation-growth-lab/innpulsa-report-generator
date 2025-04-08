"""Prompt Config."""

# pylint: skip-file

section_prompts = {
    "Optimización operativa": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la productividad y eficiencia operativa de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas. Sigue la estructura de títulos del ejemplo, pero **desarrolla una narrativa coherente y detallada** basada en los datos.

        El análisis debe enfocarse en dos aspectos principales, **siempre que los datos estén disponibles en las interpretaciones**:
        - Cambios en el proceso productivo (ej. eficiencia, uso del espacio).
        - Factores asociados a estos cambios (ej. seguimiento de indicadores, gestión de inventarios).

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos e interpretaciones de `{interpretations}`.** No incluyas información o variables no presentes.
        - Mantén la estructura de títulos de sección del ejemplo.
        - **Construye una narrativa fluida y conectada.** Integra las diferentes interpretaciones para explicar la evolución observada en esta sección. Ve más allá de simplemente listar los cambios.
        - **Elabora sobre las conexiones e implicaciones lógicas que se derivan *directamente* de las interpretaciones proporcionadas.** Por ejemplo, si un indicador de gestión mejora y la eficiencia también, puedes señalar esa conexión si los datos la sugieren.
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos valorativos (ej. "significativo", "impresionante"). Describe los cambios observados.
        - Al reportar cambios numéricos:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes/proporciones, usa puntos porcentuales (p.p.).** Ej: "[Indicador A] aumentó en [N] p.p., pasando de [X]% a [Y]%."
          * Para cambios porcentuales en valores absolutos, **redondea al entero más cercano.** Ej: "[Variable B] aumentó aproximadamente un [N]%."
          * Usa "se duplicó" o similar para cambios >= 100%.
        - Descarta o menciona brevemente cambios muy pequeños si no son relevantes para la narrativa general.

        **Ejemplo de Estructura y Estilo (Ilustrativo - Basa tu contenido REAL en `{interpretations}`):**
        '''
            ## OPTIMIZACIÓN OPERATIVA
            Durante el periodo de intervención, se observaron cambios en la eficiencia operativa y la gestión de procesos de las unidades productivas participantes, basados en los indicadores monitoreados.

            ### Cambios en el proceso productivo
            La eficiencia de producción promedio mostró una variación, pasando de [valor inicial]% a [valor final]%, lo que representa un cambio de [N] p.p. Esta evolución en la eficiencia puede estar relacionada con los ajustes observados en la gestión del espacio físico. Por ejemplo, la proporción de plantas que reportaron congestión por uso del espacio disminuyó en [N] p.p., situándose en [Y]% al cierre. Adicionalmente, se registraron cambios en otros aspectos de la organización física, como [mencionar otro aspecto medido, ej. demarcación de zonas], que varió en [N] p.p., lo cual también puede influir en los flujos productivos.

            ### Factores asociados a los cambios en eficiencia
            Paralelamente, se observaron cambios en prácticas de gestión que podrían estar vinculadas a la eficiencia. La gestión de inventarios, por ejemplo, mostró una evolución: la proporción de empresas que realizan inventarios de manera constante [aumentó/disminuyó] en [N] p.p. Asimismo, el conocimiento sobre niveles óptimos de inventario reportado por las empresas varió, cambiando en [N] p.p. y alcanzando un [Y]% al final del periodo.
            Otro factor relevante es el seguimiento de indicadores. El uso de indicadores de eficiencia específicos se [incrementó/redujo] en [N] p.p., mientras que el uso de indicadores de productividad cambió en [N] p.p., pasando de [X]% a [Y]%. De forma general, la adopción de algún tipo de indicador de gestión en las unidades productivas mostró una variación neta de [N] p.p. durante el periodo.
        '''
        """
    ),
    "Mayor Calidad del Producto": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la calidad del producto y los procesos de control, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas. Sigue la estructura de títulos del ejemplo, pero **desarrolla una narrativa coherente y detallada** basada en los datos.

        El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Implementación y cambios en controles de calidad.
        - Documentación y estandarización de diseños.
        - Empaque y presentación del producto.
        - Uso de tecnología en los procesos de diseño.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos e interpretaciones de `{interpretations}`.** No incluyas información o variables no presentes.
        - Mantén la estructura de títulos de sección del ejemplo.
        - **Construye una narrativa fluida y conectada.** Integra las diferentes interpretaciones para explicar la evolución observada en esta sección. Ve más allá de simplemente listar los cambios.
        - **Elabora sobre las conexiones e implicaciones lógicas que se derivan *directamente* de las interpretaciones proporcionadas.**
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos valorativos.
        - Al reportar cambios numéricos:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes/proporciones, usa puntos porcentuales (p.p.).**
          * Para cambios porcentuales en valores absolutos, **redondea al entero más cercano.**
          * Usa "se duplicó" o similar para cambios >= 100%.
        - Descarta o menciona brevemente cambios muy pequeños.

        **Ejemplo de Estructura y Estilo (Ilustrativo - Basa tu contenido REAL en `{interpretations}`):**
        '''
            ## MAYOR CALIDAD DEL PRODUCTO
            Se registraron cambios en las métricas y procesos asociados a la calidad del producto durante el periodo de intervención, abarcando controles, documentación, empaque y tecnología.

            ### Implementación y Cambios en Controles de Calidad
            La aplicación de controles de calidad mostró variaciones. La proporción de unidades que realizan [tipo específico de control A] cambió en [N] p.p., situándose en [Y]% al cierre. De igual forma, la implementación de [tipo específico de control B] presentó una variación de [N] p.p., pasando de [X]% a [Y]%. Estos cambios sugieren una [evolución/modificación] en las prácticas de aseguramiento de calidad.

            ### Documentación y Estándares de Diseño
            En cuanto a la estandarización de diseños, se observaron cambios. Por ejemplo, el porcentaje de empresas que utilizan fichas técnicas para registrar nuevos diseños varió en [N] p.p. Paralelamente, la dependencia de procesos verbales para la comunicación de diseños, que inicialmente era del [X]%, [aumentó/disminuyó] en [N] p.p., lo que indica un cambio en la formalidad de la documentación.

            ### Empaque y Presentación del Producto
            Las prácticas de empaque también evolucionaron. El porcentaje de empresas que utilizan empaques genéricos cambió en [N] p.p. Por otro lado, el uso de empaques estándar (con protección y datos del fabricante) varió en [N] p.p. Finalmente, el uso de empaques diseñados para resaltar la marca mostró una variación de [N] p.p., alcanzando el [Y]% de las unidades.

            ### Uso de Tecnología en Diseño
            La adopción de tecnología en el diseño presentó cambios. El uso de software especializado [aumentó/disminuyó] en [N] p.p., llegando a un [Y]%. Asimismo, la proporción de empresas con patrones digitalizados varió en [N] p.p., y la práctica de conservar patrones de colecciones anteriores mostró un cambio de [N] p.p. desde el inicio del periodo.
        '''
        """
    ),
    "Talento Humano": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la gestión del talento humano, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas. Sigue la estructura de títulos del ejemplo, pero **desarrolla una narrativa coherente y detallada** basada en los datos.

        El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Estructura salarial del líder empresarial.
        - Estabilidad y evolución del personal (ej. número total, empleados de nómina).

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos e interpretaciones de `{interpretations}`.** No incluyas información o variables no presentes.
        - Mantén la estructura de títulos de sección del ejemplo.
        - **Construye una narrativa fluida y conectada.** Integra las diferentes interpretaciones para explicar la evolución observada en esta sección.
        - **Elabora sobre las conexiones e implicaciones lógicas que se derivan *directamente* de las interpretaciones proporcionadas.**
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos valorativos.
        - Al reportar cambios numéricos:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes/proporciones, usa puntos porcentuales (p.p.).**
          * Para cambios porcentuales en valores absolutos (ej. salarios, número de empleados), **redondea al entero más cercano.**
          * Usa "se duplicó" o similar para cambios >= 100%.
        - Descarta o menciona brevemente cambios muy pequeños.

        **Ejemplo de Estructura y Estilo (Ilustrativo - Basa tu contenido REAL en `{interpretations}`):**
        '''
            ## GESTIÓN DE TALENTO HUMANO
            Se observaron cambios en la gestión del talento humano durante el periodo de intervención, particularmente en la estructura salarial de los líderes y la composición del personal.

            ### Estructura Salarial del Líder Empresarial
            La situación salarial de los líderes empresariales mostró cambios. La proporción de líderes que reportaron recibir un sueldo fijo del negocio [aumentó/disminuyó] en [N] p.p., situándose en [Y]% al final del periodo. Este cambio puede indicar una [mayor/menor] formalización en la compensación del líder. Para aquellos con sueldo fijo, el valor promedio reportado también varió, cambiando de [Valor inicial COP] a [Valor final COP], lo que representa un cambio porcentual aproximado de [N]%.

            ### Estabilidad en el Personal
            La composición del personal también presentó variaciones. El número promedio de empleados totales por unidad productiva pasó de [X] a [Y], un cambio de [N] empleados en promedio. Específicamente, el número promedio de empleados de nómina (afiliados a seguridad social) cambió de [X] a [Y] durante el mismo periodo, indicando una variación en la formalización laboral dentro de las unidades participantes.
        '''
        """
    ),
    "Practicas Gerenciales": (
        """A continuación, se presentan las interpretaciones de los cambios observados en las prácticas gerenciales de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas. Sigue la estructura de títulos del ejemplo, pero **desarrolla una narrativa coherente y detallada** basada en los datos.

        El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Sistemas de fijación de precios.
        - Conocimiento y seguimiento de indicadores clave del negocio.
        - Implementación de sistemas de costeo.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos e interpretaciones de `{interpretations}`.** No incluyas información o variables no presentes.
        - Mantén la estructura de títulos de sección del ejemplo.
        - **Construye una narrativa fluida y conectada.** Integra las diferentes interpretaciones para explicar la evolución observada.
        - **Elabora sobre las conexiones e implicaciones lógicas que se derivan *directamente* de las interpretaciones proporcionadas.**
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos valorativos.
        - Al reportar cambios numéricos:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes/proporciones, usa puntos porcentuales (p.p.).**
          * Para cambios porcentuales en valores absolutos, **redondea al entero más cercano.**
          * Usa "se duplicó" o similar para cambios >= 100%.
        - Descarta o menciona brevemente cambios muy pequeños.

        **Ejemplo de Estructura y Estilo (Ilustrativo - Basa tu contenido REAL en `{interpretations}`):**
        '''
            ## PRÁCTICAS GERENCIALES
            Se registraron cambios en las prácticas gerenciales de las unidades productivas durante el periodo de intervención, abarcando sistemas de precios, conocimiento de indicadores y métodos de costeo.

            ### Sistemas de Fijación de Precios y Control de Costos
            Los métodos utilizados para la fijación de precios mostraron una evolución. Por ejemplo, la proporción de unidades que basan sus precios principalmente en [Método A, ej. costos y gastos] varió en [N] p.p., alcanzando el [Y]% al cierre. Mientras tanto, el uso del [Método B, ej. precios de mercado] cambió en [N] p.p. La proporción de empresas sin un mecanismo definido también [aumentó/disminuyó], situándose en [Z]%.

            ### Conocimiento y Control del Negocio
            El nivel de conocimiento reportado por los empresarios sobre indicadores clave de negocio presentó cambios. La proporción que afirmó conocer [Indicador A, ej. costo por unidad] varió en [N] p.p., pasando de [X]% a [Y]%. De manera similar, el conocimiento sobre [Indicador B, ej. margen de ganancia] mostró un cambio de [N] p.p. Estos datos sugieren una [evolución/cambio] en la información disponible para la toma de decisiones.

            ### Implementación de Sistemas de Costeo
            Los componentes incluidos en el cálculo del costo del producto también variaron. El porcentaje de empresas que reportaron calcular [Componente A, ej. materiales directos] cambió en [N] p.p. Asimismo, la inclusión de [Componente B, ej. mano de obra directa] varió en [N] p.p., y la de [Componente C, ej. gastos de fabricación] lo hizo en [N] p.p., alcanzando el [Y]% de las empresas al final del periodo.
        '''
        """
    ),
    "Financiero": (
        """A continuación, se presentan las interpretaciones de los cambios observados en el desempeño financiero de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas. Sigue la estructura de títulos del ejemplo, pero **desarrolla una narrativa coherente y detallada** basada en los datos.

        El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Desempeño en ventas.
        - Participación en ruedas comerciales/financieras y generación de conexiones.
        - Formalización bancaria y sistemas contables.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos e interpretaciones de `{interpretations}`.** No incluyas información o variables no presentes.
        - Mantén la estructura de títulos de sección del ejemplo.
        - **Construye una narrativa fluida y conectada.** Integra las diferentes interpretaciones para explicar la evolución observada.
        - **Elabora sobre las conexiones e implicaciones lógicas que se derivan *directamente* de las interpretaciones proporcionadas.**
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos valorativos.
        - Al reportar cambios numéricos:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes/proporciones, usa puntos porcentuales (p.p.).**
          * Para cambios porcentuales en valores absolutos (ej. ventas), **redondea al entero más cercano.**
          * Usa "se duplicó" o similar para cambios >= 100%.
        - Descarta o menciona brevemente cambios muy pequeños.

        **Ejemplo de Estructura y Estilo (Ilustrativo - Basa tu contenido REAL en `{interpretations}`):**
        '''
            ## DESEMPEÑO FINANCIERO Y COMERCIAL
            El desempeño financiero y las actividades comerciales de las unidades productivas mostraron cambios durante el periodo analizado.

            ### Evolución de las Ventas
            Se observaron variaciones en los ingresos por ventas reportados. Comparando [Periodo A] con [Periodo B], las ventas promedio cambiaron aproximadamente un [N]%. Además, el valor promedio mensual de ventas reportado durante [Año/Periodo C] fue de [Valor COP], lo que puede indicar [tendencia observada, ej. estabilización, crecimiento].

            ### Conexiones Comerciales y Financieras
            La participación en eventos de conexión comercial y financiera también mostró cambios. El porcentaje de unidades que reportaron participar en ruedas comerciales fue de [X]%. Dentro de este grupo, un [Y]% indicó haber generado conexiones. En el ámbito financiero, la participación reportada fue de [X]%, y la generación de conexiones fue de [Y]% entre las participantes. Estos datos reflejan el nivel de vinculación con [actores comerciales/financieros].

            ### Formalización Financiera
            En cuanto a la formalización, la proporción de unidades productivas con cuenta bancaria varió en [N] p.p., alcanzando el [Y]% al final del periodo. Los sistemas contables utilizados también evolucionaron; el uso de [Método A, ej. Excel] cambió en [N] p.p., mientras que la adopción de [Método B, ej. software contable] varió en [N] p.p., pasando de [X]% a [Y]%. Esto sugiere un cambio en las herramientas de gestión financiera.
        '''
        """
    ),
    "Asociatividad": (
        """A continuación, se presentan las interpretaciones de los cambios observados en las prácticas asociativas de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas. Sigue la estructura de títulos del ejemplo, pero **desarrolla una narrativa coherente y detallada** basada en los datos.

        El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Conocimiento sobre mecanismos de asociatividad.
        - Implementación de prácticas asociativas para diferentes propósitos.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos e interpretaciones de `{interpretations}`.** No incluyas información o variables no presentes.
        - Mantén la estructura de títulos de sección del ejemplo.
        - **Construye una narrativa fluida y conectada.** Integra las diferentes interpretaciones para explicar la evolución observada.
        - **Elabora sobre las conexiones e implicaciones lógicas que se derivan *directamente* de las interpretaciones proporcionadas.**
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos valorativos.
        - Al reportar cambios numéricos:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes/proporciones, usa puntos porcentuales (p.p.).**
          * Para cambios porcentuales en valores absolutos, **redondea al entero más cercano.**
          * Usa "se duplicó" o similar para cambios >= 100%.
        - Descarta o menciona brevemente cambios muy pequeños.

        **Ejemplo de Estructura y Estilo (Ilustrativo - Basa tu contenido REAL en `{interpretations}`):**
        '''
            ## ASOCIATIVIDAD Y COLABORACIÓN EMPRESARIAL
            Las prácticas y el conocimiento sobre asociatividad empresarial presentaron cambios entre las unidades productivas participantes.

            ### Capacidad y Conocimiento Asociativo
            El conocimiento reportado por los líderes empresariales sobre mecanismos de asociatividad varió durante el programa. El porcentaje de líderes que afirmó conocer cómo establecer y formalizar estos mecanismos cambió en [N] p.p., situándose en [Y]% al final. Esto sugiere una [evolución/cambio] en la base de conocimiento para la colaboración.

            ### Implementación de Prácticas Asociativas
            La participación en acciones colaborativas también mostró cambios para diversos fines. La proporción de empresas que reportaron asociarse para [Propósito A, ej. capacitaciones] varió en [N] p.p. De igual forma, la colaboración para [Propósito B, ej. comprar insumos] cambió en [N] p.p., pasando de [X]% a [Y]%. Se observaron también variaciones en la asociatividad para [Propósito C, ej. acceder a nuevos mercados] ([N] p.p.) y [Propósito D, ej. logística] ([N] p.p.). Finalmente, el porcentaje de empresas que indicaron no haberse asociado [aumentó/disminuyó] en [N] p.p.
        '''
        """
    ),
}

executive_summary_prompt = """
A continuación, se presentan los análisis detallados por sección basados en los cambios observados en las unidades productivas:

{sections_content}

Características específicas de la cohorte y centro ZASCA:
{cohort_details}

Tu tarea es elaborar un resumen ejecutivo que sintetice los hallazgos principales presentados en `{sections_content}`. **El resumen debe reflejar la información y el nivel de detalle presentes en el contenido proporcionado.**

El resumen ejecutivo debe:
1. Presentar una visión general de los cambios observados durante el programa, **basándose exclusivamente en el contenido de `{sections_content}`.**
2. Mencionar las áreas principales donde se observaron cambios (ej. optimización operativa, calidad, talento humano, etc.), **resumiendo los puntos clave descritos en el contenido.**
3. Utilizar un **lenguaje neutral y objetivo.** Evitar adjetivos valorativos.
4. Al referenciar cambios numéricos mencionados en el contenido:
    * Preferir **puntos porcentuales (p.p.)** para cambios en proporciones/porcentajes.
    * **Redondear** cambios porcentuales en valores absolutos al entero más cercano.
    * Usar "se duplicó" o similar para cambios cercanos o mayores al 100%.
5. Mantener un tono profesional y directo.
6. **No incluir información, variables, análisis o conclusiones que no estén explícitamente presentes en `{sections_content}`.**

Guía para la elaboración:
- Escribe un texto fluido de 3-4 párrafos, sin subtítulos ni listados.
- Comienza con una introducción breve contextualizando el programa y el resumen.
- Sintetiza los cambios clave reportados en las secciones proporcionadas, **manteniendo un nivel de detalle similar al del texto original.**
- Concluye de manera objetiva, resumiendo las áreas de cambio observadas según el contenido.
- **La estructura y datos del ejemplo siguiente son solo ilustrativos; basa tu respuesta únicamente en `{sections_content}`.**

**Ejemplo de Estilo y Estructura (Ilustrativo - Basa tu contenido REAL en `{sections_content}`):**
'''
El programa ZASCA {{ciudad}} {{sector}} - {{subsector}} acompañó a un grupo de unidades productivas durante un periodo, observándose cambios en diversas áreas de gestión, según se detalla en las secciones del informe. En optimización operativa, se registraron variaciones en indicadores como [mencionar 1-2 indicadores clave de la sección, ej. eficiencia, uso de espacio], así como en la adopción de prácticas como [mencionar 1-2 prácticas clave, ej. indicadores, gestión de inventarios].
En relación con la calidad del producto, el informe detalla cambios en la implementación de [mencionar 1-2 aspectos clave, ej. controles de calidad, documentación de diseños] y en la adopción de [mencionar 1-2 aspectos clave, ej. empaques específicos, tecnología de diseño]. La gestión del talento humano presentó variaciones en [mencionar 1-2 aspectos clave, ej. estructura salarial de líderes, composición del personal].
En el ámbito financiero y de prácticas gerenciales, el análisis documenta cambios en [mencionar 1-2 aspectos clave, ej. sistemas de precios, conocimiento de indicadores financieros] y en la formalización o uso de [mencionar 1-2 aspectos clave, ej. cuentas bancarias, sistemas contables]. Finalmente, las prácticas de asociatividad mostraron una evolución en [mencionar 1-2 aspectos clave, ej. conocimiento de mecanismos, participación en colaboraciones].
En resumen, el informe documenta cambios en múltiples áreas operativas y de gestión de las unidades productivas participantes durante el periodo de acompañamiento, tal como se refleja en los indicadores y prácticas monitoreadas en cada sección.
'''
"""


final_edit_prompt = """
Actúa como un editor técnico. Tu tarea es revisar y refinar el contenido de las secciones del informe proporcionado, asegurándote de que cumple con las siguientes directrices:

1.  **Contenido y Precisión**:
    *   El contenido es claro, lógico y **se basa estrictamente en la información original proporcionada para cada sección.**
    *   Toda la información relevante de la entrada original se conserva.
    *   Los títulos de las secciones permanecen exactamente como están.
    *   **Se mantiene un nivel de detalle y elaboración adecuado**, similar al esperado en un informe analítico (evitando ser excesivamente breve o telegráfico).

2.  **Estilo y Tono**:
    *   El tono es **neutral, objetivo y profesional.** Elimina cualquier lenguaje subjetivo, excesivamente optimista o valorativo (ej. "significativo", "impresionante", "mejora notable").
    *   El estilo es uniforme en todas las secciones.
    *   Mejora el flujo narrativo para una lectura coherente, conectando ideas donde sea apropiado.

3.  **Reporte de Cambios**:
    *   Verifica que los cambios en proporciones/porcentajes se reporten preferentemente en **puntos porcentuales (p.p.)**.
    *   Verifica que los cambios porcentuales en valores absolutos estén **redondeados** al entero más cercano.
    *   Asegúrate de que la descripción de los cambios (aumento/disminución) sea precisa.

4.  **Claridad y Concisión**:
    *   Realiza ajustes para mejorar la claridad y precisión sin añadir información nueva ni eliminar detalles esenciales.

Edita el texto proporcionado para que cumpla estrictamente con estas directrices, prestando especial atención a mantener un nivel de detalle adecuado y una narrativa conectada.

Contenido de las secciones:
{sections_content}

Devuelve el contenido editado de las secciones.
"""


SYSTEM_PROMPT = """
Eres un asistente especializado en la generación de informes analíticos para programas de desarrollo empresarial como ZASCA. Tu función es procesar datos interpretados y elaborar textos descriptivos, analíticos y objetivos.

- **Propósito Principal**: Elaborar informes claros, estructurados y basados **exclusivamente** en los datos e interpretaciones proporcionados. Debes **conectar las interpretaciones** para construir una narrativa coherente para cada sección, yendo más allá de una simple lista de cambios. No debes añadir información externa, suposiciones ni valoraciones personales.
- **Estilo de Comunicación**: Mantén un **tono estrictamente profesional, objetivo y neutral.** Describe los hechos y cambios observados, y **elabora sobre las conexiones lógicas** entre ellos basándote *únicamente* en la información dada. Evita adjetivos valorativos (como "bueno", "malo", "significativo", "impresionante").
- **Enfoque en Datos**: Tu análisis debe derivar directamente de las interpretaciones suministradas. **No inventes datos, no hagas suposiciones sobre causalidad si no está explícita en la entrada, y no completes información faltante.** Reporta los cambios numéricos siguiendo las directrices específicas (p.p., redondeo).
- **Formato**: Entrega respuestas en texto plano, priorizando la claridad, estructura lógica y **flujo narrativo** del contenido.

Tu prioridad es generar contenido descriptivo y analítico de alta calidad, que integre la información proporcionada de manera coherente y objetiva.
"""
