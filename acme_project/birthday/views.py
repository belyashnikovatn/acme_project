from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from birthday.forms import BirthdayForm, ContestForm
from birthday.utils import calculate_birthday_countdown
from birthday.models import Birthday


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 3


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirhdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayCreateView(BirthdayMixin, BirhdayFormMixin,  CreateView):
    pass


class BirthdayUpdateView(BirthdayMixin, BirhdayFormMixin, UpdateView):
    pass


class BirthdayDelete(BirthdayMixin, DeleteView):
    pass


def birthday(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None
    form = BirthdayForm(request.POST or None,
                        files=request.FILES or None,
                        instance=instance)

    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context=context)


# def birthday_list(request):
#     birthdays = Birthday.objects.all().order_by('first_name')
#     paginator = Paginator(birthdays, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj}

#     return render(request, 'birthday/birthday_list.html', context=context)


def delete_birthday(request, pk):
    # Получаем объект модели или выбрасываем 404 ошибку.
    instance = get_object_or_404(Birthday, pk=pk)
    # В форму передаём только объект модели;
    # передавать в форму параметры запроса не нужно.
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    # Если был получен POST-запрос...
    if request.method == 'POST':
        # ...удаляем объект:
        instance.delete()
        # ...и переадресовываем пользователя на страницу со списком записей.
        return redirect('birthday:list')
    # Если был получен GET-запрос — отображаем форму.
    return render(request, 'birthday/birthday.html', context)
