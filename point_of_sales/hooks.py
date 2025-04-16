app_name = "point_of_sales"
app_title = "Point Of Sales"
app_publisher = "Hendro Steven"
app_description = "Point Of Sales"
app_email = "hendro.steven@gmail.com"
app_license = "mit"
app_include_js = "/assets/point_of_sales/js/order_line.js"

print("🔥 HOOKS.PY LOADED")

from point_of_sales.point_of_sales.api.routes import hello

override_http_routes = [
    {
        "method": "GET",
        "path": "/api/hello",
        "handler": "point_of_sales.point_of_sales.api.routes.hello"
    }
]

