import customtkinter as ctk
import whois
import requests
import subprocess
import platform

# --- CONFIGURACIÓN DE APARIENCIA ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AppOSINT(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Herramienta de Análisis OSINT v1.0 - Educativo")
        self.geometry("600x700")

        # --- AVISO LEGAL (Disclaimer) ---
        self.label_legal = ctk.CTkLabel(
            self,
            text="AVISO LEGAL: Esta herramienta es solo para fines educativos y auditorías autorizadas.\n"
            "Cualquier modificación o uso indebido es responsabilidad exclusiva del usuario.",
            text_color="#FF5555",
            font=("Roboto", 11, "bold"),
        )
        self.label_legal.pack(pady=10)

        # --- ENTRADA DE DATOS ---
        self.label_instrucciones = ctk.CTkLabel(
            self,
            text="Introduce una IP o Dominio (ej: google.com)",
            font=("Roboto", 14),
        )
        self.label_instrucciones.pack(pady=5)

        self.entrada = ctk.CTkEntry(self, placeholder_text="IP o Dominio...", width=350)
        self.entrada.pack(pady=10)

        # --- BOTONES DE ACCIÓN ---
        self.frame_botones = ctk.CTkFrame(self)
        self.frame_botones.pack(pady=10)

        self.btn_geo = ctk.CTkButton(
            self.frame_botones, text="Geolocalización IP", command=self.obtener_geo
        )
        self.btn_geo.grid(row=0, column=0, padx=10, pady=5)

        self.btn_whois = ctk.CTkButton(
            self.frame_botones, text="Consultar WHOIS", command=self.obtener_whois
        )
        self.btn_whois.grid(row=0, column=1, padx=10, pady=5)

        self.btn_ping = ctk.CTkButton(
            self.frame_botones, text="Realizar Ping", command=self.hacer_ping, width=300
        )
        self.btn_ping.grid(row=1, column=0, columnspan=2, pady=10)

        # --- ÁREA DE RESULTADOS ---
        self.resultado_txt = ctk.CTkTextbox(
            self, width=550, height=350, font=("Consolas", 12)
        )
        self.resultado_txt.pack(pady=20, padx=20)

        # Créditos
        self.label_creditos = ctk.CTkLabel(
            self,
            text="Desarrollado con fines académicos | Basado en librerías Open Source",
            font=("Roboto", 10),
        )
        self.label_creditos.pack(side="bottom", pady=5)

    def limpiar_y_escribir(self, texto):
        self.resultado_txt.delete("1.0", "end")
        self.resultado_txt.insert("0.0", texto)

    # --- FUNCIÓN 1: GEOLOCALIZACIÓN MEJORADA ---
    def obtener_geo(self):
        objetivo = (
            self.entrada.get().strip().replace("https://", "").replace("http://", "")
        )
        # Quitamos el 'www.' si existe para la geolocalización por API
        if objetivo.startswith("www."):
            objetivo = objetivo[4:]

        try:
            # Usamos una URL de API que acepta tanto dominios como IPs
            r = requests.get(f"http://ip-api.com/json/{objetivo}").json()

            if r.get("status") == "success":
                info = (
                    f"--- GEO-IP PÚBLICA ---\n"
                    f"IP: {r.get('query')}\n"
                    f"ISP: {r.get('isp')}\n"
                    f"Organización: {r.get('org')}\n"
                    f"Ciudad: {r.get('city')}\n"
                    f"País: {r.get('country')}\n"
                    f"Lat/Lon: {r.get('lat')}, {r.get('lon')}\n"
                    f"----------------------"
                )
            else:
                info = f"Error: No se encontraron datos para {objetivo}"

            self.limpiar_y_escribir(info)
        except Exception as e:
            self.limpiar_y_escribir(f"Error de conexión: {e}")

    # --- FUNCIÓN 2: WHOIS MEJORADO ---
    def obtener_whois(self):
        objetivo = self.entrada.get().strip()
        try:
            # WHOIS funciona mejor sin 'www.'
            if objetivo.startswith("www."):
                objetivo = objetivo[4:]

            w = whois.whois(objetivo)

            # Verificamos si trajo datos
            if w.domain_name:
                # --- Lógica para limpiar la fecha ---
                fecha = w.creation_date
                if isinstance(fecha, list):
                    # Si es una lista (como en google.com), tomamos el primer elemento
                    fecha = fecha[0]

                # Formateamos la fecha a DD/MM/AAAA si existe, sino ponemos "No disponible"
                fecha_bonita = fecha.strftime("%d/%m/%Y") if fecha else "No disponible"
                # ------------------------------------

                info = (
                    f"--- WHOIS DE DOMINIO ---\n"
                    f"Dominio: {w.domain_name}\n"
                    f"Registrador: {w.registrar}\n"
                    f"País: {w.country}\n"
                    f"Fecha Creación: {fecha_bonita}\n"
                    f"------------------------"
                )
            else:
                info = "No se encontraron datos WHOIS detallados."

            self.limpiar_y_escribir(info)
        except Exception as e:
            self.limpiar_y_escribir(f"Error al obtener WHOIS: {e}")

    # --- FUNCIÓN 3: PING ---
    def hacer_ping(self):
        objetivo = self.entrada.get()
        # Ajuste de comando según sistema operativo
        param = "-n" if platform.system().lower() == "windows" else "-c"
        comando = ["ping", param, "1", objetivo]

        try:
            resultado = subprocess.run(comando, capture_output=True, text=True)
            if resultado.returncode == 0:
                self.limpiar_y_escribir(
                    f"Ping exitoso a {objetivo}:\n\n{resultado.stdout}"
                )
            else:
                self.limpiar_y_escribir(f"El host {objetivo} no responde.")
        except:
            self.limpiar_y_escribir("Error al ejecutar el comando Ping.")


if __name__ == "__main__":
    app = AppOSINT()
    app.mainloop()
