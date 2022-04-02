from django import template


register = template.Library()


@register.filter(name='complete_to')
def complete_to(value):
    subtask = value.subtask_set.all()
    count = 0
    for st in subtask:
        if st.status == 'CO':
            count += 1
    return int(count/len(subtask)*100) if len(subtask) else 0

