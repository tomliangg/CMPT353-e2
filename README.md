# Plotting_Wikipedia_Page_Views-CMPT353_e2
<h3>This repo is created for documentation purpose. The repo contains my personal work toward the SFU CMPT353 (Computational Data Science) course. You may use my solution as a reference. The .zip archive contains the original exercise files. For practice purpose, you can download the .zip archive and start working from there.</h3>

<p><a href="https://coursys.sfu.ca/2018su-cmpt-353-d1/pages/AcademicHonesty">Academic Honesty</a>: it's important, as always.</p>
<p>Below is the exercise description </p>
<hr>

<div class="wikicontents creole tex2jax_process"><p>Due <span title="2018-05-25T23:59:59-07:00">Friday May 25 2018</span>.</p>
<p>Some files are provided that you need below: <a href="E2.zip">E2.zip</a>. As with last week, <strong>you may not write any loops</strong> in your code.</p>
<h2 id="h-plotting-wikipedia-page-views">Plotting Wikipedia Page Views</h2>
<p>For this question, we will use some data on the number of times individual Wikipedia pages were viewed in a particular hour, and then in the same hour a day later. These were extracted from <a href="https://dumps.wikimedia.org/other/pagecounts-raw/">Wikipedia's page view counts</a>. </p>
<p>To get the two provided <code>pagecounts-*.txt</code>, I selected 2500 English pages at random from the first full data set. Then I selected those pages from the second data set. The result is that some of the pages in the first data set are not in the second: those pages weren't viewed in that hour on the second day.</p>
<p>We will produce two plots of the data provided with a stand-alone <strong>Python program <code>create_plots.py</code></strong>. The filenames you operate on must be taken from the command line. Your program must run with a command like this:</p>
<pre class="highlight lang-bash">python3 create_plots.py pagecounts-20160802-150000.txt pagecounts-20160803-150000.txt</pre>
<p>To get the command line arguments (as strings), you can use the built-in <code>sys</code> module:</p>
<pre class="highlight lang-python">import sys
⋮
filename1 = sys.argv[1]
filename2 = sys.argv[2]</pre>
<p>The files contain space-separated values for the language, page name, number of views, and bytes transferred. You can get the data out of this file format something like this:</p>
<pre class="highlight lang-python">pd.read_table(filename, sep=' ', header=None, index_col=1,
        names=['lang', 'page', 'views', 'bytes'])</pre>
