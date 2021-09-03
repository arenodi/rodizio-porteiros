# Rodizio-Porteiros

### What is it about?

This is a small project that I've developed in my best effort to create a program that generates a list of 'working' days for volunteer receptionists at the church that I go to.

There were a few things that I needed to consider:

- The rotation system was still being planned by one only person using pen and paper (I do not have a problem with that, I just thought that i could ease this person's trouble), so the program would have to be somewhat flexible generating the list.
- Church services occurs on three fixed days of the week only, and some of the volunteers cannot attend the service because of work or whatever other reason, so the volunteer in question will tell ahead of the list planning which day of the week they cannot attend or in some cases if they cannot attend in even days or odd days.
- The list lists church services for about 3 or 6 months, after that a new list needs to be planned.

### What it does?

You can add or remove already added volunteer, and specify his/her availability. This information is then saved in a _.txt_ file. This _.txt_ file will be accessed when you reopen the program.

After proceeding to the 'generate list' part, you can select the start date and the end date, and after that the program will generate a list of service days and proceed to generate another list pointing one volunteer for each day, always checking if the volunteer is available that day.

### What it takes to work?

There are two main things:

#### 1. Days of the week

I needed the program to know the days of the week (Monday, Tuesday, etc) and work with only those days of the month (1,2, 19, etc) that would be on that specific day of the week. To do that I (after not so much effort) came across the Zeller's congruence algorithm. After a few stackoverflow already answered questions I was able to implement it. And yes, I'm proud to say that instead of an import or copy and paste, I opted to write it down myself :wink:.

#### 2. Volunteer availability

The program needs to take into consideration the availability of each volunteer. To do that I worked with a way of storing it for later comparison using a python _dictionary_, where the key is the volunteer's name and the value is a python _list_ containing all the availability info.
