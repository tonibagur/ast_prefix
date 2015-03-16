from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class ASTNode(MPTTModel):
    order = models.IntegerField()
    name = models.CharField(max_length=255)
    type_str = models.CharField(max_length=255)
    content = models.TextField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    line_start=models.IntegerField(null=True)
    col_start=models.IntegerField(null=True)
    line_end=models.IntegerField(null=True)
    col_end=models.IntegerField(null=True)
    class MPTTMeta:
        order_insertion_by = ['order']