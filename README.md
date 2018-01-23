# Perspecticles
### A Chrome extension that exposes favorable and unfavorable viewpoints on controversial topics.  
Created by Amber Graham, Joshua Prince, and Parker Luft at HackDavis 2017. [Devpost](https://devpost.com/software/perspecticles)
**This is the backend code, for the frontend see [here](https://github.com/ambergraham/Perspecticles).**

## Inspiration
In today's polarized political climate, many don't venture out of their social groups which makes finding diverse viewpoints difficult. We wanted to create something that would help people see both sides of an issue. This is why we created the Perspecticles!

## What it does
Perspecticles is a Google Chrome extension that subtly highlights people, words, and phrases that are particularly controversial. You simply move your mouse over the highlighted area, and a pop-up will display two links to one favorable and one unfavorable news article regarding that topic. It's that easy! It runs in the background to easily be integrated into daily life.

## How we built it
We used the IBM's Watson and Bing's search engine APIs to curate news articles while giving them a favorability rating towards specific topics. This favorability rating is a score determined by IBM Watson's Alchemy Language which performs text analysis through natural language processing. By combining this data in our back-end, we were able to incorporate it into our JavaScript front-end to dynamically display news elements on a webpage.

## Challenges we ran into
None of us had built a Chrome extension, and had minimal experience with JavaScript. We struggled to find suitable frameworks to develop the front-end.

## Accomplishments that we're proud of
We used an artificial intelligence API for the first time, and the front-end libraries we used had a steep learning curve to beginners like us. We are proud to have combined different technologies to create a product dedicated to social good.

## What's next for Perspecticles
The potential for IBM's Watson is limitless, and we want to take advantage of it. We hope to expand Perspecticles' vocabulary of controversial phrases and provide a fair representations of these issues for all.