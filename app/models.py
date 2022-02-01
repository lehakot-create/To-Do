from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username}: {self.rating}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def slug_name(title):
    dct = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO', 'Ж': 'ZH',
           'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L',
           'М': 'M', ' Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
           'Ф': 'F', 'X': 'KH', 'Ц': 'TS', 'Ч': 'CH',
           'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'YU', 'Я': 'YA', ' ': '_'}
    slug = ''
    for el in title:
        slug += dct.get(el.upper(), el)
    return slug


class Task(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    date_time_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateField(blank=True, null=True)
    time_finish = models.TimeField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='Общая')
    slug = models.SlugField(blank=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.ForeignKey('Priority', on_delete=models.CASCADE, default='Normal')
    reminder = models.DateTimeField(blank=True, null=True)

    performed = 'PE'
    complete = 'CO'
    choice = [
        (performed, 'Выполняется'),
        (complete, 'Выполнено'),
    ]
    status = models.CharField(max_length=11, choices=choice, default=performed)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.executor}: {self.title} - {self.date_finish} - {self.time_finish} - {self.status}'

    def save(self, *args, **kwargs):
        self.slug = slug_name(self.title)
        super().save(*args, **kwargs)


class SubTask(models.Model):
    id_task = models.ForeignKey('Task', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    date_time_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateField(blank=True, null=True)
    time_finish = models.TimeField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.ForeignKey('Priority', on_delete=models.CASCADE, default='Normal')
    reminder = models.DateTimeField(blank=True, null=True)
    # control = models.ForeignKey('Control', on_delete=models.CASCADE)
    performed = 'PE'
    complete = 'CO'
    choice = [
        (performed, 'Выполняется'),
        (complete, 'Выполнено'),
    ]
    status = models.CharField(max_length=11, choices=choice, default=performed)

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'

    def __str__(self):
        return f'{self.executor}: {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slug_name(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Priority(models.Model):
    low = 'Low'
    normal = 'Normal'
    high = 'Hign'
    PRIORITY = (
        (low, 'Low'),
        (normal, 'Normal'),
        (high, 'High'),
    )
    name = models.CharField(max_length=6, choices=PRIORITY, default=normal,  unique=True)

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_task = models.ForeignKey('Task', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.id_task}: {self.text}'


class Control(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    control = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Контроль'
        verbose_name_plural = 'Контроль'

    def __str__(self):
        return f'{self.user}-{self.control}'
