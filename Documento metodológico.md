## Documento metodológico
### Trabajo: Opiniones de la comunidad IT sobre la inteligencia artificial generativa

#### 1. Origen del corpus
El corpus se extrajo de la plataforma Reddit, específicamente del subreddit r/devsarg, mediante la API oficial que permite scrapear las publicaciones a través de la librería praw en Python. Este subreddit es un espacio de debate técnico y profesional, frecuentado por desarrolladores y personal IT en general, mayoritariamente de Argentina y de países del Cono Sur.
Reddit permite el acceso a su contenido público mediante su API, siempre que se respeten sus términos de uso, capacidad de las cuotas y políticas de privacidad. El corpus obtenido está destinado únicamente a fines académicos.
#### 2. Variables incluidas
El archivo del corpus se encuentra en formato .json, el que muestra una lista de campos anidados, cada uno de los cuales a mayor nivel muestra una publicación individual, y los datos relacionados a esta, es decir, los comentarios y los usuarios que realizan estos. Las principales variables incluidas son:

Variable	Descripción
id	Identificador único del comentario
author	Nombre de usuario (pseudónimo de Reddit, seudoanónimo)
created_utc	Fecha y hora de publicación en formato UTC
body	Texto completo del comentario
score	Número de arrivotos netos del comentario
permalink	Enlace permanente al comentario dentro del hilo original
subreddit	Nombre del subreddit del cual se extrajo el comentario (r/devsarg)
parent_id	Identificador del comentario o posteo al cual responde (si aplica)
link_id	Identificador del hilo de discusión completo

#### 3. Criterios de selección e inclusión
El corpus fue generado a partir de una búsqueda específica en el subreddit r/devsarg, con la función de búsqueda de la API de Reddit con la librería praw en Python.

Los criterios de selección fueron los siguientes:

Subreddit: r/devsarg, comunidad argentina de desarrolladores y personal IT.

Consulta:
"gpt OR ia OR chatgpt OR ia generativa OR vibe coding OR cursor OR llms"

Orden de resultados: por fecha de publicación, de más reciente a más antiguo (sort="new").

Límite de resultados: 20 hilos de discusión.

Para cada hilo identificado por la búsqueda, se extrajeron los metadatos del post principal y de sus comentarios asociados. Se incluyeron únicamente hilos que contenían al menos una mención relevante al tema de la inteligencia artificial generativa o herramientas afines.

#### 4. Metodología de recolección y organización del corpus
Recolección:
La recolección fue realizada mediante un script en Python utilizando:

* praw para conectarse a la API de Reddit.

* Búsquedas con filtros por palabra clave y fecha.

* Guardado automático de los resultados en formato .json.

El script completo se entrega junto al corpus y puede reproducirse para obtener nuevos datos o verificar el procedimiento. Debe incluirse una clave de acceso a la API de Reddit para su funcionamiento.

Limpieza y normalización:
Restan los siguientes pasos para la limpieza y normalización del corpus:
* Eliminación de duplicados y entradas vacías o irrelevantes.
* Conversión de fechas UTC a formato legible si se requiere.
* Revisión manual y global de muestras aleatorias para asegurar relevancia temática (esta se llevó a cabo parcialmente).

#### 5. Propósito de uso del corpus
El corpus se usará para analizar las opiniones de la comunidad IT local sobre la inteligencia artificial generativa, con el objetivo de identificar qué temas se mencionan con mayor frecuencia y qué actitudes predominan mayormente (p. ej., entusiasmo, escepticismo o temor). Mediante técnicas de minería de texto y procesamiento de lenguaje natural, se buscará contrastar las hipótesis planteadas, evaluando si el foco de las discusiones está puesto en los usos prácticos de estas tecnologías o en sus posibles consecuencias éticas, laborales y sociales.
Para ello, se aplicará un enfoque metodológico mixto que incluirá análisis de frecuencia de términos, detección de bigramas, modelado temático (LDA), análisis de sentimiento y extracción de entidades (NER). El corpus también permitirá observar patrones discursivos y relaciones entre tópicos y emociones, con lo que se logrará una base para interpretar cómo percibe esta comunidad el avance de herramientas como ChatGPT o GitHub Copilot. En última instancia, con el corpus se busca conocer las tensiones, expectativas y valoraciones que circulan en torno a la IA generativa en la industria IT de nuestro país.