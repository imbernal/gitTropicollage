from django import template

register = template.Library()

@register.tag
def generate_styles(parser, token):
	try:
		tag_name, map_pk = token.split_contents()
	except ValueError:
		msg = "Is required the map primary key before generate the styles"
		raise template.TemplateSyntaxError(msg)
	return StyleNode(map_pk)

class StyleNode(template.Node):
	def __init__(self, map_pk):
		self.map_pk = str(map_pk)

	def render(self, context):
		id = self.map_pk
		return "#map-canvas-"+id+" {\
            width: 100% !important;\
            height: 400px !important;\
        }"
