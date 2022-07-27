from calculator import calculator
from sanic import Sanic
from sanic.response import text
from sanic_openapi import doc
from sanic_openapi import openapi2_blueprint


app = Sanic("test_sanic_app")
app.blueprint(openapi2_blueprint)


@app.route("/", methods=["GET"])
async def home(request):
    return text("Mathmatic API", status=200)


description = """
Here you can sum, subtract, divide and multiple.
To do it, you have to send:

    request = {
        "first_number": int
        "second_number": int
        "operation": str
    }

To sum use "operation": "+"
To subtract use "operation": "-"
To multiply use "operation": "*"
To divide use "operation": "/"

"""


@app.route("calculator", methods=["POST"])
@doc.summary("Basic calculator with basic operations.")
@doc.description(description)
async def operations(request):
    try:
        data = request.json
        first_number = data["first_number"]
        second_number = data["second_number"]
        operation = data["operation"]
        print("asdasssssssssssssssssss")
        result = await calculator(first_number, second_number, operation)
        print("lllllllllllllllllllll")

        return text(f"The result is: {result}", status=200)

    except Exception as err:
        return text(f"Something is not working. Error: {err}", status=500)


if __name__ == "__main__":
    app.run()
