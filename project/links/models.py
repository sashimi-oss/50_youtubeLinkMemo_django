from django.db import models

class Category(models.Model):
  category_id = models.AutoField(primary_key=True)
  category = models.CharField(max_length=30, verbose_name='カテゴリー')

  def __str__(self):
    return self.category


class Link(models.Model):
  link_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100, verbose_name='タイトル')
  link = models.TextField(max_length=400, verbose_name='リンク')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=4)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title