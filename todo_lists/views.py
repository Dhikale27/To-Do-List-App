from django.shortcuts import redirect, render
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    '''
    Process:
        1. Check for request method.
        2. If condition is true then follow steps from 3 to 9.
        3. grab the data we enter in form in variable 'form'.
        4. check for enterd data validation.
        5. if data is valid the follow the step from 6 to 9.
        6. save that data in database using 'save' method.
        7. grab all item/entries in database in variable by making query.
        8. get the message to display on webpage.
        9. pass all the greabed item to further process to desplay on webpage.
        10. if condition is not true then follow step 7 and 9.
    '''
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()

            all_items = List.objects.all()
            messages.success(
                request, "You Have added new task, all the best!", )
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items})


def about(request):
    return render(request, 'about.html', {})


def delete(request, list_id):
    '''
    >proces is grab the item from database using 'list_id' and use delete method
    >Process:
        1. Grab The item from Database i.e. use 'object' manager to get the item
        2. make query to delete the item
        3. get massage to display on webpage
        4. after delete get to home page using redirect method

    '''
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, "Item has been deleted", )
    return redirect('home')


def cross_off(request, list_id):
    '''
    >Process:
        1. Make a query to grab the object which we want to cross off.
        2. Make changes in the given object.
        3. Save the changes we make.
        4. After cross off redirect to the 'home' page.
    '''
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()

    return redirect('home')


def uncross(request, list_id):
    '''
        >Process:
        1. Make a query to grab the object which we want to cross off.
        2. Make changes in the given object.
        3. Save the changes we make.
        4. After cross off redirect to the 'home' page.

    '''
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()

    return redirect('home')


def edit_item(request, list_id):
    '''
    1. Check for request method. If method is 'POST' then follow steps from 2 to 7
    2. grab the object which we want to change.
    3. Use form to make changes in objects.
    4. Check for validation of form. If form is valid then follow steps from 5 to 7
    5. Save the changes we make.
    6. Get the message to display on web page.
    7. After making changes we rediect to home page.
    8. If condition is not true then follow steps from 9 to...
    9. Grab the object we want to edit.
    10. Show this item on new webpage.


    '''

    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        # if not provide 'instance' attribute then no change will take palce
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()

            messages.success(
                request, "Item has been Edited", )
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
