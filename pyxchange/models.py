from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User

import PIL
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Image(models.Model):
    img = models.ImageField('Image', upload_to='%I')
    img_thumbnail = ImageSpecField(source='',
                                   processors=[ResizeToFill(140, 140)],
                                   format='JPEG',
                                   options={'quality': 85})
    desc = models.CharField('Title', max_length=500, help_text='Up to 500 char.')
    slug = models.SlugField(max_length=6, unique=True)
    upl_date = models.DateTimeField('Uploaded', auto_now_add=True)
    rev_date = models.DateTimeField('Last reviewed', null=True)
    rev_count = models.PositiveIntegerField('Reviews', default=0)
    like_count = models.PositiveIntegerField('Likes', default=0)
    user = models.ForeignKey(User, default=1)

    def get_absolute_url(self):
        return reverse('pyxchange:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{} - {}'.format(self.slug, self.desc)

    # Overriding the method to clean up a garbage upon an object deletion
    def delete(self, *args, **kwargs):
        self.img.delete(save=False)
        super(Image, self).delete(*args, **kwargs)
