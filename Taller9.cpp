#include <iostream> 
#include <fstream> 
#include <vector> 
#include <algorithm> 
#include <chrono> 
#include <sys/mman.h> 
#include <sys/stat.h> 
#include <fcntl.h> 
#include <unistd.h> 

using namespace std; 
using namespace chrono; 

auto now(){ return high_resolution_clock::now();} 

double ms(auto t0, auto t1){ 
return duration<double, milli>(t1 - t0).count(); 
} 

// Genera archivo binario con N enteros aleatorios 
void generar_archivo(const string& ruta, size_t n) { 
    ofstream f(ruta, ios::binary); 
    srand(42); 

    for (size_t i = 0; i < n; i++) { 
        int v = rand() % 1000000; 
        f.write(reinterpret_cast<char*>(&v), sizeof(int)); 
    } 

   cout << "Archivo: " << n << " enteros (" << (n * sizeof(int) / 1024.0 / 1024.0) << " MB)\n"; 
} 

 

//Disco 
void bench_disco(const string& ruta, size_t n){ 
    cout << "Modo disco"; 

    // Suma 
    auto t0 = now(); 

    { 

        ifstream f(ruta, ios::binary); 

        long long suma = 0; int v; 

        while (f.read(reinterpret_cast<char*>(&v), sizeof(int))) 

            suma += v; 

        cout << "  Suma: " << suma; 

    } 

    cout << "  [" << ms(t0, now()) << " ms]\n"; 

 

    // Conteo de pares 
    t0 = now(); 
    { 

        ifstream f(ruta, ios::binary); 

        size_t cnt = 0; int v; 
         while (f.read(reinterpret_cast<char*>(&v), sizeof(int))) 

            if (v % 2 == 0) cnt++; 

        cout << "  Pares: " << cnt; 

    } 

    cout << "  [" << ms(t0, now()) << " ms]\n"; 

 

    // Ordenamiento 
    t0 = now(); 

    { 

        vector<int> buf(n); 

        ifstream f(ruta, ios::binary); 

        f.read(reinterpret_cast<char*>(buf.data()), n * sizeof(int)); 

        sort(buf.begin(), buf.end()); 

        cout << "  Ordenamiento: "; 

    } 

    cout << "  [" << ms(t0, now()) << " ms]\n"; 

} 

 

//Memoria 
void bench_memoria(const string& ruta, size_t n) { 
    cout<<" Modo memoria (mmap)"; 

 

    int fd = open(ruta.c_str(), O_RDONLY); 
    size_t tam = n * sizeof(int); 
    int* datos = static_cast<int*>( 

        mmap(nullptr, tam, PROT_READ, MAP_PRIVATE, fd, 0)); 

    close(fd); 

 

    //Suma 

    auto t0 = now(); 
    long long suma = 0; 
    for (size_t i = 0; i < n; i++) suma += datos[i]; 
    cout << "  Suma: " << suma; 
    cout << "  [" << ms(t0, now()) << " ms]\n"; 

 

    //Conteo de pares 

    t0 = now(); 
    size_t cnt = 0; 
    for (size_t i = 0; i < n; i++) if (datos[i] % 2 == 0) cnt++; 
    cout << "  Pares: " << cnt; 
    cout << "  [" << ms(t0, now()) << " ms]\n"; 

 

    //Ordenamiento 

    t0 = now(); 
    vector<int> buf(datos, datos + n); 
    sort(buf.begin(), buf.end()); 
    cout << "  Ordenamiento: "; 
    cout << "  [" << ms(t0, now()) << " ms]\n"; 

 

    munmap(datos, tam);
    } 

 

int main() { 

    const string ruta = "/tmp/datos_bench.bin"; 
    const size_t N = 5000000; // 5M enteros (~20 MB) 
    generar_archivo(ruta, N); 
    bench_disco(ruta, N); 
    bench_memoria(ruta, N); 

    return 0; 
} 