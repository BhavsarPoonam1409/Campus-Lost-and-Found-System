
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q

from .models import Item
from .forms import RegisterForm, ItemForm


def home(request):
    lost_items = Item.objects.filter(
        report_type='Lost'
    ).order_by('-created_at')[:4]

    found_items = Item.objects.filter(
        report_type='Found'
    ).order_by('-created_at')[:4]

    context = {
        'lost_items': lost_items,
        'found_items': found_items,
        'lost_count': Item.objects.filter(
            report_type='Lost'
        ).count(),
        'found_count': Item.objects.filter(
            report_type='Found'
        ).count(),
        'returned_count': Item.objects.filter(
            status='Returned'
        ).count(),
    }

    return render(request, 'items/home.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                'Account created successfully!'
            )
            return redirect('home')
    else:
        form = RegisterForm()

    return render(
        request,
        'items/register.html',
        {'form': form}
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Welcome back!')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(
        request,
        'items/login.html',
        {'form': form}
    )


@login_required
def report_item(request, report_type):
    if report_type not in ['Lost', 'Found']:
        messages.error(request, 'Invalid report type.')
        return redirect('home')

    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.report_type = report_type
            item.reported_by = request.user
            item.status = (
                'Lost' if report_type == 'Lost' else 'Found'
            )
            item.save()

            messages.success(
                request,
                f'{report_type} item reported successfully!'
            )

            return redirect(
                'item_detail',
                pk=item.pk
            )
    else:
        form = ItemForm()

    return render(request, 'items/item_form.html', {
        'form': form,
        'report_type': report_type,
        'page_title': f'Report {report_type} Item',
    })


def item_list(request, report_type):
    if report_type not in ['Lost', 'Found']:
        messages.error(request, 'Invalid item type.')
        return redirect('home')

    items = Item.objects.filter(
        report_type=report_type
    ).select_related('reported_by').order_by('-created_at')

    query = request.GET.get('q', '').strip()

    if query:
        items = items.filter(
            Q(item_name__icontains=query) |
            Q(category__icontains=query)
        )

    return render(request, 'items/item_list.html', {
        'items': items,
        'report_type': report_type,
        'query': query,
    })


def item_detail(request, pk):
    item = get_object_or_404(
        Item.objects.select_related('reported_by'),
        pk=pk
    )

    return render(request, 'items/item_detail.html', {
        'item': item,
    })


@login_required
def edit_item(request, pk):
    item = get_object_or_404(
        Item,
        pk=pk,
        reported_by=request.user
    )

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Report updated successfully!'
            )
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)

    return render(request, 'items/item_form.html', {
        'form': form,
        'report_type': item.report_type,
        'page_title': 'Edit Report',
        'item': item,
    })


@login_required
def delete_item(request, pk):
    item = get_object_or_404(
        Item,
        pk=pk,
        reported_by=request.user
    )

    if request.method == 'POST':
        report_type = item.report_type
        item.delete()

        messages.success(
            request,
            'Report deleted successfully!'
        )

        if report_type == 'Lost':
            return redirect('lost_items')

        return redirect('found_items')

    return render(request, 'items/confirm_delete.html', {
        'item': item,
    })


@login_required
def update_status(request, pk):
    item = get_object_or_404(
        Item,
        pk=pk,
        reported_by=request.user
    )

    if request.method == 'POST':
        new_status = request.POST.get('status')

        allowed_statuses = {
            'Lost': ['Found', 'Returned'],
            'Found': ['Returned'],
            'Returned': [],
        }

        if new_status in allowed_statuses.get(
            item.status, []
        ):
            item.status = new_status
            item.save()
            messages.success(
                request,
                'Item status updated successfully!'
            )
        else:
            messages.error(
                request,
                'Invalid status update.'
            )

    return redirect('item_detail', pk=item.pk)


@login_required
def my_reports(request):
    items = Item.objects.filter(
        reported_by=request.user
    ).order_by('-created_at')

    return render(request, 'items/my_reports.html', {
        'items': items,
    })

