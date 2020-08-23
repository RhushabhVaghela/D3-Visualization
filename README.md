# D3-Visualization
Created a D3 visualization (Data Insights) website for the purpose of exploring Fake Scientific People and Literature

The Dataset is provided in the repository which is used for analysis of Fake scientific People and Literature.
With the help of Visulization we can determine what are the causes of generating Fake scientific Literature.
Please check out the screenshot folder to get the look of the website directly.

Prerequisites:
* System should be configured with Python 3
* Install module ‘pandas’ into python environment: pip install pandas
* Install http-server in the command line: npm install -g http-server (windows)


Converting TSV dataset to JSON:-
Files needed in directory:
ProjectTeamID_9_v3.tsv
Run code in terminal:
python tsvToJSON.py
(ProjectTeamID_9_v3.json file will be created which will be used for solr indexes.)


Building Solr Indexes for D3 visualizations:-
*Please use the solr-8.5.1
To increase the memory, please add the following line in <your-solr-directory>/bin/solr.in.cmd file:-
set SOLR_JAVA_MEM=-Xms1g -Xmx1g  
it is required to configure the memory to upload the dataset in the solr server.  

For Windows:-
Files needed in the directory:
ProjectTeamID_9_v3.tsv
(Go inside your solr directory)
(copy ProjectTeamID_9_v3.json into your solr directory and execute the following)
Run code in terminal:
bin\solr start
bin\solr create_core -c tsv_data
java -Dauto -Dc=tsv_data -jar example\exampledocs\post.jar ProjectTeamID_9_v3.json



Visualizing D3 results:-
(Go to D3-solr Visualizations directory and open a terminal inside the directory and execute the following)

http-server &
go to your browser and type: localhost:8080
(this will automatically redirect you to the homepage of the website. You can navigate to different visualization D3 webpages with the help of navigation bar at the top of the webpage.)

(Note: please install http-server to run the webpage in the browser. An http-server is required since the webpage takes input data through a file(csv, json), and without running a http-server you might get an content policy error. If somehow you can't see the webpages, you can go through the screenshots of each webpage in the "D3-solr Visualizations" directory.)

[Data used for visualization is fetched from solr index and stored in a csv file "solr_data.csv" manually in each webpage directory (a,b,c,d,e). You can see the solr url in the "solr_url.txt" file in each webpage directory. Run "data_cleaning.py" file in each directory (a,b,c,d,e) in "D3-solr Visualizations" as the data fetch from solr needs to be cleaned in order to use it for visualization. And a new "Cleaned_data.csv" will be created which will then be used as input for the Visualizations.]
