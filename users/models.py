from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Профиль'

    def save(self, *args, **kwargs):
        # Переопределение метода сохранения изображений
        super().save( *args, **kwargs)

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            # Если высота или ширина изображения больше 300, изменяем размер и пересохраняем изображение
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
