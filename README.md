# quantum-drug-discovery
Quantum-Enhanced Machine Learning platform for drug discovery using Qiskit, RDKit, and Flask with hybrid quantum-classical algorithms (QSVM, VQE, QAOA).

sudo apt update && sudo apt upgrade -y

# Essential tools
sudo apt install -y build-essential git wget curl unzip tree

# Check Python (system)
python3 --version

cd ~

# Download Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install
bash Miniconda3-latest-Linux-x86_64.sh

source ~/.bashrc

conda --version

conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

conda create -n quantum-drug python=3.10 -y

conda activate quantum-drug

pip install --upgrade pip

pip install pandas scipy matplotlib seaborn scikit-learn

pip install "numpy<2.0"

# RDKit MUST be installed via conda
conda install -c conda-forge rdkit -y

# ChEMBL dataset API
pip install chembl-webresource-client

pip install pennylane
pip install qiskit qiskit-aer qiskit-nature

pip install mlflow optuna

pip install flask

conda install -c conda-forge pyscf -y

python - <<EOF
import numpy
import pandas
import sklearn
import rdkit
import pennylane
import qiskit
import mlflow
import pyscf

print("✅ ALL LIBRARIES INSTALLED SUCCESSFULLY")
EOF

mkdir -p quantum-drug-discovery/{data,src,results}
cd quantum-drug-discovery
tree

touch src/01_dataset_import.py \
      src/02_preprocessing.py \
      src/03_classical_ml.py \
      src/04_qsvm.py \
      src/05_vqe.py \
      src/06_qaoa.py \
      src/07_hybrid_loop.py \
      src/08_mlflow_tracking.py


nano src/01_dataset_import.py

python src/01_dataset_import.py


nano src/02_preprocessing.py

python src/02_preprocessing.py


nano src/03_classical_ml.py

python src/03_classical_ml.py


nano src/04_qsvm.py

python src/04_qsvm.py


nano src/05_vqe.py

python src/05_vqe.py


nano src/06_qaoa.py

python src/06_qaoa.py


nano src/07_hybrid_loop.py

python src/07_hybrid_loop.py


nano src/08_mlflow_tracking.py

python src/08_mlflow_tracking.py



mlflow ui \
--host 0.0.0.0 \
--port 5000 \
--cors-allowed-origins '*' \
--allowed-hosts '*'

sudo ufw allow 5000

fuser -k 5000/tcp

🌐 ACCESS IN BROWSER
http://YOUR_PUBLIC_IP:5000

python app.py




## 📸 Screenshots

### 🏠 Home Page
![Home](images/home.png)

### 📊 Results Dashboard
![Results](images/results.png)

### 🧠 Prediction Page
![Predict](images/predict.png)


## 🚀 Live Demo

Run the application using Docker:

```bash
docker run -p 8000:8000 farman1/quantum-drug-app
