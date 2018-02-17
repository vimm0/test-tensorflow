# Missing code
# from apps.student.models import Mark, Student, Subject
# from django_pandas.io import read_frame
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from sklearn import datasets, linear_model
# from sklearn.metrics import mean_squared_error, r2_score
# def prediction(request):
#     template = 'prediction.html'
#     qs = Mark.objects.all()
#     df = read_frame(qs)
#     all_student = df['student_name'].unique()
#     all_subject = df['subject_name'].unique()
#     all_exam = df['exam'].unique()
#     qs = Mark.objects.filter(student_name__name='ABHINAYA PRADHAN', subject_name__subject_name__in=all_subject)
#     df = read_frame(qs)
#     student_df = np.array(df[['mark']])
#     # Split the data into training/testing sets
#     mark_X_train = student_df[:12, :]
#     mark_X_test = student_df[24:28, ]
#
#     # Split the targets into training/testing sets
#     mark_y_train = student_df[12:24, :]
#     mark_y_test = student_df[28:, :]
#
#     regr = linear_model.LinearRegression()
#     regr.fit(mark_X_train, mark_y_train)
#     g = regr.fit(mark_X_train, mark_y_train)
#     # Predict
#     mark_y_pred = regr.predict(mark_X_test)
#     # Statistical parameter
#     #coefficients
#     coefficients = regr.coef_
#     # mean squared error
#     MSE = mean_squared_error(mark_y_test, mark_y_pred)
#     # Explained variance score: 1 is perfect prediction
#     RSQ = r2_score(mark_y_test, mark_y_pred)
#     subject = ['Data Warehousing and Data Mining', 'Advanced Networking with IPv6', 'Cloud Computing',
#                'Geographical Information System']
#     exam = ['test4_exam']
#     mark_y_pred_pd = pd.DataFrame(mark_y_pred.reshape(mark_y_pred.shape[1], -1), index=exam, columns=subject)
#     mark_X_test_pd = pd.DataFrame(mark_y_test.reshape(mark_y_test.shape[1], -1), index=exam, columns=subject)
#     student_name = 'ABHINAYA PRADHAN'
#     mark_y_pred_pd_html = mark_y_pred_pd.to_html()
#     mark_X_train_html = mark_X_test_pd.to_html()
#
#     context = {
#         'MSE':MSE,
#         'RSQ':RSQ,
#         'coefficients':coefficients,
#         'student_name':student_name,
#         # 'exam':exam,
#         # 'student_name': student_name,
#         'mark_y_pred_pd_html': mark_y_pred_pd_html,
#         'mark_X_train_html': mark_X_train_html,
#     }
#     return render(request, template, context)

from apistar import annotate
from apistar import render_template
from apistar.renderers import HTMLRenderer


@annotate(renderers=[HTMLRenderer()])
def home():
    """
    Home page that serves <a>index.html</a> template.
    """
    return render_template('index.html')


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}
