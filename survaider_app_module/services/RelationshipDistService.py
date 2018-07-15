from survaider_app_module.models import Adult
from django.db.models import Count

class RelationshipDistService:

	def process(self):
		adults = Adult.objects.all().values('relationship').annotate(rel_count=Count('relationship')).order_by('relationship')
		relationships = list()
		rel_counts = list()

		for adult in adults:
			if adult['relationship'] is not None:
				relationship = adult['relationship']
				rel_count = adult['rel_count']
				relationships.append(relationship)
				rel_counts.append(rel_count)

		response = ResponseDTO()
		response.relationships = relationships
		response.rel_counts = rel_counts
		return response.to_dict()


class ResponseDTO:
	def __init__(self):
		self.relationships = None
		self.rel_counts = None

	def to_dict(self):
		dictionary = dict()
		dictionary['relationships'] = self.relationships
		dictionary['rel_counts'] = self.rel_counts

		return dictionary
