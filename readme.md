**To run this app:**

This app is containerized, so you can run it on any machine which has docker installed.  From the root of this repo, run this command to build the image:
```
$docker build --pull --rm -f "Dockerfile.dockerfile" -t fetch:latest "."
```

Run this command to start the container from the image you just built:
```
docker run -p 5000:5000 fetch:latest
```

Those commands will build a flask application running on 0.0.0.0:5000.  To make a request, submit a POST request with the two texts to compare in the body with the keys "text1" and "text2" against 0.0.0.0:5000 using your favorite request tool (postman will do, or running Invoke-WebRequest on Windows, or running curl on Linux)

For example:
```
$postparams = @{text1="my text 1"; text2="my text 2"}
Invoke-WebRequest -Uri "http://localhost:5000" -Method POST -Body $postParams -UseBasicParsing
```
The app will respond with a score for the similarity of the two texts submitted in the body as text1 and text2.

**Developer Notes:**

* Do you count punctuation or only words? _I've only counted words since the sample texts were mostly sentence-like.  If I were dealing with data which contained important punctuation or special characters, I may have considered including it._
* Which words should matter in the similarity comparison?  _I've included all words here, but I could have excluded common words (i.e. articles like 'a, an, the')_
* Do you care about the ordering of words? _For some computations, yes.  I've included three phases to this algorithm, a simple word by word comparison, a check for sets containing the same words, and a Levenshtein distance-based computation.  For the set-based computation, ordering is ignored so that texts with words out of order get higher scores_
* What metric do you use to assign a numerical value to the similarity? _I've used an average of the three methods described in the answer above unless the sets are completely identical or completely distinct (in which case, the score is set to 1 or 0, respectively)_
* What type of data structures should be used? (Hint: Dictionaries and lists are particularly helpful data structures that can be leveraged to calculate the similarity of two pieces of text.)  _I've used lists and sets here._

I've enjoyed this exercise greatly, and there are dozens of ways to solve this problem.  I stuck to simple solutions due to the limitation on pulling in libraries, but if I could have any library I wanted, I likely would have pulled in numpy and nltk to do more sophisticated matching.  Ideally, I would enjoy developing a solution which takes sentiment into account when scoring the similarity of two phrases.  I look forward to getting feedback on this solution!

Also, looks like all the commits for this were made from my cscc-luke-rouker account.  Oops!  That is also me, that happens to be the account I use for developing content at Columbus State.  
