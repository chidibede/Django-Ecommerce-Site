from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import checkoutForm, contactForm
from django.views.generic import ListView, DetailView
from .models import Smart_Watch, Essential_Oil, Adult_Product



class HomeView(ListView):
    template_name = "shop/home.html"
    context_object_name = "smart_watches"

    def get_context_data(self, **kwargs):
      context = super(HomeView, self).get_context_data(**kwargs)
      context.update({
        'essential_oils': Essential_Oil.objects.all(),
        'adult_products': Adult_Product.objects.all()

      })
      return context

    def get_queryset(self):
     return Smart_Watch.objects.all()
    



class SmartWatchView(ListView):
    template_name = "shop/smart_watches.html"
    context_object_name = "smart_watches"

    def get_queryset(self):
       return Smart_Watch.objects.order_by('name')




class EssentialOilView(ListView):
    template_name = "shop/essential_oils.html"
    context_object_name = "essential_oils"

    def get_queryset(self):
       return Essential_Oil.objects.order_by('name')




class AdultProductView(ListView):
    template_name = "shop/adult_products.html"
    context_object_name = "adult_products"

    def get_queryset(self):
       return Adult_Product.objects.order_by('name')




class SmartWatchDetailView(DetailView):
  model = Smart_Watch
  template_name = 'shop/smart_watch_details.html'


class EssentialOilDetailView(DetailView):
  model = Essential_Oil
  template_name = 'shop/essential_oil_details.html'


class AdultProductDetailView(DetailView):
  model = Adult_Product
  template_name = 'shop/adult_product_details.html'



def checkout(request):
  my_message = []
  if request.method=='POST':
    form = checkoutForm(request.POST)
    if form.is_valid():
      Subject = "Product Order"
      Full_name = form.cleaned_data['Full_name']
      Address = form.cleaned_data['Address']
      Phone_number = form.cleaned_data['Phone_number']
      Email = form.cleaned_data['Email']
      State = form.cleaned_data['State']
      my_message.append(Full_name)
      my_message.append(Address)
      my_message.append(Phone_number)
      my_message.append(State)

      try:
        send_mail(Subject, Email, my_message, ['chidibede@gmail.com'])
      except BadHeaderError:
        return HttpResponse("Invalid Header Found")
      return redirect('thanks')
  else:
    form = checkoutForm()

  return render(request, 'shop/checkout.html', {'form':form})


def contact(request):
  my_message = []
  if request.method=='POST':
    form = contactForm(request.POST)
    if form.is_valid():
      Subject = form.cleaned_data['Subject']
      Full_name = form.cleaned_data['Full_name']
      Email = form.cleaned_data['Email']
      my_message.append(Full_name)
      
      try:
        send_mail(Subject, Email, my_message, ['chidibede@gmail.com'])
      except BadHeaderError:
        return HttpResponse("Invalid Header Found")
      return redirect('thanks')
  else:
    form = contactForm()

  return render(request, 'shop/contact_us.html', {'contact_form':form})


def about(request):
  return render(request, 'shop/about.html')

def thanks(request):
  return HttpResponse("Thanks for shopping with us. Your order is being processed and will be delivered to you within 3 days")