from django.db import models

STATI = (
	('New', 'New'),
	('Started', 'Started'),
	('Testing', 'Testing'),
	('Ready', 'Ready'),
	('Archive', 'Archive')
)

EXPR = (
  ('RT130', 'RT130'),
  ('Q330', 'Q330'),
  ('Texan', 'Texan'),
  ('Other', 'Other')
)

COMP = (
  ('PC', 'PC'),
  ('MAC', 'Mac'),
  ('NOPREF', 'NOPREF'),
)

OWN = (
  ('PASSCAL', 'PASSCAL'),
  ('FLEX ARRAY', 'FLEX ARRAY'),
  ('OTHER', 'OTHER')
)

class request(models.Model):
    status = models.CharField(default='New', blank=True, max_length=40, choices=STATI)
    date = models.DateField()
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    notify = models.BooleanField(blank=True, default=0)
    readyby = models.DateField('Date Required')
    nlaptops = models.SmallIntegerField('# of Laptops')
    experimentName = models.CharField(max_length=40)
    experimentNumber = models.CharField(blank=True, max_length=40)
    location = models.CharField(blank=True, max_length=40)
    backpack = models.BooleanField(default=0)
    typeX = models.CharField("Experiment Type", blank=True, max_length=40, choices=EXPR)
    typeL = models.CharField("Laptop Type", blank=True, max_length=40, choices=COMP)
    owner = models.CharField(blank=True, max_length=40, choices=OWN)
    ninstr = models.SmallIntegerField("# of Instruments", blank=True, default=0)
    diskspace = models.CharField(blank=True, default='', max_length=40)
    media = models.CharField(blank=True, default='', max_length=40)
    software = models.CharField(blank=True, default='', max_length=40)
    notes = models.TextField(blank=True, default='')

    def __unicode__(self):
      return "{0} -- {1}".format(self.experimentName, self.date)
