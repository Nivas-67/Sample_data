from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import openpyxl


def excel_write():
    content = openpyxl.load_workbook("sample.xlsx")
    sheet = content.active()
    sheet.cell(row=1, column=1).value = "New workbook"
    content.save("sample.xlsx")


with DAG("my_dag", start_date=datetime(2021, 1, 1),
         schedule_interval="@daily", catchup=False) as dag:
    task1 = PythonOperator(
        task_id="Excel_tas",
        python_callable=excel_write
    )
