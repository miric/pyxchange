from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from random import randint
from django.utils.baseconv import base56


class Image(models.Model):
    # For future auth feature implementation
    # user = models.ForeignKey(User, default=1)
    img = models.ImageField('Image',
                            upload_to='%I')
    desc = models.CharField('Description',
                            max_length=500,
                            help_text='Up to 500 characters')
    slug = models.SlugField(max_length=6,
                            unique=True)
    upl_date = models.DateTimeField('Uploaded',
                                    default=datetime.now)
    rev_date = models.DateTimeField('Last reviewed',
                                    null=True)
    rev_count = models.PositiveIntegerField('Reviews',
                                            default=0)
    like_count = models.PositiveIntegerField('Likes',
                                             default=0)

    def get_absolute_url(self):
        return reverse('pyxchange:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{} - {}'.format(self.slug, self.desc)

    @staticmethod
    def generate_slug():
        slug = base56.encode(randint(0, 0x7fffffff))
        return slug
