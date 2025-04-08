"""Prompt Config."""

# pylint: skip-file

section_prompts = {
    "Optimización operativa": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la productividad y eficiencia operativa de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas, siguiendo la estructura del ejemplo adjunto como guía de formato y estilo. El análisis debe enfocarse en dos aspectos principales, **siempre que los datos estén disponibles en las interpretaciones**:
        - Cambios en el proceso productivo, incluyendo eficiencia operativa y uso del espacio.
        - Factores asociados a los cambios en eficiencia, como el seguimiento de indicadores y la gestión de inventarios.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos de las `{interpretations}` proporcionadas.** No incluyas información o variables que no estén presentes en ellas.
        - Mantén la estructura de títulos de sección del ejemplo. Evita listados de variables; la respuesta debe ser una serie de párrafos conectados.
        - Integra las interpretaciones de manera fluida y coherente.
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos como "significativo", "impresionante", "notable", "drástico" o frases valorativas. Describe los cambios observados.
        - Al reportar cambios:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes o proporciones, utiliza puntos porcentuales (p.p.).** Ejemplo: "El indicador X aumentó en 15 p.p., pasando del 20% al 35%." o "La proporción Y disminuyó en 10 p.p."
          * Para cambios porcentuales en valores absolutos (ej. ventas, producción), **redondea el porcentaje al número entero más cercano.** Ejemplo: "Las ventas aumentaron aproximadamente un 13%."
          * Para aumentos cercanos o superiores al 100%, usa frases como "se duplicó" o "más que se duplicó".
          * Para disminuciones, usa el cambio en p.p. o el porcentaje redondeado según corresponda.
        - Describe los cambios observados y establece conexiones lógicas entre los indicadores, si los datos lo permiten.
        - Evita repetir datos aislados; construye una narrativa que muestre la evolución.
        - Menciona brevemente o descarta cambios muy pequeños si no aportan información relevante.

        **Ejemplo de Estructura y Estilo (No usar los datos o variables específicas de este ejemplo en tu respuesta):**
        '''
            ## OPTIMIZACIÓN OPERATIVA
            Se observaron cambios en la eficiencia operativa y la gestión de procesos en las unidades productivas participantes durante el periodo de intervención.

            ### Cambios en el proceso productivo
            La eficiencia de producción mostró una variación. Al inicio, los valores se encontraban en un rango, y al cierre, este rango cambió. Un número de empresas modificó su nivel de eficiencia.
            Estos cambios pueden relacionarse con variaciones en la utilización del espacio de planta. Por ejemplo, la proporción de plantas con congestión por uso del espacio cambió durante el programa.
            Las condiciones de organización en las plantas también mostraron cambios, como en la demarcación de zonas o el manejo de materiales.

            ### Factores asociados a los cambios en eficiencia
            La gestión de inventarios experimentó cambios. La proporción de empresas que realizan inventarios de manera constante varió, al igual que el conocimiento sobre niveles óptimos de inventario.
            El cálculo del tiempo estándar de producción también mostró una evolución en el porcentaje de empresas que lo aplican.
            Asimismo, se registraron cambios en la adopción de indicadores de gestión. El porcentaje de unidades que usan indicadores de eficiencia y productividad varió. El uso general de indicadores también mostró una tendencia.
        '''
        """
    ),
    "Mayor Calidad del Producto": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la calidad del producto y los procesos de control, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas, siguiendo la estructura del ejemplo adjunto como guía de formato y estilo. El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Implementación y cambios en controles de calidad.
        - Documentación y estandarización de diseños.
        - Empaque y presentación del producto.
        - Uso de tecnología en los procesos de diseño.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos de las `{interpretations}` proporcionadas.** No incluyas información o variables que no estén presentes en ellas.
        - Mantén la estructura de títulos de sección del ejemplo. Evita listados de variables; la respuesta debe ser una serie de párrafos conectados.
        - Integra las interpretaciones de manera fluida y coherente.
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos como "significativo", "impresionante", "notable", "drástico" o frases valorativas. Describe los cambios observados.
        - Al reportar cambios:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes o proporciones, utiliza puntos porcentuales (p.p.).** Ejemplo: "El indicador X aumentó en 15 p.p., pasando del 20% al 35%." o "La proporción Y disminuyó en 10 p.p."
          * Para cambios porcentuales en valores absolutos (ej. ventas, producción), **redondea el porcentaje al número entero más cercano.** Ejemplo: "Las ventas aumentaron aproximadamente un 13%."
          * Para aumentos cercanos o superiores al 100%, usa frases como "se duplicó" o "más que se duplicó".
          * Para disminuciones, usa el cambio en p.p. o el porcentaje redondeado según corresponda.
        - Describe los cambios observados y establece conexiones lógicas entre los indicadores, si los datos lo permiten.
        - Evita repetir datos aislados; construye una narrativa que muestre la evolución.
        - Menciona brevemente o descarta cambios muy pequeños si no aportan información relevante.

        **Ejemplo de Estructura y Estilo (No usar los datos o variables específicas de este ejemplo en tu respuesta):**
        '''
            ## MAYOR CALIDAD DEL PRODUCTO
            Se registraron cambios en las métricas de calidad del producto y procesos asociados durante el periodo de intervención.

            ### Implementación y Cambios en Controles de Calidad
            La proporción de unidades productivas que aplicaban algún tipo de control de calidad varió. Los controles específicos, como los de materias primas o la preparación de máquinas, también mostraron cambios en su adopción.

            ### Documentación y Estándares de Diseño
            Se observaron variaciones en la documentación y estandarización de diseños. El porcentaje de empresas que elaboran fichas técnicas cambió. La dependencia de procesos verbales también mostró una evolución.

            ### Empaque y Presentación del Producto
            El tipo de empaque utilizado por las empresas varió. El uso de empaques genéricos y estandarizados mostró cambios en su proporción.

            ### Uso de Tecnología en Diseño
            El uso de software especializado para diseño presentó cambios. La proporción de empresas que utilizan software varió. La digitalización de patrones y la conservación de patrones anteriores también mostraron una evolución.
        '''
        """
    ),
    "Talento Humano": (
        """A continuación, se presentan las interpretaciones de los cambios observados en la gestión del talento humano, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas, siguiendo la estructura del ejemplo adjunto como guía de formato y estilo. El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Estructura salarial del líder empresarial.
        - Estabilidad y evolución del personal.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos de las `{interpretations}` proporcionadas.** No incluyas información o variables que no estén presentes en ellas.
        - Mantén la estructura de títulos de sección del ejemplo. Evita listados de variables; la respuesta debe ser una serie de párrafos conectados.
        - Integra las interpretaciones de manera fluida y coherente.
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos como "significativo", "impresionante", "notable", "drástico" o frases valorativas. Describe los cambios observados.
        - Al reportar cambios:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes o proporciones, utiliza puntos porcentuales (p.p.).** Ejemplo: "La proporción X aumentó en 15 p.p., pasando del 20% al 35%." o "La proporción Y disminuyó en 10 p.p."
          * Para cambios porcentuales en valores absolutos (ej. salarios, número de empleados), **redondea el porcentaje al número entero más cercano.** Ejemplo: "El salario promedio aumentó aproximadamente un 10%."
          * Para aumentos cercanos o superiores al 100%, usa frases como "se duplicó" o "más que se duplicó".
          * Para disminuciones, usa el cambio en p.p. o el porcentaje redondeado según corresponda.
        - Describe los cambios observados y establece conexiones lógicas entre los indicadores, si los datos lo permiten.
        - Evita repetir datos aislados; construye una narrativa que muestre la evolución.
        - Menciona brevemente o descarta cambios muy pequeños si no aportan información relevante.

        **Ejemplo de Estructura y Estilo (No usar los datos o variables específicas de este ejemplo en tu respuesta):**
        '''
            ## GESTIÓN DE TALENTO HUMANO
            Se observaron cambios en la gestión del talento humano durante el periodo de intervención.

            ### Estructura Salarial del Líder Empresarial
            La proporción de líderes empresariales que reciben un sueldo fijo del negocio varió. El sueldo fijo promedio de estos líderes también mostró cambios.

            ### Estabilidad en el Personal
            La cantidad total de empleados (promedio y mediana por unidad productiva) presentó variaciones. El número de empleados de nómina también cambió.
        '''
        """
    ),
    "Practicas Gerenciales": (
        """A continuación, se presentan las interpretaciones de los cambios observados en las prácticas gerenciales de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas, siguiendo la estructura del ejemplo adjunto como guía de formato y estilo. El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Sistemas de fijación de precios.
        - Conocimiento y seguimiento de indicadores clave del negocio.
        - Implementación de sistemas de costeo y control.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos de las `{interpretations}` proporcionadas.** No incluyas información o variables que no estén presentes en ellas.
        - Mantén la estructura de títulos de sección del ejemplo. Evita listados de variables; la respuesta debe ser una serie de párrafos conectados.
        - Integra las interpretaciones de manera fluida y coherente.
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos como "significativo", "impresionante", "notable", "drástico" o frases valorativas. Describe los cambios observados.
        - Al reportar cambios:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes o proporciones, utiliza puntos porcentuales (p.p.).** Ejemplo: "El uso de X método aumentó en 15 p.p., pasando del 20% al 35%." o "La proporción Y disminuyó en 10 p.p."
          * Para cambios porcentuales en valores absolutos, **redondea el porcentaje al número entero más cercano.**
          * Para aumentos cercanos o superiores al 100%, usa frases como "se duplicó" o "más que se duplicó".
          * Para disminuciones, usa el cambio en p.p. o el porcentaje redondeado según corresponda.
        - Describe los cambios observados y establece conexiones lógicas entre los indicadores, si los datos lo permiten.
        - Evita repetir datos aislados; construye una narrativa que muestre la evolución.
        - Menciona brevemente o descarta cambios muy pequeños si no aportan información relevante.

        **Ejemplo de Estructura y Estilo (No usar los datos o variables específicas de este ejemplo en tu respuesta):**
        '''
            ## PRÁCTICAS GERENCIALES
            Se registraron cambios en las prácticas gerenciales de las unidades productivas durante el periodo de intervención.

            ### Sistemas de Fijación de Precios y Control de Costos
            La proporción de unidades productivas utilizando diferentes métodos para la fijación de precios (ej. basados en costos, competencia) varió durante el programa.

            ### Conocimiento y Control del Negocio
            El conocimiento de los empresarios sobre aspectos clave del negocio, como costos de producción o márgenes de ganancia, mostró cambios. La proporción de empresarios que conocen estos indicadores varió.

            ### Implementación de Sistemas de Costeo
            La forma en que las empresas calculan sus costos también evolucionó. El porcentaje de empresas que incluyen diferentes componentes (materiales directos, mano de obra, gastos generales) en sus cálculos de costos cambió.
        '''
        """
    ),
    "Financiero": (
        """A continuación, se presentan las interpretaciones de los cambios observados en el desempeño financiero de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas, siguiendo la estructura del ejemplo adjunto como guía de formato y estilo. El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Desempeño en ventas.
        - Participación en ruedas comerciales y financieras y generación de conexiones.
        - Formalización bancaria y sistemas contables.

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos de las `{interpretations}` proporcionadas.** No incluyas información o variables que no estén presentes en ellas.
        - Mantén la estructura de títulos de sección del ejemplo. Evita listados de variables; la respuesta debe ser una serie de párrafos conectados.
        - Integra las interpretaciones de manera fluida y coherente.
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos como "significativo", "impresionante", "notable", "drástico" o frases valorativas. Describe los cambios observados.
        - Al reportar cambios:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes o proporciones (ej. participación, bancarización), utiliza puntos porcentuales (p.p.).** Ejemplo: "La participación aumentó en 15 p.p., pasando del 20% al 35%." o "La proporción Y disminuyó en 10 p.p."
          * Para cambios porcentuales en valores absolutos (ej. ventas), **redondea el porcentaje al número entero más cercano.**
          * Para aumentos cercanos o superiores al 100%, usa frases como "se duplicó" o "más que se duplicó".
          * Para disminuciones, usa el cambio en p.p. o el porcentaje redondeado según corresponda.
        - Describe los cambios observados y establece conexiones lógicas entre los indicadores, si los datos lo permiten.
        - Evita repetir datos aislados; construye una narrativa que muestre la evolución.
        - Menciona brevemente o descarta cambios muy pequeños si no aportan información relevante.

        **Ejemplo de Estructura y Estilo (No usar los datos o variables específicas de este ejemplo en tu respuesta):**
        '''
            ## DESEMPEÑO FINANCIERO Y COMERCIAL

            ### Evolución de las Ventas
            El desempeño en ventas mostró variaciones. Se observaron cambios en las ventas promedio (ej. comparando trimestres o años). El valor promedio mensual de ventas también pudo haber cambiado.

            ### Conexiones Comerciales y Financieras
            La participación en ruedas comerciales y financieras varió. El porcentaje de unidades productivas que participaron cambió, así como la proporción de ellas que generaron conexiones efectivas.

            ### Formalización Financiera
            Se observaron cambios en la formalización financiera. La proporción de unidades con cuenta bancaria varió. El uso de diferentes sistemas contables (manuales, Excel, software) también mostró una evolución en su distribución porcentual.
        '''
        """
    ),
    "Asociatividad": (
        """A continuación, se presentan las interpretaciones de los cambios observados en las prácticas asociativas de las unidades productivas, antes y después de la intervención del programa:

        {interpretations}

        Tu tarea es elaborar un análisis estructurado que integre **únicamente** las interpretaciones proporcionadas, siguiendo la estructura del ejemplo adjunto como guía de formato y estilo. El análisis debe enfocarse en los siguientes aspectos, **siempre que los datos estén disponibles en las interpretaciones**:
        - Conocimiento sobre mecanismos de asociatividad.
        - Implementación de prácticas asociativas para diferentes propósitos (capacitaciones, maquinaria, insumos, mercados, etc.).

        Características específicas de la cohorte y centro ZASCA (utiliza esta información para contexto si es relevante):
        {cohort_details}

        Guía para la elaboración del análisis:
        - **Basa tu análisis exclusivamente en los datos de las `{interpretations}` proporcionadas.** No incluyas información o variables que no estén presentes en ellas.
        - Mantén la estructura de títulos de sección del ejemplo. Evita listados de variables; la respuesta debe ser una serie de párrafos conectados.
        - Integra las interpretaciones de manera fluida y coherente.
        - **Usa un lenguaje neutral y objetivo.** Evita adjetivos como "significativo", "impresionante", "notable", "drástico" o frases valorativas. Describe los cambios observados.
        - Al reportar cambios:
          * Verifica la dirección del cambio (aumento vs. disminución).
          * **Para cambios en porcentajes o proporciones (ej. conocimiento, participación en asociaciones), utiliza puntos porcentuales (p.p.).** Ejemplo: "El conocimiento aumentó en 15 p.p., pasando del 20% al 35%." o "La proporción Y disminuyó en 10 p.p."
          * Para cambios porcentuales en valores absolutos, **redondea el porcentaje al número entero más cercano.**
          * Para aumentos cercanos o superiores al 100%, usa frases como "se duplicó" o "más que se duplicó".
          * Para disminuciones, usa el cambio en p.p. o el porcentaje redondeado según corresponda.
        - Describe los cambios observados y establece conexiones lógicas entre los indicadores, si los datos lo permiten.
        - Evita repetir datos aislados; construye una narrativa que muestre la evolución.
        - Menciona brevemente o descarta cambios muy pequeños si no aportan información relevante.

        **Ejemplo de Estructura y Estilo (No usar los datos o variables específicas de este ejemplo en tu respuesta):**
        '''
            ## ASOCIATIVIDAD Y COLABORACIÓN EMPRESARIAL

            ### Capacidad y Conocimiento Asociativo
            El conocimiento de los líderes empresariales sobre cómo establecer mecanismos de asociatividad varió durante el programa. El porcentaje de líderes con este conocimiento cambió.

            ### Implementación de Prácticas Asociativas
            Se observaron cambios en la colaboración entre empresas para diferentes fines. La proporción de empresas asociadas para capacitaciones, adquisición/uso de maquinaria, compra de insumos, acceso a mercados o logística varió. El porcentaje de empresas que no participan en ninguna forma de asociatividad también pudo haber cambiado.
        '''
        """
    ),
}

