# **Data Science Inquiry Workshop**

**Topic:** Forecasting air pollution via a data science approach


## **Summary **

This is a two-day workshop scheduled in the beginning of the second week of Shodor apprenticeship program. The workshop is designed for students in Grade 8-12 with the goal to gain an authentic experience in data science process by building an air pollution forecasting model. Students will come back in November/December to form teams and lead a data science project from end-to-end. 

During the first day of the workshop, students will use the 2017 U.S. air quality and population data to model the relationship between population and air pollution. By working with this data set, students will learn how to use histograms to describe the distribution of one variable and use scatter plots to describe the relationship between two variables. 

During the second day of the workshop, students will also use two linear models to describe and predict the relationship between air pollutant and population, and use a holdout data set to validate and evaluate the error of the linear models. After all students become familiar with the data, tools, and relevant statistical concepts, students will use the daily air quality, weather, and yearly population data in North Carolina from 2013-2017 to build a PM2.5 forecasting model using the decision tree algorithm. The workshop will conclude with small group presentations to showcase their prediction models.

<span style="text-decoration:underline;">Importance** **</span>



1. The research topic “Human Impacts on Air Pollution” addresses one of the NGSS core ideas in Earth and Space Sciences: _ESS3.C: Human Impacts on Earth Systems_.
2. The statistical concepts used in this workshop align well with NC Mathematics State Core Standards, including _Summarize, represent, and interpret data on two categorical and quantitative variables_ and _Interpret linear models_.
3. This topic is complementary to other ongoing data science curriculum development efforts, such as the [workshops](http://oceansofdata.org/projects/zoom-learning-science-data) developed by ODI.

<span style="text-decoration:underline;">Data and Tools</span>



1. Data of U.S. county air quality (five pollutants) and population estimates: air quality data is pulled from EPA Historical Air Quality database. Population estimate data is from U.S. Census Bureau. 
2. Data exploration interface: CODAP with Shodor Interactivate Histogram as a plug-in.
3. Data modeling interface: Jupyter notebook (Google Colab). 
4. Other materials for hands-on activities exploring air pollutants & decision tree model.
5. Using Google products to manage real-time feedback (Form), collaboration (Document & Sheet), data analysis tools (CODAP files) & presentation+demo.


## **Overview**


<table>
  <tr>
   <td><strong>Unit/Time estimate</strong>
   </td>
   <td><strong>Data Science process</strong>
   </td>
   <td><strong>Learning goals</strong>
   </td>
   <td><strong>Description of activities</strong>
   </td>
   <td><strong>Data/Tools</strong>
   </td>
  </tr>
  <tr>
   <td><strong>

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "Unit 1"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.tnl3pqhs4uo">Unit 1</a></strong>
<p>
(Day 1: morning)
   </td>
   <td>Research Question
   </td>
   <td>Students will gain a broad understanding of ways to describe the quality of air, and the connections between human activity and air quality.
   </td>
   <td>Use relevant graphs/data to engage and motivate students, including a combination of lecture, reading, & discussion
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><a href="https://docs.google.com/document/d/1thk-AOHsUVdg5aKoNTaKxKKU1Pex8MuyuJNcH1-QE1s/edit#heading=h.ciiuf6nnmfln">Unit 2 </a></strong>
<p>
(Day 1: morning+afternoon)
   </td>
   <td>Data cleaning  & Visualization
   </td>
   <td>Students will be able to use histograms to describe the distribution of one variable.
<p>
Use scatter plots to describe the relationship between two variables
<p>
Students will learn that association does not imply causation.
   </td>
   <td>With some motivating questions (e.g., highest mean no2 county in NC), students use CODAP+Shodor plug-in to load the data table and make histogram, box plots, and scatter plots.
   </td>
   <td><a href="https://www.dropbox.com/s/00hi8pezgfko60a/popair_2017.csv?dl=0">Dataset_1</a>
<p>
<a href="https://www.dropbox.com/s/yfkoo4ufr4uctey/Exploring%20data.codap?dl=0">CODAP</a>
   </td>
  </tr>
  <tr>
   <td><strong><a href="https://docs.google.com/document/d/1thk-AOHsUVdg5aKoNTaKxKKU1Pex8MuyuJNcH1-QE1s/edit#heading=h.5qhax8mhuoin">Unit 3</a></strong>
<p>
(Day 2)
   </td>
   <td>Modeling & Interpretation
   </td>
   <td>Students will be able to use a linear model to describe the relationship between two variables.
<p>
Students will be able to use a decision tree model to predict binary outcomes.
<p>
They will also be able to validate the models using both qualitative and quantitative evidence.
   </td>
   <td>Motivated by predicting a set of counties with unknown air quality, students will use a linear model (a straight line and a quadratic) to describe the relationships and make predictions.
<p>
They will classify a small test data set by building a decision tree.
<p>
Students will build a forecasting model for PM2.5 using a decision tree model. 
<p>
Students will evaluate the errors of models using a holdout data set.
<p>
Some further discussion on the need of more sophisticated models, other relevant variables for further investigations
   </td>
   <td><a href="https://github.com/clhung/shodor_jupyter/tree/master">Jupyter notebook</a>
   </td>
  </tr>
</table>



## **Detailed Schedule**


### **Day 1 (August 12):**

9:00 -- Introduction, group discussion, setting expectations, logistics

9:20 -- Group discussion - share their experience with air pollution

9:30 -- Read-pair-share articles related to air pollution

10:00 -- A brief summary lecture on air pollutants we’ll focus on today and how to quantify them

10:15 -- Students read graphs and write down questions they have about the graph

10:30 -- Break

10:45 -- Introducing CODAP, making sure data are understandable 

11:00 -- Exploring CODAP, making plots, answer basic questions about the data (possibly histogram)

12:00 -- Lunch break

13:00 -- Regroup, Gallery walk, picking one question that interest you the most

13:20 -- Using CODAP to answer the question

14:15 -- Break

14:30 -- Wrap up investigation

14:45 -- [Self-reflection sheet](https://docs.google.com/document/d/1Mh92-QenACYUcMXDAZI-gcu3uXP03GM6T5eGOO9M8OA/edit)

14:55 -- Making posters

15:15 -- Poster presentation (5 minutes each)

15:35 -- Summary, wrap up for day 1


### **Day 2 (August 13):**

9:00 -- Recap on what we learned yesterday: Data science process

9:10 -- Brainstorming/discussing trends we saw yesterday; Whole group discussion to build an analysis plan

9:20 -- Introducing to Jupyter/Python, making sure everyone can run and work with Jupyter

9:30 -- Small group (same as yesterday) investigation with linear model

10:15 -- Break

10:30 -- continue investigation

10:40 -- [Self-reflection sheet](https://docs.google.com/document/d/1xiop34XL60fWZzMoKlRCThNXJy4nc3o9nxT7qfu5ufk/edit)

10:50 -- Jigsaw to share each group’s finding

11:00 -- Regroup, summary of linear model

11:10 -- Intro to decision tree

11:20 -- Small group build a decision tree using sample data 

12:00 -- Lunch break

13:00 -- Recap & Goals for afternoon

13:05 -- Share trees with whole class (walk through)

13:15 -- Introducing to concept of IG, Jupyter tool to calculate that

13:35 -- Modify decision tree using IG

13:55 -- Building predicting tool for PM2.5 using decision tree model in Jupyter

14:15 -- Break

14:30 -- Building predicting tool for PM2.5 using decision tree model in Jupyter

15:20 -- Self reflection sheet

15:30 -- Jigsaw discussion

15:40 -- Summary, Wrap up for Day 2


## **Activity and Facilitation Plan**


### **Unit 0: Workshop Introduction**

0.1: Overview of the workshop and getting to know each other



*   Share with the group: one minute share (1) how should we call you? (2) share one new thing you learned last week, and (3) what do you think “data science” is?
*   Logistics: we’re all here to learn, everyone has a different experience and may find different things difficult or challenging.


### **Unit 1: Research Background Introduction**

1.1 Motivation



*   Whole group discussion: share your experience about air pollution. When and where might you notice the air quality is good or bad? How did you notice that (e.g., allergy)?
*   Based on what students bring up, some of the relevant concepts might be indoor v.s. outdoor pollution, locations (Durham v.s. Smokys), day v.s. night time, other observations like the visibility.
*   Facilitator emphasizes a subset of concepts that are relevant to this investigation. e.g., It seems like some of you notice that the air quality depends on location, or perhaps, human activity in that area. Some of you talked about the visibility, what are those smogs made of?

1.2 Air pollution: investigating five air pollutants



*   Pair with neighbor(s) to read a paragraph (e.g., from[ EPA](https://www.epa.gov/criteria-air-pollutants)) & a relevant news article (e.g.,[ news](https://www.cnn.com/2018/10/31/politics/epa-air-pollution/index.html)) about one air pollutant and then share with neighbor groups: 

<table>
  <tr>
   <td>
Pollutant
   </td>
   <td>Causes
   </td>
   <td>Articles/Tools
   </td>
   <td>Note (for investigation later)
   </td>
  </tr>
  <tr>
   <td>Ground-level Ozone
   </td>
   <td>Air pollutants like NO2 and VOC interact with sunlight
   </td>
   <td><a href="https://www.epa.gov/ground-level-ozone-pollution/ground-level-ozone-basics#wwh">EPA article</a>
<p>
<a href="https://www.airnow.gov/">AirNow</a>
   </td>
   <td>Data show no correlation with population (in log)
   </td>
  </tr>
  <tr>
   <td>Particulate Matter (PM10&PM25)
   </td>
   <td>They are formed of many different chemicals; Some direct emission & some through chemical reaction of NO2, SO2
   </td>
   <td><a href="https://www.epa.gov/pm-pollution/particulate-matter-pm-basics#PM">EPA article</a>
<p>
<a href="https://www.airnow.gov/">AirNow</a>
   </td>
   <td>PM25 data show weak correlation
   </td>
  </tr>
  <tr>
   <td>Carbon Monoxide
   </td>
   <td>Outdoor CO sources are cars, trucks, and other vehicles or machinery that burn fossil fuels
   </td>
   <td><a href="https://www.epa.gov/co-pollution/basic-information-about-carbon-monoxide-co-outdoor-air-pollution#What%20is%20CO">EPA article</a>
   </td>
   <td>CO data show positive correlation
   </td>
  </tr>
  <tr>
   <td>Nitrogen Dioxide
   </td>
   <td>Emitted through burning fuels by cars, trucks, power plants, and others
   </td>
   <td><a href="https://www.epa.gov/no2-pollution/basic-information-about-no2#What%20is%20NO2">EPA article</a>
<p>
<a href="https://www.nasa.gov/content/goddard/nasa-scientists-relate-urban-population-to-air-pollution/">NASA article</a>
<p>
<a href="https://www.sciencedaily.com/releases/2013/08/130819185352.htm">ScienceDaily</a>
   </td>
   <td>NO2 data show positive correlation
   </td>
  </tr>
  <tr>
   <td>Sulfur Dioxide
   </td>
   <td>Largest sources from fossil fuel combustion at power plants and other industrial facilities. Smaller sources include industrial processes such as extracting metal from ore. Natural sources such as volcanoes. Others like locomotives, ships and other vehicles and heavy equipment that burn fuel with a high sulfur content.    
   </td>
   <td><a href="https://www.epa.gov/so2-pollution/sulfur-dioxide-basics#what%20is%20so2">EPA article</a>
   </td>
   <td>Highest point is Hawaii county (Big Island);
   </td>
  </tr>
</table>




*   Facilitator summarizes the five pollutants for this investigation

1.3 How to describe air quality based on each of these pollutants?



*   Facilitator continues the summary/lecture
*   AQI (Air Quality Index):[ Link](https://airnow.gov/aqi/aqi-basics)

1.4 Raising questions



*   Facilitator show a series of plots on the table (2 sets), including US population map, a few monthly average wind maps, and 2017 average AQI maps for NO2, PM2.5, and SO2.
*   Students are free to write down any questions they have related to these plots (one question per strip)

Other notes:



*   [It’s Our Air](http://itsourair.org/) project has some great introduction videos.
*   An [interactive tool](http://has.concord.org/air-pollution.html) by Concord.


### **Unit 2: Cleaning data & Visualization**

2.1 Getting to know the data



*   Pair with a neighbor to read a paragraph (embedded in CODAP) that describes what are included data table. Students should be able to answer questions like, “What does average AQI o3 mean? What properties does it average over?” “Why the blank cells? What does that mean?"



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Shodor-data0.png "image_tooltip")


	Human activity:



*   A good proxy is population; population estimate methodology used by the US census bureau[ Link](https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2010-2017/2017-natstcopr-meth.pdf) 

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data1.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Shodor-data1.png "image_tooltip")


2.2 Distribution of one variable in CODAP



*   Look at the values in the table, what are the typical numbers of average AQI for NO2? What are the typical air conditions in the scale from Good to Hazardous?
*   Open a “Graph” and drag an attribute (avgAQI_no2) to the bottom of the graph. How do we make sense of this plot? Is what we see consistent with our expectation?
*   Which counties have the highest average AQI? which ones have the lowest?

2.3 Histogram (Interactivate)



*   Find the “Shodor Histogram” panel. Click on “Load data.” 
*   Drag the control bar to change the interval size. At what interval size you see similar plot as in step 2.2? 
*   Explore the plot with different bin sizes. What interval size do you think is easy to visualize but still retain useful information?
*   Compare NO2 and SO2 data

2.4 Relationships between two variables in CODAP



*   Show students’ predictions from the end of Unit 1. Students may predict air quality would show a positive association with population, or depend on specific pollutants.
*   In CODAP, create a new attribute uses the formula of Log(POPESTIMATE2017, 10).
*   Open a “Graph” and drag the attribute “Log_Population” to the bottom of the graph, and drag another attribute (avgAQI_no2) to the left of the graph. How do we make sense of this plot? Is what we see consistent with the prediction?
*   Pair up to explore individual data points, outliers, etc. Observe the scatter plots for each of the pollutants NO2 & CO —> O3 & PM25 —> SO2.

<table>
  <tr>
   <td>


<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data2.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/Shodor-data2.png" width="" alt="alt_text" title="image_tooltip">

   </td>
   <td>

<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data3.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/Shodor-data3.png" width="" alt="alt_text" title="image_tooltip">

   </td>
  </tr>
  <tr>
   <td>

<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data4.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/Shodor-data4.png" width="" alt="alt_text" title="image_tooltip">

   </td>
   <td>

<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data5.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/Shodor-data5.png" width="" alt="alt_text" title="image_tooltip">

   </td>
  </tr>
  <tr>
   <td>

<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data6.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/Shodor-data6.png" width="" alt="alt_text" title="image_tooltip">

   </td>
   <td>
   </td>
  </tr>
</table>


2.5 Assessment



*   Short google form to assess students’ understanding. Students conclude what they observed when plotting Air Quality v.s. Population. Comment on whether they think scatter plots can be used to justify whether the change of one variable “causes” the change of the other variable. Google Form Link

2.6 Conclusion: association is NOT causation



*   Facilitator summarizes: human activities produce some of these air pollutants (volcano is a noticeable exception), but there are other relevant factors such as the weather that affect the amount of pollutants measured. The world is full of complex systems like this example, we cannot say one parameter “causes (or does not cause)” the other parameter simply because we see an association (or no association) between two parameters. 
*   Students explore intriguing examples such as those from[ spurious correlations](http://tylervigen.com/spurious-correlations)


### **Unit 3: Modeling & Interpretation**


#### Part I: Linear model

3.1 Brainstorming: _can we describe the relation between air pollutants and population? What about those counties without measurements? Can we predict that?  Furthermore, can we predict air pollutant (forecasting) based on data we have in the past?_



*   Work individually to write down their ideas on a Google Form.
*   Share the idea with a neighbor, and see if it’s possible to consolidate the idea

3.2 Whole class discussion: build the analysis plan



*   Come up with a “model” based on places we know population and air quality, and then use the model to predict the air quality of places with unknown air quality.
*   What should our model be? Quick guess perhaps a straight line. 
*   Quick fit using CODAP, assessing the model by eye.
*   Perhaps the model also depend on the squared of air quality?
*   How do we validate our models' accuracy? Strategy —> leave out some part of our data and use them to validate our models.
*   Analysis plan:



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data7.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Shodor-data7.png "image_tooltip")


3.3 Small group investigation based on the analysis plan in Jupyter



*   Students work in small groups and carry out the analysis plan in Jupyter notebook
*   The content prompt here is “Predict air qualities of counties without measurements using a linear model. Justify your choice of Model 1 or Model 2 based on the validation using the hold out data set." 



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data8.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Shodor-data8.png "image_tooltip")




<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Shodor-data9.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Shodor-data9.png "image_tooltip")


3.4 Jigsaw discussion & Synthesis



*   Students will do a Jigsaw discussion to share with members of other groups about their findings.
*   The discussion is evaluated based on the Rubric below

<table>
  <tr>
   <td>
    <strong>Dimension</strong>
   </td>
   <td>
<strong>0 </strong>
<p>
<strong>Misunderstanding or incomplete understanding</strong>
   </td>
   <td><strong>1-2</strong>
   </td>
   <td><strong>3</strong>
<p>
<strong>Sufficient understanding</strong>
   </td>
  </tr>
  <tr>
   <td>Models as a means to describe data and make predictions 
   </td>
   <td>Student may say the model can not be used because it does not perfectly “crosses” all the data.
<p>
Say there should only be “one true model” to describe the data.
   </td>
   <td>Students see models as either a tool to describe the data or make prediction.
   </td>
   <td>Students say something like “the distribution of the data look like a straight line”, “I think it can be better described as XX”, “if the county has XX population, they may have XX air quality based on the model." 
   </td>
  </tr>
  <tr>
   <td>Different models can give different predictions, and predictions are not real measurements
   </td>
   <td>Students may say the predictions should be the same from different models.
<p>
Do not clearly state whether a number is real measurement or a prediction.
   </td>
   <td>
   </td>
   <td>Students may say “the predicted value for this county is XX based on model one, but is YY based on model 2."
   </td>
  </tr>
  <tr>
   <td>Models can be validated based on a holdout data set
   </td>
   <td>Do not validate the models, and just provide the predicted values,
   </td>
   <td>May use the training data set to assess the errors of the models.
   </td>
   <td>Students provide predictions based on model validated using the holdout set.
   </td>
  </tr>
  <tr>
   <td>Total score
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>




*   The facilitator synthesize the core content learning goals and clarify misconceptions raised during the discussion.
*   Why using a holdout data set is a good and commonly used practice, and how you might use it in other investigation.


#### Part II: Making an air pollutant forecasting tool using decision tree model 

3.5 Build a decision tree using a small test data set (ten data points)



*   Students work in small group to build a decision tree to classify air pollution level (Good or Warning) of 10 data points. Each data point is explicitly written out on a sheet of paper. [Demo data](https://www.dropbox.com/s/bkhwgijixiwltie/dt_demodata.csv?dl=0)
*   Each group briefly presents their “tree.” Whole class discussion on the similarity/difference of each tree. How many levels? What questions to ask, and in what order?
*   Introduce the concept of entropy and information gain.
*   Each group use the Jupyter tool (Information_gain.ipynb) to calculate the information gain and design a new decision tree.

3.6 Build a forecasting tool for PM2.5 using a decision tree algorithm ([Link](https://github.com/clhung/shodor_jupyter/tree/master))



*   Use the full data set (daily weather and pollution level data in US from 2013-2017).
*   Students work in small groups to build a forecasting tool in the Jupyter notebook (forecasting_dt.ipynb): using 2013-2016 data as the training set and 2017 data as the test set.
*   Explore the maximum depth of the decision tree, and construct the confusion matrix of the model.

3.7 Poster presentation



*   Student groups summarize their findings in a poster and each group takes turns to present to the entire class.

<!-- Docs to Markdown version 1.0β17 -->
