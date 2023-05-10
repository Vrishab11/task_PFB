from django.shortcuts import render


from django.shortcuts import render, redirect  
from customer.forms import CustomerForm  
from customer.models import Customer
  

def cust(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            cid = form.cleaned_data['cid']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            form.save()
            return redirect('show')
    else:
        form = CustomerForm() 
    return render(request,'index.html',{'form':form})  
def show(request):  
    customers = Customer.objects.all()  
    return render(request,"show.html",{'customers':customers})  
def edit(request, id):  
    customer = Customer.objects.get(id=cid)  
    return render(request,'edit.html', {'customer':customer})  
def update(request, id):
    customer = Customer.objects.get(id=cid)  
    form = CustomersForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'customer': customer})  
def destroy(request, id):
    try:
        customer = Customer.objects.get(id=cid)
    except Customer.DoesNotExist:
        return redirect('customer_list')

    customer.delete()
    return redirect('customer_list')