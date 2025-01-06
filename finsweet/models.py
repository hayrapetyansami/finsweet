from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField(db_index=True)
    image = models.ImageField(upload_to="posts", blank=True, null=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Author(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to="authors", blank=True, null=True)
    position = models.CharField(
        max_length=100, db_index=True, blank=True, null=True)
    fb = models.URLField(
        max_length=255,
        unique=True,
        db_index=True,
        blank=True,
        null=True
    )
    x = models.URLField(
        max_length=255,
        unique=True,
        db_index=True,
        blank=True,
        null=True
    )
    ig = models.URLField(
        max_length=255,
        unique=True,
        db_index=True,
        blank=True,
        null=True
    )
    ln = models.URLField(
        max_length=255,
        unique=True,
        db_index=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(
        upload_to="categories",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class About_us(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField(db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Our_mission(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField(db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Our Mission"
        verbose_name_plural = "Our Mission"
