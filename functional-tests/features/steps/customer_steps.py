from behave import given, when, then

@given("the customer directory API is available")
def step_api(context):
    context.response = context.client.get("/health")

@when("I search for a customer")
def step_search(context):
    context.response = context.client.get("/api/customers?name=demo")

@then("the response should be successful")
def step_ok(context):
    assert context.response.status_code == 200
