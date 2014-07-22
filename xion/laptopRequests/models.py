from django.db import models

#'ENUM' which outlines the possible statuses of equipment
STATI = (
	('New', 'New'),
	('Started', 'Started'),
	('Testing', 'Testing'),
	('Ready', 'Ready'),
	('Archive', 'Archive')
)

#Experiment types
EXPR = (
  ('RT130', 'RT130'),
  ('Q330', 'Q330'),
  ('Texan', 'Texan'),
  ('Other', 'Other')
)

#Computer types
COMP = (
  ('PC', 'PC'),
  ('MAC', 'Mac'),
  ('NOPREF', 'NOPREF'),
)

#Possible equipment owners
OWN = (
  ('PASSCAL', 'PASSCAL'),
  ('FLEX ARRAY', 'FLEX ARRAY'),
  ('OTHER', 'OTHER')
)

class request(models.Model):
    """Defines the request object for the database.
    This outline is copied from the old laptop database which
    this project succeeded.

    status -- the status of the laptop defined by a list of choices
    data -- the date the request was entered
    name -- the name of the requestor
    email -- the email of the requestor
    password -- optional password
    notify -- whether or not to notify by email
    readyby -- the date that the laptop is due
    nlaptops -- the number of laptops Required
    experimentName -- the name of the experimentName
    experimentNumber -- the experiment number
    location -- where the experiment is to take replaces
    backpack -- whether or not to include a backpack
    typeX -- the experiment types
    typeL -- the laptop type
    owner -- the equipment owners
    ninstr -- number of instruments on the experiment
    diskspace -- the amount of diskspace to include
    media -- lists any other media to include
    software -- lists all needed software
    notes -- any additional notes
    """

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
      """Outlines how the object is named in Django Admin.
      This replaces the old 'request object' title with
      something more descriptive:

        EXPERIMENT_NAME -- ENTRY_DATE (YYYY-MM-DD)
      """

      return "{0} -- {1}".format(self.experimentName, self.date)


class note(models.Model):
  """ Outlines the laptop notes which are stored separately from requests
  """

  reqid = models.IntegerField()
  item = models.CharField(max_length=40)
  barcode = models.CharField(max_length=40)
  specs = models.TextField(blank=True)
  status = models.CharField(default='New', blank=True, max_length=40, choices=STATI)
  comments = models.TextField(blank=True)
