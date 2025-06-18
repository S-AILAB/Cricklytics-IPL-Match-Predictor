<h1>🏏 Cricklytics: IPL Match Predictor</h1>

<p><strong>Cricklytics</strong> is a real-time web app that predicts the winning probability of an IPL team using live match inputs like target, score, overs, and wickets.  
It combines machine learning and interactive visuals to provide quick, insightful predictions during a match.</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>🧠 Win probability prediction (Logistic Regression)</li>
  <li>🧹 Cleaned and preprocessed IPL match data</li>
  <li>📊 Exploratory Data Analysis (EDA)</li>
  <li>🧪 Feature engineering:
    <ul>
      <li>Current Run Rate (CRR)</li>
      <li>Required Run Rate (RRR)</li>
      <li>Runs Left, Wickets Left, Balls Remaining</li>
    </ul>
  </li>
  <li>📈 Visualizations:
    <ul>
      <li>Horizontal win probability bar</li>
      <li>Donut-style pie chart</li>
      <li>Score vs Target bar chart</li>
    </ul>
  </li>
</ul>

<hr>

<h2>🧰 Tech Stack</h2>
<ul>
  <li><strong>Language:</strong> Python</li>
  <li><strong>Libraries:</strong> Streamlit, Pandas, NumPy, scikit-learn, Matplotlib</li>
  <li><strong>Model:</strong> Logistic Regression</li>
</ul>

<hr>

<h2>📊 Data Workflow</h2>

<h3>🔸 Data Cleaning</h3>
<ul>
  <li>Removed matches with missing/irrelevant data</li>
  <li>Filtered D/L method and incomplete innings</li>
</ul>

<h3>🔸 EDA</h3>
<ul>
  <li>Analyzed match patterns: early wickets, RRR, venue bias</li>
  <li>Visualized score dynamics and match outcomes</li>
</ul>

<h3>🔸 Feature Selection</h3>
<ul>
  <li>CRR, RRR, Runs Left, Wickets Left, Balls Remaining</li>
  <li>Batting Team, Bowling Team, Host City</li>
</ul>

<hr>

<h2>▶️ Getting Started</h2>

<h4>1. Install dependencies</h4>
<pre><code>pip install -r requirements.txt</code></pre>

<h4>2. Run the app</h4>
<pre><code>streamlit run app.py</code></pre>

<hr>

<h2>🙌 Author</h2>
<p><strong>Siddharth Jain</strong><br>
🔗 <a href="https://www.linkedin.com/in/siddharth-jain-8b56a2321/" target="_blank">LinkedIn Profile</a></p>

<hr>

<h2>📷 Screenshots / Demo</h2>
<p><em>Coming soon — stay tuned!</em></p>

<hr>
