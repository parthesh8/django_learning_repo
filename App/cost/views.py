from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def cost(request):
    return render(request, "form.html")


def process_parameters_view(request):
    gps_status = request.POST.get('gps_status')
    mark_in_date = request.POST.get('mark_in_date')
    mark_in_time = request.POST.get('mark_in_time')
    mark_out_date = request.POST.get('mark_out_date')
    mark_out_time = request.POST.get('mark_out_time')
    mark_in_datetime = datetime.strptime('{} {}'.format(mark_in_date, mark_in_time), '%Y-%m-%d %H:%M')
    mark_out_datetime = datetime.strptime('{} {}'.format(mark_out_date, mark_out_time), '%Y-%m-%d %H:%M')
    time_difference = mark_out_datetime - mark_in_datetime
    gps_status = gps_status.lower()

    if time_difference > timedelta(days=6) and gps_status == "no":
        result = 200
    else:
        result = 0
#   processor = ParameterProcessor()
#   result = processor.process_parameters(gps_status, mark_in_time, mark_in_date, mark_out_time, mark_out_date)
    context = {
        'result': result,
    }
    return render(request, 'result.html', context)
