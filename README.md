# Algoritmo Shor para factorización de números utilizando Qiskit en Python

## 1. Preparación del ambiente de trabajo:
SO: VM Ubuntu 22.04 LTS

Instalar Python:

Actualizar el sistema operativo:

```code
sudo apt-get update
sudo apt-get upgrade
```

Instalar Python 3.8:

```code
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8 python3.8-venv python3.8-dev
```

Instalar PIP y herramientas necesarias:

```code
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.8 get-pip.py
python3.8 -m pip install --upgrade pip setuptools wheel
sudo apt-get install build-essential cmake ninja-build libblas-dev liblapack-dev
```

Crear y Activar un Entorno Virtual (Para importar librerías específicas del ejercicio):

```code
python3.8 -m venv quantum_env
source quantum_env/bin/activate
```

Instalar Qiskit y sus Componentes:

```code
pip install qiskit==0.43
pip install qiskit-aqua==0.9.0
```

Verificar la Instalación de Qiskit:

```code
python -c "from qiskit.algorithms import Shor; from qiskit import BasicAer; from qiskit.utils import QuantumInstance; print('Qiskit está instalado correctamente')"
```

## 2. Ejecución del ejemplo con Qiskit:

clonar el proyecto y dentro del entorno virtual de python (quantum_env)

ejecutar el archivo shor_example.py:

```code
python shor_example.py
```

Resultado esperado:

```code
Resultado de Shor:
{'factors': [[3, 5]], 'successful_counts': 17, 'total_counts': 63}
Factores encontrados: [[3, 5]]
```

