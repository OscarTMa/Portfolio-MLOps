# src/train.py
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train():
    # 1. Cargar datos (Simulamos un ETL)
    print("Cargando datos...")
    data = load_iris()
    X, y = data.data, data.target

    # 2. Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Entrenar
    print("Entrenando modelo...")
    model = RandomForestClassifier(n_estimators=10, max_depth=5)
    model.fit(X_train, y_train)

    # 4. Evaluar
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")

    # 5. Guardar el modelo (Serialización)
    # Esto es CRÍTICO en MLOps: guardar el artefacto
    joblib.dump(model, 'models/model.pkl')
    print("Modelo guardado en models/model.pkl")

if __name__ == "__main__":
    train()
