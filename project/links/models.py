from django.db import models

class Link(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100, verbose_name='タイトル')
  link = models.TextField(max_length=400, verbose_name='リンク')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title