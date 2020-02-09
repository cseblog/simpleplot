import plotly.express as px
import pandas as pd
import uuid


header = """ <html>
<head>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
<div class="content">
"""
footer = """
</div>
</body>
</html>
"""

'''
generate line chart
'''


def lc_gen(file_name):
    df = pd.read_csv("data/" + file_name)
    fig = px.line(df, x="ts", y="max")
    fig.add_scatter(x=df['ts'], y=df['mean'], mode='lines')
    fig.add_scatter(x=df['ts'], y=df['min'], mode='lines')
    fig_json = fig.to_json()
    r_id = str(uuid.uuid1())
    template = """
        <div>
        <div id='""" + r_id + """'></div>
        <script>
            var plotly_data = """ + fig_json + """
            Plotly.react('""" + r_id + """', plotly_data.data, plotly_data.layout);
        </script>
        </div>
    """
    return template


'''
generate_tbl_html
reading csv file name 
return html block for the table
'''


def tbl_gen(file_name):
    df = pd.read_csv('data/' + file_name)
    tb = df.describe()
    tb = tb\
        .to_html()\
        .replace('<table border="1" class="dataframe">','<table class="table table-striped">')
    return tb


# main
tbl = tbl_gen("tempTb1.csv")

lchart1 = lc_gen("raw1.csv")
lchart2 = lc_gen("raw2.csv")

page = header + tbl + lchart1 + lchart2 + footer
with open('new_plot.html', 'w') as f:
    f.write(page)

