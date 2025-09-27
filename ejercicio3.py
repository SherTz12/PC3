import requests
import time

def obtener_tipo_cambio_2025():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={anio}"
    datos = []

    for mes in range(1, 13):
        try:
            response = requests.get(url.format(mes=mes, anio=2025))
            response.raise_for_status()
            data = response.json()
            
            if not data:
                print(f"No hay datos para el mes {mes}")
                continue

            for item in data:
                datos.append({
                    "fecha": item["fecha"],
                    "compra": float(item["compra"]),
                    "venta": float(item["venta"]),
                    "diferencia": float(item["venta"]) - float(item["compra"])
                })

            time.sleep(2)

        except requests.RequestException as e:
            print(f"Error al obtener datos del mes {mes}: {e}")

    return datos


def analizar_tipo_cambio(datos):
    if not datos:
        return None

    min_compra = min(d["compra"] for d in datos)
    fechas_min_compra = [d["fecha"] for d in datos if d["compra"] == min_compra]

    max_venta = max(d["venta"] for d in datos)
    fechas_max_venta = [d["fecha"] for d in datos if d["venta"] == max_venta]

    max_diferencia = max(d["diferencia"] for d in datos)
    fechas_max_diferencia = [d["fecha"] for d in datos if d["diferencia"] == max_diferencia]

    return {
        "compra_min": {"valor": min_compra, "fechas": fechas_min_compra},
        "venta_max": {"valor": max_venta, "fechas": fechas_max_venta},
        "dif_max": {"valor": max_diferencia, "fechas": fechas_max_diferencia}
    }


if __name__ == "__main__":
    datos = obtener_tipo_cambio_2025()

    print("\n=== Primeros registros obtenidos ===")
    for d in datos[:10]:  
        print(d)

    resultado = analizar_tipo_cambio(datos)

    if resultado:
        print("\n Compra mínima:", resultado["compra_min"])
        print("Venta máxima:", resultado["venta_max"])
        print("Diferencia máxima:", resultado["dif_max"])
    else:
        print("No se pudieron analizar los datos (lista vacía).")
