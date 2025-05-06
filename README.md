# Opiniones de la comunidad IT sobre la inteligencia artificial generativa: un análisis de comentarios en Reddit

## Objetivo general
Analizar las opiniones y preocupaciones expresadas por desarrolladores y personal IT respecto a la inteligencia artificial generativa y los grandes modelos de lenguaje (LLM), a través de sus comentarios en Reddit.

## Objetivos específicos
- Identificar temas recurrentes en las discusiones sobre IAG dentro de comunidades técnicas.  
- Explorar las emociones y actitudes predominantes respecto a herramientas como ChatGPT, GitHub Copilot, etc.  
- Detectar patrones de aceptación, resistencia o preocupación vinculados al impacto laboral, ético o productivo de estas tecnologías.

## Pregunta de investigación
**¿Qué piensan los desarrolladores y profesionales IT sobre la inteligencia artificial generativa y sus aplicaciones?**

**Subpreguntas:**
- ¿Qué temas o preocupaciones se mencionan con mayor frecuencia?  
- ¿Qué actitudes predominan: entusiasmo, escepticismo, temor, indiferencia?

## Hipótesis
- **H1:** La mayoría de los comentarios de desarrolladores sobre la inteligencia artificial generativa se enfocan en sus usos prácticos más que en sus consecuencias laborales.  
- **H2:** Las preocupaciones éticas y sobre la veracidad de los contenidos generados por IAs tienen mayor peso que el temor a perder el empleo.  
- **H3:** Los profesionales con experiencia técnica avanzada tienden a mostrar actitudes más positivas y exploratorias frente a los LLM que los perfiles junior o no técnicos.  
- **H4:** La percepción negativa sobre la IA se asocia más frecuentemente a problemas de calidad de las respuestas, sesgos o limitaciones técnicas que al miedo al desempleo.  
- **H5:** Existe un segmento de la comunidad IT que ve a la IA generativa como una herramienta de aumento de productividad, no como un reemplazo.

## Metodología a utilizar (tentativo)
Enfoque exploratorio y descriptivo, con análisis de texto basado en técnicas de minería de texto y procesamiento de lenguaje natural (NLP). Se utilizarán herramientas en Python para la extracción de datos y R para el análisis, con visualizaciones y redacción final en Quarto.

## Descripción del corpus o conjunto de datos
**Fuente (de elaboración propia):** Comentarios extraídos mediante la API de Reddit con la librería `praw` en Python.  
**Subreddit:** [r/devsarg](https://www.reddit.com/r/devsarg)  
**Contexto:** Reddit es una plataforma muy utilizada por profesionales IT. En este caso, el subreddit es un espacio de discusión activa sobre tendencias y herramientas, por lo que se puede observar de forma directa las percepciones del sector.

## Antecedentes
Uno de los antecedentes más relevantes para este trabajo es la *Stack Overflow Developer Survey 2023*, una encuesta anual que recopila percepciones, hábitos y opiniones de más de 90.000 desarrolladores a nivel global. Sin embargo, este proyecto busca localizar el análisis en un entorno virtual frecuentado mayormente por usuarios de Argentina y, en términos más amplios, del cono sur.

> Fuente: [Stack Overflow Developer Survey 2023 – Sentiment and usage: AI](https://survey.stackoverflow.co/2023/#sentiment-and-usage-ai-select)
