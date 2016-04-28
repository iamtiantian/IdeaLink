from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
	url(r'^$' , views.index , name = 'index') ,
	url(r'^register$' , views.register , name = 'register') ,
	url(r'^login$' , views.login , name = 'login') ,
	url(r'^home$' , views.home , name='home'),
	url(r'^index$' , views.logout , name='logout'),
	url(r'^setting$' , views.setting , name='setting'),
	url(r'^setting/contact$' , views.settingContact , name='settingContact'),
	url(r'^setting/experience$' , views.settingExperience , name='settingExperience'),
	url(r'^setting/skill$' , views.settingSkill , name='settingSkill'),
	url(r'^setting/skill/(?P<skill_type>\w+)$' , views.deleteSkill , name='deleteSkill'),
]