from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from carWashMng.models import MainMenu, Profile, Product, Cart, CartItem
from carWashMng.models import Service
from carWashMng.models import Booking
from carWashMng.forms import BookingForm, ProfileForm


# Create your views here.


def index(request):
    return render(request,
                  'carWashMng/index.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


def home(request):
    return render(request,
                  'carWashMng/home.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )


def aboutUs(request):
    return render(request,
                  'carWashMng/aboutUs.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):

        response = super().form_valid(form)

        user = form.instance
        Profile.objects.get_or_create(user=user)

        return response


def service_s(request):
    services = Service.objects.all()
    for s in services:
        s.picture = s.picture.url[9:]
    return render(request,
                  'carWashMng/services.html',
                  {
                      'services': services,
                      'item_list': MainMenu.objects.all(),
                  })


def product_list(request):
    products = Product.objects.all()
    for p in products:
        p.picture = p.picture.url[9:]
    return render(request,
                  'carWashMng/product_list.html',
                  {
                      'products': products,
                      'item_list': MainMenu.objects.all(),
                  })


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.picture = product.picture.url[9:]
    return render(request,
                  'carWashMng/product_detail.html',
                  {
                      'product': product,
                      'item_list': MainMenu.objects.all(),
                  })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    total_price = sum(item.total_price for item in cart_items)
    return render(request,
                  'carWashMng/view_cart.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'total_price': total_price,
                      'cart_items': cart_items,
                  })


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')


@login_required
def increase_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    if cart_item.quantity < cart_item.product.stock:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')


@login_required
def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    # Process the payment here (integration with payment gateway required)
    cart_items.delete()
    return HttpResponse(f"Checkout successful. Total amount: ${total_price}")


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'carWashMng/booking_list.html',
                  {
                      'bookings': bookings,
                      'item_list': MainMenu.objects.all(),
                  })


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Do not save the form to the database yet
            booking.user = request.user  # Set the user to the currently logged-in user
            booking.save()  # Save the booking with the user information
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'carWashMng/booking.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                   })


def check_availability(request):
    date = request.GET.get('date')
    time = request.GET.get('time')
    available = not Booking.objects.filter(booking_date=date, booking_time=time).exists()
    return JsonResponse({'available': available})


@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'carWashMng/profile.html',
                  {
                      'profile': profile,
                      'bookings': bookings,
                      'item_list': MainMenu.objects.all(),
                  })


@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'carWashMng/profile_edit.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                  })

