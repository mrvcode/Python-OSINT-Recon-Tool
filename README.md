Markdown

# 🛡️ Python OSINT Recon-Tool

Una herramienta de interfaz gráfica (GUI) desarrollada en Python para realizar tareas de reconocimiento pasivo (OSINT) y diagnóstico de red. Este proyecto ha sido creado con fines exclusivamente **académicos y de aprendizaje** en el ámbito de la ciberseguridad y la programación.

## ⭐ Características Principales

* **Geolocalización IP:** Consulta la ubicación física, el proveedor de servicios de internet (ISP) y la organización de cualquier dirección IP o dominio.
* **Consulta WHOIS:** Obtiene datos de registro de dominios, incluyendo el registrador, país de origen y fecha de creación (ideal para verificar la legitimidad de un sitio).
* **Diagnóstico de Red (Ping):** Comprueba la latencia y disponibilidad de un host mediante paquetes ICMP.
* **Interfaz Moderna:** Implementada con `CustomTkinter` para ofrecer una experiencia de usuario clara y con soporte para modo oscuro.

---

## ⚙️ Instalación y Uso

Para ejecutar esta herramienta localmente, asegúrate de tener Python instalado y sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/mrvcode/Python-OSINT-Recon-Tool.git](https://github.com/mrvcode/Python-OSINT-Recon-Tool.git)
Instalar dependencias:

Bash

pip install -r requirements.txt
Ejecutar la aplicación:

Bash

python AppOSINT.py
⚠️ AVISO LEGAL IMPORTANTE
ESTE SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO.

Uso Ético: Esta herramienta debe utilizarse únicamente sobre objetivos de los cuales se tenga permiso explícito o sobre infraestructura pública. El usuario asume toda la responsabilidad por las acciones realizadas con este software.

Responsabilidad: El autor no se hace responsable del mal uso, modificaciones o daños que puedan derivarse del uso de esta herramienta en redes ajenas.

Leyes Locales: El acceso no autorizado a sistemas o la realización de escaneos masivos puede ser ilegal en ciertas jurisdicciones. Cumpla siempre con las normativas vigentes.

Modificaciones: Cualquier cambio en el código fuente original es responsabilidad exclusiva de la persona que lo realice.

🧠 Contexto Técnico
En el análisis de amenazas, verificar la antigüedad de un dominio (vía WHOIS) es una técnica clave para detectar posibles servidores de Comando y Control (C2). Muchos ataques de Tunelización DNS (utilizando herramientas especializadas como Iodine o DNScat2) suelen emplear dominios registrados recientemente para evadir filtros de seguridad basados en reputación.

Desarrollado con fines académicos por @mrvcode | 2025 Basado en librerías Open Source: CustomTkinter, python-whois y requests.
