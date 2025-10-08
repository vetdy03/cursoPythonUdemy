from django import template 
register = template.Library() #crea un decorador

@register.filter(name="add_attr")
def add_attr(field, css):
    attrs= {}
    return field.as_widget(attrs=attrs)

