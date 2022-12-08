from django.shortcuts import render

from lessons.forms.administrator.transaction_filter_form import \
    TransactionFilterForm
from lessons.helpers import get_balance_for_student, get_invoice_amount
from lessons.models import Invoice, Payment, User

# Generate the cards for the balance transaction, creating a list of balances for each student
def generate_cards_for_balances_transaction_type(student):
    # Generate list of balances for each student
    balances = []

    if student == "all":
        students = User.objects.filter(role="Student")

        for student in students:
            balances.append({"student": student, "amount": get_balance_for_student(student)})
    else:
        balances.append({"student": student, "amount": get_balance_for_student(student)})

    # Convert these balances to cards
    def convert_balance_to_card(balance):
        return {
            "heading":
                f"{balance['student']}",
            "info": [{
                "title": "Amount Owed",
                "description": balance["amount"],
            }, {
                "title": "Student",
                "description": balance["student"],
            }],
        }

    return map(convert_balance_to_card, balances)

# Generates the cards for the invoice transactions, creating a list of invoices for each student.
def generate_cards_for_invoices_transaction_type(student):
    invoices = []

    if student == "all":
        invoices = Invoice.objects.all()
    else:
        invoices = Invoice.objects.filter(user=student)

    # Convert these invoices to cards
    def convert_invoice_to_card(invoice):
        return {
            "heading":
                invoice,
            "info": [{
                "title": "Amount",
                "description": get_invoice_amount(invoice)
            }, {
                "title": "Student",
                "description": invoice.user,
            }],
        }

    return map(convert_invoice_to_card, invoices)

# Generate card for payment transaction, createing a list of payments for each student.
def generate_cards_for_payments_transaction_type(student):
    payments = []

    if student == "all":    # Creating a filter for the students
        payments = Payment.objects.all()
    else:
        payments = Payment.objects.filter(user=student)

    # Convert these payments to cards
    def convert_payment_to_card(payment):
        return {
            "heading":
                payment.user,
            "info": [{
                "title": "Amount",
                "description": f"£{payment.amount_paid}"
            }, {
                "title": "Student",
                "description": payment.user,
            }],
        }

    return map(convert_payment_to_card, payments)

# Generates the card for the transaction
def generate_cards_for_transaction_type(student, transaction_type):
    if transaction_type == "balances":
        return generate_cards_for_balances_transaction_type(student)
    elif transaction_type == "invoices":
        return generate_cards_for_invoices_transaction_type(student)
    elif transaction_type == "payments":
        return generate_cards_for_payments_transaction_type(student)

# Gets the form for the student balance
def student_balances(request):
    if request.method == "POST":
        form = TransactionFilterForm(request.POST)
    else:
        form = TransactionFilterForm(initial={"student_filter": "all", "transaction_filter": "balances"})

    # Get the selected (if any) student and transaction type
    selected_student = form["student_filter"].value()
    transaction_type = form["transaction_filter"].value()

    # Generate cards for that transaction type
    if selected_student == "":
        selected_student = "all"

    if selected_student != "all":
        selected_student = User.objects.get(pk=selected_student)

    cards = generate_cards_for_transaction_type(selected_student, transaction_type)

    return render(
        request, "administrator/student_balances.html", {
            "allowed_roles": ["Administrator"],
            "dashboard": {
                "heading":
                    "Student Balances",
                "subheading":
                    "Check the balances of all and individual students, along with their invoices and payments."
            },
            "form": form,
            "cards": cards
        })
