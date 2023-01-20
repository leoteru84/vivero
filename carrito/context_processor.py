def total_factura(request):
    total = 0
    if request.user.is_authenticated:
        if request.session["carrito"].items():
            for key, value in request.session["carrito"].items():
                total += float(value["acumulado"])
    return {"total_factura": total}