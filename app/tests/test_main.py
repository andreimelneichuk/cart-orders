from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={"name": "Laptop", "description": "Gaming Laptop", "price": 1500.0, "stock": 10})
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"