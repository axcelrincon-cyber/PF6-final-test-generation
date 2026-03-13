import requests
def invasive_species(num):
    url = "https://api-colombia.com/api/v1/InvasiveSpecie"
    response = requests.get(url)

    if response.status_code == 200:
        especies = response.json()
        if 0 <= num < len(especies):
            especie = especies[num]
            return {
                "nombre": especie.get("commonName", "Desconocido"),
                "nombre_cientifico": especie.get("scientificName", "Desconocido"),
                "origen": especie.get("origin", "No disponible"),
                "impacto": especie.get("impact", "No disponible")
            }
        else:
            return {"error": "Número fuera de rango"}
    else:
        return {"error": "No se pudo conectar con la API"}


def main():
    print("¡Hola, estudiantes!")
    print("Bienvenidos al programa de especies invasoras de Colombia.")

    try:
        num = int(input("Ingrese el número de la especie (ejemplo 0, 1, 2...): "))
        resultado = invasive_species(num)
        print("Información de la especie:")
        print(resultado)
    except ValueError:
        print("Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