<p>We will produce a single plot with two subplots on the left and right. Matplotlib can do that with a skeleton like this:</p>
<pre class="highlight lang-python">import matplotlib.pyplot as plt
⋮
plt.figure(figsize=(10, 5)) # change the size to something sensible
plt.subplot(1, 2, 1) # subplots in 1 row, 2 columns, select the first
plt.plot(…) # build plot 1
plt.subplot(1, 2, 2) # ... and then select the second
plt.plot(…) # build plot 2
plt.show()</pre>
<h3 id="h-plot-1-distribution-of-views">Plot 1: Distribution of Views</h3>
<p>For the first plot, we will use <strong>only the first data set</strong>. Based on statistics knowledge gained from blog posts and YouTube videos, I believe the distribution of page views should be a 
<a href="https://en.wikipedia.org/wiki/Pareto_distribution">Pareto distribution</a>.</p>
<p>Let's have a look: using only the first input file, sort the data by the number of views (decreasing). [Hint: <code>sort_values</code>.] If you give <code>plt.plot</code> a single data set, it will be plotted against a 0 to n-1 range, which will be what we want.</p>
<p>But, if we give matplotlib a Pandas Series (like <code>data['views']</code> will be), it will try to use its index as the x-coordinate. To convince it to do otherwise, we have two options: (1) pass the underlying NumPy array (<code>data['views'].values</code>), or (2) create a range to explicitly use as the x-coordinates (with <code>np.arange</code>).</p>
<h3 id="h-plot-2-daily-views">Plot 2: Daily Views</h3>
<p>The second plot we want to create is a scatterplot of views from the first data file (x-coordinate) and the corresponding values from the second data file (y-coordinate). It's fairly reasonable to expect a linear relationship between those values.</p>
<p>To do that, you'll need to get the two series into the same DataFrame. If you used the hint above to read the file, the page name will be the index.</p>
<p>You can then use these indexes: if you copy a Series from one DataFrame to another, elements are identified <em>by their index</em>. Since the DataFrames have the page name as their index, you can just put the two Series representing page views from both days into a single DataFrame and view counts for each page will end up alongside each other.</p>
<p>With default settings, I get a scatterplot like this (on different randomly-chosen data):</p>
<div style="margin-left:2em"><p> <img src="E2-non-log/view" title="E2-non-log/view" alt="E2-non-log/view" /></p>
</div>
<p>Because of the distribution of the values, the linear axes don't make much sense. Change this plot to log-scale on both axes using <a href="https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xscale">plt.xscale</a> and  <a href="https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.yscale">plt.yscale</a>.</p>
<h3 id="h-final-output">Final Output</h3>
<p>You can use <code>plt.show()</code> to see the figure as the program runs. That's probably easiest for testing, but as a final result, don't <code>show()</code>, but <strong>create a PNG file</strong> <code>wikipedia.png</code> like this:</p>
<pre class="highlight lang-python">plt.savefig('wikipedia.png')</pre>
<p>Use the functions <code>plt.title</code>, <code>plt.xlabel</code>, and <code>plt.ylabel</code> to give some useful labels to the plots.</p>
<p>A sample <code>wikipedia.png</code> (with different input data) is included in the ZIP file.</p>
<h2 id="h-pup-inflation-analysing-tweets">Pup Inflation: Analysing Tweets</h2>
<p>This question is heavily inspired by <a href="http://dhmontgomery.com/2017/03/dogrates/">David H. Montgomery's Pup Inflation</a> post. His analysis is an excellent data science task, and we will ask the same question here: has there been grade inflation on the  <a href="https://twitter.com/dog_rates">@dog_rates</a> Twitter, which rates the cuteness of users' dog pictures?</p>
<p>I scraped the @dog_rates feed with <a href="https://gist.github.com/yanofsky/5436496">tweet_dumper.py</a>. The result it produced is provided in the <code>dog_rates_tweets.csv</code> file, so we don't all have to scrape the data.</p>
<p>Do this analysis in a <strong>Jupyter notebook <code>dog-rates.ipynb</code></strong>. To look for score inflation, we'll first have to make sense of the data. The steps I think are necessary to do this:</p>
<ul><li>Load the data from the CSV into a DataFrame. (Assume a <code>dog_rates_tweets.csv</code> file is in the same folder as the notebook file.)
</li><li>Find tweets that contain an <span>&ldquo;</span>\(n\)/10<span>&rdquo;</span> rating (because not all do). Extract the numeric rating. Exclude tweets that don't contain a rating.
</li><li>Remove outliers: there are a few obvious ones. Exclude rating values that are too large to make sense. (Maybe larger than 25/10?)
</li><li>Make sure the 'created_at' column is a datetime value, not a string. You can either do this by applying a function that parses the string to a date (likely using <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime">strptime</a> to create a datetime object), or by asking Pandas' <code>read_csv</code> function to parse dates in that column with a <code>parse_dates</code> argument.
</li><li>Create a scatter plot of date vs rating, so you can see what the data looks like.
</li></ul>
<p>[The question continues, and there are a few hints below. You may want to do this part of the question and make sure things are working before continuing.]</p>
<h3 id="h-linear-fitting">Linear Fitting</h3>
<p>One analysis Montgomery didn't do on the data: a best-fit line.</p>
<p>The <code>scipy.stats.linregress</code> function can do a linear regression for us, but it works on numbers, not datetime objects. Datetime objects have a <code>.timestamp()</code> method that will give us a number (of seconds after some epoch), but we need to get that into our data before using it. If you write a function <code>to_timestamp</code> then you can do one of these (if it's a normal Python function, or if it's a NumPy ufunc, respectively):</p>
<pre class="highlight lang-python">data['timestamp'] = data['created_at'].apply(to_timestamp)
data['timestamp'] = to_timestamp(data['created_at'])</pre>
<p>You can then use <code>linregress</code> to get a slope and intercept for a best fit line.</p>
<p>Produce results like those found in the provided screenshot, <code>dog-rates-result.png</code>. <strong>At the end of your notebook</strong> (so the TA knows where to look), show the data itself, the slope and intercept of the best-fit line, and a scatterplot with fit line.</p>
<h3 id="h-hints">Hints</h3>
<p>This  <a href="https://docs.python.org/3/library/re.html">Python regular expression</a> will look for <span>&ldquo;</span>\(n\)/10<span>&rdquo;</span> strings in the format they seem to occur in the tweets. If this is found by searching in a tweet, then the resulting <a href="https://docs.python.org/3/library/re.html#match-objects">match object</a> can be used to get the numeric rating as a string, which can then be converted to a float.</p>
<pre class="highlight lang-python">r'(\d+(\.\d+)?)/10'</pre>
<p>I think the easiest way to <span>&ldquo;</span>exclude<span>&rdquo;</span> some rows from the DataFrame is to return <code>None</code> for rating values that aren't valid ratings, and then use <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.notnull.html#pandas.Series.notnull">Series.notnull</a> to create a boolean index. There are certainly other ways to do the job as well.</p>
<p>To plot the best-fit line, the \(x\) values must be datetime objects, not the timestamps. To add the best-fit line, you can plot <code>data['created_at']</code> against <code>data['timestamp']*fit.slope + fit.intercept</code> to get a fit line (assuming you stored the results of <code>linregress</code> in a variable <code>fit</code>).</p>
<p>Here are some hints to style the plot as it appears in my screenshot, which seems to look nice enough:</p>
<pre class="highlight lang-python">plt.xticks(rotation=25)
plt.plot(???, ???, 'b.', alpha=0.5)
plt.plot(???, ???, 'r-', linewidth=3)</pre>
<h2 id="h-questions">Questions</h2>
<p>Answer these questions in a file <code>answers.txt</code>. [Generally, these questions should be answered in a few sentences each.]</p>
<ol><li>In the hint above, describe the values that are the result of <code>data['timestamp']*fit.slope + fit.intercept</code>? How is this calculated?
</li><li>In the same hint, why does this produce a fit line on the graph? Why are the <code>created_at</code> values and <code>timestamp</code> values paired correctly to make points on the plot?
</li></ol>
<h2 id="h-submitting">Submitting</h2>
<p>Submit your files through CourSys for <a href="/2018su-cmpt-353-d1/+e2/">Exercise 2</a>.</p></div>

<div class="updateinfo">Updated Fri May 25 2018, 08:38 by ggbaker.

</div>
