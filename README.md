# ⚽ Goal 26 - FIFA World Cup 2026 Predictions 

## Project Overview
Goal26 is an independent data science and web-based application built to predict the outcomes of the FIFA 2026 World Cup pre-tournament. 

> 🌟 **Featured In & Press Coverage:**
>  - Featured in the **Girls Who Code** newsletter!
>  - Published in **AI Journal**
>  - Featured across local newspapers

## Why This Project?
Since fourth grade, I have played soccer myself in school. Around my earlier years of high school, I started watching more soccer games and attending MLS games. I would like to major in a field in technology, so I wanted to see how combining my passion of soccer and technology would go hand-in-hand. Also, I wanted to see how AI in data science may change the sports forecasting industry: how do humans and AI predictions compare and who is more accurate to true data—and what does this mean for the sports analytics world?

## Key Features
- **AI Match Predictions:** Using AI model, win, draw, and loss percentage probabilities are calculated for each predicted match.
- **Round Jump-To Navigation:** Instead of having to scroll down to see different rounds of the tournament, just click the Jump to Round bar to go directly to the round (Round of 32, Round of 16, Quarterfinals, Semifinals, and Final).
- **Match and Venue Details:** Match details, like stadium location, dates, country flag, different probabilities to win, draw, lose, and for group stages, whether AI was correct or not.
- **Articles and Research:** Integrated different article feed about this project to educate those interested or potentially in sports analytics and AI, giving insight of tournament prediction insights, how to build a model, and my research paper. 

## File Structure and Primary Functions
### `goal26/templates/admin_submit.html`
Allows one in the admin profile to submit articles on the webpage.

### `goal26/templates/article_detail.html`
Gives the default template of how articles should be displayed with fields like article name, description, and publish date.

### `goal26/templates/index.html`
Used to display articles on page, jump-to feature to jump to specific tournament round matches (to avoid longscrolling), display match team and flag image, display model’s prediction per match with a win, draw, loss, and previously to collect user data on game result predictions.

### `goal26/.env.example`
Serves as a template for setting up local environment variables and secret keys securely.

### `goal26/app.py`
Stores all the country’s flags for aesthetic purposes, creates a table in Match class to display each of the fields on the web page, as well as articles and previously whether a user agreed or disagreed with AI’s prediction, as well as an admin log-in to edit articles.

### `goal26/matches.csv`
Stores all of the FIFA 2026 World Cup matches in a table storing date, match_number, teams, group, stadium, and date_dt for game display on the page.

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, Templates, CSS
- **Data and Storage:** CSV, SQL Database
- **Deployment:** Heroku 

## Data Collection and Filtering
- **Match Data:** Gathered international football match data from a Kaggle dataset.
- **User Predictions:** Collected over 50,000 human match predictions in partnership with WCpredictor.app through user submissions to study user predictions versus AI. 
- **Data Filtering:** Filtered historical match data spanning from 1998 to 2026 and removed unnecessary fields before saving to `matches.csv`. 

## What the Model Considers
- **Fields:** FIFA ranking, Rolling form, Home field advantage for Host Countries
  
## 📄 Research Paper & Resources
For more information on the dataset, model architecture, and detailed prediction findings, access the research paper in the website's articles section.

## Conclusion
AI does not outpower humans, but neither do humans. In the sports analytics world, AI might have better historical records and statistical accuracy, but humans bring the cheer, passion, and energy factor that no algorithm can replicate. In the future, I expect to see more AI integration for match probabilities.


## About Me
I am Riya Deb, a high school student and soccer enthusiast passionate about data science and artificial intelligence. I developed Goal26 to bridge machine learning analytics with real-world sports predictions.


