from django.http import HttpResponse, JsonResponse
import pandas as pd
import numpy as np

SOURCE_DIR = "D:\\download\\Exp2OutputCSV\\Exp2OutputCSV\\"
SOURCE_AGGREGATE_DIR = "C:\\Users\\耳东七月\\PycharmProjects\\DVPROJECT\\temporary\\"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def csv_to_list(csv_dir, csv_file):
    header = pd.read_csv(csv_dir + csv_file, encoding="utf-8").columns.values
    df = pd.read_csv(csv_dir + csv_file, encoding="utf-8")
    df_array = np.array(df)
    data_list = []
    data_list.append(header.tolist())
    data_list.extend(df_array.tolist())
    # print(data_list)
    return data_list


def get_aggregate(request):
    if request.method == 'GET':
        agg_type = request.GET.get('type')
        data = csv_to_list(SOURCE_AGGREGATE_DIR, f"{agg_type}_error.csv")
        return JsonResponse({"data": data}, status=200)
    else:
        return JsonResponse({"error": "Method Not Allowed"}, status=405)


def get_exact(request):
    if request.method == 'GET':
        model = request.GET.get('model')
        bar_chart_type = request.GET.get('bar_chart_type')
        sampling_method = request.GET.get('sampling_method')
        sampling_target = request.GET.get('sampling_target')
        down_sampling_level = request.GET.get('down_sampling_level')
        test_index = request.GET.get('index')
        data = csv_to_list(SOURCE_DIR, f"{bar_chart_type}{model}{sampling_target}{sampling_method}.{down_sampling_level}.{test_index}.csv")
        return JsonResponse({"data": data}, status=200)
    else:
        return JsonResponse({"error": "Method Not Allowed"}, status=405)


