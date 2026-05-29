#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <chrono> // Añadido para medir el tiempo

// Función map MODIFICADA: simula el procesamiento a gran escala multiplicando el texto
void map(const std::string &texto, std::map<std::string, int> &frecuencias) {
    // 10000 = Escala Baja 
    // 50000 = Escala Media   FABI HAY QUE PROBAR CON ESOS 3 VALORES DE LA ESCALA PARA CACHAR COMO CAMBIA
    // 100000 = Escala Alta
    const int ESCALA = 10000; 

    for (int i = 0; i < ESCALA; ++i) {
        std::istringstream iss(texto);
        std::string palabra;
        while (iss >> palabra) {
            ++frecuencias[palabra];
        }
    }
}

// Función reduce: combina las frecuencias de palabras de varios mapas (Intacta)
void reduce(const std::vector<std::map<std::string, int>> &mapas, std::map<std::string, int> &resultado) {
    for (const auto &mapa : mapas) {
        for (const auto &par : mapa) {
            resultado[par.first] += par.second;
        }
    }
}

int main() {
    // Datos de entrada: un vector de textos (Intacto)
    std::vector<std::string> entradas = {
        "MapReduce es un modelo de programación",
        "MapReduce permite procesar grandes volúmenes de datos",
        "MapReduce se popularizó con Hadoop",
    };

    // --- Inicio de la medición de tiempo ---
    auto t0 = std::chrono::high_resolution_clock::now();

    // Aplica la función map a cada entrada
    std::vector<std::map<std::string, int>> mapas(entradas.size());
    for (size_t i = 0; i < entradas.size(); ++i) {
        map(entradas[i], mapas[i]);
    }

    // Aplica la función reduce a los mapas para obtener el resultado final
    std::map<std::string, int> resultado;
    reduce(mapas, resultado);

    auto t1 = std::chrono::high_resolution_clock::now();
    double tiempo = std::chrono::duration<double, std::milli>(t1 - t0).count();
    // --- Fin de la medición ---

    // Imprime el resultado
    for (const auto &par : resultado) {
        std::cout << par.first << ": " << par.second << std::endl;
    }

    // Corrección del error de sintaxis del return original (era : en vez de ;)
    std::cout << "\n[Tiempo de ejecucion]: " << tiempo << " ms" << std::endl;
    return 0;
}