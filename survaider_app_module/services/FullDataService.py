from survaider_app_module.models import Adult
from django.db.models import Count

class FullDataService:

	def process(self, page, size):
		LIMIT = int(size)
		if page is None:
			page = 0
		page = int(page)
		start = page*LIMIT
		end	= (page+1) * LIMIT

		adults = Adult.objects.all().order_by('id')[start:end]
		response = ResponseDTO()
		for adult in adults:

			response.ages.append( adult.age)
			response.workclasses.append( adult.workclass)
			response.fnlwgts.append( adult.fnlwgt)
			response.educations.append( adult.education)
			response.education_nums.append( adult.education_num)
			response.marital_statuses.append( adult.marital_status)
			response.occupations.append( adult.occupation)
			response.relationships.append( adult.relationship)
			response.races.append( adult.race)
			response.sexes.append( adult.sex)
			response.capital_gains.append( adult.capital_gain)
			response.capital_losses.append( adult.capital_loss)
			response.hours_per_weeks.append( adult.hours_per_week)
			response.native_countries.append( adult.native_country)
			response.salaries.append( adult.salary)

		return response.to_dict()


class ResponseDTO:
	def __init__(self):
		self.ages = list()
		self.workclasses = list()
		self.fnlwgts = list()
		self.educations = list()
		self.education_nums = list()
		self.marital_statuses = list()
		self.occupations = list()
		self.relationships = list()
		self.races = list()
		self.sexes = list()
		self.capital_gains = list()
		self.capital_losses = list()
		self.hours_per_weeks = list()
		self.native_countries = list()
		self.salaries = list()

	def to_dict(self):
		dictionary = dict()
		dictionary['ages'] = self.ages
		dictionary['work_classes'] = self.workclasses
		dictionary['fnlwgts'] = self.fnlwgts
		dictionary['educations'] = self.educations
		dictionary['education_nums'] = self.education_nums
		dictionary['marital_statuses'] = self.marital_statuses
		dictionary['occupations'] = self.occupations
		dictionary['relationships'] = self.relationships
		dictionary['races'] = self.races
		dictionary['sexes'] = self.sexes
		dictionary['capital_gains'] = self.capital_gains
		dictionary['capital_losses'] = self.capital_losses
		dictionary['hours_per_weeks'] = self.hours_per_weeks
		dictionary['native_countries'] = self.native_countries
		dictionary['salaries'] = self.salaries

		return dictionary
	
