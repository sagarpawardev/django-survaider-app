from survaider_app_module.models import Adult
from django.db.models import Count

class MaleFemaleDistService:

	def process(self):
		adults = Adult.objects.all().values('sex', 'native_country').annotate(sex_count=Count('sex')).order_by('native_country')
		main_map = dict()
		for adult in adults:
			if adult['native_country'] is not None and adult['sex'] is not None:

				sex = adult['sex']
				country = adult['native_country']
				count = adult['sex_count']

				elem = main_map.get(country, dict())
				elem[sex] = count

				main_map[country] = elem

		result = dict();
		countries = list()
		male_count = list()
		female_count = list()

		for country, sex_count in main_map.items():
			countries.append(country)
			m_count = sex_count.get('Male', 0)
			f_count = sex_count.get('Female', 0)
			male_count.append(m_count)
			female_count.append(f_count)

		result['countries'] = countries
		result['male_count'] = male_count
		result['female_count'] = female_count

		response = ResponseDTO()
		response.countries = countries
		response.male_count = male_count
		response.female_count = female_count
		return result


class ResponseDTO:
	def __init__(self):
		self.countries = None
		self.male_count = None
		self.female_count = None
