# Looping_script
 This Script will connect to redshift and gets number of months to be processed. It will also trigger iics linear task as many times the loop iterates.

1. You can run your iics taskflows as many time you what based on the data available in table.
2. This script read the month to be processed from redshift and store as a list.
3. We are looping throught the list, for each loop iics linear task will be executed. as this python script will trigger run_informatica_cloud.bat files with arguments. 
4. run_informatica_cloud.bat uses runajob utlity and trigger iics linear task. and it is alos responsible for getting return code and pass to python script.
