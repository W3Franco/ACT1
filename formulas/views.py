from django.shortcuts import render
from .forms import FormulaForm
from sympy import sympify, symbols, SympifyError, Number, Add, Mul, Pow


def input_formula(request):
    result = None
    variables = None
    numbers = None
    operators = None
    error = None
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            formula = form.cleaned_data['formula']
            try:
                # Use sympy to evaluate the formula
                expr = sympify(formula)
                result = expr

                # Extract variables used in the expression
                variables = expr.free_symbols  # Get the free symbols (variables)

                # Extract numerical constants used in the expression
                numbers = {n for n in expr.atoms(Number)}  # Get all numeric constants

                # Extract operators used in the expression
                operators = {op for op in expr.atoms(Add) | expr.atoms(Mul) | expr.atoms(Pow)}  # Get all operators
            except SympifyError:
                error = "Invalid formula. Please enter a valid mathematical expression."
    else:
        form = FormulaForm()

    return render(request, 'formulas/input_formula.html', {
        'form': form,
        'result': result,
        'variables': variables,
        'numbers': numbers,
        'operators': operators,
        'error': error
    })