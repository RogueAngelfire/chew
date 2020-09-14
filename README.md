# Chew

This is the 3rd Milestone Assignment by Robin Collins

### A website for people to store and share recipies

I like the idea of recipes uploaded based on the ingredients provided to identify if the dish is indulgent or healthy
the selling point for this would be the instant recognition of a graphical Devil/Demon or Angel/Cherub to
see if the food is healthy or not so healthy (all food better than no food).

I'd like to include a macro pie chart identifying the Proteins, Carbohydrates and fats using the information
gathered by the Angel or its evil counterpart. Again this will be a visual representation for even athletes or bodybuilders
and select the best options for their fitness goals.

At this early stage of the project, my concerns are more to the users who supply their recipes and should be in a position
to be the only person to edit/delete their input. However, I feel this could be a stretch goal for this assignment
but will this will protect peoples creative input and further protect them from malicious intervention from a maybe a rival chef or
just a troll in general.

### Wireframes

Here are the initial designs made of this website with the idea of simplicity.

[Wireframes Images Can be found Here](https://github.com/RogueAngelfire/chew/blob/be80a7f03f60fe1fdd8c2ed8da530c40294cc18d/static/images/ux/Chew_design_1.png)

Apologies with all the Markdown guides I have found it impossible to display the image here as intended.


This is a large image which can be scrolled across revealling the page layout with mobile and tablet design including desktop views.

###  UI

For this particular assignment, I thought a lot harder over my visual design as what I like was not received as well as I expected. As I decided I was making a recipe based website I knew that I needed
to reflect a colour associated with food that looks fresh and stands out. Fresh being like fresh produce, therefore, using green as like plants and vegetables.
However, I didn't want to use red of the meat as could be offensive as a colour that can bleed on the screen
and possibly be detrimental to an audience as vegetarian and vegan dishes welcome and becoming more popular
and have come a long way in 20 years and this could give people the curiosity and could opt for a healthy alternative or just try a new alternative.

I did originally have a light green option then I thought a darker green would be better but chose the subtle colour of my first choice then I also went with a lighter grey as the 
alternate footer colour as this added contrast to the green almost in a sense of country and city where
again this could reflect into the website suggesting rural and urban foods, for example, a meal made by foraging
and the another that is a Street Dish.

I like the idea that when on a Desktop view people can get inspired with the tablet and mobile options there is
the look and feel of a menu or a cookbook with simplistic but beautifully presented information. This would tick the boxes of being designed with the approach of mobile-first due to its responsive design.

### UX

I worked briefly as a trainee chef last year when my photography career was struggling. However, my bosses egos became an
obstacle in one of the passions I had for 20 years which was a real shame as I've always seen all careers as an extension
of a family. As there are enough weddings for all photographers to share the wealth and the same applies to all chefs, cooks
and web designers. However, there are small pockets of selfishness all around these days. That's partially where this idea comes from
as I have plenty of friends, family and ex colleges very interested in my idea as a long term project.

I'm hoping to have a login area where people can submit their recipes. There will be options for them to place them into categories for example Breakfast, Lunch and Dinner. It workout based on the percentage of Proteins, Carbohydrates, fats and
sugars if the meal is healthy or something for not so healthy but a tasty treat. The information will  be displayed as
I mentioned before in the format of an Angel or Demon. This I feel will be the challenge and possible the stretch goal but some
form macros displayed in a pie chart possible beneficial to athletes as I mentioned earlier. I find this challenge
daunting and extremely exciting at the same time as has now struck a chord with one of my other passions of exercise and fitness
which has become more important with the unfortunate crisis of 2020.

Inputs from users will be protected from malicious possible rivalry as I could potentially lose all menus through general vindictiveness
which sadly is the darker side of the benefits of technology.

The page will feature an "add" menu option which features the following mandatory input required to contribute to the Recipies:

Select Meal - Breakfast, Lunch and Dinner
Menu Name
add image  
submitted by (hopefully I can get this to register with a user who has already logged in)
ingredients
Method
Proteins
Carbohydrates
sugars

I feel more could be added but that might be a stretch goal with so many already.
A further stretch goal could feature comments from other users who tried a menu and has improved it
or turned it into a completely different dish entirely. Cooking is probably the only universal thing everyone has some passion.
My mother says she hates it but is making cakes all the time as cooking has many subsections.
Another stretch goal would be to add to Breakfast, Lunch and Dinner a go further with possibly Starter, Mains and Dessert.
The possibilities could be endless with even a amuse bouche and side-orders a possibility.

For now, though I will focus on security with Submit, Edit and Delete - Hopefully with a confirmation that delete was requested.

### Features

This Website features
- Home page
- View Recipes page
- Contact Page
- Profile Page (Once signed up)
- Submit Recipe Page (once logged in)
- Logout option (Only when logged in)

Home has a introduction to Chew which I think I have mangaged to write to entise the audience.

View recipes list all the submitted recipes. By clicking on them it drops down with Author information
this is different to the username. The sumission day can be seen With the list of ingredients and the 
method to how to prepare the dish.
It idicates if the dish is vegetarian or vegan as a Icon of Cheese for vegetarian, or a leaf for vegan
will be present. This also shows up on the title drop down to quicky identify their preference.

There is the options to add Proteins, Carbohydrates, fats and sugars. Ideally I wanted this feature to
incorporate all 4 and be out of 100% but that is now as I indicated a stretch goal for this project.

Providing your username submitted the image you will be entitled to edit or delete your submission.

Clicking Edit recalls all the information regarding  what was previously submitted for correcting possible
spelling issues or even quantities of ingredients. A cancel button also feature should the user change their
mind rather than use the back button.

The Profile page just tells the user they are logged in. It is replaced by login when not present.

Submit recipie looks similar to the Edit View however, it is the essential submission page for the user.

Click logout will instatly logout the user.

I added a Favicon just by installing the Lobster font into my computer making the image square saving as 
a png the submitting it as an icon where gitpod did the scaling automatiaclly.



### Design

I want colours and images to give a fresh organic feel.

## Colours

- #8bc24b This Light Green is used on the Navigation and also with the header settings.
white and black are my alternate colours with greys on the forms.

- I also used a #9e9e9e grey footer.

## Fonts

I picked Lobster font for the Chew logo it works really well I think, simple and effective.
The other font was Roboto as I wanted to stick with it from previous project for its popularity and my continuity.

#### Exsisting Features

I am happy that this features a login security feature by using [werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security)

On the link to the utilites page we use the terms generate_password_hash and check_password_hash.

On the app.py file I would import both features below the bson.objectid.

### Defensive Design

Once logged in only that user can edit or delete their Recipe(s) preventing malicious attacks.

Also an attemtpt to loging with wrong information will be unsuccessful and flag a message stating the 
username or password maybe wrong.

#### Features Left to Implement

My initial idea of the Angel and Demon and my macros pie chart are what I have yet to complete as Icon design was limited in free options
and knew I would want to use Adobe illustrator so the design was uniquie to me therefore I felt the importance was the functionality of
the website in its CRUD (Create, Read, Update, Delete) capacity.

I am still passionate about this project so these now stretch goals will be implimented once my assinment has been assesed.

I do feel that with the Edit option it should retrieve everything from the database and allow subtle changes because a simple spelling error could of 
been submitted originally and I think it would be daunting for a user to have to add the information all over again from scratch. However at the time 
of writing this I have 13 hours to submit my assignment and I want greatness to prevail so I am working on it. I fortunately managed to resolve this 
with the correction of two errors in my app.py code.

I added a contact form for show I haven't connected it to EmailJS as with links to previous projects I'm expected to pay subscriptions costs
and I am currently furloughed from my previous employment. This will be something I'd implement but not a requirement to this project.
However, I thought it best to justify my reasons why it isn't working at this stage.

I would have like to include a confirmation button as Delete could be pressed in error.
 

### Technologies Used

- Balsamiq for my Wireframes.
- Bootstrap was used for testing mainly.
- Materialize for the majority of my frameworks.
- Font Awesome has been implimented for all my icons.
- Github was used as hosting service.
- GitPod for where I carried out all my coding.
- Heroku is what I used to deploy this app which is a container-based cloud platform service.
- Unsplash is where I obtained my images from when I worked out I couldn't submit mine to MongoDB which brings me to
- MongoDB an amazing database website.
- RandomKeygen.com
-

## For this assignment I used the following languages:

HTML5
CSS3
Javascript
Python3

## The Libraries used were as follows:

- Flask
- jQuery
- Bootstrap CCS and JS
- Font Awesome
- PyMongo
- Flask
- PyMongo
- bson
- Werkzeug

## Database used:

- MongoDB

## For Hosting I used:

- Github
- Heroku

### Testing

I have used Materialize for my Wireframes but I ran into many issues with the carousel. It there remains a static image until I have a better understanding of
how to implement its features as it's want very straight forward. I had played with the Bootstrap version also but the images proved too small despite being large files.
Visually I find what is there still simple and effective.

Used Google Developers tools for checking the website visuals to enable changes in CSS.

For my photographs I organised my back catalogue of food stock from Adobe Lightroom but found I had nowhere to host them as I was originally under the illusion I could
submit images as data to MongoDB but my research soon pointed out that it will only store the URL. I did then uploaded my images to my The Image File photo gallery on my 
photography business website but turned out the links where protected so I used photographs from Unsplash as an alternative to save on time. I hope to use my own images
post assesment.

For Checking my HTML code I used [Validator w3](https://validator.w3.org/)

I also used [PEP8 Online](http://pep8online.com/)

For formatting I used the following [Webformatter](https://webformatter.com/html) for HTML, Javascript, JSON and CSS.

I tested the website with various browsers Google, Mozilla Firefox which worked wondefully.

I then tested with Safari and the images became stretched and distorted. At this stage It was late and I needed to submit my assignment I will impliment a webkit at a later
date rather than miss my submission time.

### Deployment

### MongoDB

1. Login to [MongoDB](https://www.mongodb.com/)

2. Click on clusters then click on collections.

3. Click create Database.

4. Name the assignemt to suit your project adding a collection name. Then click the green create button.

5. I created an additonal users database for adding logged in customers.

6. Clicking on my chew_tasks I would add the following: menu_name: for my first example and I would proceed in adding more.

7. Now I have some data I can build my project upon this data. Do note I did change and add to the database over during the project
   for easier identifying certain links I admit I was apprehensive as one broken link will cause problems and can be time consuming.

### Heroku and GitHub

1. Starting from from my [Github Repository](https://github.com/RogueAngelfire/chew)

2. I then clicked on the green button for GitPod.

3. Once open I go back to the GitPod work space by clicking on the blue Gitpod logo on the left hand side below the browser.
   This is so I can run my orininal Master and not a cloned work space.

4. I then click on Chew Master that has been pinned to my Workspace and proceed.

5. Now in the terminal at the base of the screen it will say gitpod /workspace/chew $

6. Enter the folling: pip3 install Flask 

7. I would then add and app.py file and a env.py file and and in the terminal write touch .gitignore

8. Then I would add the enviroment varables to env.py 

9. I will then add my IP, PORT and SECRETKEY

10. At the moment I have debug set to True in my app.py file before deployment this will be set to False.

11. If I type in the terminal git status I can check that my env.py file is not being tracked.

12. In the termainal I type the folling code to get requirements documents: pip3 freeze --local > requirements.text

13. I would then press enter and then type the following for a Procfile: echo web: python app.py > Procfile  and press enter

14. Now head over to [Heroku](https://www.heroku.com/)

15. Login and click on New on the left hand side of the screen and selecting the option create a new app.

16. This will require a unique name selected without spaces. Then click the region as Europe.

17. We can use the Heroku CLI information to connect the app using their step by step terminal instructions.

18. This can be simplified by choosing the secton above where it says deployment method. The middle icon is connect with GitHub.

19. Clicking on this check that your Github profile is displayed and add the repository name mine being chew-menu.

20. Clicking on the search button. It then finds it then proceed by clicking on the connect button.

21. So before launching as it won't work at this stage click on the Settings tab. Then Click on RevealConfig Vars.

22. First we add the IP details which are stored in the env.py file copy this information over without the quotes.

23. Then the PORT then the SECRETKEY and the MONGO_URI and MONGO_DBNAME.

24. Going back to the Terminal type the following: git status

25. git add requirements.txt

26. git commit -m "Add requirements.txt"

27. git add Procfile  followed by git commit -m "Add Procfile"

28. git push - this then sends everything to Github.

29. Now going to Heroku click Enable Automatic Deployment then Deploy Branch.

30. If successful it will state your app was successfully deployed.

31. As I mentioned earlier the final deployment requires debug to be False for security on final deployment.


## Credits

Istock non watermarked photo credits goes to Alex Souto Maior of Brazil.

#### Content

All content I used has been stated free to use watermark remain present as require by Istock.

#### Media

Photographs are taken mainly as place holders from Istock for the carousel and Unsplash for the recipes.

All text was written by myself with some input by Grammerly

#### Acknowledgements

I have been privileged with the Support and encouragement of my mentor Brian Macharia, I salute you, Sir. Furthermore,
I'd like to give a special thank you to Code Institute tutor Tim Nelson for his assistance tutoring me for this part of the course.
