#dataframe
# source: https://colab.research.google.com/drive/1BlubmdD_pBGY9fij3ycSQxKu1aJ4EbzV?usp=sharing#scrollTo=kx1CddcU-mmN

import os
import pandas as pd
#import numpy as np
import plotly.graph_objects as go
import plotly.express as px
#import statsmodels.api as sm
#from google.colab import files

def tidy_dataset(df):
    #split age into age min and max
    df[["age_min", "age_max"]] = df["age"].str.split("-", n=1, expand=True)
    df = df.drop("age", axis=1)
    # convert salary from text to numeric
    df.salary = df.salary.str.replace(" kr", "")
    df.salary = df.salary.str.replace(",", ".")
    #Erstatter hard space med ingenting
    df.salary = df.salary.str.replace(" ", "")
    df.salary = df.salary.str.replace(" ", "")
    df.salary = df.salary.astype(float)
    # experience, gjøre om kolonna til float.
    df.experience = df.experience.str.replace(",", ".")
    df.experience = df.experience.astype(float)
    return df

def get_data():
    df = pd.read_csv("https://raw.githubusercontent.com/HaliaeetusAlbicilla/k24salary/master/kode24salary.csv")
    df.columns = [
        "age",
        "education",
        "experience",
        "work_situation",
        "county",
        "work_field",
        "salary",
        "bonus",
        "satisfied",
    ]
    return df 

def get_aggregates(df):
    df2 = (
        df.groupby("work_situation")
        .agg({"salary": ["mean", "median", "count"], "experience": ["mean"]})
        .reset_index()
    )

    df2.columns = [
        "work_situation",
        "salary_mean",
        "salary_median",
        "work_situation_count",
        "experience_mean",
    ]
    df2 = df2.sort_values(by="salary_median", ascending=False)
    return df2

def plot(dff):
    fig = go.Figure()

    y = dff.salary_median
    y.index = dff.work_situation

    fig.add_trace(
        go.Bar(
            name="Median",
            x=y.index,
            y=y,
            hovertemplate="<i>Salary</i>: NOK %{y:.0f} <br><i>Group</i>: %{x}",
        )
    )

    y = dff.salary_mean
    y.index = dff.work_situation

    fig.add_trace(
        go.Bar(
            name="Gjennomsnitt",
            x=y.index,
            y=y,
            hovertemplate="<i>Salary</i>: NOK %{y:.0f} <br><i>Group</i>: %{x}",
        )
    )

    # Rotere labels:
    fig.update_layout(barmode="group", xaxis_tickangle=-45)

    # Tallformatering og hover label
    fig.update_layout(
        yaxis_tickformat=",",
        yaxis_hoverformat=",.0f",
    )

    # Tekst
    fig.update_layout(
        yaxis_title="Gjennomsnittlig årslønn i kr",
        legend_title="Sentralmål",
        title="Lønn per arbeidssituasjon",
    )

    # Ticksplassering
    fig.update_layout(yaxis=dict(tickmode="linear", tick0=0, dtick=200000))
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)

    # Vis figur
    fig.show()
    return

def plot_bubbles(dff):
    fig = px.scatter(
        dff,
        x="experience_mean",
        y="salary_mean",
        size="work_situation_count",
        color="work_situation",
        log_x=True,
        size_max=100,
    )

    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    fig.show()
    return

def plot_bubbles2(df):
    dff = (
        df.groupby("work_field")
        .agg({"salary": ["mean", "median", "count"], "experience": ["mean"]})
        .reset_index()
    )
    dff.columns = [
        "work_field",
        "salary_mean",
        "salary_median",
        "work_field_count",
        "experience_mean",
    ]
    
    fig = px.scatter(
        dff,
        x="experience_mean",
        y="salary_median",
        size="work_field_count",
        color="work_field",
        log_x=True,
        size_max=100,
        title="Lønn og arbeidserfaring etter arbeidsoppgaver",
        labels={
            "work_field": "Hva jobber du mest med?",
            "experience_mean": "Gjennomsnittlig arbeidserfaring",
            "salary_median": "Medianlønn",
        },
    )

    fig.update_traces(
        hovertemplate="Gjennomsnittlig arbeidserfaring: %{x:.1f} år <br>Medianlønn: %{y:,0f} kr"
    )

    fig.show()
    return

#start function
def clear_console():
    os.system('clear')
    print('----------------------------\n')
#end function

#start the programme
def main_module():
    clear_console()
    df = get_data()

    #print some content of dataset
    #print(df.work_situation.value_counts(),'\n')
    df = tidy_dataset(df)
    print('Høyeste lønn i datasett: ', df.salary.max(),'\n')
    #print(df[df.salary == 2600000.0],'\n')

    #add aggregates to a 2nd dataset
    df2 = get_aggregates(df)
    #print(df2.head(),'\n')
        
    #plot the second dataset - is shown in default browser
    print('plot kommer i default browser\n')
    plot(df2)
    # another plot - bubble chart
    plot_bubbles(df2)
    plot_bubbles2(df)

#end main programme

#test if this is the main programme, or if this code is imported into another main programme
if __name__ == '__main__':
    main_module()