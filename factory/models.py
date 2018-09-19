from django.shortcuts import render
from django.db import models
from django.utils.text import slugify
# Create your views here.
from django.urls import reverse


class FactoryContact(models.Model):

    first_name = models.CharField('Contact First Name', max_length=30, blank=True)
    last_name = models.CharField('Contact Last Name', 'contact_last_name', max_length=30, blank=True)
    phone = models.CharField('Phone Number', 'contact_phone_number', blank=True, max_length=30)
    email = models.EmailField('Contact Email', 'contact_email', max_length=30, blank=True)
    slug = models.SlugField("Slug", blank=True, help_text="Slug Field")

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        slug1 = slugify(self.first_name)
        slug2 = slugify(self.id)
        slugs = slug1+" "+slug2
        self.slug = slugify(slugs)
        super(FactoryContact, self).save(*args, **kwargs)

    def get_absolute_url(self):

        #return reverse('customer_detail', args=[str(self.pk)])
        return reverse('factory:factory_contact_detail', kwargs={'pk':self.id})

    def get_update_url(self):

        return reverse('factory:update_factory_contact', kwargs={'pk': self.id})


class Factory(models.Model):

    name = models.CharField("Company Name", "name", max_length=64)
    contact_name = models.ForeignKey("factory.FactoryContact", max_length=64, blank=True, on_delete='CASCADE')
    address1 = models.CharField("Address1", "address1", max_length=64, blank=True)
    address2 = models.CharField("Address2", "address2", max_length=64, blank=True)
    address3 = models.CharField("Address3", "address3", max_length=64, blank=True)
    country = models.CharField("country", "coutnry", max_length=64, blank=True)
    state = models.CharField("State-Province", "state/prov", max_length=64, blank=True)
    zip = models.CharField("Zip or Postal Code", "zip-postal", max_length=10, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    website = models.URLField("Website", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdOn = models.DateTimeField("Created on", auto_now_add=True)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField("Slug", blank=True, help_text="Slug Field")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug1 = slugify(self.name)
        slug2 = slugify(self.id)
        slugs = slug1+" "+slug2
        self.slug = slugify(slugs)
        super(Factory, self).save(*args, **kwargs)

    def get_absolute_url(self):

        #return reverse('customer_detail', args=[str(self.pk)])
        return reverse('factory:factory_detail', kwargs={'pk':self.pk})

    def get_update_url(self):

        return reverse('factory:update_factory', kwargs={'pk': self.pk})