from behave import given, when, then
@given("the OrderFlow API is available")
def step_api(context):
    context.response = context.client.get("/health")
@when("I submit a valid order")
def step_order(context):
    context.response = context.client.post("/api/orders", json={"customer_id": 1, "items": [{"price": 10, "quantity": 1}]})
@then("the order should be created")
def step_created(context):
    assert context.response.status_code == 201
