def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_products(client):
    response = client.get("/api/products")
    assert response.status_code == 200
    assert len(response.json) >= 1

def test_create_order(client):
    response = client.post("/api/orders", json={
        "customer_id": 1, "items": [{"price": 12, "quantity": 2}]
    })
    assert response.status_code == 201