executive_summary_prompt = """
A continuación, se presentan los análisis detallados por sección basados en los cambios observados en las unidades productivas:

{sections_content}

Características específicas de la cohorte y centro ZASCA:
{cohort_details}

Tu tarea es elaborar un resumen ejecutivo que sintetice los hallazgos principales presentados en `{sections_content}`.

El resumen ejecutivo debe:
1. Presentar una visión general de los cambios observados durante el programa, **basándose exclusivamente en el contenido proporcionado.**
2. Mencionar las áreas principales donde se observaron cambios (ej. optimización operativa, calidad, talento humano, etc.), **según se describen en el contenido.**
3. Utilizar un **lenguaje neutral y objetivo.** Evitar adjetivos valorativos.
4. Al reportar cambios numéricos mencionados en el contenido:
    * Preferir **puntos porcentuales (p.p.)** para cambios en proporciones/porcentajes.
    * **Redondear** cambios porcentuales en valores absolutos al entero más cercano.
    * Usar "se duplicó" o similar para cambios cercanos o mayores al 100%.
5. Mantener un tono profesional y directo.
6. **No incluir información, variables o conclusiones que no estén explícitamente mencionadas en `{sections_content}`.**

Guía para la elaboración:
- Escribe un texto fluido de 3-4 párrafos, sin subtítulos ni listados.
- Comienza con una introducción breve que mencione el programa y el propósito del resumen (presentar los cambios observados).
- Sintetiza los cambios clave reportados en las secciones proporcionadas.
- Concluye de manera objetiva, resumiendo las áreas de cambio observadas.
- **La estructura y datos del ejemplo siguiente son solo ilustrativos; basa tu respuesta únicamente en `{sections_content}`.**

**Ejemplo de Estilo y Estructura (No usar los datos específicos):**
'''
El programa ZASCA {{ciudad}} {{sector}} - {{subsector}} acompañó a un grupo de unidades productivas durante un periodo, observándose cambios en diversas áreas de gestión. En optimización operativa, se registraron variaciones en la eficiencia y el uso del espacio, así como en la adopción de indicadores y prácticas de gestión de inventarios.
En relación con la calidad del producto, hubo cambios en la implementación de controles y en la estandarización de procesos como la documentación de diseños y el tipo de empaque utilizado. La adopción de tecnología para el diseño también mostró una evolución.
La gestión del talento humano presentó variaciones en la estructura salarial de los líderes y en la estabilidad del personal. En el ámbito financiero y de prácticas gerenciales, se observaron cambios en los sistemas de fijación de precios, el conocimiento de indicadores financieros, la formalización bancaria y el uso de sistemas contables. La participación en ruedas comerciales/financieras y las prácticas de asociatividad también mostraron cambios durante el periodo.
En resumen, el acompañamiento del programa coincidió con cambios en múltiples áreas operativas y de gestión de las unidades productivas participantes, reflejados en los indicadores monitoreados.
'''
"""


