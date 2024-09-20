from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm, BookingForm, CustomUserCreationForm
from .models import Event, Booking

def home(request):
    return render(request, 'webapp/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('event_list')
    else:
        form = AuthenticationForm()
    return render(request, 'webapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'webapp/logout.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'webapp/event_list.html', {'events': events})
def add(request):
     if request.method == "POST":
        title=request.POST.get('title','')
        description= request.POST.get('description','')
        location = request.POST.get('location','')
        date = request.POST.get('date', '')
        available_seats =request.POST.get('available_seats','')
        event = Event(title=title,description=description,location=location,date=date,available_seats=available_seats)
        event.save()
     return render(request, 'webapp/add_event.html')


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.user = request.user
            booking.save()
            event.available_seats -= 1
            event.save()
            return redirect('booking_status')
    else:
        form = BookingForm()
    return render(request, 'webapp/event_detail.html', {'event': event, 'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'webapp/register.html', {'form': form})



def booking_status(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Retrieve the number of tickets from the session, default to 0
    number_of_tickets = request.session.get('number_of_tickets', 0)

    # Ensure it's an integer
    try:
        number_of_tickets = int(number_of_tickets)
    except (ValueError, TypeError):
        number_of_tickets = 0

    # Calculate remaining seats after booking
    remaining_seats = event.available_seats

    return render(request, 'webapp/booking_status.html', {
        'event': event,
        'number_of_tickets': number_of_tickets,
        'remaining_seats': remaining_seats
    })



@login_required

def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        number_of_tickets = request.POST.get('number_of_tickets')

        if number_of_tickets:
            number_of_tickets = int(number_of_tickets)

            # Check if there are enough available seats
            if number_of_tickets > event.available_seats:
                messages.error(request, "Not enough seats available.")
                return render(request, 'webapp/book_event.html', {'event': event})

            # Check if the user has already booked this event
            existing_booking = Booking.objects.filter(event=event, user=request.user).first()

            if existing_booking:
                messages.error(request, "You have already booked this event.")
                return render(request, 'webapp/book_event.html', {'event': event})

            # Create a new booking
            Booking.objects.create(
                event=event,
                user=request.user,
                number_of_tickets=number_of_tickets
            )

            # Update the event's available seats
            event.available_seats -= number_of_tickets
            event.save()

            # Store the number of tickets in the session
            request.session['number_of_tickets'] = number_of_tickets

            messages.success(request, "Successfully booked the event!")
            return redirect('booking_status', event_id=event.id)

    return render(request, 'webapp/book_event.html', {'event': event})
