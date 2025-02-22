from qiskit.algorithms import Shor
from qiskit import BasicAer
from qiskit.utils import QuantumInstance

def main():
    N = 15  # Factorizar 15 => factores (3, 5)
    
    # Crear el backend qasm_simulator
    backend = BasicAer.get_backend('qasm_simulator')
    
    # Usamos QuantumInstance para asociar el backend
    quantum_instance = QuantumInstance(backend)
    
    # Inicializar el algoritmo Shor
    shor = Shor(quantum_instance=quantum_instance)
    
    # Ejecutar el algoritmo
    result = shor.factor(N)
    
    # Imprimir el resultado completo para verificar la estructura
    print("Resultado de Shor:")
    print(result)
    
    # Mostrar el resultado directo si no hay 'successful_counts'
    if hasattr(result, 'factors'):
        print("Factores encontrados:", result.factors)
    else:
        print("No se encontraron factores en el resultado.")
    
if __name__ == "__main__":
    main()