final_edit_prompt = """
Actúa como un editor técnico. Tu tarea es revisar y refinar el contenido de las secciones del informe proporcionado, asegurándote de que cumple con las siguientes directrices:

1.  **Contenido y Precisión**:
    *   El contenido es claro, lógico y **se basa estrictamente en la información original proporcionada para cada sección.**
    *   Toda la información relevante de la entrada original se conserva.
    *   Los títulos de las secciones permanecen exactamente como están.

2.  **Estilo y Tono**:
    *   El tono es **neutral, objetivo y profesional.** Elimina cualquier lenguaje subjetivo, excesivamente optimista o valorativo (ej. "significativo", "impresionante", "mejora notable").
    *   El estilo es uniforme en todas las secciones.
    *   Mejora el flujo narrativo para una lectura coherente.

3.  **Reporte de Cambios**:
    *   Verifica que los cambios en proporciones/porcentajes se reporten preferentemente en **puntos porcentuales (p.p.)**.
    *   Verifica que los cambios porcentuales en valores absolutos estén **redondeados** al entero más cercano.
    *   Asegúrate de que la descripción de los cambios (aumento/disminución) sea precisa.

4.  **Claridad y Concisión**:
    *   Realiza ajustes para mejorar la claridad y precisión sin añadir información nueva ni eliminar detalles esenciales.

Edita el texto proporcionado para que cumpla estrictamente con estas directrices.

Contenido de las secciones:
{sections_content}

Devuelve el contenido editado de las secciones.
"""


SYSTEM_PROMPT = """
Eres un asistente especializado en la generación de informes analíticos para programas de desarrollo empresarial como ZASCA. Tu función es procesar datos interpretados y elaborar textos descriptivos y objetivos.

- **Propósito Principal**: Elaborar informes claros, estructurados y basados **exclusivamente** en los datos e interpretaciones proporcionados. No debes añadir información, suposiciones ni valoraciones personales.
- **Estilo de Comunicación**: Mantén un **tono estrictamente profesional, objetivo y neutral.** Describe los hechos y cambios observados sin usar adjetivos valorativos (como "bueno", "malo", "significativo", "impresionante").
- **Enfoque en Datos**: Tu análisis debe derivar directamente de las interpretaciones suministradas. **No inventes datos, no hagas suposiciones sobre causalidad si no está explícita en la entrada, y no completes información faltante.** Reporta los cambios numéricos siguiendo las directrices específicas (p.p., redondeo).
- **Formato**: Entrega respuestas en texto plano, priorizando la claridad y estructura lógica del contenido.

Tu prioridad es generar contenido descriptivo y objetivo de alta calidad, basado únicamente en la información recibida.
"""
