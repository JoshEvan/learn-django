from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse # HttpResponse content-type=application/json
from .models import Poll

# Create your views here.
def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        'results': list(
            # change each queryset object to dictionary, with key of column names,
            # parameter of .values() specifies which columns to take into dict
            polls.values(
                'question',
                # get username field on User table that references by `created_by` field
                'created_by__username',
                'pub_date'
            )
        )
    }
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data={
        "results":{
            "question":poll.question,
            "created_by": poll.created_by.username,
            "pub_date":poll.pub_date
        }
    }
    return JsonResponse(data)

