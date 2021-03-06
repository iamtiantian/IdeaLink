from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from accounts.models import Account

class WechatQRCode(models.Model) :
	account = models.OneToOneField(
		Account,
		on_delete = models.CASCADE,
		)

	wechat_openid = models.CharField(max_length=100,primary_key=True)
	qrcode_url = models.CharField(max_length=100,blank=True)

	@classmethod
	def create(cls,account,openid):
		return cls(account = account, wechat_openid = openid)

class Project(models.Model) :
	"""
	Project information , many to many relationship to account

	"""
	
	# Basic info for project
	project_name = models.CharField(max_length=50, unique=True)

	project_description = models.CharField(max_length=140,blank=True)
	project_start_date = models.CharField(max_length=50,blank=True)
	project_expire_date = models.CharField(max_length=50,blank=True)
	project_status = models.CharField(max_length=20)

	project_owner = models.ForeignKey(
		Account,
		on_delete=models.CASCADE
		)
	project_members = models.ManyToManyField(
		Account,
		related_name='%(app_label)s_%(class)s_related')
	project_applicants = models.ManyToManyField(
		Account,
		related_name='%(app_label)s_applicant_related')

	@classmethod
	def create(cls, account, name, description):
		
		return cls(project_owner = account, project_name = name , project_description = description,project_expire_time = datetime.now().strftime("%Y-%m-%d"))

	# Modification update
	def update_project(self,proj_name,proj_description,proj_deadline,proj_status):
		self.project_name = proj_name
		self.project_description = proj_description
		self.project_expire_date = proj_deadline
		self.project_status = proj_status

	def __str__(self) :
		project_info = 'Project: ' + self.project_name
		return project_info
	__repr__ = __str__	



# Task information , many to one relationship to Project
class Task(models.Model) :
	"""
	Task information

	"""
	project = models.ForeignKey(
		Project,
		on_delete = models.CASCADE
		)

	task_name = models.CharField(max_length=50, unique=True)
	task_description = models.CharField(max_length=140,blank=True)
	task_start_date = models.DateField(blank=True)
	task_expire_time = models.DateField(blank=True)
	task_status = models.CharField(max_length=20)

	# members involved in this task , many to many relationship to accounts.Account
	task_members = models.ManyToManyField(Account)
	
	@classmethod
	def create(cls, name, description):
		return cls(task_name = name, task_description = description)
	def change_status(self,status):
		self.task_status = status

	

# Tag information , modified by administrator , many to many relationship to project
class Tag(models.Model) :
	"""
	Tag information

	"""
	tag_name = models.CharField(max_length=50,unique=True)
	tag_description = models.CharField(max_length=80 , unique=True)

	# Projects envolved in this tag
	tag_project = models.ManyToManyField(Project)


	# properties update
	def update_tag(self, name, description):
		self.tag_name = name
		self.tag_description = description

	# Representations
	def __str__(self):
		return 'Tag:' + tag_name + " --- " + tag_description
	__repr__ = __str__ 