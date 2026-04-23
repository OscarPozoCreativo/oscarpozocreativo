from pathlib import Path

# Cambia este nombre si tu archivo tiene espacios raros
INPUT_FILE = "index.html"
OUTPUT_FILE = "index_reescrito_10_10.html"

text = Path(INPUT_FILE).read_text(encoding="utf-8")

replacements = {
    "Diseño con impacto comercial": "Diseño con impacto comercial real",
    "Diseño sistemas visuales que elevan la marca, ordenan la ejecución y fortalecen la presencia comercial.": "Diseño sistemas visuales para retail y marcas de consumo que elevan percepción, ordenan ejecución y sostienen consistencia a escala.",
    "Soy Oscar Pozo, Senior Design Lead especializado en branding comercial, packaging, material POP y campañas retail. Trabajo para que la marca se vea más clara, más sólida y más consistente entre empaque, punto de venta, editorial y comunicación digital.": "Soy Oscar Pozo, Senior Design Lead enfocado en branding comercial, packaging, POP, editorial retail y campañas multiformato. Mi valor no es solo ejecutar piezas: es convertir complejidad operativa en sistemas visuales claros, replicables y listos para producción real.",

    "años en diseño comercial, branding aplicado y ejecución visual de alto volumen": "años construyendo branding comercial, campañas retail y ejecución visual de alto volumen con criterio de sistema",
    "sucursales en contexto retail donde la consistencia visual importa": "sucursales como contexto real donde la consistencia visual, la velocidad y el control de marca sí importan",
    "presencia de marca entre packaging, POP, editorial, social media y punto de venta": "presencia de marca entre packaging, POP, editorial, social media y punto de venta con lenguaje visual unificado",
    "criterio enfocado en claridad, percepción, escalabilidad y control visual": "criterio orientado a claridad, percepción premium, escalabilidad y control visual sostenido",

    "Diseño para marcas que necesitan orden, coherencia y presencia.": "Diseño para marcas que necesitan orden, coherencia y una presencia comercial difícil de ignorar.",
    "Construyo sistemas visuales que hacen más fuerte la marca entre campañas, retail, packaging y comunicación multicanal.": "Construyo sistemas visuales que reducen improvisación, aceleran implementación y vuelven más sólida la marca entre campañas, retail, packaging y comunicación multicanal.",
    "Branding comercial · Packaging · POP · Campañas retail": "Branding comercial · Packaging · POP · Editorial retail · Campañas multiformato",
    "Branding comercial con pensamiento de sistema": "Branding comercial con pensamiento de sistema y criterio operativo",
    "Ejecución coherente entre canales y formatos": "Ejecución coherente entre canales, piezas y formatos",
    "Dirección visual capaz de escalar sin perder calidad": "Dirección visual capaz de escalar sin perder calidad ni control",

    "Cuando la marca se fragmenta entre campaña, empaque, POP y retail, el negocio pierde claridad.": "Cuando la marca se fragmenta entre campaña, empaque, POP, editorial y retail, el negocio pierde claridad, velocidad y percepción.",
    "Mi trabajo consiste en ordenar esa complejidad para que la comunicación se entienda mejor, la marca se perciba más fuerte y la ejecución visual gane consistencia.": "Mi trabajo consiste en ordenar esa complejidad para que la comunicación se entienda más rápido, la marca se perciba más sólida y la ejecución visual gane consistencia real entre formatos y equipos.",

    "Jerarquía comercial precisa": "Jerarquía comercial que se entiende en segundos",
    "Organizo información, beneficios, categorías y mensajes para que cada pieza comunique con rapidez e intención.": "Organizo información, beneficios, categorías y mensajes para que cada pieza se escanee rápido, reduzca fricción y empuje una decisión clara.",
    "Estructura visual escalable": "Sistema visual preparado para crecer",
    "Desarrollo reglas y patrones reutilizables que permiten crecer sin improvisación ni desgaste visual.": "Desarrollo reglas y patrones reutilizables para que la marca pueda crecer sin improvisación, sin desgaste visual y sin romper consistencia.",
    "Calidad sostenida en entornos reales": "Ejecución sólida en contextos de presión real",
    "Diseño pensando en producción, despliegue, consistencia operativa y presencia visual en contextos de alta exigencia.": "Diseño pensando en producción, despliegue, consistencia operativa y presencia visual en contextos donde el volumen y la velocidad importan.",

    "años de experiencia en branding comercial, retail y ejecución visual aplicada.": "años de experiencia en branding comercial, retail y ejecución visual aplicada con foco en sistema y claridad.",
    "sucursales como contexto real de consistencia visual y operación retail.": "sucursales como contexto real de consistencia visual, despliegue y operación retail.",
    "trabajo aplicado entre packaging, POP, editorial, social media y punto de venta.": "trabajo aplicado entre packaging, POP, editorial, social media y punto de venta con criterio de sistema.",
    "sistemas visuales pensados para repetirse con control, no piezas aisladas.": "sistemas visuales pensados para repetirse con control, no para depender de improvisación ni piezas aisladas.",

    "Tres casos para demostrar criterio, estructura y ejecución visual de nivel senior.": "Tres casos para demostrar por qué este trabajo se paga como senior: criterio, estructura, claridad y aplicación real.",
    "Cada caso está planteado desde problema, enfoque y resultado para que el trabajo se lea como dirección visual aplicada, no como piezas sueltas.": "Cada caso está planteado desde problema, decisión, rol y resultado para que el trabajo se lea como dirección visual aplicada y no como una galería decorativa.",

    "Sistema de packaging para una línea de consumo masivo orientada a legibilidad, diferenciación y presencia de marca.": "Sistema de packaging para una línea de consumo masivo construido para mejorar lectura, diferenciación y control visual de marca.",
    "Diseñé una estructura visual para la línea Gold Selects con el objetivo de mejorar reconocimiento de marca, lectura rápida en anaquel y coherencia entre variantes. El enfoque fue construir un sistema capaz de organizar información y sostener extensión de línea dentro del contexto retail.": "Mi rol fue estructurar una base visual capaz de sostener extensión de línea, diferenciar categorías y mejorar la lectura en anaquel sin perder reconocimiento de marca. El trabajo se resolvió como sistema, no como empaque aislado.",
    "Ordenar beneficios, familias de producto e identidad visual dentro de una estructura clara, reconocible y escalable.": "Ordenar beneficios, familias de producto e identidad visual dentro de una estructura clara, reconocible, replicable y lista para crecimiento.",
    "El empaque fue trabajado como sistema de información visual: jerarquía de marca, contraste funcional, diferenciación cromática por categoría y base adaptable para nuevas variantes.": "Trabajé el empaque como sistema de información visual: jerarquía de marca, contraste funcional, diferenciación cromática por categoría y base adaptable para nuevas variantes y futuras extensiones.",
    "Una presencia más sólida, más ordenada y más consistente, preparada para sostener crecimiento sin perder unidad general.": "Un sistema de empaque más sólido, más ordenado y más fácil de escalar, con mejor lectura y una presencia de marca más consistente en contexto comercial.",
    "Base visual preparada para crecimiento y nuevas variantes.": "Base visual preparada para crecimiento, nuevas variantes y control de línea.",
    "Marca reconocible por encima de la sobrecarga gráfica.": "Marca reconocible por encima del ruido gráfico y la saturación competitiva.",
    "Jerarquía clara para beneficio, categoría y reconocimiento rápido.": "Jerarquía clara para beneficio, categoría, variedad y reconocimiento rápido.",

    "Sistema editorial promocional para campañas retail de alta densidad informativa.": "Sistema editorial promocional para campañas retail de alta densidad, diseñado para claridad, velocidad y consistencia.",
    "Trabajé campañas editoriales promocionales para Plaza Lama en contextos donde conviven múltiples ofertas, categorías, precios y mensajes simultáneos. La solución fue una estructura editorial clara y repetible capaz de sostener orden visual sin debilitar la fuerza comercial.": "Mi rol fue organizar campañas editoriales promocionales para Plaza Lama en contextos donde conviven múltiples ofertas, categorías, precios y mensajes simultáneos. La solución fue una estructura editorial clara y repetible que sostuviera orden visual sin debilitar presión comercial.",
    "Evitar saturación visual dentro de piezas promocionales de alta densidad sin perder impacto ni consistencia general.": "Evitar saturación visual dentro de piezas promocionales de alta densidad sin perder impacto, velocidad de lectura ni consistencia general.",
    "Jerarquía editorial clara, ritmo visual consistente, uso estratégico del color promocional y estructuras capaces de contener complejidad sin ruido.": "Jerarquía editorial clara, ritmo visual consistente, uso estratégico del color promocional y estructuras capaces de contener complejidad sin ruido ni fricción cognitiva.",
    "Una campaña más limpia, más confiable y mejor organizada, alineada con una comunicación promocional fuerte y sostenible.": "Una campaña más limpia, más confiable y mejor organizada, capaz de sostener volumen promocional sin degradar percepción ni legibilidad.",
    "Capacidad para ordenar múltiples ofertas y mensajes sin caos gráfico.": "Capacidad para ordenar múltiples ofertas, precios y mensajes sin caer en caos gráfico.",
    "Sistema pensado para campañas promocionales repetibles y legibles.": "Sistema pensado para campañas promocionales repetibles, legibles y rápidas de adaptar.",
    "Diseño preparado para despliegue rápido dentro de contexto comercial real.": "Diseño preparado para despliegue rápido dentro de un contexto comercial real y exigente.",

    "Exhibidores y material POP diseñados como herramientas de visibilidad y orden comercial.": "Exhibidores y material POP diseñados como herramientas de visibilidad, orden y navegación comercial.",
    "Desarrollé exhibidores y material POP para distintas categorías dentro del entorno retail con enfoque en navegación visual, presencia de marca y organización de producto. El objetivo no fue ocupar espacio, sino convertir ese espacio en una extensión funcional de la marca.": "Mi rol fue desarrollar exhibidores y material POP para distintas categorías dentro del entorno retail con enfoque en navegación visual, presencia de marca y organización de producto. El objetivo no fue ocupar espacio: fue convertir ese espacio en una extensión funcional de la marca.",
    "Crear estructuras que ayudaran a organizar producto, comunicar beneficios y reforzar identidad visual dentro de un entorno comercial competitivo.": "Crear estructuras que ayudaran a organizar producto, comunicar beneficios y reforzar identidad visual dentro de un entorno comercial competitivo y saturado.",
    "Mayor presencia visual y una estructura más ordenada, donde el display opera como herramienta comercial real dentro del punto de venta.": "Mayor presencia visual y una estructura más ordenada, donde el display deja de ser soporte decorativo y opera como herramienta comercial real.",
    "Aplicación directa en contexto retail y punto de venta.": "Aplicación directa en contexto retail y punto de venta, no en escenarios ficticios.",
    "Organización visual por segmento, producto y beneficio.": "Organización visual por segmento, producto, beneficio y navegación.",
    "Estructuras pensadas para lectura a distancia y presencia comercial.": "Estructuras pensadas para lectura a distancia, reconocimiento rápido y presencia comercial.",
    "Lenguaje adaptable para nuevas activaciones y líneas.": "Lenguaje adaptable para nuevas activaciones, temporadas y líneas.",

    "Senior Design Lead con enfoque en branding comercial, retail, packaging y sistemas visuales.": "Senior Design Lead enfocado en branding comercial, retail, packaging y sistemas visuales con criterio de negocio.",
    "Experiencia desarrollada en contextos donde la marca no vive en una sola pieza, sino entre campañas, empaques, promociones, displays, redes y punto de venta. Esa realidad exige criterio de sistema, no solo capacidad de ejecución.": "Mi experiencia se ha construido en contextos donde la marca no vive en una sola pieza, sino entre campañas, empaques, promociones, displays, redes y punto de venta. Esa realidad exige criterio de sistema, no solo capacidad de ejecución.",
    "La dirección visual se aborda desde claridad, control y percepción premium. El objetivo es construir marcas que se vean sólidas, consistentes y listas para crecer sin perder identidad.": "La dirección visual se aborda desde claridad, control y percepción premium. El objetivo es construir marcas que se vean sólidas, consistentes y listas para crecer sin perder identidad ni velocidad de implementación.",

    "Enfoque profesional": "Cómo debe leerse este perfil",
    "Perfil orientado a roles donde el diseño tiene impacto estructural dentro de branding, campañas, retail y sistemas visuales aplicados.": "Este perfil debe leerse como una combinación de criterio, estructura y ejecución para roles donde el diseño tiene impacto directo en branding, campañas, retail y sistemas visuales aplicados.",
    " para marcas comerciales, campañas retail y sistemas visuales aplicados.": " para marcas comerciales, campañas retail y sistemas visuales aplicados donde la consistencia y la claridad tienen impacto real.",
    "Art Director": "Dirección visual",
    " en entornos que requieren dirección estética, criterio visual y consistencia multicanal.": " en entornos que requieren dirección estética, criterio visual y consistencia multicanal, sin perder control operativo.",
    "Brand Systems Lead": "Pensamiento de sistema",
    " cuando la prioridad es estructurar lenguaje visual, escalabilidad y orden de marca.": " cuando la prioridad es estructurar lenguaje visual, escalabilidad y orden de marca por encima de la improvisación.",

    "Disponible para oportunidades, colaboraciones y proyectos con foco en branding, retail y sistemas visuales.": "Disponible para roles senior, colaboraciones selectivas y proyectos donde el diseño tenga impacto real en marca, claridad y ejecución.",
    "Para posiciones, colaboraciones o proyectos donde el diseño necesite ordenar comunicación, fortalecer percepción de marca y sostener una ejecución consistente, la conversación está abierta.": "Para posiciones, colaboraciones o proyectos donde el diseño necesite ordenar comunicación, elevar percepción de marca y sostener una ejecución consistente entre múltiples formatos, la conversación está abierta.",
    "Branding comercial, retail, packaging, POP, editorial y sistemas visuales": "Branding comercial, retail, packaging, POP, editorial, campañas multiformato y sistemas visuales",
}

for old, new in replacements.items():
    text = text.replace(old, new)

Path(OUTPUT_FILE).write_text(text, encoding="utf-8")
print(f"Archivo generado: {OUTPUT_FILE}")