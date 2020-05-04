import psycopg2
import sys
import boto3
import psycopg2
import logging
import json
import os
import subprocess as sp
import time


RS_PORT = 5439
RS_USER = 'user'
DATABASE = 'database'
CLUSTER_ID = 'cluster name'
RS_HOST = 'server id'
my_east_session = boto3.Session(region_name = 'us-east-1')
client = my_east_session.client('redshift')
cluster_creds = client.get_cluster_credentials(DbUser=RS_USER,
                                               DbName=DATABASE,
                                          ClusterIdentifier=CLUSTER_ID,
                                               AutoCreate=False)
try:
      conn = psycopg2.connect(
        host=RS_HOST,
        port=RS_PORT,
        user=cluster_creds['DbUser'],
        password=cluster_creds['DbPassword'],
        database=DATABASE
)

except psycopg2.Error:  
   logger.exception('Failed to open database connection.')

cur = conn.cursor()
cur.execute("select distinct src_sys_name from datawarehouse.month where process_completed_flag='N' order by src_sys_name")
source=cur.fetchall()
for line8 in source:
      line9=''.join(line8)
      print(line9)
      cur.execute("select distinct fiscal_year_variant::varchar(30) from datawarehouse.month where process_completed_flag='N' and src_sys_name='{0}' order by fiscal_year_variant ".format(line9))
      no_of_months1=cur.fetchall()
      for line10 in no_of_months1:
            print(line10[0])
            line11=''.join(line10)
            cur.execute("truncate table datawarehouse.current_process_month")
            cur.execute("commit;")
            cur.execute("insert into datawarehouse.current_process_month  (fiscal_year_variant,src_sys_nm) values(%s,%s)",(line11,line9))
            cur.execute("commit;")
            temp=sp.Popen('C:/run_informatica.bat Lineartask Workflow')
            print(temp.communicate())
            print(temp.communicate())
            print(temp.communicate())
            print(temp.returncode)
            if temp.returncode!=0:
                  
                  print("fail")
                  break;
            else:
              print("task pass")
              cur.execute("update datawarehouse.month set process_completed_flag='Y' where  fiscal_year_variant ='{0}' and src_sys_name='{1}'".format(line11,line9) )
              cur.execute("commit;")
            
                                                      
cur.close()


