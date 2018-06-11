# Plotting_Wikipedia_Page_Views-CMPT353_e2_p1
<h3>This repo is created for documentation purpose. The repo contains my personal work toward the SFU CMPT353 (Computational Data Science) course. You may use my solution as a reference. The .zip archive contains the original exercise files. For practice purpose, you can download the .zip archive and start working from there.</h3>

<p><a href="https://coursys.sfu.ca/2018su-cmpt-353-d1/pages/AcademicHonesty">Academic Honesty</a>: it's important, as always.</p>

<br />
<p>You are given some data on the number of times individual Wikipedia pages were viewed in a particular hour, and then in the same hour a day later. The task of this exercise is to:
        <ul>
                <li>Created a plot of popularity distribution (x-axis: Rank, y-axis: Views)<li/>
                <li>Create a scatterplot of views from the first data file (x-coordinate) and the corresponding values from the second data file (y-coordinate)<li/>
         <ul/>
<p/>                    
<br />
                
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
