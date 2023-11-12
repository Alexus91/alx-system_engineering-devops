# Postmortem - FreePost 
## Issue Summary:
### Duration:
Start Time: [4pm 12/08/2022]
End Time: [12am 13/08/2022]
### Impact:
Brace yourselves - FreePost experienced an unexpected site , taking a brief hiatus from the internet for 3 hours.
Users embarked on a rollercoaster of emotions, from confusion to mild panic, as they discovered the platform was on an impromptu vacation.
Approximately  35% of users found themselves in the midst of a digital Bermuda Triangle.
##  Timeline:
Detection Time:
An unsuspecting engineer's inbox was bombarded with alert notifications around 6pm , signaling the beginning of our digital drama.
Detection Method:
Our vigilant monitoring tools lit up like a Christmas tree, frantically waving virtual red flags at the abnormal increase in database errors.
Actions Taken:
The investigative squad dived into the database server like a SWAT team entering a high-stakes operation, suspecting a potential config heist or resource hostage situation.
Misleading Paths:
Our initial hunch? DDoS attack. Because why not suspect foul play when the digital winds are blowing in a mysterious direction?
Escalation:
Unable to coax the database server into revealing its secrets, the distress call echoed through the halls, reaching the mystical realms of Kamal Fadl, our full-stack sorcerer.
Resolution:
After a harrowing battle with lines of code and incantations, Kamal cast optimization spells on database queries, increased connection limits, and summoned caching wizards. Additional server reinforcements were deployed, sending the traffic surge into retreat.
## Root Cause and Resolution:
### Root Cause:
the database server was drowning in connection requests like a popular rockstar besieged by adoring fans. The surge in traffic turned the server into a virtual mosh pit.
### Resolution:
The magic recipe included optimizing database queries to be more VIP-friendly, beefing up connection limits, and strategically placing caches to handle the digital stampede. Server reinforcements were summoned from the cloud, ensuring future traffic surges would be met with a well-prepared welcome party.
## Corrective and Preventative Measures:
Improvements/Fixes:
Autobots, roll out! Implement auto-scaling for the database server to dynamically adapt to traffic fluctuations.
Fortify the virtual castle walls with enhanced network security, complete with a digital moat and dragons.
Tasks to Address:
Conduct a codebase treasure hunt, identifying resource-hungry bandits and optimizing their loot-hoarding tendencies.
Update the incident response manual, adding a section on wrangling server gremlins and streamlining communication during digital catastrophes.
This postmortem comes with a side of humor and a visual feast to capture your attention. Because when technology throws a tantrum, a sprinkle of laughter makes the debugging journey a little more enjoyable!

