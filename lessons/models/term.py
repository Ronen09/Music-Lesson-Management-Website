from django.db import models


class Term(models.Model):
    # Represents order in year, e.g. is this second term out of the six terms in a year?
    order = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
