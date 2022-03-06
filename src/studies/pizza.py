def make_pizza(size, *toppings):
    """Descrever a pizza pedida"""
    print(f"\nFazendo uma pizza tamanho {size}cm com os ingredientes:")
    for topping in toppings:
        print(f"- {topping}")