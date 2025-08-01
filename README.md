# Cat vs Dog Classifier 🐱🐶

This is a PyTorch-based binary image classification project that predicts whether an input image is of a cat or a dog.
The goal is to demonstrate how to train a simple deep learning model, run inference manually, and eventually integrate CI/CD and MLOps practices using tools like Docker and Jenkins.


---

## 🧠 Model Details

- **Framework**: PyTorch
- **Model Type**: CNN (Convolutional Neural Network)
- **Task**: Binary classification (Cat vs Dog)
- **Input**: RGB image
- **Output**: Class prediction (Cat or Dog)

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd mlops-cat-dog

## 2. Create and activate a venv
python3 -m venv myvenv
source myvenv/bin/activate

##3. Install Dependencies
pip install -r requirements.txt

🏋️‍♂️ Training the Model
Ensure your dataset is placed in the data/ directory with appropriate folder structure:
data/
├── train/
    ├── cat/
    └── dog/

python train.py
This will train a CNN model and save it to model/catdog_model.pt.

🔍 Running Inference
take any image of dog or cat
python inference.py test_dog.jpg

Expected output:
Predicted class: Dog

