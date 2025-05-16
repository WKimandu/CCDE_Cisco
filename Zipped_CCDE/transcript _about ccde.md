Detecting language using up to the first 30 seconds. Use `--language` to specify the language
Detected language: English
[00:06.360 --> 00:11.020]  Hello everybody. Thanks for stopping by and listening to me talking about network design.
[00:11.620 --> 00:15.860]  My name is Mark Holm. I am the exam program manager for the CCD certification here at
[00:15.860 --> 00:22.360]  Learning and Certifications. So I talk network design all the time. That's what I do and that's
[00:22.360 --> 00:29.580]  how I make a living in my professional career at the moment. I make sure that if you go take
[00:29.580 --> 00:34.140]  the CCD exam, it's my job to make sure we test you the right way. But I'm not going to talk so
[00:34.140 --> 00:39.880]  much about the DE today. I'm going to talk much more about some of the stuff you need to know to
[00:39.880 --> 00:46.480]  be able to be a network designer. Because at the end of the day, network design is not just making
[00:46.480 --> 00:52.280]  some drawings in Visio or other drawing programs. This is about knowing the requirements, knowing
[00:52.280 --> 00:58.500]  your customer, knowing your organization to make sure they have or get what they need.
[00:59.920 --> 01:04.200]  So it's not just about technical knowledge. You need other things as well. So that's what I'm going
[01:04.200 --> 01:09.160]  to cover today. I'm going to give you an example that's going to look very simple, but it's going
[01:09.160 --> 01:16.760]  to have two very different outcomes depending on the requirements. So quickly, there is a
[01:16.760 --> 01:20.820]  Webex space for this. So after the session, if you registered, you should have been added to Room.
[01:21.300 --> 01:25.780]  If not, let us know. Otherwise, feel free to ask me questions afterwards if you have
[01:25.780 --> 01:28.220]  any follow-up questions or anything I've been saying today.
[01:31.400 --> 01:35.620]  So let's have a look at some of the required skills that you need.
[01:38.220 --> 01:45.860]  Because network design is not an exact science. You need to have technical knowledge and you need
[01:45.860 --> 01:52.100]  to have experience, right? Because without the experience, it will be harder for you to design
[01:53.000 --> 01:59.140]  well-functioning networks that are built to the purpose they are supposed to do.
[02:00.380 --> 02:03.800]  And then you need to understand the goals of what you are trying to do.
[02:04.100 --> 02:09.640]  So if you're working on a project, you need to understand why this project, what are the goals,
[02:10.120 --> 02:13.820]  what do you want to achieve, your customer or your organization, what are you trying to get
[02:13.820 --> 02:19.460]  to? Don't just blindly assume, oh, this is just a network. It won't be. There's going to be some
[02:19.460 --> 02:24.120]  requirements. There's going to be some business behind it that needs this to make sure they are
[02:24.120 --> 02:27.300]  fully able to utilize this network afterwards.
[02:29.580 --> 02:36.980]  And we see this every day. Network designs that are bad, they cause problems every day.
[02:38.040 --> 02:45.200]  So essentially, you spend a lot of time and money fixing those problems. Those money would have been
[02:45.200 --> 02:51.760]  much better spent making a proper design at the beginning of the project. But the thing here,
[02:52.460 --> 02:58.560]  and this is bullet number four here, is very important. There is no one size fits all. That
[02:58.560 --> 02:59.560]  doesn't exist. There is no one size fits all. There is no one size fits all. There is no one size fits all.  
[02:59.560 --> 03:04.820]  So when we talk about Cisco validated designs, they are very good. They are validated,
[03:05.000 --> 03:10.680]  of course, hence their name. But at the end of the day, they should be seen as a starting point.
[03:10.760 --> 03:16.900]  You need to trust and verify. Make sure it actually fits. Because there might be or likely
[03:16.900 --> 03:24.180]  will be a requirement somewhere in this information you get from your customer that says, we can't use       
[03:24.180 --> 03:28.580]  the solution as it is. We need to make some adjustments. And there's always going to be
[03:28.580 --> 03:29.220]  some tradeoffs somewhere.
[03:30.220 --> 03:37.000]  You can't build the coolest network ever built because the customer probably can't afford it.
[03:37.740 --> 03:45.120]  You need to make sure that you find a balance between features and what's actually needed.
[03:45.280 --> 03:50.020]  Don't just throw in a lot of features because somebody has to pay for it at the end of the day.
[03:50.600 --> 03:59.300]  And money, it always wins. Every time. No matter what you do, if there's no money to buy what you're
[03:59.300 --> 04:05.460]  suggesting, you won't win. It's going to be shut down. It's not going to be valid design for this
[04:05.460 --> 04:11.300]  game. So this is why you need not a master's degree, but you need a business understanding
[04:11.860 --> 04:17.180]  to be able to do proper network design and be a true expert in that field.
[04:21.180 --> 04:28.100]  So you need to be able to analyze and understand what you're working with, what you're working in,
[04:28.100 --> 04:32.600]  and who you're working for. If you don't have that understanding,
[04:32.920 --> 04:36.340]  chances are you will be making wrong decisions somewhere along the path
[04:36.340 --> 04:41.900]  and will fail to meet the requirements that you've been asked or tasked to do.
[04:43.900 --> 04:49.820]  So you need to make sure that whatever you do, it supports whatever goals and strategy are set for
[04:49.820 --> 04:54.840]  that business. Again, if you fail, they won't call you next time they need a design project.
[04:55.060 --> 04:57.560]  You need to make sure that whatever you do,
[04:58.100 --> 05:03.020]  is aligned with the strategy. So you need to ask questions. You need to make sure you understand
[05:03.020 --> 05:11.120]  this. Don't assume it. Verify it by asking. And then you need to, of course, meet all the
[05:11.120 --> 05:15.540]  requirements, but there's also going to be some constraints. It might be, oh, we can't use new
[05:15.540 --> 05:22.040]  technologies. We can't use, hopefully nobody says that today, but we can't use VXLAN. We will only
[05:22.040 --> 05:27.980]  use traditional VLANs. Okay? It might happen. But there might be constraints that you need
[05:27.980 --> 05:32.360]  to add to that will completely take away everything that you have learned recently here at
[05:32.360 --> 05:36.680]  Cisco Live. So this is a new, cool technology. This is what you should all be doing. But if a
[05:36.680 --> 05:42.080]  customer says, we don't want that, then you have to meet that requirement by not doing it.
[05:43.720 --> 05:47.840]  So again, it ties into that you know who you're working for. So if you're working on a new project,
[05:48.500 --> 05:53.020]  spend a little time researching the company name, researching what they do,
[05:53.180 --> 05:57.620]  what kind of company are you working with? Because if you do that, you might have a better
[05:57.980 --> 06:02.380]  understanding and a good starting point in succeeding and understanding what they're doing.
[06:05.680 --> 06:12.420]  You need, and we talk about this, I say business requirements. You also need to have deep,
[06:12.560 --> 06:18.640]  solid technical understanding of the features, the protocols, all the technologies. You need to
[06:18.640 --> 06:22.960]  have good knowledge of them. Because you need to know what kind of problems they can solve
[06:22.960 --> 06:27.000]  and how they can solve them. And you only have that by having a deep technical knowledge. You can
[06:27.000 --> 06:32.120]  just, oh, I think VLAN will be good here. You need to know why VLAN will be good. Because you need
[06:32.120 --> 06:38.400]  to ask them why questions. So if you talk about the CCIE, which is much more about implementation,
[06:38.820 --> 06:44.460]  so this is more how you do it. When you do a design, you have to ask why.
[06:46.600 --> 06:51.080]  Because you don't implement, you typically in a way, you don't implement as a network designer.
[06:51.300 --> 06:55.120]  You design the network and you hand it off to somebody else to actually do the implementation.
[06:55.860 --> 06:56.660]  You don't
[06:57.000 --> 07:02.160]  do everything yourself unless you're a very small organization where you might have both caps on.
[07:04.340 --> 07:09.340]  But most importantly, you have to size it right. Don't gold plate it. Again,
[07:09.440 --> 07:13.620]  it ties back to the requirements. If they don't have a requirement to do feature set,
[07:14.680 --> 07:19.900]  then don't put it there because it will be over plating and it will be a waste of time and
[07:19.900 --> 07:26.700]  resources to build in a feature they will never use or don't even want. And then lastly, this is
[07:27.000 --> 07:32.080]  where the business stuff come in. You need to be comfortable working with topics like CapEx, OpEx,
[07:32.840 --> 07:39.200]  TCO, total cost of ownership, return on investment. Because you need to understand, again, the money
[07:40.260 --> 07:46.220]  is king, not technology. So you need to be able to work with these numbers and figure out what's
[07:46.220 --> 07:50.380]  going to cost long, what's going to be OpEx, what's going to be CapEx. And you need to
[07:50.380 --> 07:55.900]  understand this could be cost of operating and owning this network. So not only the acquiring the
[07:55.900 --> 08:01.200]  hardware and requiring the, you know, the hours to implement it, you also need to operate it
[08:01.200 --> 08:05.740]  until the day you have to refresh everything. So remember, everything is cyclical. It all goes back.
[08:05.900 --> 08:10.440]  You design then you run it and at some point you're gonna go back and make a new design
[08:10.440 --> 08:16.800]  because things change and this is also what a designer does. Understand that there is always
[08:16.800 --> 08:24.020]  gonna be changes. One of the most important things you need to do is… Listen.
[08:25.340 --> 08:25.880]  Figuring out When you're doing something you'rewarting –and that's not a PRO – when you're
[08:25.880 --> 08:29.060]  set in meetings with your customer you have to listen to what they are saying
[08:29.680 --> 08:36.200]  and also what they're not saying because it's hardly ever going to happen to you
[08:36.200 --> 08:40.000]  that a customer is going to say exactly we want this and we want it like that
[08:40.820 --> 08:45.580]  they don't know it's your job so what they are saying and then what they're
[08:45.580 --> 08:49.800]  not saying listen to what's between blinds because they might not say
[08:49.800 --> 08:54.200]  directly so you need to be able to catch oh this is what you really want you're
[08:54.200 --> 08:59.020]  saying you wanting this but in reality you want something over here but often
[08:59.020 --> 09:04.360]  these people that you're talking to as a network signer might be CTOs or CFOs
[09:04.360 --> 09:09.520]  they might not know all the technical slides you need to be able to speak
[09:09.520 --> 09:13.600]  business language and understand that they are going to express something in
[09:13.600 --> 09:18.600]  what we need for our business and then you have to listen to them a figure out
[09:18.600 --> 09:22.960]  and translate that into the design at the end of the day so you're going to
[09:22.960 --> 09:23.820]  talk to a bunch of
[09:23.820 --> 09:23.980]  people
[09:23.980 --> 09:28.040]  relevant people, not only CTOs and things like that,
[09:28.100 --> 09:29.300]  but you're also going to talk to network engineers.
[09:29.500 --> 09:31.080]  You're going to talk to them, okay, so what do you need?
[09:31.220 --> 09:34.420]  What are your pain problems today?
[09:34.520 --> 09:36.060]  What do you struggle with today?
[09:36.500 --> 09:39.220]  And how can you, what are your skill sets?
[09:39.480 --> 09:40.800]  Because another thing you have to consider,
[09:40.920 --> 09:42.400]  if you're bringing brand new technology,
[09:42.660 --> 09:43.600]  there's also going to be training.
[09:44.620 --> 09:46.260]  If you don't have the necessary skills
[09:46.820 --> 09:48.260]  in the organization to run the network,
[09:48.400 --> 09:51.220]  again, it's not relevant, it's going to be useless
[09:51.220 --> 09:52.260]  at the end of the day.
[09:52.260 --> 09:54.960]  So if you get to a customer that doesn't have
[09:54.960 --> 09:58.200]  a budget for training or time for training, you lose.
[09:59.600 --> 10:02.060]  Because if you put in new technology that requires training,
[10:02.300 --> 10:05.000]  the staff is not skilled for it, you lost.
[10:05.620 --> 10:07.260]  You didn't do your job as a network designer.
[10:10.860 --> 10:13.900]  Keep everything you've gathered information, keep it there.
[10:14.060 --> 10:16.240]  Because it might be something that's not relevant now,
[10:16.280 --> 10:17.600]  it might become relevant down the road.
[10:18.240 --> 10:20.500]  Or again, make sure you have it available,
[10:20.660 --> 10:21.760]  don't throw it away and assume,
[10:21.820 --> 10:22.240]  oh, this is not relevant.
[10:22.260 --> 10:23.740]  I'm never going to use this piece of information.
[10:24.400 --> 10:26.520]  Make good, you need to have good notes.
[10:26.660 --> 10:30.420]  Taking skills probably will be a good thing to do.
[10:31.900 --> 10:36.140]  And first of all, no preconceived notions and ideas.
[10:36.900 --> 10:39.020]  Because if you do, you're going to have a bias towards
[10:39.020 --> 10:40.680]  a certain solution even before you know
[10:40.680 --> 10:41.420]  what the requirements are.
[10:41.760 --> 10:44.760]  You need to make sure that you leave your head open,
[10:44.820 --> 10:48.040]  a mind open to everything can happen.
[10:48.320 --> 10:51.540]  So if you avoid those preconceived notions, that means,
[10:52.300 --> 10:55.660]  you're open to adjust, so you might have an idea
[10:55.660 --> 10:58.700]  of what you want to do, but then you're much more willing
[10:58.700 --> 11:02.100]  and able to adjust and change course based on what you hear.
[11:02.820 --> 11:05.180]  If you're going to say, it's going to be VXLan no matter what.
[11:06.440 --> 11:08.820]  You end up saying, this is not VXLan, it's not the right fit.
[11:10.800 --> 11:12.940]  Then again, you lost, you didn't do your job.
[11:14.580 --> 11:16.540]  And you don't want to make assumptions,
[11:16.720 --> 11:19.920]  so you want to talk to the people, ask them questions.
[11:20.800 --> 11:21.520]  Never assume.
[11:21.520 --> 11:25.120]  Never assume anything unless you've been told
[11:25.120 --> 11:26.260]  you can assume this.
[11:26.740 --> 11:28.700]  So never automatically assume anything.
[11:30.140 --> 11:32.960]  And finally, the 2 a.m. in the morning test,
[11:33.200 --> 11:35.680]  if somebody calls you, can you justify the decisions
[11:35.680 --> 11:39.080]  you have made, right?
[11:39.840 --> 11:42.860]  Can you at any point say, why did you choose VXLan?
[11:42.980 --> 11:45.340]  Oh, it was because you told me this, this, this,
[11:45.420 --> 11:46.840]  and you have this requirement, this requirement,
[11:47.420 --> 11:49.300]  and you have the skills to support it.
[11:50.160 --> 11:50.600]  Okay.
[11:51.520 --> 11:52.160]  That's the right decision.
[11:52.300 --> 11:54.040]  But if you can't, you're probably wrong.
[11:55.180 --> 11:57.580]  Then, if you can't justify decisions, again,
[11:57.700 --> 11:59.500]  you haven't done your job right.
[12:02.480 --> 12:05.020]  So network designer, you will work with high-level designs.
[12:06.120 --> 12:08.980]  So these are not going to be anything about protocol timers
[12:08.980 --> 12:11.960]  or how you implement OSPF in the areas,
[12:12.12
(Content truncated due to size limit. Use line ranges to read in chunks)