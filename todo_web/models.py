from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_name"
            )
        ]

    def __str__(self):
        return self.name


class Task(models.Model):

    content = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(
        auto_now_add=False,
        default=None,
        blank=True,
        null=True
    )
    is_completed = models.BooleanField(default=False)
    tags = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.content
